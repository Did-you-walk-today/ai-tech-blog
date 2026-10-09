module Jekyll
  # Corrects four things the theme and jekyll-seo-tag print that search engines read as errors,
  # without copying theme layouts into this repo (a copied layout stops receiving theme updates).
  #
  # Found by a live audit on 2026-10-09 against the SEO reference in the AdPrepare repo
  # (SEO_기술_총람_2026-10-09.md §3-4, §3-5):
  #
  # - Home and /pageN/: Chirpy's home layout prints every post card title as <h1>, so the
  #   home page had 10 h1 elements and no heading that names the page. Card titles become
  #   <h2> (the .card-title rule sets the font size, so they look the same) and the page
  #   gets one visually hidden <h1> with the site title.
  # - /pageN/: jekyll-paginate copies index.html, so every page of the list had the title
  #   "Json House", the same as the home page. They now say "Json House | Page N".
  # - jekyll-seo-tag writes "@type":"imageObject"; schema.org types are case-sensitive,
  #   so the image was not read as an ImageObject.
  # - jekyll-seo-tag writes twitter:site "@" (twitter.username is empty in _config.yml)
  #   and twitter:creator "@Json House" (the author name is not a handle). Both are invalid
  #   handles and are dropped.
  # - 404: the page is noindex (assets/404.html front matter); its canonical pointed at
  #   /404.html and is removed.
  #
  # Reversible: delete this file. Nothing else depends on it.
  module SeoOutputFixes
    CARD_H1 = %r{<h1 class="card-title([^"]*)">(.*?)</h1>}m.freeze
    PAGINATED = %r{\A/page(\d+)/\z}.freeze

    module_function

    def apply(item)
      html = item.output
      return unless html.is_a?(String) && item.output_ext == '.html'

      html = html.gsub('"@type":"imageObject"', '"@type":"ImageObject"')
      html = html.gsub(%r{<meta name="twitter:site" content="@"\s*/?>\s*}, '')
      html = html.gsub(%r{<meta name="twitter:creator" content="@[^"]*\s[^"]*"\s*/?>\s*}, '')

      url = item.url.to_s
      html = list_page(html, url, item.site.config['title'].to_s) if url == '/' || url.match?(PAGINATED)
      html = html.sub(%r{<link rel="canonical"[^>]*>\s*}, '') if url == '/404.html'

      item.output = html
    end

    def list_page(html, url, site_title)
      html = html.gsub(CARD_H1) { %(<h2 class="card-title#{Regexp.last_match(1)}">#{Regexp.last_match(2)}</h2>) }
      html = html.sub('<div id="post-list"', %(<h1 class="visually-hidden">#{site_title}</h1><div id="post-list"))
      number = url[PAGINATED, 1]
      return html unless number

      paged = "#{site_title} | Page #{number}"
      escaped = Regexp.escape(site_title)
      html = html.sub(%r{<title>\s*#{escaped}\s*</title>}, "<title>#{paged}</title>")
      html.gsub(%r{(<meta property="(?:og|twitter):title" content=")#{escaped}(")}) { "#{Regexp.last_match(1)}#{paged}#{Regexp.last_match(2)}" }
    end
  end

  Hooks.register [:pages, :documents], :post_render do |item|
    SeoOutputFixes.apply(item)
  end
end
