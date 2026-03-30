# Task: Apply Chirpy Theme to Jekyll Blog

## Project Context
- Jekyll blog at current directory (jsonhouse.com / AI Tech Resource Blog)
- Current: custom minimal theme with no CSS framework
- Goal: Apply Chirpy theme while preserving all existing content and SEO settings

## Current Structure
- Posts: _posts/
- Layouts: _layouts/
- Config: _config.yml
- Custom files to preserve: llms.txt, robots.txt, ads.txt, CNAME, api/, category/

---

## Steps

### Step 0. Backup first
Run git commit to save current state:
```
git add -A
git commit -m "backup before chirpy migration"
```

---

### Step 1. Replace Gemfile
Overwrite Gemfile with this content:
```
source "https://rubygems.org"
gem "jekyll-theme-chirpy", "~> 7.0"
gem "jekyll-sitemap"
gem "jekyll-seo-tag"
gem "jekyll-feed"
```

Then run:
```
bundle install
```

---

### Step 2. Update _config.yml
Keep all existing values and ADD these Chirpy-specific fields:

```yaml
title: "AI Tech Resource Blog"
description: "Structured AI/LLM data resource for developers and power users."
url: "https://www.jsonhouse.com"
baseurl: ""
lang: "en"
timezone: Asia/Seoul

theme: jekyll-theme-chirpy

markdown: kramdown
highlighter: rouge
permalink: /posts/:title/

plugins:
  - jekyll-sitemap
  - jekyll-seo-tag
  - jekyll-feed

toc: true
comments: false
math: false
mermaid: false

social:
  name: "AI Tech Resource Blog"
  links: []

paginate: 10

twitter:
  username: ""

author:
  name: "AI Tech Resource Blog"

defaults:
  - scope:
      path: ""
      type: "posts"
    values:
      layout: "post"
      toc: true
      author: ai_tech_blog

exclude:
  - Gemfile
  - Gemfile.lock
  - PIPELINE_PROMPT.md
  - PROJECT_CONTEXT.md
  - CLAUDE.md
  - SEO_GUIDE.md
  - SOURCES.md
  - "*.docx"
  - node_modules
  - vendor
  - pipeline_output

feed:
  categories:
    - ai-models
    - ai-developer-tools
    - prompt-engineering
    - ai-productivity
    - ai-data
    - ai-safety
```

---

### Step 3. Create _data/authors.yml
Create file _data/authors.yml with this content:

```yaml
ai_tech_blog:
  name: "AI Tech Resource Blog"
  url: https://www.jsonhouse.com
```

---

### Step 4. Create _data/contact.yml
Create file _data/contact.yml with this content:

```yaml
[]
```

---

### Step 5. Create _data/share.yml
Create file _data/share.yml with this content:

```yaml
[]
```

---

### Step 6. Update all posts front matter
For every file in _posts/, check front matter and add if missing:
- toc: true
- author: ai_tech_blog

Do NOT change title, date, categories, tags, or description.

---

### Step 7. Add copyright to footer
Create or edit _includes/footer.html and add at the bottom:

```html
<p style="text-align:center; font-size:0.85rem; color:#888; margin-top:1rem;">
  © 2026 AI Tech Resource Blog (jsonhouse.com). All rights reserved.
  Unauthorized reproduction or redistribution is strictly prohibited.
</p>
```

If _includes/footer.html does not exist, check if Chirpy provides it via the gem.
In that case, create _includes/footer.html and add only the copyright paragraph,
then at the top include the original with: {{ site.theme | ... }}
Actually: just append the copyright block to _layouts/default.html before closing </body> if footer override is complex.

---

### Step 8. Create LICENSE file
Create LICENSE file in project root with this content:

```
© 2026 AI Tech Resource Blog (jsonhouse.com)
All Rights Reserved.

The content, design, and code of this site are protected by copyright law.
Unauthorized copying, reproduction, or distribution of any material
from this site without express written permission is strictly prohibited.
```

---

### Step 9. Preserve these files — do NOT overwrite
- llms.txt
- robots.txt
- ads.txt
- CNAME
- api/ (entire folder)
- category/ (entire folder)
- _posts/ (entire folder)
- CLAUDE.md
- pipeline_output/ (entire folder)

---

### Step 10. Test locally
Run:
```
bundle exec jekyll serve
```

Then verify:
- Home page loads with Chirpy sidebar
- Dark mode toggle appears
- At least one post renders with TOC
- /llms.txt accessible
- /sitemap.xml accessible
- No build errors in terminal

---

### Step 11. Fix common Chirpy issues
If build fails with "layout not found":
- Chirpy requires layouts to extend its base. Remove custom _layouts/ files and let Chirpy handle them.
- If custom layouts are needed, start with: ---\nlayout: default\n---

If posts show unstyled:
- Confirm front matter has: layout: post

If categories 404:
- Confirm category/ files have correct front matter with layout: category (Chirpy built-in)

If assets not loading:
- Run: bundle exec jekyll build and check _site/ folder

---

## Success Criteria
- Home page shows Chirpy sidebar + dark mode toggle
- Posts render with TOC on the right side
- All existing posts are accessible at /posts/:title/
- llms.txt, sitemap.xml, feed.xml still working
- LICENSE file exists in root
- Copyright notice visible in footer
- No build errors
