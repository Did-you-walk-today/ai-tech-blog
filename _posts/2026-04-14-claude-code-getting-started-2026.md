---
layout: post
published: false
title: "Claude Code Getting Started 2026: Install to Agent"
date: 2026-04-14 09:00:00 +0000
categories: [ai-developer-tools]
tags: [claude-code, anthropic, ai-coding, getting-started, cli, agent, "2026"]
description: "Install Claude Code and run your first autonomous agent task in under 10 minutes. Step-by-step 2026 guide covering setup, key commands, CLAUDE.md, and real workflows."
canonical_url: https://www.jsonhouse.com/posts/claude-code-getting-started-2026
permalink: /posts/claude-code-getting-started-2026/
data_updated: 2026-04-10
toc: true
author: ai_tech_blog
schema_type: Article
format_type: C
category_id: CAT2
quality_score: auto
image:
  path: https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80
  alt: Claude Code terminal AI coding agent 2026
sources:
  - https://docs.anthropic.com/en/docs/claude-code/overview
  - https://docs.anthropic.com/en/docs/claude-code/quickstart
  - https://claude.com/pricing
---

Claude Code doesn't work like an IDE plugin. You don't get autocomplete suggestions while you type. Instead, you describe what needs to happen, and it reads your codebase, edits files, runs tests, uses git, and executes shell commands — autonomously. Then you review the result.

That's a different mental model. Most developers either click with it immediately or bounce off in the first hour. The ones who bounce off usually gave up before they hit the real value: handing Claude a 200K-token codebase and a complex task, then watching it do in 3 minutes what would take you 45.

This guide gets you installed, configured, and past that first-hour friction as fast as possible.

---

## TL;DR

- **Install** in one command: `npm install -g @anthropic-ai/claude-code`
- **Requires** a Claude Pro ($20/mo) or Max ($100/mo) subscription — no separate API key needed.
- **CLAUDE.md** is your project configuration file — Claude reads it automatically at the start of every session.
- **Slash commands** (`/plan`, `/review`, `/commit`) are the fastest way to trigger structured workflows.
- **MCP servers** extend Claude Code to connect to databases, APIs, and external tools.

---

![Claude Code running in terminal](/assets/img/posts/claude-conde-terminal.png)
_Screenshot: Claude Code session in terminal — provide this from your own setup_{: .shadow }

## Prerequisites

| Requirement | Minimum | Check command |
|-------------|---------|--------------|
| Node.js | 18.0.0 | `node --version` |
| npm | 9.0.0 | `npm --version` |
| Claude subscription | Pro ($20/mo) or Max ($100/mo) | claude.com/settings |
| OS | macOS 12+, Ubuntu 20.04+, Windows 11 (WSL2) | — |

> **Note:** An API key (`ANTHROPIC_API_KEY`) also works if your team prefers usage-based billing over a flat subscription. Pro/Max subscriptions include the conversational Claude interface too — you're not paying twice.

---

## Installation

```bash
# Install Claude Code globally
npm install -g @anthropic-ai/claude-code

# Verify installation
claude --version

# Authenticate (opens browser for OAuth login)
claude login
```

