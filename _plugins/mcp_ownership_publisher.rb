require 'json'
require 'csv'
require 'zlib'

module Jekyll
  # Publishes the weekly MCP registry ownership check as a static lookup index.
  #
  # The registry does not verify that an entry's repository.url belongs to the
  # publisher. mcp_registry_collect.py adds that check and stores the result in
  # the weekly roster. This generator turns the newest roster into shards that a
  # browser — or an agent — can query one file at a time.
  #
  # Why a generator and not committed files: the roster is regenerated weekly and
  # the shards are derived from it. Committing them adds ~1.5MB of churn per week
  # and lets the index drift from its source the first time someone forgets to
  # regenerate. This repo already derives rather than commits (data_publisher.rb,
  # link_graph.py); this follows that.
  #
  # Spec: _plans/2026-08-26-mcp-ownership-lookup-spec.md
  class McpOwnershipPublisher < Generator
    # safe: false, same as data_publisher.rb — the site builds via GitHub Actions
    # (pages-deploy.yml), not GitHub Pages native, so custom plugins run.
    safe false
    priority :normal

    ROSTER_DIR   = '_data/mcp_registry_history/roster'.freeze
    OUT_DIR      = 'data/mcp/ownership'.freeze
    SHARD_DIR    = "#{OUT_DIR}/by-repo".freeze
    ROSTER_RE    = /\A(\d{4}-\d{2}-\d{2})\.tsv\.gz\z/.freeze

    # Deliberately not accusatory. A mismatch means two strings differ, and an
    # ownership transfer to an org produces that difference honestly — the
    # published ranking post says so twice, and 504 mismatches are real named
    # accounts. The UI states what was measured and stops there.
    LABELS = {
      'verified'     => 'Namespace owner matches the repository owner',
      'mismatch'     => 'Namespace and repository owners differ — worth checking this entry',
      'unverifiable' => 'Domain namespace — this check cannot rule either way',
      'no_repo'      => 'No repository declared — nothing to check against'
    }.freeze

    def generate(site)
      path, date = latest_roster(site)
      unless path
        Jekyll.logger.warn 'McpOwnership:',
                           "No roster found under #{ROSTER_DIR} — skipping ownership index."
        return
      end

      rows = read_roster(path)
      return if rows.nil?

      shards, ownership, indexed = build_shards(rows, date)

      shards.each do |shard, payload|
        emit(site, SHARD_DIR, "#{shard}.json", payload)
      end

      emit(site, OUT_DIR, 'index.json',
           manifest(date, rows.size, indexed, ownership, shards))

      Jekyll.logger.info 'McpOwnership:',
                         "#{indexed} entries in #{shards.size} shards from roster #{date}"
    end

    private

    # Newest roster wins. A missed week leaves the previous week's file in place,
    # which is the intended behaviour: the page then reports that older date
    # rather than reporting nothing.
    def latest_roster(site)
      dir = File.join(site.source, ROSTER_DIR)
      return [nil, nil] unless Dir.exist?(dir)

      newest = Dir.children(dir)
                  .filter_map { |f| [f, ROSTER_RE.match(f)] if ROSTER_RE.match?(f) }
                  .map { |f, m| [File.join(dir, f), m[1]] }
                  .max_by { |_, d| d }

      newest || [nil, nil]
    end

    def read_roster(path)
      tsv = Zlib::GzipReader.open(path, external_encoding: 'UTF-8', &:read)
      CSV.parse(tsv, col_sep: "\t", headers: true, quote_char: nil).map(&:to_h)
    rescue Zlib::Error, CSV::MalformedCSVError, ArgumentError => e
      Jekyll.logger.warn 'McpOwnership:',
                         "Could not read #{File.basename(path)} (#{e.class}: #{e.message}) — skipping."
      nil
    end

    # Keyed by the lowercased repository path so a pasted GitHub URL matches
    # regardless of casing. 437 repositories are declared by more than one
    # registry entry (one is declared by 127), so every value is a list.
    def build_shards(rows, date)
      buckets   = Hash.new { |h, k| h[k] = {} }
      ownership = Hash.new(0)
      indexed   = 0

      rows.each do |row|
        status = row['ownership'].to_s.strip
        ownership[status] += 1 unless status.empty?

        repo = row['repo'].to_s.strip
        next if repo.empty?

        key = repo.downcase
        buckets[shard_of(key)][key] ||= []
        # repo keeps its original casing here — the key is lowercased for
        # lookup, but GitHub displays the owner and name as registered.
        buckets[shard_of(key)][key] << [row['name'].to_s, repo, status, stars(row['stars'])]
        indexed += 1
      end

      payloads = buckets.keys.sort.to_h do |shard|
        [shard, {
          'snapshot_date' => date,
          'shard'         => shard,
          'entries'       => buckets[shard].sort.to_h
        }]
      end

      [payloads, ownership, indexed]
    end

    # One character. Two would multiply the file count twentyfold while barely
    # moving the largest shard, because the skew comes from single bulk
    # registrants rather than from letter frequency.
    def shard_of(key)
      c = key[0]
      c =~ /[a-z0-9]/ ? c : '_'
    end

    # 2,630 entries have no star count because their repository was unreachable
    # at collection time. That is missing data, not zero.
    def stars(value)
      v = value.to_s.strip
      v.empty? ? nil : v.to_i
    end

    def manifest(date, total, indexed, ownership, shards)
      {
        'schema_version' => '1.0',
        'generated'      => Time.now.utc.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'snapshot_date'  => date,
        'description'    => 'Repository-ownership check for every MCP registry entry that ' \
                            'declares a repository, from the Json House weekly sweep.',
        'method'         => 'An entry on an io.github.* namespace is compared against the owner ' \
                            'of the repository it declares. The registry itself does not perform ' \
                            'this check. Domain namespaces cannot be checked either way.',
        'totals'         => {
          'servers_in_snapshot' => total,
          'indexed'             => indexed,
          'not_indexed'         => total - indexed
        },
        'ownership'      => ownership.sort.to_h,
        'labels'         => LABELS,
        'coverage_note'  => 'Entries that declare no repository are not in this index. ' \
                            'Absence from it is not evidence that a server is unregistered.',
        'sharding'       => {
          'key'         => 'repository path (owner/name), lowercased',
          'scheme'      => 'first character; [a-z0-9] as-is, anything else in "_"',
          'url_pattern' => "/#{SHARD_DIR}/{shard}.json"
        },
        'record_fields'  => %w[name repo ownership stars],
        'shards'         => shards.keys.sort.to_h { |s| [s, shards[s]['entries'].size] },
        'source_post'    => 'https://www.jsonhouse.com/posts/mcp-registry-report-2026/',
        'attribution'    => {
          'source'               => 'Json House',
          'source_url'           => 'https://www.jsonhouse.com/posts/mcp-registry-report-2026/',
          'dataset_url'          => "https://www.jsonhouse.com/#{OUT_DIR}/index.json",
          'citation'             => 'Json House, "MCP Server Rankings 2026", jsonhouse.com ' \
                                    "(#{date})",
          'attribution_required' => true,
          'terms_url'            => 'https://www.jsonhouse.com/data-policy/'
        }
      }
    end

    def emit(site, dir, name, payload)
      page = PageWithoutAFile.new(site, site.source, dir, name)
      page.content = JSON.generate(payload)
      page.data['layout'] = nil
      page.data['sitemap'] = false
      site.pages << page
    end
  end
end
