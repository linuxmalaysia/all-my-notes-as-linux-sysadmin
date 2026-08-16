---
title: "Writing Effective Skills"
description: "DSOM Guide document for Writing Effective Skills."
type: "guide"
id: "docs/WRITING-EFFECTIVE-SKILLS.md"
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

# Writing Effective Skills

This guide covers best practices for creating powerful, reusable Claude Skills that work reliably.

## The Golden Rules

### 1. One Skill = One Job
Skills that try to do everything end up doing nothing well. Each skill should have a single, clear purpose.

**Good:**
- `tdd-workflow` - Just TDD practices
- `api-design` - Just API conventions
- `code-review` - Just review checklists

**Bad:**
- `everything-skill` - TDD + API + review + deployment + ...

### 2. Write Descriptions Like Search Queries
Claude finds skills through semantic matching. Your description should include words and phrases users would actually say:

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

### 3. Be Specific, Not Vague
Instead of general advice, give concrete instructions:

**Vague:**
> Write clean code that is easy to read.

**Specific:**
> Code Standards:
> - Functions must be under 50 lines
> - Maximum 3 parameters per function
> - No abbreviations in variable names (use `customerName` not `custNm`)
> - Every public function needs a JSDoc comment

## Structure Your Instructions

### Use Clear Hierarchies

```markdown
# Skill Name

## When to Use This Skill
Clear trigger conditions...

## Step-by-Step Process
### Step 1: First thing
Details...

### Step 2: Second thing
Details...

## Output Format
How to structure the response...

## Examples
### Input
"User request..."

### Output
"Expected response..."
```

### Include Checklists
Checklists help Claude be thorough:

```markdown
## Security Review Checklist
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] Parameterized SQL queries
- [ ] Output encoding for XSS prevention
- [ ] Authentication checked on sensitive routes
```

### Define Edge Cases

```markdown
## Special Cases

If reviewing a test file:
- Skip code quality checks
- Focus on assertion coverage

If the file is under 20 lines:
- Skip the refactoring suggestions
- Only flag critical issues
```

## Use Progressive Disclosure

Don't put everything in SKILL.md. Large skills should use reference files:

```text
testing-skill/
├── SKILL.md              # Core workflow (keep under 500 lines)
├── references/
│   ├── jest-patterns.md  # Jest-specific examples
│   ├── rtl-patterns.md   # React Testing Library patterns
│   └── mocking.md        # Advanced mocking strategies
```

Claude loads reference files only when needed, saving context window.

In SKILL.md:
```markdown
## Advanced Topics

For complex mocking scenarios, see `references/mocking.md`.
For React-specific patterns, see `references/rtl-patterns.md`.
```

## Tell Claude What NOT to Do

Anti-patterns are as important as patterns:

```markdown
## Avoid

- Do NOT suggest style changes if a linter is configured
- Do NOT recommend rewriting entire functions
- Do NOT flag issues marked with `// intentional:` comments
- Do NOT add comments to self-explanatory code
```

## Include Examples

Real examples are worth a thousand words of explanation:

```markdown
## Example: Converting a callback to async/await

### Before
```javascript
function fetchUser(id, callback) {
  db.query('SELECT * FROM users WHERE id = ?', [id], (err, result) => {
    if (err) callback(err);
    else callback(null, result[0]);
  });
}
```

### After
```javascript
async function fetchUser(id) {
  const [user] = await db.query('SELECT * FROM users WHERE id = ?', [id]);
  return user;
}
```

### Why
- Cleaner control flow
- Easier error handling with try/catch
- Works with Promise.all for parallel operations
```

## Testing Your Skill

Before publishing, test these scenarios:

### 1. Trigger Testing
- Does Claude activate the skill when expected?
- Does it NOT activate for unrelated requests?

### 2. Output Testing  
- Is the output in the correct format?
- Does it follow all the instructions?

### 3. Edge Case Testing
- How does it handle unusual inputs?
- Does it gracefully handle missing information?

### 4. Conflict Testing
- Does it work alongside your other skills?
- Any conflicts with project-level CLAUDE.md?

## Common Mistakes

### 1. Too Long
If your SKILL.md is over 1000 lines, split it up. Claude's context is limited.

### 2. Too Abstract
"Write good code" is useless. Give specific, actionable instructions.

### 3. Conflicting Instructions
Review your skill for contradictions:
```markdown
# Bad - contradictory
"Always add comments"
"Don't add unnecessary comments"
```

### 4. Missing Context
Don't assume Claude knows your stack:

```markdown
# Bad
"Use the standard testing pattern"

# Good
"Use Jest with React Testing Library. Structure tests as:
describe('ComponentName', () => {
  it('should render correctly', () => {...});
});"
```

## Iteration is Key

The best skills evolve over time:
- **Start minimal** - Basic instructions that work
- **Observe failures** - Note when Claude gets it wrong
- **Add specifics** - Address the failure cases
- **Repeat** - Keep refining based on real usage

Don't try to anticipate everything upfront. Let real usage guide improvements.
