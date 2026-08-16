---
title: "What Are Skills"
description: "DSOM Guide document for What Are Skills."
type: "guide"
id: "docs/WHAT-ARE-SKILLS.md"
dsom_governance:
  domain: "AI"
  context_tier: "L2-Operational"
tags:
  - "dsom-protocol"
  - "diataxis-quadrant"
related_links:
  - "docs/reference/index.md"
nav_order: 10
layout: "default"
---

# What Are Claude Skills?

If you've been using Claude and wondered why it sometimes feels like starting from scratch with every conversation, you're not alone. That's exactly the problem Claude Skills solve.

## TL;DR

Claude Skills are reusable instruction packages that teach Claude specialized workflows and domain expertise. Think of them as "muscle memory" for AI - instead of explaining your preferences every time, Skills let Claude automatically apply your standards, processes, and knowledge when relevant.

## The Problem Skills Solve

Here's a scenario every Claude user has experienced:

- You spend 20 minutes explaining your coding standards to Claude
- Claude writes perfect code following your guidelines
- Next conversation: Claude has completely forgotten everything
- Repeat forever

This isn't a bug - it's how LLMs work. They don't retain memory between conversations. Every session starts fresh.

Skills fix this permanently.

With Skills, Claude can:
- Automatically apply your code style preferences
- Follow your testing workflows without reminders
- Use your templates for documents and presentations
- Execute multi-step procedures reliably

## What Exactly Is a Skill?

At its core, a Skill is just a folder containing a SKILL.md file. That's it.

```text
my-skill/
├── SKILL.md          # Required: instructions + metadata
├── scripts/          # Optional: executable code
├── references/       # Optional: additional docs
└── assets/           # Optional: templates, examples
```

The SKILL.md file has two parts:

1. **YAML Frontmatter** (metadata Claude always sees):
```yaml
---
name: code-reviewer
description: Reviews code for security vulnerabilities, performance issues, 
  and style violations. Use when reviewing pull requests or auditing code.
---
```

2. **Markdown Instructions** (loaded when the skill is triggered):
```markdown
# Code Review Process

## Step 1: Security Scan
Check for common vulnerabilities:
- SQL injection
- XSS attacks
- Hardcoded secrets
...
```

The genius is in the progressive disclosure:

| What Loads | When | Token Cost |
| :--- | :--- | :--- |
| Name + description | Always | ~100 tokens |
| Full instructions | When triggered | ~500-5000 tokens |
| Reference files | As needed | Unlimited |

This means you can install dozens of Skills without burning through your context window. Claude only loads what's relevant for the current task.

## Skills vs. Everything Else

If you're coming from other AI tools, here's how Skills compare:

### Skills vs. GPT Custom Instructions

| Feature | Claude Skills | GPT Custom Instructions |
| :--- | :--- | :--- |
| Persistence | Across all conversations | Single conversation |
| Can include code | Yes | No |
| File bundling | Unlimited reference files | No |
| Context efficiency | Loads only when relevant | Always consumes context |

### Skills vs. CLAUDE.md Files

Both customize Claude, but for different purposes:
- **CLAUDE.md**: Project-specific context that's always loaded (build commands, file structure, conventions)
- **Skills**: Reusable workflows that load on-demand across any project

Think of CLAUDE.md as "what you need to know about this codebase" and Skills as "how to do specific tasks."

### Skills vs. MCP (Model Context Protocol)

This is a common confusion:
- **MCP**: Gives Claude access to external data and tools
- **Skills**: Teaches Claude what to do with that data

They're complementary. MCP without Skills = powerful but generic. Skills without MCP = knowledgeable but limited.

## Real Examples of Useful Skills

### Development Skills

**TDD Workflow** - Forces test-driven development:
> When implementing any feature:
> 1. Write failing tests FIRST
> 2. Implement minimum code to pass
> 3. Refactor only after tests pass
> 4. Never write implementation before tests exist

