---
okf_version: 0.1
type: agent_skill
name: noss-cpc-docx-formatter
title: noss-cpc-docx-formatter
description: "This skill equips an AI agent to **generate** the official NOSS Level 3 Competency Profile Chart (CPC) document in two formats:  | Output | Description | | :----- | :---------- | | `CPC-Level-3-Gen..."
noss_section: "K62 COMPUTER PROGRAMMING, CONSULTANCY AND RELATED ACTIVITIES"
noss_group: "622 COMPUTER CONSULTANCY AND COMPUTER FACILITIES MANAGEMENT ACTIVITIES"
noss_code: 
target_level: 3
---


# NOSS CPC DOCX Formatter Skill

## 1. Purpose

This skill equips an AI agent to **generate** the official NOSS Level 3
Competency Profile Chart (CPC) document in two formats:

| Output | Description |
| :----- | :---------- |
| `CPC-Level-3-Generated.md` | GitHub-flavoured Markdown representation of the CPC |
| `CPC-Level-3-Generated.docx` | Word document matching the exact coloured grid layout |

The CPC is a **colour-coded visual matrix** — fundamentally different from the CP.
It maps every Competency Unit (CU) to its Work Activities (WA) in a compact
6-column grid with coloured fills, vertical cell merging, and overflow row logic.

---

## 2. Prerequisites

The agent must verify the following before running:

1. **Node.js ≥ 18** is available (`node --version`).
2. **`docx` npm package** is installed in the project root
   (`npm list docx` — must show a version, including `AlignmentType`, `VerticalAlign`, `BorderStyle`).
3. **CU profile source files** exist at:
   `noss-rebuild/competency-profiles/<cuXX>/<cuXX>-profile.md`
   for each CU to compile.

If the `docx` package is missing, run: `npm install docx`

---

## 3. Reference Format Specification

### 3.1 Global Document Settings

| Property | Value |
| :------- | :---- |
| Font family | **Times New Roman** |
| Font size | **11 pt** (22 in half-points) |
| Page margins | Top: 720, Right: 720, Bottom: 720, Left: 720 (twips) |
| Heading | `"1. Competency Profile Chart (CPC)"` — Heading 1 style |

### 3.2 Document Structure (in order)

```
Heading 1: "1. Competency Profile Chart (CPC)"
Empty paragraph
[Table 1: Metadata Header]    ← grey/red coloured 5-column table
Empty paragraph
[Table 2: CPC Grid]           ← 6-column colour matrix, 50% page width
```

---

### 3.3 Table 1 — Metadata Header

**Width:** 100% of page  
**Grid:** 5 equal columns  
**Cell borders:** Single black `000000`, sz=4 on all sides  
**Cell alignment:** CENTER, vAlign CENTER  
**Margins:** top/start/bottom/end = 100 dxa  

| Row | Col 1 (grey `EFEFEF`) | Col 2–5 (white `FFFFFF`, text RED `FF0000`, colSpan=4) |
| :-- | :-------------------- | :------------------------------------------------------- |
| 1   | SECTION               | K62 COMPUTER PROGRAMMING, CONSULTANCY AND RELATED ACTIVITIES |
| 2   | GROUP                 | 622 COMPUTER CONSULTANCY AND COMPUTER FACILITIES MANAGEMENT ACTIVITIES |
| 3   | AREA                  | (value from config) |
| 4   | NOSS TITLE            | (value from config) |
| 5   | NOSS LEVEL (grey)     | LEVEL 3 (red text, white) \| NOSS CODE (grey) \| IT-020-3:2026 (red, white, colSpan=2) |

**Label cells** (`EFEFEF` fill): plain black text, NOT bold  
**Value cells** (`FFFFFF` fill): text colour `FF0000` (red), NOT bold  

Row 5 has **4 separate cells**: NOSS LEVEL label | LEVEL 3 value | NOSS CODE label | code value (colSpan=2)

---

### 3.4 Table 2 — CPC Grid

