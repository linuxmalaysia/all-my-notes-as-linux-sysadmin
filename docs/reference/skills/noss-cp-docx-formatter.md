---
title: "Noss Cp Docx Formatter"
description: "DSOM Reference document for Noss Cp Docx Formatter."
type: "reference"
id: "docs/reference/skills/noss-cp-docx-formatter.md"
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

-- | :---------- | | `CP-Level-3-Generated.md` | ..."
noss_section: "K62 COMPUTER PROGRAMMING, CONSULTANCY AND RELATED ACTIVITIES"
noss_group: "622 COMPUTER CONSULTANCY AND COMPUTER FACILITIES MANAGEMENT ACTIVITIES"
noss_code: 
target_level: 3
---


# NOSS CP DOCX Formatter Skill

## 1. Purpose

This skill equips an AI agent to **generate** the official NOSS Level 3
Competency Profile document in two formats:

| Output | Description |
| :----- | :---------- |
| `CP-Level-3-Generated.md` | GitHub-flavoured Markdown replica of the CP |
| `CP-Level-3-Generated.docx` | Word document matching the exact table/font specification |

Both outputs must be **byte-for-byte structurally equivalent** — meaning every
heading, every cell width, every bold label, every line-break must match the
reference document described in Section 3.

---

## 2. Prerequisites

The agent must verify the following before running:

1. **Node.js ≥ 18** is available (`node --version`).
2. **`docx` npm package** is installed in the project root
   (`npm list docx` — must show a version).
3. **CU profile source files** exist at:
   `noss-rebuild/competency-profiles/<cuXX>/<cuXX>-profile.md`
   for each CU the agent intends to compile.

If the `docx` package is missing, run: `npm install docx` in the project root.

---

## 3. Reference Format Specification

### 3.1 Global Document Settings

| Property | Value |
| :------- | :---- |
| Font family | **Times New Roman** |
| Font size | **11 pt** (22 in half-points, the docx unit) |
| Page margins | Top: 720, Right: 720, Bottom: 720, Left: 720 (twips) |
| Table width | **100%** of page width |
| Table borders | Single, `color="auto"`, `sz=4` on all 6 sides (top, bottom, left, right, insideH, insideV) |
| Cell margins | Top: 100, Left: 100, Bottom: 100, Right: 100 (dxa) |

### 3.2 Document Structure (in order)

```
Heading 1: "1. Competency Profile (CP)"
Empty paragraph
[Header Table]        ← 4-column grid, 25%/75% colspans
Empty paragraph
For each CU:
  [CU Header Table]   ← 2-column, 25%/75%
  Empty paragraph
  [WA Matrix Table]   ← 3-column, 30%/35%/35%
  Empty paragraph
```

### 3.3 Header Table (Section/Group/Area/NOSS metadata)

- 4 logical columns (each `gridCol w:w="100"`), percentage-based widths
- Row layout:

| Row | Col 1 (25%, bold) | Col 2 (75%, bold, colSpan=3) |
| :-- | :---------------- | :--------------------------- |
| 1   | SECTION           | (J) Information and Communication |
| 2   | GROUP             | (620) Computer Programming, Consultancy and Related Activities |
| 3   | AREA              | Computer System Administration |
| 4   | NOSS TITLE        | Sovereign IT Infrastructure Operations |
| 5   | NOSS LEVEL (25%)  | LEVEL 3 (25%) \| NOSS CODE (25%, bold) \| IT-020-3:2026 (25%) |

Row 5 has **4 separate cells** (no colspan), each 25%.

### 3.4 CU Header Table (per CU)

- 2 logical columns, percentage-based
- Row 1: `CU TITLE & CU CODE` (bold, 25%) | `<title> (<code>)` (bold, 75%)
- Row 2: `CU DESCRIPTOR` (bold, 25%) | descriptor text (NOT bold, 75%)
  - Descriptor uses `\n\n` for paragraph breaks in DOCX (NOT `<br>`)

### 3.5 WA Matrix Table (per CU)

- 3 columns: **30%** / **35%** / **35%**
- Row 1 (header): `WORK ACTIVITIES` | `WORK STEPS` | `PERFORMANCE CRITERIA` (all bold)
- Per WA row:
  - **Col 1** – WA name + `\n(WA code)` in a single cell, NOT bold
  - **Col 2** – One `Paragraph` element per work step, numbered `N.M text`
  - **Col 3** – One `Paragraph` element per PC, numbered `N.M text`
  - Steps and PCs are separate `Paragraph` children inside the cell (not `<br>`)

---

## 4. Markdown Format Specification

The `.md` file is a direct mirror of the DOCX using GitHub table syntax.

### 4.1 Document Header Block

```markdown
# 1. Competency Profile (CP)

| SECTION | (J) Information and Communication | | |
| :---- | :---- | :---- | :---- |
| GROUP | (620) Computer Programming, Consultancy and Related Activities | | |
| AREA | Computer System Administration | | |
| NOSS TITLE | Sovereign IT Infrastructure Operations | | |
| NOSS LEVEL | LEVEL 3 | NOSS CODE | IT-020-3:2026 |
```

### 4.2 Per-CU Block

```markdown
| CU TITLE & CU CODE | <Title> (<Code>) |
| :---- | :---- |
| CU DESCRIPTOR | <Paragraph 1><br><br><Paragraph 2><br><br><Paragraph 3> |

| WORK ACTIVITIES | WORK STEPS | PERFORMANCE CRITERIA |
| ----- | ----- | ----- |
| <WA Name>..<br>(<WA Code>) | N.1 Step one.<br>N.2 Step two. | N.1 PC one.<br>N.2 PC two. |
```

