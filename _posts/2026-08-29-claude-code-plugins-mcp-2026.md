---
title: "Claude Code Plugins and MCP 2026: How They Differ"
description: "A plugin packages capability; MCP connects to it. What separates the two, what each keeps resident in your context window, and why most useful plugins go unfound."
date: 2026-08-29 09:00:00 +0000
last_modified_at: 2026-08-29 09:00:00 +0000
categories: [ai-developer-tools]
tags: [mcp, claude-code, plugins, agent-skills, developer-tools, "2026"]
format: A
cluster: CLUSTER_DEVTOOLS
image:
  path: /assets/img/posts/claude-code-plugins-mcp-2026-cover.jpg
  alt: "A curl of steel shaving lifting off a freshly machined surface, cyan light raking one edge and amber catching the other"
data_updated: 2026-08-29
author: jsonhouse
faq:
  - q: "What is the difference between a Claude Code plugin and an MCP server?"
    a: "They sit at different layers. MCP is an open protocol for connecting an AI application to an external system — a database, an API, a browser. A plugin is a packaging and distribution format that can carry skills, subagents, hooks, LSP servers and MCP servers together, installed with one command and toggled with one switch. A plugin can contain MCP servers, so the two are complementary rather than parallel choices."
  - q: "Do MCP tool definitions still load into every request in 2026?"
    a: "Not by default in Claude Code. Tool search is the default path, and the documentation describes a discovery cache where a previously used remote server shows as 'connects on first use' rather than connecting at startup. Configurations that opt out — a custom ANTHROPIC_BASE_URL, ENABLE_TOOL_SEARCH=false, or a pre-4.5 model on Google Cloud's Agent Platform — fall back to the older behaviour."
  - q: "How do I find out what Claude Code plugins exist?"
    a: "Run /plugin and open the Discover tab, or browse the catalog at claude.com/plugins. The official Anthropic marketplace registers itself the first time you start Claude Code interactively, but the community marketplace does not — you add it yourself with `/plugin marketplace add anthropics/claude-plugins-community`. Until you run that command, its entire catalog is invisible to you."
  - q: "How much context does a plugin add?"
    a: "The /plugin details pane shows a Context cost estimate for how many tokens the plugin adds to your context window every turn, alongside its Last updated date and a Will install list of its components. Not every plugin supplies that data — for local or custom marketplaces the row may be missing entirely."
  - q: "When is a skill the better choice than an MCP server?"
    a: "When the work is instructions rather than a live connection. A skill's body loads only when used, and its listing entry is capped at 1,536 characters of description text. If your 'server' mostly tells Claude how to do something with tools it already has, a skill carries that at near-zero resident cost."
---

Claude Code now has two ways to add capability, and they are easy to confuse because they often arrive together. MCP connects the assistant to something outside it. A plugin packages a set of extensions — including MCP servers — so they install and update as one unit. Understanding which is which decides where your context budget goes, and, increasingly, whether you find the useful thing at all.

## TL;DR

- **MCP is a protocol.** It connects an AI application to external systems and keeps a live connection open while the session runs.
- **A plugin is a packaging format.** It bundles skills, subagents, hooks, LSP servers, executables — and MCP servers — behind one install and one toggle.
- Claude Code's MCP documentation describes tool search as **the default**, with a discovery cache reporting a server as `connects on first use`.
- A skill's listing entry is capped at **1,536 characters**; its body loads only on use, then stays for the session.
- The official marketplace registers itself; **the community marketplace does not**. Until you run one command, an entire catalog stays invisible.

## What MCP does, and what it costs

The [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) is an open standard for connecting AI applications to external systems. Its own documentation reaches for a hardware metaphor: "Think of MCP like a USB-C port for AI applications."

That framing is precise about the problem it solves. Before a shared protocol, every client needed a bespoke integration with every data source. MCP collapses that into one interface both sides implement once.

What a server exposes is a live capability. It runs as a process or a remote endpoint, it holds credentials, and it answers calls while the session is open. Reading a database, driving a browser, querying an issue tracker — the work happens outside the model, which only decides when to ask.

That design carries three costs, and they are structural rather than incidental.

**The tool definitions have to reach the model.** For the model to call a tool it must know the tool exists, what it takes, and what it returns. Historically that meant every connected server's schemas sat in the request whether or not the session touched them.

**A server is all-or-nothing.** You connect it and get its whole surface. A server exposing twenty tools contributes twenty tools' worth of description even when your task needs one.

**Distribution was left as an exercise.** MCP standardises the connection, not the delivery. Sharing a working setup with a teammate meant sharing config, install steps and credentials by hand.

The third cost is the one plugins were built to answer.

## What a plugin is

