# OpenSkills

Universal skills loader for AI coding agents

One CLI. Every agent. Same format as Claude Code.

## Quick Start

```bash
npx openskills install anthropics/skills
npx openskills sync
```

By default, installs are project-local (`./.claude/skills`, or `./.agent/skills` with `--universal`). Use `--global` for `~/.claude/skills`.

## What Is OpenSkills?

OpenSkills brings Anthropic's skills system to every AI coding agent — Claude Code, Cursor, Windsurf, Aider, Codex, and anything that can read `AGENTS.md`.

Think of it as the universal installer for `SKILL.md`.

## Why OpenSkills

- Exact Claude Code compatibility — same prompt format, same marketplace, same folder structure
- Universal — works with Claude Code, Cursor, Windsurf, Aider, Codex, and more
- Progressive disclosure — load skills only when needed (keeps context clean)
- Repo-friendly — skills live in your project and can be versioned
- Private friendly — install from local paths or private git repos

## How It Works

### Claude Code System Prompt (Skills)

Claude Code ships skills as `SKILL.md` files and exposes them inside a `<available_skills>` block. When the user asks for a task, Claude dynamically loads the matching skill.

```xml
<available_skills>
<skill>
<name>pdf</name>
<description>Comprehensive PDF manipulation toolkit for extracting text and tables...</description>
<location>plugin</location>
</skill>
</available_skills>
```

### OpenSkills: Same Format, Universal Loader

OpenSkills generates the exact same `<available_skills>` XML in your `AGENTS.md` and loads skills via:

```bash
npx openskills read <skill-name>
```

So any agent that can read `AGENTS.md` can use Claude Code skills without needing Claude Code itself.

### Side-by-Side

| Aspect | Claude Code | OpenSkills |
| :--- | :--- | :--- |
| Prompt Format | `<available_skills>` XML | Same XML |
| Skill Storage | `.claude/skills/` | `.claude/skills/` (default) |
| Invocation | `Skill("name")` tool | `npx openskills read <name>` |
| Marketplace | Anthropic marketplace | GitHub (`anthropics/skills`) |
| Progressive Disclosure | ✅ | ✅ |

## Install Skills

**From Anthropic Marketplace**
```bash
npx openskills install anthropics/skills
```

**From Any GitHub Repo**
```bash
npx openskills install your-org/your-skills
```

**From a Local Path**
```bash
npx openskills install ./local-skills/my-skill
```

**From Private Git Repos**
```bash
npx openskills install git@github.com:your-org/private-skills.git
```

## Universal Mode (Multi-Agent Setups)

If you use Claude Code and other agents with one `AGENTS.md`, install to `.agent/skills/` to avoid conflicts with Claude's plugin marketplace:

```bash
npx openskills install anthropics/skills --universal
```

Priority order (highest wins):
1. `./.agent/skills/`
2. `~/.agent/skills/`
3. `./.claude/skills/`
4. `~/.claude/skills/`

## Commands

```bash
npx openskills install <source> [options]  # Install from GitHub, local path, or private repo
npx openskills sync [-y] [-o <path>]       # Update AGENTS.md (or custom output)
npx openskills list                        # Show installed skills
npx openskills read <name>                 # Load skill (for agents)
npx openskills update [name...]            # Update installed skills (default: all)
npx openskills manage                      # Remove skills (interactive)
npx openskills remove <name>               # Remove specific skill
```

**Flags**
- `--global` — Install globally to `~/.claude/skills` (default: project install)
- `--universal` — Install to `.agent/skills/` instead of `.claude/skills/`
- `-y, --yes` — Skip prompts (useful for CI)
- `-o, --output <path>` — Output file for sync (default: AGENTS.md)

## The SKILL.md Format

OpenSkills uses Anthropic's exact format:

```yaml
---
name: pdf
description: Comprehensive PDF manipulation toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, and handling forms.
---
```
```markdown
# PDF Skill Instructions

When the user asks you to work with PDFs, follow these steps:
1. Install dependencies: `pip install pypdf2`
2. Extract text using scripts/extract_text.py
3. Use references/api-docs.md for details
```

Skills are loaded on demand, keeping your agent's context clean and focused.

## FAQ

**Why CLI instead of MCP?**
MCP is for dynamic tools. Skills are static instructions + resources.
- Skills are just files → no server required
- Works with every agent → no MCP support needed
- Matches Anthropic's design → SKILL.md is the spec

MCP and skills solve different problems. OpenSkills keeps skills lightweight and universal.
