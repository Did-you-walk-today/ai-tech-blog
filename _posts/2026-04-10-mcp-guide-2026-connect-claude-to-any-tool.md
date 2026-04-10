---
layout: post
published: false
title: "MCP Guide 2026: Connect Claude to Any Tool"
date: 2026-04-10 09:00:00 +0000
categories: [ai-developer-tools]
tags: [mcp, model-context-protocol, claude, anthropic, ai-tools, "2026"]
description: "Model Context Protocol (MCP) lets Claude connect to databases, APIs, and tools in 2026. Complete setup guide with 10 server examples and code."
canonical_url: https://www.jsonhouse.com/posts/mcp-guide-2026-connect-claude-to-any-tool
permalink: /posts/mcp-guide-2026-connect-claude-to-any-tool/
data_updated: 2026-04-10
toc: true
author: ai_tech_blog
schema_type: Article
format_type: C
category_id: CAT2
quality_score: auto
image:
  path: https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80
  alt: Model Context Protocol MCP guide 2026
sources:
  - https://modelcontextprotocol.io
  - https://github.com/modelcontextprotocol/servers
  - https://docs.anthropic.com/en/docs/claude-code/mcp
---

Before MCP, every AI-to-tool integration was custom glue code. You'd write a tool definition for your database, a different one for your GitHub API, another for your Slack. Each model had a different format. New tool = new integration project.

MCP ended that in November 2024. Anthropic's open protocol is now running 97 million monthly downloads and every major AI provider has adopted it. It works like USB-C — any MCP server plugs into any MCP client without custom adapters. One integration standard for the entire AI ecosystem.

This guide gets you from zero to Claude querying your database and reading your GitHub issues in under 10 minutes.

---

## TL;DR

- **MCP** is an open protocol that gives Claude structured access to external tools and data sources.
- Claude Code supports MCP natively — add servers via `claude mcp add` in one command.
- The **host** (Claude Code) connects to **MCP servers** (your tools) through a **client** layer.
- Over **200 MCP servers** are publicly available covering databases, APIs, browsers, and dev tools.
- No API key sharing or custom plugin code required — servers run locally or on your infrastructure.

---

## What MCP Actually Does

![MCP architecture: Claude connecting to external tools](https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=80)
_Photo: [Unsplash](https://unsplash.com)_

The practical result: Claude can query your Postgres database, read your GitHub issues, search your Notion docs, and run browser automation — all in a single conversation, with no custom integration code on your end.

> **Tip:** The fastest way to understand MCP value: add the filesystem server, point it at your project, and ask Claude to explain a function by reading the actual code. No copy-pasting. No context window filling. Claude just reads it.

---

## MCP Architecture

MCP uses a three-component model:

| Component | Role | Example |
|-----------|------|---------|
| **Host** | The AI application that manages connections | Claude Code, Claude Desktop |
| **Client** | Protocol handler inside the host (1:1 per server) | Built into Claude Code |
| **Server** | External process exposing tools and resources | `@modelcontextprotocol/server-postgres` |

Each MCP server exposes three primitives:

- **Tools** — Functions Claude can call (e.g., `query_database`, `create_issue`)
- **Resources** — Data Claude can read (e.g., file contents, API responses)
- **Prompts** — Pre-built prompt templates the server provides

Communication uses JSON-RPC 2.0 over stdio (local) or HTTP with Server-Sent Events (remote). Local servers are the most common and run entirely on your machine — no data leaves your environment.

---

## Setup: Adding MCP Servers to Claude Code

### Prerequisites

- Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- Node.js 18+ or Python 3.10+ depending on the server
- A Claude Pro or Max subscription

![MCP setup in Claude Code terminal](/assets/img/posts/mcp-connected.jpg)
_Screenshot: Claude Code after connecting MCP servers — provide this from your own setup_{: .shadow }

### Method 1: CLI (Recommended)

```bash
# Add a server by package name
claude mcp add @modelcontextprotocol/server-filesystem

# Add with custom arguments
claude mcp add @modelcontextprotocol/server-postgres \
  --env DATABASE_URL="postgresql://localhost/mydb"

# List installed servers
claude mcp list

# Remove a server
claude mcp remove server-filesystem
```

### Method 2: Config File

MCP servers are stored in `~/.claude/mcp.json`. You can edit this directly:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/you/projects"],
      "env": {}
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "postgresql://localhost/mydb"
      }
    }
  }
}
```

### Verify the Connection

```bash
# Start Claude Code and check tool availability
claude
> /mcp