A [Claude Code plugin](https://code.claude.com/docs/en/plugins) is a directory with a manifest that can carry skills, subagents, hooks, LSP servers, background monitors, executables on `PATH`, default settings — and MCP servers, through a `.mcp.json` at the plugin root.

The [plugins reference](https://code.claude.com/docs/en/plugins-reference) is explicit about how those bundled servers behave: "Plugin MCP servers start automatically when the plugin is enabled," and there is no separate switch for them — they follow the parent plugin's enabled state.

So the relationship is containment, not substitution. Installing a plugin can be how an MCP server arrives on your machine. Anthropic's own official marketplace works exactly this way: its external-integration plugins for `github`, `slack`, `notion`, `linear`, `figma` and `sentry` are described as bundling "pre-configured MCP servers so you can connect Claude to external services without manual setup."

## The difference in one table

Two different layers, two different jobs.

| | MCP server | Plugin |
|---|---|---|
| What it is | Open connection protocol | Packaging and distribution format |
| Solves | Talking to an external system | Shipping, versioning and toggling a set of extensions |
| Unit of install | One server, configured by hand | One command, one manifest |
| Can contain the other | No | Yes — via `.mcp.json` |
| Lifecycle | Per-server configuration | All bundled components follow the plugin's enabled state |
| Scope options | Per configuration file | User, project, local, or managed |

> **Raw data**: [data/claude-code-plugins-mcp-2026.json](https://www.jsonhouse.com/data/claude-code-plugins-mcp-2026.json) — machine-readable structured data for AI crawlers and citation.

## What each component keeps resident

"Resident" means present in the model's context before you do anything; "on use" means it arrives when invoked. This is the table that decides what your window costs.

| Component | Resident at startup | Loaded on use | Published cost figure |
|---|---|---|---|
| MCP server (tool search on, default) | Tool names via discovery cache | Full schemas through `ToolSearch` | Not published |
| MCP server (tool search off) | Full tool definitions | — | Not published |
| Agent Skill | `description` + `when_to_use`, capped at 1,536 chars | Body, then stays for the session | 1,536-char listing cap |
| Hook | Nothing | Nothing — output only | n/a |
| Subagent | Its listing entry | Runs in its own context | Not published |
| `bin/` executable | Nothing | Nothing — called through Bash | n/a |

The first row is the one that has moved. Claude Code's [MCP documentation](https://code.claude.com/docs/en/mcp) describes tool search as "the default," and a cached remote server showing a status such as `cached 2h ago · connects on first use · 5 tools`. The tool list comes from a cache saved in a previous session; the server connects the first time Claude calls one of its tools.

Opting out is possible and sometimes involuntary. The docs name three cases where tool search is absent: a custom `ANTHROPIC_BASE_URL`, `ENABLE_TOOL_SEARCH=false`, and a model earlier than the Claude 4.5 generation on Google Cloud's Agent Platform. Those configurations keep the older cost model.

Anthropic does not publish a general token figure for tool definitions. The MCP page publishes limits in the other direction — a warning when tool output exceeds 10,000 tokens, and a 25,000-token default cap — but those govern what a server returns, not what its schemas occupy. Per plugin, the `/plugin` details pane does show a **Context cost** estimate of "how many tokens the plugin will add to your context window every turn," though the documentation notes that not every plugin supplies the data behind that field.

## The plugins are piling up faster than anyone finds them

Here is the practical problem that the layer diagram does not capture. The official marketplace already ships plugins that would save an ordinary working day real time — `slack`, `notion`, `atlassian` for Jira and Confluence, `linear`, `asana`, `figma`, `sentry`, plus eleven language-server plugins that give Claude type errors and go-to-definition after every edit.

Almost nobody outside the developer bubble knows those exist.

The discovery path is not obvious, and part of it is not automatic. Claude Code registers the official Anthropic marketplace by itself the first time you start it interactively. The [community marketplace does not register itself](https://code.claude.com/docs/en/discover-plugins) — you have to know it exists and add it. One line registers the reviewed third-party catalog:
```shell
/plugin marketplace add anthropics/claude-plugins-community
```
Until someone runs that line, an entire reviewed catalog is invisible to them, and nothing in the interface announces that it is missing. The same is true of the demo marketplace, which also requires a manual add.

Even the browsing step assumes you know where to look. Plugins are listed under `/plugin` in the **Discover** tab, or in the web catalog at `claude.com/plugins`. Neither surfaces itself during ordinary work; you go there because you already suspected there was something to find.

The forgetting is documented too. Claude Code lists plugins you installed but have not used in at least two weeks across at least ten sessions under a **Not used recently** header, explicitly so you can find "plugins that still add startup and context cost even though you no longer use them." That feature exists because installing and forgetting is the normal outcome.

The gap, then, is not capability. It is that the catalog grows faster than the average user's map of it, and the cost of an unfound plugin is invisible — you simply keep doing the task by hand, never knowing the shortcut shipped months ago.

## Choosing between them

Since a plugin can contain MCP servers, the question is rarely "which one." It is closer to: what is this capability actually made of?

**Use an MCP server when the work needs a live connection** — state, credentials, or a running process. A database session, an authenticated API, a browser being driven. Nothing lighter does that job.

**Use a skill when the work is instructions.** A great deal of what people build as servers is a procedure: check these things in this order, format the output this way, apply this house rule. Anthropic's [skills documentation](https://code.claude.com/docs/en/skills) is direct — "a skill's body loads only when it's used, so long reference material costs almost nothing until you need it."

The same page names the other side of that bargain: "Once a skill loads, its content stays in context across turns, so every line is a recurring token cost." Cheap while dormant, permanent once woken. Long reference material is fine; a bloated skill you invoke every session is not.

**Use a hook when the check is deterministic.** Hooks run as shell commands on tool events and never enter the model's context — our own pipeline runs thirty-plus post rules that way, and the model pays only for the lines a hook prints when something fails. We described that arrangement in [AI content quality gates](/posts/ai-content-quality-gates-2026/).

**Use a plugin to ship whichever of those you built.** It is the layer that gives your work a version, an install command and an off switch for a whole team.

For what else sits in this stack, our [AI coding tools comparison](/posts/best-ai-coding-tools-2026/) covers the surrounding landscape, and [LLM cache pricing](/posts/llm-cache-pricing-2026/) covers what resident context costs once it is billed.

## Methodology

Every claim here is read from vendor documentation on 2026-08-29, not measured by us. Sources: the Claude Code plugins, plugins reference, discover-plugins, skills and MCP pages at `code.claude.com`, and the Model Context Protocol introduction at `modelcontextprotocol.io`. Direct quotations are reproduced verbatim and linked at the point of the claim.

Where a document does not state a figure, the table records `Not published` rather than an estimate. No token counts in this post are our own measurements.

## Limitations

This is a documentation review, not a benchmark. We did not measure token usage on any configuration, so the post cannot tell you what your setup costs — only what the vendor does and does not publish about the mechanism.

The marketplace contents listed here are the official catalog as documented on the retrieval date; catalogs change without notice. Claude Code's loading behaviour has already changed at least once in this area, and the three documented opt-outs from tool search mean readers on non-default configurations will see the older behaviour. Check `/context` and the `/plugin` details pane in your own session before acting on any third-party number.

## Update cadence

Reviewed when Claude Code changes how plugins or MCP servers load or are distributed, rather than on a fixed schedule — a calendar cadence would produce identical pages most months. Last checked 2026-08-29.

## FAQ

### What is the difference between a Claude Code plugin and an MCP server?

They sit at different layers. MCP is an open protocol for connecting an AI application to an external system — a database, an API, a browser. A plugin is a packaging and distribution format that can carry skills, subagents, hooks, LSP servers and MCP servers together, installed with one command and toggled with one switch. A plugin can contain MCP servers, so the two are complementary rather than parallel choices.

### Do MCP tool definitions still load into every request in 2026?

Not by default in Claude Code. Tool search is the default path, and the documentation describes a discovery cache where a previously used remote server shows as "connects on first use" rather than connecting at startup. Configurations that opt out — a custom `ANTHROPIC_BASE_URL`, `ENABLE_TOOL_SEARCH=false`, or a pre-4.5 model on Google Cloud's Agent Platform — fall back to the older behaviour.

### How do I find out what Claude Code plugins exist?

Run `/plugin` and open the **Discover** tab, or browse the catalog at `claude.com/plugins`. The official Anthropic marketplace registers itself the first time you start Claude Code interactively, but the community marketplace does not — you add it yourself with `/plugin marketplace add anthropics/claude-plugins-community`. Until you run that command, its entire catalog is invisible to you.

### How much context does a plugin add?

The `/plugin` details pane shows a **Context cost** estimate for how many tokens the plugin adds to your context window every turn, alongside its **Last updated** date and a **Will install** list of its components. Not every plugin supplies that data — for local or custom marketplaces the row may be missing entirely.

### When is a skill the better choice than an MCP server?

When the work is instructions rather than a live connection. A skill's body loads only when used, and its listing entry is capped at 1,536 characters of description text. If your "server" mostly tells Claude how to do something with tools it already has, a skill carries that at near-zero resident cost.

## Changelog

- **2026-08-29** — First published. Documentation reviewed at `code.claude.com` and `modelcontextprotocol.io` on this date.
