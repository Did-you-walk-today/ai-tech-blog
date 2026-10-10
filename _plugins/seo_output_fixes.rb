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
  # - First screen image: see eager_first_image below.
  # - Render-blocking CDN stylesheets: see async_cdn_styles below.
  # - 404: the page is noindex (assets/404.html front matter); its canonical pointed at
  #   /404.html and is removed.
  #
  # Reversible: delete this file. Nothing else depends on it.
  module SeoOutputFixes
    CARD_H1 = %r{<h1 class="card-title([^"]*)">(.*?)</h1>}m.freeze
    PAGINATED = %r{\A/page(\d+)/\z}.freeze
    CDN_STYLE = %r{<link rel="stylesheet" href="(https://(?:cdn\.jsdelivr\.net|fonts\.googleapis\.com)/[^"]+)">}.freeze
    SEARCH_LOADER = %r{<script> document\.addEventListener\('DOMContentLoaded', \(\) => \{ SimpleJekyllSearch\(\{(.*?)\}\); \}\); </script>}m.freeze
    SEARCH_JSON = "json: '/assets/js/data/search.json',"

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
      html = eager_first_image(html, '<div id="post-list"') if url == '/' || url.match?(PAGINATED)
      html = eager_first_image(html, '<article') if url.start_with?('/posts/')
      html = async_cdn_styles(html)
      html = lazy_search_index(html)

      item.output = html
    end

    # The theme's search loader fetches the whole search index (/assets/js/data/search.json, 159 KB)
    # on DOMContentLoaded, on every page, while the first screen is still loading. Measured 2026-10-10
    # (Lighthouse mobile, home): it was the largest request before the LCP once the first-screen
    # image had loaded. The index is now fetched when the search box first gets focus and handed to
    # SimpleJekyllSearch as an object; a query typed before it arrived is searched once it has.
    # If the theme changes this script the pattern stops matching and the page keeps the theme's.
    def lazy_search_index(html)
      html.sub(SEARCH_LOADER) do
        options = Regexp.last_match(1)
        next Regexp.last_match(0) unless options.include?(SEARCH_JSON)

        options = options.sub(SEARCH_JSON, 'json: json,')
        "<script> document.addEventListener('DOMContentLoaded', () => { " \
          "const input = document.getElementById('search-input'); if (!input) return; " \
          "input.addEventListener('focus', () => { fetch('/assets/js/data/search.json')" \
          ".then((response) => response.json()).then((json) => { SimpleJekyllSearch({#{options}}); " \
          "if (input.value) input.dispatchEvent(new Event('input')); }); }, { once: true }); }); </script>"
      end
    end

    # Every stylesheet the theme loads from jsdelivr (Font Awesome icons, tocbot, glightbox, the lazy
    # loading polyfill) or Google Fonts blocks the first paint, and none of them styles the first
    # screen's layout: the fonts already swap in (display=swap), so text paints in the fallback font
    # either way. Measured 2026-10-10 (Lighthouse mobile, home): render-blocking requests estimated at
    # 2.0 s, Font Awesome 1.4 s and Google Fonts 0.9 s of it; FCP 3.4 s -> 2.2 s on a local build with
    # both changed. They now load with media="print" and switch to "all" once loaded; the noscript
    # copy keeps them for browsers without JavaScript.
    def async_cdn_styles(html)
      html.gsub(CDN_STYLE) do
        href = Regexp.last_match(1)
        %(<link rel="stylesheet" href="#{href}" media="print" onload="this.media='all'">) +
          %(<noscript><link rel="stylesheet" href="#{href}"></noscript>)
      end
    end

    # The first image after the marker is the largest thing on the first screen (the first card's
    # cover on list pages, the cover on a post), and the theme prints it with loading="lazy", so the
    # browser waits for layout before fetching it. Measured 2026-10-09 (Lighthouse mobile, home):
    # LCP 9.6 s, of which 3.0 s load delay. Only that one image changes; the rest stay lazy.
    def eager_first_image(html, marker)
      start = html.index(marker)
      return html unless start

      tail = html[start..].sub(/<img\b[^>]*>/) { |tag| tag.sub(' loading="lazy"', ' fetchpriority="high"') }
      html[0...start] + tail
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
