---
layout: page
title: "AI Data"
description: "Structured AI datasets from Json House: weekly LLM API pricing snapshots, statistical resources, and verification data, all published as machine-readable JSON."
icon: fas fa-chart-bar
order: 5
---

<p>Structured datasets, pricing databases, and statistical resources for AI.</p>

<ul class="post-list">
{% assign cat_posts = site.posts | where_exp: "post", "post.categories contains 'ai-data' or post.categories contains 'ai-data-statistics'" %}
{% for post in cat_posts %}
  <li>
    <a href="{{ post.url }}"><strong>{{ post.title }}</strong></a>
    <span style="color:#888; font-size:0.85em;"> — {{ post.date | date: "%b %d, %Y" }}</span>
    {% if post.description %}<br><span style="font-size:0.9em; color:#555;">{{ post.description }}</span>{% endif %}
  </li>
{% endfor %}
{% if cat_posts.size == 0 %}<li>No posts yet.</li>{% endif %}
</ul>
