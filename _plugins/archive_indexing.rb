module Jekyll
  # Withholds jekyll-archives' generated tag and category pages from the sitemap
  # and from the index, without removing the pages themselves.
  #
  # Why this exists: on 2026-08-13 the GSC "not indexed" export ran to 97 URLs, of
  # which 51 were /tags/ pages. The sitemap was 110 URLs — 75 tags, 8 categories,
  # and only 14 actual posts (12.7%). A 16-post site was asking Google to crawl 83
  # auto-generated listing pages, and Google answered by crawling almost none of
  # it: six live posts, the CLUSTER_LLM pillar among them, had never been fetched
  # at all (GSC last-crawl 1970-01-01). Crawl budget on a young domain is small,
  # and thin archive pages were spending all of it.
  #
  # What stays and what goes:
  #
  # - The pages keep rendering and keep their URLs. Chirpy prints a post's tags as
  #   links, so removing them would leave dangling links in every post.
  # - `noindex, follow` — withdraw from the index, keep passing link equity to the
  #   posts they list. Same mechanism already used for deprecated-cluster posts
  #   (see _includes/metadata-hook.html); this sets the flag from the generator
  #   because archive pages have no front matter to edit.
  # - `sitemap: false` — jekyll-sitemap filters on `doc.sitemap != false`, and
  #   Archive subclasses Jekyll::Page, so setting page data is enough.
  #
  # Categories are included deliberately. /categories/{id}/ duplicates the curated
  # hub tab declared for that category in _data/taxonomy.yml (ai-models-intelligence
  # -> /ai-models/, and so on). The hub is the entry point we actually maintain;
  # the archive is a second listing of the same posts. Only one of them should be
  # in the index, and it should be the one taxonomy.yml governs.
  #
  # Reversible: delete this file. Nothing else in the build depends on it.
  #
  # Priority note: must run after jekyll-archives (:normal) creates the pages and
  # before jekyll-sitemap (:lowest) reads them. :low sits between the two.
  class ArchiveIndexing < Generator
    safe false
    priority :low

    def generate(site)
      return unless defined?(Jekyll::Archives::Archive)

      touched = site.pages.count do |page|
        next false unless page.is_a?(Jekyll::Archives::Archive)

        page.data["sitemap"] = false
        page.data["noindex"] = true
        true
      end

      Jekyll.logger.info "ArchiveIndexing:", "withheld #{touched} archive pages from sitemap and index"
    end
  end
end
