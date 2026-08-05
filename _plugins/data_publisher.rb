require 'json'
require 'set'

module Jekyll
  # Publishes post-specific _data/*.json files as public HTTP endpoints.
  #
  # _data/ is Jekyll's private build-time store and is never served publicly.
  # This generator reads every date-prefixed JSON file from site.data and
  # emits it as a real page at /data/{slug}.json, plus a /data/index.json
  # manifest so AI crawlers can discover all datasets with one request.
  #
  # Files matched: YYYY-MM-DD-* (post data files only)
  # Files skipped: authors.yml, contact.yml, share.yml, etc.
  #
  # PUBLICATION GATE: a data file is emitted only when a matching published
  # post exists in _posts/. Data files are written during Phase 3 (draft
  # generation), long before 기웅 approves the post at Phase 5 — without this
  # gate, unapproved data leaks to /data/ and /data/index.json ahead of the
  # post it belongs to. The post is the approval record; no post, no data.
  class DataPublisher < Generator
    # safe: false is required because this is a custom plugin.
    # This works because the site is built via GitHub Actions
    # (pages-deploy.yml), NOT GitHub Pages native build.
    # Switching to GitHub Pages native would disable this plugin entirely.
    safe false
    priority :normal

    POST_DATA_PATTERN = /^\d{4}-\d{2}-\d{2}-.+$/.freeze

    def generate(site)
      index_entries = {}
      published = published_post_basenames(site)

      site.data.each do |key, data|
        next unless key.match?(POST_DATA_PATTERN)
        next unless data.is_a?(Hash)

        unless published.include?(key)
          Jekyll.logger.info "DataPublisher:",
                             "Withholding #{key} — no published post in _posts/"
          next
        end

        page = PageWithoutAFile.new(site, site.source, 'data', "#{key}.json")
        begin
          page.content = JSON.generate(data)
        rescue JSON::GeneratorError => e
          Jekyll.logger.warn "DataPublisher:", "Skipping #{key}: #{e.message}"
          next
        end
        page.data['layout'] = nil
        site.pages << page

        # Posts, llms.txt, and CLAUDE.md all reference the date-less form
        # /data/{slug}.json, so publish an alias alongside the dated file.
        slug = data['slug']
        if slug.is_a?(String) && !slug.empty? && slug != key
          alias_page = PageWithoutAFile.new(site, site.source, 'data', "#{slug}.json")
          alias_page.content = page.content
          alias_page.data['layout'] = nil
          site.pages << alias_page
        end

        index_entries[key] = {
          'url'          => "/data/#{key}.json",
          'slug'         => data['slug'],
          'title'        => data['title'],
          'description'  => data['description'],
          'category'     => data['category'],
          'cluster'      => data['cluster'],
          'format'       => data['format'],
          'data_updated' => data['data_updated']
        }
      end

      index = PageWithoutAFile.new(site, site.source, 'data', 'index.json')
      index.content = JSON.generate({
        'generated' => Time.now.utc.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'count'     => index_entries.size,
        'datasets'  => index_entries
      })
      index.data['layout'] = nil
      site.pages << index
    end

    private

    # Basenames (YYYY-MM-DD-slug) of posts that are actually going live in
    # this build. Drafts are excluded even when Jekyll runs with --drafts,
    # so a local preview build cannot mint a public dataset URL either.
    def published_post_basenames(site)
      site.posts.docs.reject { |doc| draft?(doc) }
                     .map(&:basename_without_ext)
                     .to_set
    end

    def draft?(doc)
      return doc.draft? if doc.respond_to?(:draft?)

      doc.relative_path.to_s.include?('_drafts')
    end
  end
end
