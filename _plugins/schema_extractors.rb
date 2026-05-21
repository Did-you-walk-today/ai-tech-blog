# ═══════════════════════════════════════════════════════════
# _plugins/schema_extractors.rb
# 위치: jsonhouse 레포의 _plugins/ 폴더에 저장
# 역할: 본문 markdown에서 FAQ와 HowTo step을 자동 추출해서
#       page.faqs, page.howto_steps에 주입 → JSON-LD 자동 완성
# ═══════════════════════════════════════════════════════════

module Jekyll
  module SchemaExtractors

    # ───────────────────────────────────────────────────────
    # FAQ Extractor
    # 본문에서 "## Frequently Asked Questions" 섹션을 찾아
    # ### 질문 / 답변 패턴을 page.faqs 배열로 추출
    # ───────────────────────────────────────────────────────
    class FaqGenerator < Jekyll::Generator
      safe true
      priority :low

      def generate(site)
        site.posts.docs.each do |post|
          next unless post.data['schema_types']&.include?('FAQPage')
          next if post.data['faqs'] # 이미 front matter에 있으면 skip

          faqs = extract_faqs(post.content)
          post.data['faqs'] = faqs if faqs.any?
        end
      end

      private

      def extract_faqs(content)
        # "## Frequently Asked Questions" 또는 "## FAQ" 섹션 찾기
        faq_section_match = content.match(
          /^##\s+(?:Frequently Asked Questions|FAQ).*?(?=^##\s|\z)/im
        )
        return [] unless faq_section_match

        section = faq_section_match[0]

        # ### 질문 + 다음 ### 또는 ## 까지의 답변 추출
        faqs = []
        section.scan(/^###\s+(.+?)\s*\n+(.+?)(?=^###\s|\z)/m) do |q, a|
          # 답변에서 markdown 링크 등 정리
          answer = a.strip
                    .gsub(/\[([^\]]+)\]\([^\)]+\)/, '\1')  # [text](url) → text
                    .gsub(/[\*_`]/, '')                     # remove markdown
                    .gsub(/\s+/, ' ')                       # collapse whitespace
                    .strip

          next if answer.empty? || answer.length > 500  # 너무 긴 답변 제외

          faqs << { 'q' => q.strip, 'a' => answer }
        end

        faqs
      end
    end

    # ───────────────────────────────────────────────────────
    # HowTo Step Extractor
    # 본문에서 "## Step N: ..." 패턴을 찾아
    # page.howto_steps 배열로 추출
    # ───────────────────────────────────────────────────────
    class HowToGenerator < Jekyll::Generator
      safe true
      priority :low

      def generate(site)
        site.posts.docs.each do |post|
          next unless post.data['schema_types']&.include?('HowTo')
          next if post.data['howto_steps']

          steps = extract_steps(post.content, post.url, site.config['url'])
          post.data['howto_steps'] = steps if steps.any?
        end
      end

      private

      def extract_steps(content, post_url, site_url)
        steps = []

        # "## Step N: Title" 패턴 매칭
        content.scan(/^##\s+Step\s+(\d+):\s+(.+?)\s*\n+(.+?)(?=^##\s+Step\s+\d+:|^##\s|\z)/m) do |num, title, body|
          # body 첫 단락만 추출 (간략하게)
          first_para = body.strip.split(/\n\n/).first.to_s
                           .gsub(/\[([^\]]+)\]\([^\)]+\)/, '\1')
                           .gsub(/[\*_`]/, '')
                           .gsub(/\s+/, ' ')
                           .strip
                           .slice(0, 300)

          steps << {
            'position' => num.to_i,
            'name'     => title.strip,
            'text'     => first_para,
            'url'      => "#{site_url}#{post_url}#step-#{num}"
          }
        end

        steps
      end
    end
  end
end

# ═══════════════════════════════════════════════════════════
# 이 플러그인을 추가하면:
# 1. 작성자가 본문에 "## Frequently Asked Questions" 섹션에
#    ### 질문 / 답변을 자연스럽게 쓰면 됨
# 2. 작성자가 본문에 "## Step 1: ..." 패턴을 따르면 됨
# 3. _layouts/post.html이 page.faqs, page.howto_steps를 자동으로 사용
#
# GitHub Pages는 unsafe plugin을 막아두기 때문에
# Jekyll을 GitHub Actions에서 빌드하는 방식 권장:
# (build → gh-pages branch로 push)
# ═══════════════════════════════════════════════════════════
