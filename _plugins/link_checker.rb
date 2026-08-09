module Jekyll
  # Fails the build when a post links to a /posts/<slug>/ that does not exist.
  #
  # .claude/hooks/sync-link-graph.sh already catches this, but only for edits made
  # through Claude Code. Links also arrive from other sessions sharing this working
  # tree, from the GitHub web editor, and from hand edits — none of which fire a
  # hook. This is the backstop: a dangling internal link cannot reach production
  # because the deploy build stops first.
  #
  # CLAUDE.md records the cost of not having this: one slug change broke nine
  # internal links, discovered only after publishing.
  #
  # Deliberately not checked here: orphans, thin outbound counts, links to noindex
  # pages. Those are judgment calls that belong in LINK_GRAPH.md, not gates that
  # block a deploy.
  class InternalLinkChecker < Generator
    safe false
    priority :low

    LINK_RE = %r{\]\(/posts/([a-z0-9][a-z0-9-]*)/?(?:[#?][^)]*)?\)}
    FENCE_RE = /```.*?```/m

    def generate(site)
      known = site.posts.docs.map { |d| slug_of(d) }.compact.to_set
      broken = []

      site.posts.docs.each do |doc|
        body = doc.content.gsub(FENCE_RE, '')
        body.scan(LINK_RE).flatten.uniq.each do |target|
          next if known.include?(target)
          broken << [File.basename(doc.path), target]
        end
      end

      return if broken.empty?

      lines = broken.map { |src, target| "  #{src} -> /posts/#{target}/" }
      raise Jekyll::Errors::FatalException, <<~MSG
        Internal link check failed — #{broken.size} link(s) point at a slug that does not exist in _posts/:

        #{lines.join("\n")}

        Fix the link, or publish the missing post. Full graph: LINK_GRAPH.md
        Run locally: python3 .claude/hooks/link_graph.py --report
      MSG
    end

    private

    # Prefer the real permalink slug; fall back to the filename for safety.
    def slug_of(doc)
      doc.data['slug'] || File.basename(doc.path, '.md').sub(/\A\d{4}-\d{2}-\d{2}-/, '')
    end
  end
end