**Width:** 50% of page (`w:w="5000" w:type="pct"`)  
**Layout:** Fixed (`w:tblLayout w:type="fixed"`)  
**Grid:** 6 columns of 1744/1744/1744/1745/1744/1745 dxa  
**Alignment:** left-justified (`w:jc w:val="start"`)  
**Cell borders:** Single black `000000`, sz=4, space=0 on all sides  
**Cell alignment:** CENTER horizontal, CENTER vertical  
**Margins:** top/start/bottom/end = 100 dxa  
**Spacing:** before=100, after=100 per paragraph  

#### Colour Palette

| Constant | Hex | Usage |
| :------- | :-- | :---- |
| `COLOR_ORANGE` | `FFC000` | CORE category column (col 0, vertical merge) |
| `COLOR_YELLOW` | `FFFF00` | CU Title cell (col 1, WA name rows) |
| `COLOR_GREEN`  | `92D050` | CU Code cell (col 1, code rows) + col-1 header |
| `COLOR_BLUE`   | `DDEBF7` | WA Code cells (cols 2–5, code rows) + cols 2–5 header |
| `COLOR_WHITE`  | `FFFFFF` | WA Title cells (cols 2–5, name rows) + spacers |

#### Table 2 Row Structure

The grid follows this repeating pattern:

```
ROW 0 (header):
  [col 0: white, empty]
  [col 1: GREEN "←COMPETENCY UNIT→"]
  [col 2–5: BLUE colspan=4, "←WORK ACTIVITIES→"]

ROW 1 (spacer):
  [col 0–5: WHITE colspan=6, empty]

For each CU block (3 or 5 rows depending on WA count):
  [NAME ROW A]:
    col 0: ORANGE "C\nO\nR\nE" (first CU only) or empty,
           vMerge restart, rowSpan = 2 (or 4 if overflow)
    col 1: YELLOW — CU full name (title case)
    col 2–5: WHITE — WA names 1–4 (fill empty if < 4 WAs)

  [CODE ROW A]:
    col 0: vMerge continuation (no text, no fill)
    col 1: GREEN — "CODE CUXX"
    col 2–5: BLUE — "CODE CUXX-WA01" ... "CODE CUXX-WA04" (empty if unused)

  IF CU has more than 4 WAs (overflow):
    [NAME ROW B]:
      col 0: vMerge continuation
      col 1: WHITE — empty
      col 2–5: WHITE — WA names 5–8 (fill empty if < 4 overflow WAs)

    [CODE ROW B]:
      col 0: vMerge continuation
      col 1: WHITE — empty
      col 2–5: BLUE — "CODE CUXX-WA05"... (empty if unused)

  [SPACER ROW]:
    col 0–5: WHITE colspan=6, empty

END OF PATTERN
```

#### vMerge Rules

The orange CORE column (col 0) uses `rowSpan` in the `docx` library which maps
to `w:vMerge w:val="restart"` on the first row and `w:vMerge` (continuation) on
subsequent merged rows. The rowSpan value is:
- **2** if the CU has 4 or fewer WAs (2 rows: name + codes)
- **4** if the CU has 5 or more WAs (4 rows: name + codes + overflow name + overflow codes)

Only the **first CU** displays the `"C\nO\nR\nE"` text in the orange column.
All subsequent CUs have the orange column empty (but still merged).

---

## 4. Markdown Format Specification

The CPC `.md` file uses a simplified 2-column table representation.

### 4.1 Header Block

```markdown
# Competency Profile Chart (CPC)

| SECTION | (J) Information and Communication |
| :--- | :--- |
| **GROUP** | (620) Computer Programming, Consultancy and Related Activities |
| **AREA** | Computer System Administration |
| **NOSS TITLE** | Sovereign IT Infrastructure Operations |
| **NOSS LEVEL** | LEVEL 3 |
| **NOSS CODE** | IT-020-3:2026 |
```

### 4.2 Core Competencies Table