**Systematic Debugging** - Prevents random fix attempts:
> When debugging:
> 1. Reproduce the issue reliably
> 2. Identify the root cause (not symptoms)
> 3. Write a test that captures the bug
> 4. Fix and verify the test passes

### Document Skills

Anthropic provides official Skills for:
- **Excel/xlsx** - Create spreadsheets with formulas and charts
- **PowerPoint/pptx** - Generate presentations with branding
- **Word/docx** - Create formatted documents
- **PDF** - Extract, fill forms, merge documents

### Productivity Skills

**Linear Issue Logging** - One user described their setup:
> "Now I just say 'log that auth bug' and it creates the issue with correct labels, deeplinks to relevant docs, and assigns to the right team"

## Best Practices from Power Users

### 1. Keep Your Global CLAUDE.md Minimal
Put only universally-applicable rules in `~/.claude/CLAUDE.md`:
- **Current date**: 2025-12-18
- **Git Commits**: Use conventional format
- **Style**: Prefer self-documenting code over comments

### 2. One Skill = One Job
Skills that try to do everything end up doing nothing well. Focus each skill on a single, specific workflow.

**Good:**
- `tdd-workflow` - Just TDD practices
- `api-design` - Just API conventions
- `code-review` - Just review checklists

**Bad:**
- `everything-skill` - TDD + API + review + deployment + ...

### 3. Write Descriptions Like Search Queries
Claude finds Skills by semantic matching. Include keywords users would actually say:

**Good:**
```yaml
description: Creates unit tests for React components using Jest and 
  React Testing Library. Use when testing React, writing test cases, 
  or setting up component tests.
```

**Bad:**
```yaml
description: Helps with testing stuff.
```

### 4. Use Progressive Disclosure
Don't put everything in SKILL.md. Split into reference files:

```text
testing-skill/
├── SKILL.md              # Core workflow (500 lines max)
├── references/
│   ├── jest-patterns.md  # Detailed Jest examples
│   ├── rtl-patterns.md   # React Testing Library patterns
│   └── mocking.md        # Mock strategies
```
Claude will read reference files only when needed.

## The Skills Ecosystem

### Official Skills
- **anthropics/skills** - Anthropic's official library
- **Claude Skills Page** - Pre-built document skills

### Community Resources
- **awesome-claude-skills** - Curated community skills
- **agentskills.io** - Open standard specification

## Skills as an Open Standard

Here's the exciting part: Anthropic released Agent Skills as an open standard. This means skills work across:
- Claude.ai
- Claude Code
- Cursor
- OpenCode
- VS Code
- And more

One skill, every platform. No vendor lock-in.

## Common Pitfalls to Avoid

### 1. Skill Not Triggering
**Symptoms:** Claude ignores your skill even when relevant.
**Fixes:**
- Check the description includes relevant keywords
- Restart Claude Code (fixes 80% of issues)
- Verify the skill is enabled in settings

### 2. CLAUDE.md Bloat
**Symptoms:** Slow responses, hitting token limits fast.
**Fix:** Move procedural knowledge to Skills (on-demand loading) and keep CLAUDE.md for essential project context only.

### 3. Vague Skills
**Symptoms:** Claude uses the skill but produces generic output.
**Fix:** Add concrete examples, specific constraints, and clear success criteria.

## Security Considerations

Skills can include executable code. Before installing third-party skills:
- **Audit all files** - Read through the SKILL.md and any scripts
- **Check for network calls** - Watch for unexpected data exfiltration
- **Verify the source** - Stick to trusted repositories
- **Sandbox first** - Test in a non-critical environment

## What's Next?

Skills represent a fundamental shift in how we work with AI. Instead of treating Claude as a blank slate every conversation, Skills let you build cumulative expertise that compounds over time.

The ecosystem is still young. The best skills haven't been written yet - maybe by you.

Ready to dive in?
- Browse existing skills at Skills Directory
- Install a few that match your workflow
- Create your first custom skill for a task you repeat often
- Share what you build with the community


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
