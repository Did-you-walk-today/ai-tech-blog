---
layout: page
title: "Prompts"
icon: fas fa-comment-dots
order: 3
---

<h2>Prompt Engineering</h2>
<p>Prompt libraries, system prompt templates, and engineering techniques.</p>

<ul class="post-list">
{% assign cat_posts = site.posts | where_exp: "post", "post.categories contains 'prompt-engineering'" %}
{% for post in cat_posts %}
  <li>
    <a href="{{ post.url }}"><strong>{{ post.title }}</strong></a>
    <span style="color:#888; font-size:0.85em;"> — {{ post.date | date: "%b %d, %Y" }}</span>
    {% if post.description %}<br><span style="font-size:0.9em; color:#555;">{{ post.description }}</span>{% endif %}
  </li>
{% endfor %}
{% if cat_posts.size == 0 %}<li>No posts yet.</li>{% endif %}
</ul>