# Claude will list all connected servers and their available tools
```

---

## 10 MCP Servers Worth Installing in 2026

```json
{
  "data_updated": "2026-04-10",
  "total_available_servers": 200,
  "servers": [
    {
      "name": "Filesystem",
      "package": "@modelcontextprotocol/server-filesystem",
      "category": "File System",
      "tools": ["read_file", "write_file", "list_directory", "search_files"],
      "use_case": "Read and write files in specified directories",
      "install": "claude mcp add @modelcontextprotocol/server-filesystem /path/to/dir",
      "local_only": true,
      "official": true
    },
    {
      "name": "PostgreSQL",
      "package": "@modelcontextprotocol/server-postgres",
      "category": "Database",
      "tools": ["query", "list_tables", "describe_table"],
      "use_case": "Read-only SQL queries against your Postgres database",
      "install": "claude mcp add @modelcontextprotocol/server-postgres --env DATABASE_URL=...",
      "local_only": true,
      "official": true
    },
    {
      "name": "GitHub",
      "package": "@modelcontextprotocol/server-github",
      "category": "Code Repository",
      "tools": ["list_repos", "get_issue", "create_issue", "search_code", "get_pr"],
      "use_case": "Read/write GitHub issues, PRs, and code search",
      "install": "claude mcp add @modelcontextprotocol/server-github --env GITHUB_TOKEN=...",
      "local_only": false,
      "official": true
    },
    {
      "name": "Brave Search",
      "package": "@modelcontextprotocol/server-brave-search",
      "category": "Web Search",
      "tools": ["web_search", "local_search"],
      "use_case": "Real-time web search without leaving Claude Code",
      "install": "claude mcp add @modelcontextprotocol/server-brave-search --env BRAVE_API_KEY=...",
      "local_only": false,
      "official": true
    },
    {
      "name": "Puppeteer",
      "package": "@modelcontextprotocol/server-puppeteer",
      "category": "Browser Automation",
      "tools": ["navigate", "screenshot", "click", "fill_form", "extract_content"],
      "use_case": "Headless browser control for scraping and E2E testing",
      "install": "claude mcp add @modelcontextprotocol/server-puppeteer",
      "local_only": true,
      "official": true
    },
    {
      "name": "SQLite",
      "package": "@modelcontextprotocol/server-sqlite",
      "category": "Database",
      "tools": ["query", "list_tables", "create_table", "insert"],
      "use_case": "Full read/write access to local SQLite databases",
      "install": "claude mcp add @modelcontextprotocol/server-sqlite /path/to/db.sqlite",
      "local_only": true,
      "official": true
    },
    {
      "name": "Slack",
      "package": "@modelcontextprotocol/server-slack",
      "category": "Communication",
      "tools": ["list_channels", "post_message", "get_thread", "search_messages"],
      "use_case": "Read Slack channels and post messages from Claude",
      "install": "claude mcp add @modelcontextprotocol/server-slack --env SLACK_TOKEN=...",
      "local_only": false,
      "official": true
    },
    {
      "name": "Google Maps",
      "package": "@modelcontextprotocol/server-google-maps",
      "category": "Location",
      "tools": ["geocode", "reverse_geocode", "search_places", "get_directions"],
      "use_case": "Location data and directions for apps with geo features",
      "install": "claude mcp add @modelcontextprotocol/server-google-maps --env MAPS_API_KEY=...",
      "local_only": false,
      "official": true
    },
    {
      "name": "Sentry",
      "package": "@modelcontextprotocol/server-sentry",
      "category": "Observability",
      "tools": ["get_issues", "get_event", "list_projects", "resolve_issue"],
      "use_case": "Query Sentry errors directly from your coding session",
      "install": "claude mcp add @modelcontextprotocol/server-sentry --env SENTRY_TOKEN=...",
      "local_only": false,
      "official": true
    },
    {
      "name": "Memory",
      "package": "@modelcontextprotocol/server-memory",
      "category": "Persistence",
      "tools": ["store", "retrieve", "list", "delete"],
      "use_case": "Persistent key-value memory across Claude sessions",
      "install": "claude mcp add @modelcontextprotocol/server-memory",
      "local_only": true,
      "official": true
    }
  ]
}
```

---

## Real Workflow Examples

### Example 1: Debug a Production Error End-to-End

With Sentry + GitHub + Filesystem MCP installed:

```
You: "Find the most recent unresolved Sentry error in the payments service,
     locate the relevant code, and suggest a fix."