If you are using an API key instead of OAuth:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
claude
```

---

## Your First Session

Navigate to any project directory and start Claude Code:

```bash
cd ~/your-project
claude
```

You will see the Claude Code prompt. Try these starter tasks:

```
> What does this project do?
> Show me the most complex function in this codebase
> Are there any obvious bugs in the authentication module?
> Run the tests and summarize what failed
```

Claude Code reads your files, executes commands, and responds in your terminal. It will ask for permission before writing files or running commands that modify state.

---

## Key Commands Reference

```json
{
  "data_updated": "2026-04-10",
  "commands": [
    {
      "command": "/help",
      "description": "Show all available slash commands",
      "scope": "global"
    },
    {
      "command": "/plan",
      "description": "Enter plan mode — Claude proposes changes before executing anything",
      "scope": "global",
      "best_for": "Multi-file changes, architectural decisions"
    },
    {
      "command": "/review",
      "description": "Code review of recent changes or specified files",
      "scope": "global",
      "best_for": "Pre-commit review, catching issues before push"
    },
    {
      "command": "/commit",
      "description": "Stage, write a commit message, and commit current changes",
      "scope": "global",
      "best_for": "Quick commits with auto-generated messages"
    },
    {
      "command": "/mcp",
      "description": "List connected MCP servers and their available tools",
      "scope": "global",
      "best_for": "Debugging MCP connectivity"
    },
    {
      "command": "/clear",
      "description": "Clear conversation context (start fresh without restarting)",
      "scope": "global",
      "best_for": "Switching tasks, context getting stale"
    },
    {
      "command": "/init",
      "description": "Generate a CLAUDE.md file for the current project",
      "scope": "project",
      "best_for": "New project setup"
    },
    {
      "command": "! <command>",
      "description": "Run a shell command and inject the output into Claude's context",
      "scope": "global",
      "example": "! git log --oneline -10",
      "best_for": "Providing external context (logs, test output, git history)"
    }
  ]
}
```

---

## Understanding CLAUDE.md

`CLAUDE.md` is a Markdown file you place in your project root. Claude Code reads it automatically at the start of every session. Think of it as a standing brief that tells Claude about your project, tech stack, and working conventions — so you do not have to explain them every session.

### Minimal CLAUDE.md

```markdown
# Project: Payment Service

## Tech Stack
- Python 3.12, FastAPI, PostgreSQL 15
- pytest for testing, black + ruff for formatting
- Docker Compose for local development

## Key Rules
- Never commit to main directly — always branch and PR
- Run `make test` before any commit
- Database migrations use Alembic — never modify schema directly

## Architecture
- `app/api/` — FastAPI route handlers
- `app/services/` — Business logic (no database calls here)
- `app/repositories/` — Database layer (SQLAlchemy)
- `tests/` — Mirror app/ structure

## Test Database
Local: postgresql://localhost:5432/payment_test
Run: docker compose up -d db
```

### Generate CLAUDE.md Automatically

```bash
claude
> /init
```

Claude Code analyzes your codebase and generates a `CLAUDE.md` draft. Review and edit it — especially the rules section, which requires your judgment about project conventions.

---

## Core Workflows

### Workflow 1: Implement a Feature with Plan Mode

Always use `/plan` for changes that touch more than two files:

```
> /plan Add rate limiting to all API endpoints using Redis.
         Limit: 100 requests per minute per user ID.
```

Claude Code will:
1. Analyze your existing code structure
2. Propose a file-by-file implementation plan
3. Wait for your approval before writing anything

This prevents Claude from making unintended changes while you think through the approach.

---

### Workflow 2: Debug a Failing Test

```
> The test `test_checkout_flow` is failing. Find the root cause and fix it.
```

Claude Code will:
1. Run the failing test to see the error
2. Trace through the relevant code
3. Identify the root cause
4. Propose and implement a fix
5. Re-run the test to confirm it passes

---

### Workflow 3: Code Review Before Committing

```
> /review
```

Claude reviews all staged and unstaged changes, categorizes issues by severity (CRITICAL / HIGH / MEDIUM / LOW), and provides specific line-level feedback. Fix issues before committing.

---

### Workflow 4: Git Workflow Integration

```
# Commit with auto-generated message
> /commit

# Claude inspects diff, writes a conventional commit message, and commits
# feat: add Redis rate limiting to API endpoints (100 req/min per user)

# For PR creation (requires GitHub CLI)
> Create a pull request for the current branch with a summary of changes
```

---

### Workflow 5: Understand an Unfamiliar Codebase

```
> Explain how authentication works in this project. Trace from the login endpoint
  to the JWT token generation and storage.