**Critical rules:**
- Descriptor paragraphs separated by `<br><br>` (double break)
- WA name ends with `..` before `<br>(Code)`
- Steps and PCs use `<br>` between items within a cell
- Blank line between each CU block

---

## 5. Source Data Contract

The agent reads from **CU profile Markdown files** at:
`noss-rebuild/competency-profiles/<cuXX>/<cuXX>-profile.md`

Each profile file must contain:

### 5.1 Title (line 1)
```markdown
# <CU Title>
```

### 5.2 CU Descriptor (in a 2-column table)
```markdown
| **CU DESCRIPTOR** | <full three-paragraph descriptor> |
```

### 5.3 Work Activities Matrix (in a 3-column table)
```markdown
| WORK ACTIVITIES | WORK STEPS | PERFORMANCE CRITERIA |
| :--- | :--- | :--- |
| **N. <WA Title>**<br>*(<WA Code>)* | N.1 Step.<br>N.2 Step. | N.1 PC.<br>N.2 PC. |
```

---

## 6. Step-by-Step Agent Instructions

### Step 1 – Verify environment

```bash
node --version
npm list docx
```

If `docx` is not installed:
```bash
npm install docx
```

### Step 2 – Locate source files

For each CU to compile (default: cu01 through cu06), verify:
```
noss-rebuild/competency-profiles/cu01/cu01-profile.md
noss-rebuild/competency-profiles/cu02/cu02-profile.md
...
noss-rebuild/competency-profiles/cu06/cu06-profile.md
```

Report any missing files before proceeding.

### Step 3 – Run the generator

The canonical generator script is at:
```
scripts/generate_rebuild_cp.js
```

Run:
```bash
node scripts/generate_rebuild_cp.js
```

Expected output:
```
Saved Markdown to .../CP-Level-3-Generated.md
Saved DOCX to .../CP-Level-3-Generated.docx
```

### Step 4 – Verify outputs

Check that both files exist and have non-zero size:
```bash
node -e "const fs=require('fs'); ['noss-rebuild/references/CP-Level-3-Generated.md','noss-rebuild/references/CP-Level-3-Generated.docx'].forEach(f=>{const s=fs.statSync(f);console.log(f,s.size,'bytes')})"
```

### Step 5 – Quality gate

Run the Markdown verification check:
```bash
node -e "
const fs=require('fs');
const md=fs.readFileSync('noss-rebuild/references/CP-Level-3-Generated.md','utf8');
const cuCount=(md.match(/CU TITLE/g)||[]).length;
const waCount=(md.match(/IT-020-3:2026-CU\d+-WA\d+/g)||[]).length;
console.log('CU blocks found:',cuCount);
console.log('WA codes found:',waCount);
if(cuCount<6) console.error('FAIL: Expected at least 6 CU blocks');
else console.log('PASS: CU count OK');
"
```

---

## 7. Manual Authoring Rules (when writing content by hand)

When an AI agent writes or edits CP content directly (not via generator),
it MUST follow these rules:

### 7.1 CU Descriptor — 3-Paragraph Formula

```
Paragraph 1: <CU Title> describes [scope of activities].
             This activity typically takes place [context].

Paragraph 2: The person who is competent in this CU should be able to
             [WA1], [WA2], [WA3], and [WA4/5].

Paragraph 3: The outcome of this CU is [measurable deliverable]
             in accordance with [standard/policy/SOP].
```

### 7.2 Work Steps — Active Voice Rules

- Begin with an **action verb** (Install, Configure, Verify, Connect...)
- Use present tense
- Reference a concrete tool or command where applicable
- Format: `N.M [Action Verb] [Object] [Qualifier/Tool].`

### 7.3 Performance Criteria — Passive Voice Rules

- Object first, verb passive (past participle)
- End with `in accordance with [standard/policy/procedure]`
- Format: `N.M [Object] [Passive Verb] in accordance with [reference].`

### 7.4 WA Title Convention

- Start with action verb
- Follow NOSS naming: `[Verb] [Object] [Qualifier]`
- Append WA code in parentheses on a separate line in the DOCX cell

---

## 8. Error Patterns & Fixes

| Symptom | Root Cause | Fix |
| :------ | :--------- | :-- |
| DOCX missing CU | Profile file not found | Verify file path matches `cu0X-profile.md` naming |
| Descriptor split wrong | Missing `\n\n` between paragraphs | Add blank line between descriptor paragraphs in profile |
| WA steps merged into one line | `<br>` not present in profile table | Ensure `<br>` separates steps in the source table cell |
| PC count ≠ Step count | Matrix misalignment | Count steps and PCs; add missing entries to balance |
| DOCX not generated | `docx` package missing | Run `npm install docx` |
| Font appears different | Font not specified per run | Ensure every `TextRun` includes `font: "Times New Roman", size: 22` |

---

## 9. Extending to Other Document Types

This skill covers **CP only**. For related documents, use these companion skills:
- **CPC (Competency Profile Chart):** Use skill `noss-cpc-docx-formatter`
- **CoCU (Content of Competency Unit):** Use skill `noss-cocu-docx-formatter`
- **Job Sheets:** Use skill `noss-job-sheet-formatter`

---

## 10. Pedagogical Scope Boundary

> **⚠️ LEVEL 3 CONSTRAINT**
>
> All content generated by this skill must remain within **NOSS Level 3**
> boundaries:
> - Use only fundamental Linux/Windows CLI commands
> - Do not reference Kubernetes, Ansible, Terraform, or advanced orchestration
> - Work Steps must be executable by an SPM-entry vocational trainee
> - Do not introduce scripting logic beyond basic one-liner commands
