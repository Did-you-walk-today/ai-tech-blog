---
layout: page
title: "Safety"
icon: fas fa-shield-alt
order: 6
---

<h2>AI Safety &amp; Ethics</h2>
<p>Security checklists, responsible AI practices, and OWASP LLM guidelines.</p>

<ul class="post-list">
{% assign cat_posts = site.posts | where_exp: "post", "post.categories contains 'ai-safety-ethics'" %}
{% for post in cat_posts %}
  <li>
    <a href="{{ post.url }}"><strong>{{ post.title }}</strong></a>
    <span style="color:#888; font-size:0.85em;"> — {{ post.date | date: "%b %d, %Y" }}</span>
    {% if post.description %}<br><span style="font-size:0.9em; color:#555;">{{ post.description }}</span>{% endif %}
  </li>
{% endfor %}
{% if cat_posts.size == 0 %}<li>No posts yet.</li>{% endif %}
</ul>
