# SKILL.md Format

This is the complete reference for the SKILL.md file format.

## Overview

A `SKILL.md` file has two parts:

- YAML frontmatter - Metadata about the skill
- Markdown body - Instructions for Claude

```yaml
---
name: skill-name
description: Brief description of what this skill does.
---
```
```markdown
# Skill Title

Markdown instructions here...
```

## Frontmatter Fields

### Required Fields

#### name
A unique identifier for the skill. Used for referencing and installation.
```yaml
name: code-review
```
Rules:
- Lowercase letters, numbers, and hyphens only
- No spaces or special characters
- Should be descriptive but concise
- Must be unique within your skills directory

#### description
A brief description of what the skill does and when to use it.
```yaml
description: Reviews code for bugs, security issues, and style violations.
  Use when reviewing pull requests or checking code quality.
```
Tips:
- Include keywords users might say
- Describe the use case, not just the function
- Keep under 200 characters for best results

### Optional Fields

#### version
Semantic version of the skill.
```yaml
version: 1.2.0
```

#### author
Creator of the skill.
```yaml
author: Your Name
```

#### tags
Categories for the skill.
```yaml
tags:
  - development
  - code-quality
  - review
```

#### requires
Other skills or tools this skill depends on.
```yaml
requires:
  - git
  - eslint
```

## Markdown Body

### Structure
A well-organized skill body includes:

```markdown
# Skill Name

## Overview
Brief explanation of the skill's purpose.

## When to Use
Describe scenarios that trigger this skill.

## Instructions
Step-by-step process for Claude to follow.

## Output Format
How responses should be structured.

## Examples
Input/output examples.

## Notes
Additional context or warnings.
```

### Supported Markdown
`SKILL.md` supports standard GitHub-Flavored Markdown:

#### Headings
```markdown
# H1 - Skill title
## H2 - Major sections
### H3 - Subsections
#### H4 - Details
```

#### Code Blocks
```javascript
function example() {
  return "hello";
}
```

#### Lists
```markdown
- Unordered item
- Another item

1. Ordered item
2. Another item

- [ ] Checkbox item
- [x] Completed item
```

#### Tables
| Column 1 | Column 2 |
|----------|----------|
| Value 1  | Value 2  |

#### Emphasis
**Bold text**
*Italic text*
`inline code`
> Blockquotes

### Special Patterns

#### File References
Reference other files in your skill:
> See `references/examples.md` for detailed examples.

Claude will load these files when needed.

#### Conditional Instructions
Use headings to create conditional sections:
```markdown
## If the code is TypeScript
- Check type annotations
- Verify interface definitions

## If the code is JavaScript
- Check for runtime type errors
- Suggest TypeScript migration
```

#### Checklists
Create verification lists:
```markdown
## Security Checklist
- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] SQL queries parameterized
```

## Complete Example

```yaml
---
name: api-endpoint-creator
description: Creates RESTful API endpoints following best practices. Use when
  building new endpoints, designing APIs, or implementing CRUD operations.
version: 1.0.0
author: Skills Directory
tags:
  - api
  - backend
  - rest
---
```
```markdown
# API Endpoint Creator

## Overview

This skill helps create well-structured RESTful API endpoints with proper
error handling, validation, and documentation.

## When to Use

- Creating new API endpoints
- Implementing CRUD operations
- Designing RESTful resources
- Adding validation to existing endpoints

## Process

### Step 1: Analyze Requirements
Understand what resource is being created and what operations are needed.

### Step 2: Design the Endpoint
Determine:
- HTTP method (GET, POST, PUT, DELETE)
- URL structure
- Request/response format

### Step 3: Implement
Create the endpoint with:
- Input validation
- Error handling
- Proper status codes
- Documentation comments

### Step 4: Verify
Check against REST best practices.

## Output Format

Provide:
1. Endpoint implementation code
2. Request/response examples
3. Error cases

## Conventions

| Operation | Method | URL Pattern | Success Code |
|-----------|--------|-------------|--------------|
| List | GET | /resources | 200 |
| Create | POST | /resources | 201 |
| Read | GET | /resources/:id | 200 |
| Update | PUT | /resources/:id | 200 |
| Delete | DELETE | /resources/:id | 204 |

## Example

### Input
"Create an endpoint to manage user profiles"

### Output
```typescript
// GET /users/:id/profile
router.get('/users/:id/profile', async (req, res) => {
  const { id } = req.params;
  
  const profile = await getUserProfile(id);
  if (!profile) {
    return res.status(404).json({ error: 'Profile not found' });
  }
  
  return res.status(200).json(profile);
});
```

## Notes

- Always validate path parameters
- Use consistent error response format
- Include rate limiting for public endpoints

## Validation

### Check Your SKILL.md

Ensure your file:

1. **Has valid YAML frontmatter**
   - Starts and ends with `---`
   - Valid YAML syntax

2. **Has required fields**
   - `name` is present and valid
   - `description` is present and meaningful

3. **Has useful content**
   - Clear instructions
   - Examples when helpful
   - Proper markdown formatting

### Common Errors

#### Invalid YAML
```yaml
# Wrong - missing colon
name skill-name

# Correct
name: skill-name
```

#### Multiline Description
```yaml
# Wrong - unquoted multiline
description: This is a long
description that spans lines.

# Correct - use folded style
description: >
  This is a long description
  that spans multiple lines.
```
