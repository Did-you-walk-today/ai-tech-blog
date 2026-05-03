require 'json'

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
  class DataPublisher < Generator
    safe false
    priority :normal

    POST_DATA_PATTERN = /^\d{4}-\d{2}-\d{2}-.+$/.freeze

    def generate(site)
      index_entries = {}

      site.data.each do |key, data|
        next unless key.match?(POST_DATA_PATTERN)
        next unless data.is_a?(Hash)

        page = PageWithoutAFile.new(site, site.source, 'data', "#{key}.json")
        page.content = JSON.generate(data)
        page.data['layout'] = false
        site.pages << page

        index_entries[key] = {
          'url'          => "/data/#{key}.json",
          'slug'         => data['slug'],
          'data_updated' => data['data_updated']
        }
      end

      index = PageWithoutAFile.new(site, site.source, 'data', 'index.json')
      index.content = JSON.generate({
        'generated' => Time.now.utc.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'count'     => index_entries.size,
        'datasets'  => index_entries
      })
      index.data['layout'] = false
      site.pages << index
    end
  end
end