Claude:
1. [Sentry] Queries latest unresolved issues → finds NullPointerException in checkout.py:142
2. [GitHub] Searches codebase for checkout.py → retrieves current implementation
3. [Filesystem] Reads local version with recent uncommitted changes
4. Analyzes root cause and writes a patch
```

### Example 2: Generate a Report from Live Data

With PostgreSQL + Filesystem MCP:

```
You: "Query the orders table for last week's revenue by product category
     and save it as a CSV to /reports/weekly-revenue.csv"

Claude:
1. [PostgreSQL] Runs aggregation query
2. [Filesystem] Writes CSV to specified path
3. Reports row count and total revenue figure
```

### Example 3: Automate a Web Form

With Puppeteer MCP:

```
You: "Go to our staging environment at localhost:3000, log in with
     test@example.com/password123, and verify the checkout flow works."

Claude:
1. [Puppeteer] Navigates to localhost:3000
2. Fills login form and submits
3. Walks through checkout steps
4. Reports pass/fail with screenshot
```

---

## Security Considerations

MCP servers run with the permissions of the process that starts them. Before installing any server:

- **Review the package source** — prefer the official `@modelcontextprotocol/` namespace
- **Scope filesystem access** — pass only the directories Claude needs, not `~/`
- **Use read-only database connections** — create a dedicated read-only DB user for MCP
- **Rotate tokens regularly** — MCP server tokens stored in `mcp.json` should be short-lived where possible
- **Audit tool calls** — Claude Code logs all MCP tool invocations; review them in `.claude/logs/`

---

## Frequently Asked Questions

### Does MCP work with Claude.ai (the web interface)?

MCP is currently supported in Claude Code (CLI) and Claude Desktop. The claude.ai web interface does not support custom MCP servers as of April 2026. For MCP-enabled workflows, Claude Code is the primary interface.

### Can I build my own MCP server?

Yes. Anthropic provides SDKs in TypeScript and Python. A minimal server takes about 50 lines of code. The TypeScript SDK (`@modelcontextprotocol/sdk`) is the more mature option. See the official spec at `modelcontextprotocol.io` for the full schema.

### Are MCP servers safe to use with proprietary code?

Servers marked `local_only: true` (like Filesystem, SQLite, Puppeteer) run entirely on your machine — no data is sent to any external service beyond what Claude Code itself sends to Anthropic's API. For servers that connect to external APIs (GitHub, Slack), data flows through those services' standard APIs under their existing privacy policies.

### How many MCP servers can I run simultaneously?

There is no hard limit. In practice, 5–10 servers covers most workflows. Each server spawns a separate process; memory usage scales linearly with the number of active servers. Unused servers can be disabled in `mcp.json` without uninstalling.

---

## Related Posts

- [Best AI Coding Tools 2026: Claude Code vs Cursor vs Copilot](/posts/best-ai-coding-tools-2026/) — full tool comparison with benchmark data
- [Claude Code Getting Started 2026: Install to First Agent](/posts/claude-code-getting-started-2026/) — step-by-step setup guide for Claude Code
- [Best LLMs for Coding 2026: Benchmark Results](/posts/best-llms-for-coding-2026-benchmark-results/) — model comparison for developer use cases

---

Last updated: 2026-04-10
