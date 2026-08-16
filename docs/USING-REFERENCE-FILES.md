---
title: "Using Reference Files"
description: "DSOM Reference document for Using Reference Files."
type: "reference"
id: "docs/USING-REFERENCE-FILES.md"
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

# Using Reference Files

Reference files let you extend your skill's knowledge without bloating the main `SKILL.md`. This guide covers how to use them effectively.

## Why Use Reference Files?

**Context Efficiency**
Claude only loads reference files when needed, preserving context window for actual work.

**Organization**
Keep your main instructions focused while storing detailed examples and edge cases separately.

**Maintainability**
Update specific topics without editing the entire skill.

## Creating Reference Files

### 1. Create the references directory
```bash
mkdir -p my-skill/references
```

### 2. Add reference files
```text
my-skill/
├── SKILL.md
└── references/
    ├── examples.md
    ├── edge-cases.md
    └── api-reference.md
```

### 3. Reference them in SKILL.md
```markdown
# My Skill

## Basic Usage
[core instructions here]

## Advanced Usage
For detailed examples, see `references/examples.md`.
For edge cases and special handling, see `references/edge-cases.md`.
```

## Best Practices

### Keep Files Focused
Each reference file should cover one topic:

**Good:**
```text
references/
├── authentication.md      # Just auth patterns
├── error-handling.md      # Just error patterns
└── pagination.md          # Just pagination
```

**Bad:**
```text
references/
└── everything.md          # 2000 lines of mixed content
```

### Use Clear Names
Name files by their content, not by when they're used:

**Good:**
```text
references/react-hooks.md
references/typescript-types.md
```

**Bad:**
```text
references/advanced.md
references/part2.md
```

### Size Guidelines
- Keep each file under 200 lines
- If a file grows larger, split it into subtopics

### Include Context
Start each reference file with context about its contents:

```markdown
# React Hooks Patterns

This reference covers common React hooks patterns for this skill.
Parent skill: component-generator

## useState Patterns
...

## useEffect Patterns
...
```

## How Claude Loads References

Claude's loading behavior:
1. **Discovery phase:** Only reads SKILL.md frontmatter (name + description)
2. **Activation:** Loads full SKILL.md body
3. **Reference needed:** Loads specific reference file when mentioned

This means you can have many reference files without impacting performance until they're actually needed.

## Linking Between Files

**From SKILL.md to references**
```markdown
## Database Patterns
For query optimization, see `references/database.md`.
```

**Between reference files**
```markdown
# Error Handling

For authentication errors specifically, see `authentication.md`.
```

**Inline vs. Block References**

*Inline (load and incorporate):*
> Claude will automatically read the referenced file when encountering this pattern.
> See `references/examples.md` for examples of this pattern.

*Block (explicit instruction):*
```markdown
## Extended Examples

Before proceeding, read the full examples in `references/examples.md` and apply
those patterns to the current task.
```

## Organizing Complex Skills

### Hierarchical Structure
For complex skills, organize references by category:

```text
api-skill/
├── SKILL.md
└── references/
    ├── rest/
    │   ├── conventions.md
    │   ├── error-codes.md
    │   └── versioning.md
    ├── graphql/
    │   ├── schema.md
    │   └── resolvers.md
    └── common/
        ├── authentication.md
        └── rate-limiting.md
```

### Index Files
For large reference collections, add an index:

```markdown
# references/index.md

## REST API
- `rest/conventions.md` - RESTful design patterns
- `rest/error-codes.md` - Standard error responses
- `rest/versioning.md` - Versioning strategies

## GraphQL
- `graphql/schema.md` - Schema design
- `graphql/resolvers.md` - Resolver patterns
```

## Common Patterns

### Examples Collection
```markdown
# references/examples.md

## Example 1: Basic CRUD
[input and output examples]

## Example 2: Complex Query
[input and output examples]

## Example 3: Error Handling
[input and output examples]
```

### Troubleshooting Guide
```markdown
# references/troubleshooting.md

## Common Issues

### Issue: Skill doesn't trigger
**Symptoms**: Claude ignores the skill
**Solution**: Check description keywords

### Issue: Incomplete output  
**Symptoms**: Response is cut off
**Solution**: Reduce complexity or split request
```

### Checklists
```markdown
# references/checklists.md

## Pre-Deployment Checklist
- [ ] All tests passing
- [ ] Documentation updated
- [ ] Changelog entry added
- [ ] Version bumped

## Security Checklist
- [ ] No hardcoded secrets
- [ ] Input validation complete
- [ ] Rate limiting configured
```

## Tips

### 1. Start with SKILL.md Only
Add references as your skill grows. Don't over-engineer upfront.

### 2. Reference Naturally
Write `SKILL.md` as if references are always available. Claude handles the loading.

### 3. Test Loading
Verify Claude actually reads your references when needed. If not, make the reference more explicit.

### 4. Keep References Current
When you update `SKILL.md`, check if references need updates too.


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
