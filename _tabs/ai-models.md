---
layout: page
title: "AI Models"
description: "Compare leading LLMs on capability, context limits, and real subscription cost. Benchmark reports and model analysis, each shipped with a public dataset."
icon: fas fa-robot
order: 1
---

<p>Benchmark reports, model comparisons, and LLM pricing guides.</p>

<ul class="post-list">
{% assign cat_posts = site.posts | where_exp: "post", "post.categories contains 'ai-models-intelligence'" %}
{% for post in cat_posts %}
  <li>
    <a href="{{ post.url }}"><strong>{{ post.title }}</strong></a>
    <span style="color:#888; font-size:0.85em;"> — {{ post.date | date: "%b %d, %Y" }}</span>
    {% if post.description %}<br><span style="font-size:0.9em; color:#555;">{{ post.description }}</span>{% endif %}
  </li>
{% endfor %}
{% if cat_posts.size == 0 %}<li>No posts yet.</li>{% endif %}
</ul>
