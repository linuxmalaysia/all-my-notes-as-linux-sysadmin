---
title: "Creating Your First Skill"
description: "DSOM Guide document for Creating Your First Skill."
type: "guide"
id: "docs/CREATING-YOUR-FIRST-SKILL.md"
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

# Creating Your First Skill

This tutorial walks you through creating your first Claude Skill from scratch.

## The Quickest Way

The easiest way to create a skill is to ask Claude:
> Help me create a skill for [your workflow]

Claude will ask clarifying questions and generate the SKILL.md structure for you.

## Manual Creation

### Step 1: Create the folder structure

```bash
mkdir -p ~/.claude/skills/my-first-skill
cd ~/.claude/skills/my-first-skill
```

### Step 2: Create SKILL.md

Create a file called `SKILL.md` with this structure:

```yaml
---
name: my-first-skill
description: A brief description of what this skill does and when to use it.
  Include keywords that someone might say when they need this skill.
---
```
```markdown
# My First Skill

## Overview

Describe what this skill helps with.

## Instructions

Step-by-step instructions for Claude to follow.

### Step 1: Do the first thing

Details about step 1...

### Step 2: Do the next thing

Details about step 2...

## Examples

### Example Input
"Help me with X"

### Example Output
Here's what Claude should produce...
```

### Step 3: Test it

Open Claude and try using your skill:
> Use the my-first-skill skill to help me with X

## A Real Example: Code Review Skill

Let's create a practical skill for code reviews:

```yaml
---
name: code-review
description: Reviews code for bugs, security issues, and improvements. 
  Use when reviewing pull requests, checking code quality, or auditing code.
---
```
```markdown
# Code Review Skill

## Review Process

When reviewing code, follow this checklist:

### 1. Security Check
- [ ] No hardcoded secrets or API keys
- [ ] Input validation on all user data
- [ ] SQL queries use parameterized statements
- [ ] No XSS vulnerabilities in output

### 2. Code Quality
- [ ] Functions are small and focused
- [ ] Variable names are descriptive
- [ ] No code duplication
- [ ] Error handling is present

### 3. Performance
- [ ] No N+1 query issues
- [ ] Expensive operations are cached
- [ ] No memory leaks

## Output Format

Provide feedback as:
1. **Critical** - Must fix before merge
2. **Important** - Should fix soon
3. **Suggestion** - Nice to have

Include line numbers and specific code references.
```

## Adding Reference Files

For complex skills, split instructions into multiple files:

```text
code-review/
├── SKILL.md              # Main instructions
├── references/
│   ├── security.md       # Detailed security checklist
│   ├── react-patterns.md # React-specific patterns
│   └── api-review.md     # API review guidelines
```

In your `SKILL.md`, reference these files:

```markdown
## Detailed Guidelines

For security reviews, see `references/security.md`.
For React code, also check `references/react-patterns.md`.
```

Claude will read these files when needed.

## Best Practices

### 1. Start Small
Begin with a minimal skill and iterate. You can always add more instructions later.

### 2. Use Concrete Examples
Instead of:
> Write good code

Write:
> Functions should:
> - Be under 50 lines
> - Have a single responsibility
> - Use descriptive names like `calculateTotalPrice` not `calc`

### 3. Define Edge Cases
```markdown
## Special Cases

If the file is a test file:
- Focus on test coverage, not implementation details
- Check for edge cases in assertions

If the file is configuration:
- Only check for security issues
- Skip code quality checks
```

### 4. Include Anti-Patterns
Tell Claude what NOT to do:
```markdown
## Avoid

- Don't suggest style changes if the codebase uses a linter
- Don't recommend rewriting entire functions
- Don't flag issues that are clearly intentional (marked with comments)
```

## Testing Your Skill

- **Test the trigger** - Does Claude activate the skill when expected?
- **Test the output** - Is the output in the correct format?
- **Test edge cases** - How does it handle unusual inputs?
- **Test conflicts** - Does it work alongside your other skills?

## Publishing Your Skill

Once your skill works well:
- Add it to a public GitHub repository
- Submit it to the Skills Directory
- Share it with the community

## Next Steps
- Learn about Skill File Structure
- Read Writing Effective Skills
- Explore the SKILL.md Format Reference