```markdown
## 🟢 CORE COMPETENCIES

| COMPETENCY UNIT (CU) | WORK ACTIVITIES (WA) |
| :--- | :--- |
| **<CU TITLE IN CAPS>**<br>`[CODE: CUxx]` | **1.** WA Title One `[CUxx-WA01]`<br><br>**2.** WA Title Two `[CUxx-WA02]`<br><br>... |
```

**Rules:**
- CU title in `**UPPERCASE BOLD**`
- CU code in backtick monospace: `` `[CODE: CU01]` ``
- Each WA entry: `**N.** WA Title` followed by `` `[CUxx-WAxx]` `` code
- WA entries separated by `<br><br>` (double break)
- Blank line between the header table and the CORE COMPETENCIES section

---

## 5. Source Data Contract

The agent reads from CU profile Markdown files at:
`noss-rebuild/competency-profiles/<cuXX>/<cuXX>-profile.md`

### What is extracted per CU:

| Field | Source location in profile |
| :---- | :------------------------- |
| CU Title | First line: `# <Title>` |
| CU Code | Derived: `CODE CU0X` / `IT-020-3:2026-CU0X` |
| WA Titles | Competency Matrix table, column 1, `**N. <Title>**` pattern |
| WA Codes | Derived: `CODE CU0X-WA0Y` |

The CPC does **not** use the CU Descriptor or Performance Criteria.
It only uses CU titles and WA titles/codes.

---

## 6. Step-by-Step Agent Instructions

### Step 1 – Verify environment

```bash
node --version
npm list docx
```

If `docx` is missing:
```bash
npm install docx
```

### Step 2 – Locate source files

Verify these exist for each CU (default cu01–cu06):
```
noss-rebuild/competency-profiles/cu01/cu01-profile.md
...
noss-rebuild/competency-profiles/cu06/cu06-profile.md
```

### Step 3 – Run the CPC generator

```bash
node scripts/generate_rebuild_cpc_docx.js
```

Expected output:
```
Successfully generated DOCX at .../CPC-Level-3-Generated.docx
```

> **Note:** The CPC generator currently only produces DOCX.
> The Markdown CPC is maintained separately in `noss-rebuild/references/CPC-Level-3.md`
> or generated by a companion MD-only script.

### Step 4 – Verify output

```bash
node -e "const fs=require('fs'); const s=fs.statSync('noss-rebuild/references/CPC-Level-3-Generated.docx'); console.log('DOCX size:', s.size, 'bytes'); if(s.size < 5000) console.error('FAIL: File too small'); else console.log('PASS');"
```

### Step 5 – Quality gate

```bash
node -e "
const fs=require('fs');
const {Document,Packer}=require('docx');
// Check that source profiles parse correctly
const profilesDir='noss-rebuild/competency-profiles';
const cuList=['cu01','cu02','cu03','cu04','cu05','cu06'];
let ok=true;
cuList.forEach(id=>{
  const f=profilesDir+'/'+id+'/'+id+'-profile.md';
  if(!fs.existsSync(f)){console.error('MISSING:',f);ok=false;}
  else {
    const c=fs.readFileSync(f,'utf8');
    const was=(c.match(/\*\*\d+\./g)||[]).length;
    console.log(id,'- WA count:',was);
    if(was<1){console.error('FAIL: No WAs found in',id);ok=false;}
  }
});
if(ok) console.log('PASS: All profiles found and parseable');
"
```

---

## 7. WA Overflow Logic (more than 4 WAs per CU)

When a CU has more than 4 WAs, the grid wraps into additional rows.

```
CU with 6 WAs → 4 rows + spacer:
  Row A (name): [ORANGE-CORE] [YELLOW: CU title] [WA1] [WA2] [WA3] [WA4]
  Row A (code): [vMerge cont] [GREEN: CODE CUxx] [WA01] [WA02] [WA03] [WA04]
  Row B (name): [vMerge cont] [WHITE: empty]     [WA5] [WA6] [empty] [empty]
  Row B (code): [vMerge cont] [WHITE: empty]     [WA05] [WA06] [empty] [empty]
  Spacer:       [WHITE colspan=6]

CU with 4 WAs → 2 rows + spacer:
  Row A (name): [ORANGE-CORE] [YELLOW: CU title] [WA1] [WA2] [WA3] [WA4]
  Row A (code): [vMerge cont] [GREEN: CODE CUxx] [WA01] [WA02] [WA03] [WA04]
  Spacer:       [WHITE colspan=6]
```