```

Claude Code reads the relevant files, traces the code path, and gives you a clear explanation with specific file and line references — useful for onboarding to a new repository or returning to code you have not touched in months.

---

## Permission Modes

Claude Code has three permission settings that control how much it can do without asking:

| Mode | Behavior | Best For |
|------|----------|----------|
| Default | Asks before writing files or running commands | General daily use |
| Auto-accept edits | Writes files without asking, still confirms commands | Trusted, well-scoped tasks |
| Full auto | Executes everything autonomously | Scripted pipelines, non-interactive runs |

Switch modes in the session:

```bash
# Start in auto-accept mode
claude --auto-accept-edits

# Start in full auto (use with caution)
claude --dangerously-skip-permissions
```

The default mode is the right choice for most interactive work. Reserve full auto for scripted, well-understood tasks where you have reviewed the plan in advance.

---

## Adding MCP Servers

MCP (Model Context Protocol) servers extend Claude Code with access to external tools. Install any server in one command:

```bash
# Connect to your Postgres database (read-only)
claude mcp add @modelcontextprotocol/server-postgres \
  --env DATABASE_URL="postgresql://localhost/mydb"

# Add GitHub integration
claude mcp add @modelcontextprotocol/server-github \
  --env GITHUB_TOKEN="ghp_..."

# Add web search
claude mcp add @modelcontextprotocol/server-brave-search \
  --env BRAVE_API_KEY="..."
```

See the [MCP Guide 2026](/posts/mcp-guide-2026-connect-claude-to-any-tool/) for a full list of available servers.

---

## Common Mistakes to Avoid

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Starting without CLAUDE.md | Claude guesses project conventions | Run `/init` on day one |
| Using full auto on unfamiliar tasks | Unintended file changes | Default mode until you know the codebase |
| Long sessions without `/clear` | Context drift, stale assumptions | Clear context when switching tasks |
| Asking for features without `/plan` | Claude makes changes you did not anticipate | Use `/plan` for any change touching 3+ files |
| Ignoring `/review` findings | Bugs in production | Fix CRITICAL and HIGH before committing |

---

## Frequently Asked Questions

### Does Claude Code work without an internet connection?

No. Claude Code sends your code to Anthropic's API for processing. It requires an active internet connection and a valid Claude subscription or API key. All data is transmitted over HTTPS. Anthropic's data retention policy for Claude Code sessions can be found in the Claude privacy policy.

### Can I use Claude Code in CI/CD pipelines?

Yes. Use the `--print` flag for non-interactive output and set `ANTHROPIC_API_KEY` as a CI secret. A common pattern is to run Claude Code in CI for automated code review on every pull request.

```bash
# Non-interactive review in CI
claude --print "Review the diff and list any CRITICAL or HIGH issues" \
  --no-color
```

### How does Claude Code handle large repositories?

Claude Code uses your file system directly and loads files into context on demand rather than indexing the entire repository upfront. For very large repositories (>100K files), response times on repository-wide questions may be slower. The 200K token context window handles most practical codebases; for repositories larger than ~50K lines of code, scoping your questions to specific directories or modules improves both speed and accuracy.

### Is Claude Code the same as using Claude.ai?

No. Claude.ai is the web chat interface. Claude Code is a terminal-based coding agent that can read your local files, run commands, and interact with your development environment. Claude.ai cannot access your local filesystem. The underlying models overlap (both can use Claude Sonnet 4.6 or Opus 4.6), but the capabilities are fundamentally different.

---

## Related Posts

- [Best AI Coding Tools 2026: Claude Code vs Cursor vs Copilot](/posts/best-ai-coding-tools-2026/) — how Claude Code compares to IDE-based alternatives
- [MCP Guide 2026: Connect Claude to Any Tool](/posts/mcp-guide-2026-connect-claude-to-any-tool/) — extend Claude Code with databases, APIs, and more
- [Claude System Prompt Templates 2026: 25+ Ready](/posts/claude-system-prompt-templates-2026/) — CLAUDE.md templates to configure Claude for specific roles

---

Last updated: 2026-04-10
