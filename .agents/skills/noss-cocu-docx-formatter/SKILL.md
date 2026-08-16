---
okf_version: 0.1
type: agent_skill
name: noss-cocu-docx-formatter
title: noss-cocu-docx-formatter
description: "This skill teaches AI agents how to programmatically generate NOSS Level 3 curriculum and support documents (CoCU matrices, Element Content Weightage, Competency Weightage, and TEM lists) matching ..."
noss_section: "K62 COMPUTER PROGRAMMING, CONSULTANCY AND RELATED ACTIVITIES"
noss_group: "622 COMPUTER CONSULTANCY AND COMPUTER FACILITIES MANAGEMENT ACTIVITIES"
noss_code: 
target_level: 3
---

# NOSS COCU DOCX Formatter Skill

## 1. Purpose

This skill teaches AI agents how to programmatically generate NOSS Level 3 curriculum and support documents (CoCU matrices, Element Content Weightage, Competency Weightage, and TEM lists) matching the official JPK TVET layout. It relies on the shared utility module at [noss-docx-template.js](file:///D:/Users/LinuxMalaysia/Projects/skills-noss-l3/scripts/utils/noss-docx-template.js) to enforce layout consistency.

---

## 2. Prerequisites

The agent must verify that:
1. `docx` library version `^9.7.1` is installed.
2. The helper module `scripts/utils/noss-docx-template.js` exists and is accessible.

---

## 3. Formatting Standards & Specifications

All generated documents must comply with the following parameters:

### 3.1 Page Settings & Margins
*   **Page Size:** Standard A4 (`width: 11907 dxa`, `height: 16840 dxa`).
*   **Orientation (Multi-Section):**
    *   **Section 1 (Page 1):** **Portrait** (`width: 11907 dxa`, printable table width `9027 dxa`) for CoCU Metadata Header Table.
    *   **Section 2 (Page 2+):** **Landscape** (`width: 16840 dxa`, printable table width `13443 dxa`) for CoCU 5-Column Matrix Table.
*   **LibreOffice ODT XML Patching:** For `.odt` documents, execute XML patching on `styles.xml` (`fo:page-width="29.7cm"` and `fo:page-height="21.001cm"` for `Converted1`) and `content.xml` (`style:page-name="Converted1"` on paragraph break before `Table2`) to ensure LibreOffice Writer natively transitions Page 1 to Portrait and Page 2+ to Landscape.
*   **Margins:** 1.0 inch (`1440 dxa`) on all sides (top, bottom, left, right).
*   **Fonts:** **Times New Roman** only.
    *   **Matrix Content:** `10 pt` (size `20` in half-points).
    *   **Normal Body Text:** `12 pt` (size `24` in half-points).
    *   **Titles / Headings:** H1: `14 pt` (size `28`) or `16 pt` (size `32`); H2: `12 pt` (size `24`).
*   **Cell Margins (Padding):** Top/Bottom/Left/Right: `55 dxa` (~2.75 pt).
*   **Borders:** Single solid line, `0.5 pt` size (`4` in docx package), black.

### 3.2 Specific Column Widths (in DXA)

To match the template tables exactly, column widths must be defined explicitly:

| Table Type | Column Widths (DXA) | Header Background Color |
| :--- | :--- | :--- |
| **CoCU Metadata (Header)** | `[2780, 10673]` | Left cell: `D9D9D9` (Light Grey) |
| **CoCU Matrix** | `[1814, 2268, 2835, 2835, 3691]` | All headers: `D9D9D9` (Light Grey) |
| **Element Weightage** | `[2154, 3842, 7684]` | All headers: `BFBFBF` (Medium Grey) |
| **Competency Weightage** | `[1836, 3204, 1851, 4247, 2299]` | All headers: `BFBFBF` (Medium Grey) |
| **TEM Matrix** | `[955, 3667, 1478]` *(1478 dxa per CU column)* | All headers: `BFBFBF` (Medium Grey) |

---

## 4. How to Use the Shared Formatting Module

AI agents should import layout settings and cell helpers from `scripts/utils/noss-docx-template.js`:

```js
const {
  PAGE_A4_PORTRAIT,
  PAGE_A4_LANDSCAPE,
  MARGIN_DEFAULT,
  COLOR_GREY_LIGHT,
  COLOR_GREY_MEDIUM,
  TABLE_WIDTHS,
  createTableCell,
  createMetadataRow,
  DEFAULT_DOCUMENT_STYLES
} = require('../utils/noss-docx-template');
```

### 4.1 Creating Paragraphs with Line Breaks and Bullets
Use the helper `createTableCell(content, options)` which parses line breaks (`<br>`) and bullet symbols (`•`) automatically.
*   Line breaks inside cells must be written as `<br>` in markdown strings.
*   Bullets must be written starting with a bullet symbol `•`.

### 4.2 Adding a Metadata Row
To append rows to the CU Metadata table:
```js
new TableRow({
  children: [
    createTableCell("SECTION", { width: TABLE_WIDTHS.COCU_HEADER[0], bg: COLOR_GREY_LIGHT, bold: true }),
    createTableCell("K62 COMPUTER PROGRAMMING...", { width: TABLE_WIDTHS.COCU_HEADER[1] })
  ]
})
```
Or use the shorthand helper:
```js
createMetadataRow("SECTION", "K62 COMPUTER PROGRAMMING...")
```

---

## 5. Matrix Guidelines & Rules

1.  **Landscape Orientation for Tables:** All matrix, weightage, and TEM tables must sit inside a landscape section.
    *   **CRITICAL FIX:** When defining `sections` in the `docx` library, you MUST explicitly include `type: SectionType.NEXT_PAGE` in the section properties to force Google Docs and LibreOffice to respect the orientation change.
    *   Example: `properties: { type: SectionType.NEXT_PAGE, page: { size: PAGE_A4_LANDSCAPE, margin: MARGIN_DEFAULT } }`
    *   **GOOGLE DOCS GEOMETRY HACK:** Due to a bug in the `docx` v7 library auto-swapping dimensions when `orientation: PageOrientation.LANDSCAPE` is set, you MUST intentionally define `PAGE_A4_LANDSCAPE` with reversed dimensions (`width: 11907`, `height: 16840`). This tricks the library into outputting the correct larger width in the XML.
2.  **Explicit Table Widths:** Always define explicit table widths (`width: { size: X, type: WidthType.DXA }`) when constructing tables.
    *   CoCU Matrix: `13443 dxa`
    *   CoCU Metadata: `13453 dxa`
    *   Competency Weightage: `13437 dxa`
    *   TEM Matrix: `13489 dxa`
3.  **Cross-Platform Table Borders:** Google Docs strictly ignores `insideH` and `insideV` borders applied at the `TableCell` level. You MUST explicitly pass a default border configuration (e.g. `borders: TABLE_BORDERS_DEFAULT`) to every `Table` wrapper instantiation.
    *   Failure to specify explicit widths will cause the tables to collapse to zero-width columns on the page margin in LibreOffice/Word.
3.  **Google Docs Table Layout Compatibility (CRITICAL):** When instantiating a `new Table(...)` from the `docx` library, you MUST explicitly declare `layout: TableLayoutType.FIXED` and provide the `columnWidths` array matching the DXA cell widths. Failure to include this will cause Google Docs to collapse all columns to zero width upon import.
    *   Example: `new Table({ width: { size: 9027, type: WidthType.DXA }, layout: TableLayoutType.FIXED, columnWidths: [2780, 6247], rows: docxRows })`
    *   You must also ensure `TableLayoutType` is imported from `docx`.
4.  **Learning Outcomes construction:** Dynamically build the learning outcome cell by gathering the work activities of the CU:
    `"The learning outcomes of this competency are to enable the trainees to perform <cuTitle>. Upon completion, trainees should be able to:<br>" + workActivitiesList`
5.  **Pedagogical Boundary:** Do not add Windows Server configuration/licensing items to Linux CUs or vice-versa. Maintain separate items or files.
6.  **Standalone Deliverables Architecture & Formatting Rules:**
    *   Deliverables MUST be generated as individual standalone files (`.odt`, `.docx`, `.md`) inside `noss-rebuild-v2/cocu/` (for core CoCU packages) and `noss-rebuild-v2/addon-knowledge/` (for support matrices and glossaries). Monolithic combined master documents are prohibited.
    *   **ODT Patching Constraint:** If a script generates `.odt` files with multiple CoCUs, the Python XML patcher (`patch_odt_landscape.py`) must be configured to loop through and patch **all** even-numbered tables (`Table2`, `Table4`, `Table6`, etc.) to ensure every matrix receives the `Converted1` landscape page style.
    *   Supporting reference document tables (Audit Matrix, TEM, Weightage, Abbreviations, Job Sheets) MUST NOT contain bullet points (`•`) inside table cells and MUST enforce **Times New Roman 10pt** font to match official CoCU standards.
    *   Section B / CoCU 5-column table formats and internal bullets MUST remain untouched.

---

## 6. Examples

*   **CoCU Matrix Generation Example:** See [example-generator.js](file:///D:/Users/LinuxMalaysia/Projects/skills-noss-l3/.agents/skills/noss-cocu-docx-formatter/examples/example-generator.js)
*   **TEM Matrix Generation Example:** See [example-tem-generator.js](file:///D:/Users/LinuxMalaysia/Projects/skills-noss-l3/.agents/skills/noss-cocu-docx-formatter/examples/example-tem-generator.js)


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