The `rowSpan` on the orange CORE cell must match the total data rows
(excluding the spacer):
- 2 WA rows → `rowSpan: 2`
- 4 WA rows (overflow) → `rowSpan: 4`

---

## 8. Exact docx API Mapping

```javascript
// Required imports
const {
  Document, Packer, Paragraph, Table, TableCell, TableRow,
  WidthType, TextRun, HeadingLevel,
  AlignmentType, VerticalAlign, BorderStyle
} = require('docx');

// Standard cell with colour fill
function createCell(content, bgColor, colSpan = 1, rowSpan = 1) {
  return new TableCell({
    children: Array.isArray(content)
      ? content
      : [new Paragraph({
          children: [new TextRun({ text: content, font: 'Times New Roman', size: 22 })],
          alignment: AlignmentType.CENTER,
          spacing: { before: 100, after: 100 }
        })],
    shading: { fill: bgColor },
    columnSpan: colSpan,
    rowSpan: rowSpan,
    verticalAlign: VerticalAlign.CENTER,
    margins: { top: 100, bottom: 100, left: 100, right: 100 },
    borders: {
      top:    { style: BorderStyle.SINGLE, size: 4, color: '000000' },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: '000000' },
      left:   { style: BorderStyle.SINGLE, size: 4, color: '000000' },
      right:  { style: BorderStyle.SINGLE, size: 4, color: '000000' },
    }
  });
}

// Red text cell (for metadata values)
function createRedTextCell(text, bgColor = 'FFFFFF', colSpan = 1) {
  return createCell(
    [new Paragraph({
      children: [new TextRun({ text, font: 'Times New Roman', size: 22, color: 'FF0000' })],
      alignment: AlignmentType.CENTER,
      spacing: { before: 100, after: 100 }
    })],
    bgColor, colSpan
  );
}

// CPC Grid table: fixed layout, 50% width
const gridTable = new Table({
  width: { size: 50, type: WidthType.PERCENTAGE },
  layout: 'fixed',                // maps to w:tblLayout w:type="fixed"
  rows: [ ...coreRows ]
});
```

---

## 9. Error Patterns & Fixes

| Symptom | Root Cause | Fix |
| :------ | :--------- | :-- |
| WA overflow rows misaligned | rowSpan calculated without overflow | Check WA count: if >4 use rowSpan=4 else rowSpan=2 |
| Orange column not merging | Missing `rowSpan` argument to createCell | Always pass `rowSpan` for col 0 cells |
| Grid wider than expected | Table width set to 100% | Set `size: 50, type: WidthType.PERCENTAGE` |
| WA codes wrong format | Hardcoded vs dynamic | Generate as `CODE CU0X-WA0Y` (zero-padded) |
| CU title not uppercase | Missing `.toUpperCase()` | Title must be all-caps in the DOCX grid |
| Red text not appearing | Missing `color: 'FF0000'` in TextRun | All metadata values use red text |
| Grey label cells wrong | Using bold instead of EFEFEF fill | Labels use fill `EFEFEF`, NOT bold |

---

## 10. Extending This Skill

This skill covers **CPC only**. For related documents:
- **CP (Competency Profile):** Use skill `noss-cp-docx-formatter`
- **CoCU (Content of CU):** Use skill `noss-cocu-docx-formatter`
- **Job Sheets:** Use skill `noss-job-sheet-formatter`

---

## 11. Pedagogical Scope Boundary

> **⚠️ LEVEL 3 CONSTRAINT**
>
> The CPC is a structural/administrative document. Its content must faithfully
> reflect the WA titles from the approved Level 3 profile files. Do not
> introduce new WA titles, merge WAs, or alter codes without explicit
> human approval from the principal maintainer.


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
