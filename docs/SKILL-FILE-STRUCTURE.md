---
title: "Skill File Structure"
description: "DSOM Guide document for Skill File Structure."
type: "guide"
id: "docs/SKILL-FILE-STRUCTURE.md"
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

# Skill File Structure

This guide explains the anatomy of a Claude Skill and how to organize its files.

## Basic Structure

At minimum, a skill is a folder with a `SKILL.md` file:

```text
my-skill/
└── SKILL.md
```

## Full Structure

A complete skill can include multiple types of files:

```text
my-skill/
├── SKILL.md              # Required: main instructions
├── references/           # Optional: additional documentation
│   ├── api-guide.md
│   ├── examples.md
│   └── troubleshooting.md
├── scripts/              # Optional: executable code
│   ├── generate.py
│   └── validate.sh
├── templates/            # Optional: file templates
│   ├── component.tsx.template
│   └── test.spec.ts.template
└── assets/               # Optional: static files
    ├── logo.png
    └── config.json
```

## Directory Purposes

### SKILL.md (Required)
The main skill file containing:
- YAML frontmatter with metadata
- Markdown instructions for Claude

```yaml
---
name: my-skill
description: What this skill does and when to use it.
---
```
```markdown
# Skill Title

Instructions go here...
```

### references/
Additional documentation that Claude can read when needed. Use this for:
- Detailed API documentation
- Extended examples
- Framework-specific guides
- Troubleshooting guides

Claude only loads these when referenced, saving context window.
**Best practice**: Keep individual reference files under 200 lines.

### scripts/
Executable code that Claude can run. Common uses:
- Code generation scripts
- Validation tools
- Build helpers
- Data transformation utilities

```python
# scripts/generate.py
#!/usr/bin/env python3
import sys

def generate_component(name):
    template = f'''
export function {name}() {{
  return <div>{name}</div>;
}}
'''
    print(template)

if __name__ == "__main__":
    generate_component(sys.argv[1])
```
*Note: Scripts require appropriate permissions to execute.*

### templates/
File templates for generating new files. Use template markers:

```tsx
// templates/component.tsx.template
import React from 'react';

interface {{ComponentName}}Props {
  // Props here
}

export function {{ComponentName}}({ }: {{ComponentName}}Props) {
  return (
    <div>
      {{ComponentName}}
    </div>
  );
}
```

### assets/
Static files the skill might need:
- Configuration files
- Images
- JSON data
- Any binary files

## File Size Guidelines

| File Type | Recommended Max Size |
| :--- | :--- |
| SKILL.md | 500 lines |
| Reference files | 200 lines each |
| Scripts | 300 lines each |
| Templates | 100 lines each |

Larger files can work but impact Claude's context window.

## Naming Conventions

### Folders
- Use lowercase with hyphens: `my-skill/`, `code-review/`
- Keep names short but descriptive

### Files
- `SKILL.md` must be uppercase
- Reference files: lowercase with hyphens `api-guide.md`
- Scripts: lowercase with extension `generate.py`
- Templates: include target extension `component.tsx.template`

## Loading Behavior

Claude loads skill contents progressively:

| Content | When Loaded |
| :--- | :--- |
| name + description | Always (skill discovery) |
| SKILL.md body | When skill is triggered |
| Reference files | When explicitly needed |
| Scripts | When execution requested |

This progressive loading keeps Claude efficient even with many installed skills.

## Example: Complete API Skill

```text
api-design/
├── SKILL.md
│   # Contains: Core API design principles
│   # ~300 lines of main instructions
│
├── references/
│   ├── rest-conventions.md    # RESTful patterns
│   ├── graphql-patterns.md    # GraphQL specific
│   ├── error-formats.md       # Standard error responses
│   └── versioning.md          # API versioning strategies
│
├── scripts/
│   ├── generate-openapi.py    # Generate OpenAPI spec
│   └── validate-schema.sh     # Validate against spec
│
├── templates/
│   ├── endpoint.ts.template   # New endpoint template
│   └── error-handler.ts.template
│
└── assets/
    └── openapi-base.json      # Base OpenAPI structure
```

## Tips for Organization

### 1. Start Simple
Begin with just `SKILL.md`. Add other directories as needed.

### 2. Reference Liberally
In `SKILL.md`, reference other files:
> For detailed REST conventions, see `references/rest-conventions.md`.

### 3. Keep SKILL.md Focused
Move detailed examples and edge cases to reference files.

### 4. Version Control Friendly
Structure your skill to work well with git:
- Separate logical concerns into different files
- Keep files small for easier diffs
- Use meaningful commit messages for skill updates
