/**
 * minimal-cpc-generator.js
 * ========================
 * NOSS CPC DOCX Formatter Skill — Standalone Example
 *
 * Purpose:
 *   Demonstrates the exact docx library API calls required to produce
 *   a CPC document matching the CPC-Level-3-Generated.docx reference format.
 *
 *   This example produces BOTH a Markdown (.md) and DOCX (.docx) output.
 *
 * Usage:
 *   node minimal-cpc-generator.js
 *
 * Output:
 *   ./example-cpc-output.md
 *   ./example-cpc-output.docx
 *
 * Dependencies:
 *   npm install docx
 */

'use strict';

const fs   = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, Table, TableCell, TableRow,
  WidthType, TextRun, HeadingLevel, AlignmentType, VerticalAlign, BorderStyle
} = require('docx');

// ─────────────────────────────────────────────
// COLOUR CONSTANTS (matching reference DOCX exactly)
// ─────────────────────────────────────────────
const COLOR_ORANGE = 'FFC000'; // CORE column
const COLOR_YELLOW = 'FFFF00'; // CU Title cells
const COLOR_GREEN  = '92D050'; // CU Code cells + column header
const COLOR_BLUE   = 'DDEBF7'; // WA Code cells + column header
const COLOR_WHITE  = 'FFFFFF'; // WA Title cells, spacers
const COLOR_GREY   = 'EFEFEF'; // Metadata label cells (Table 1)

// ─────────────────────────────────────────────
// SAMPLE DATA (replace with data parsed from profile .md files)
// ─────────────────────────────────────────────

const NOSS_METADATA = {
  section:   'K62 COMPUTER PROGRAMMING, CONSULTANCY AND RELATED ACTIVITIES',
  group:     '622 COMPUTER CONSULTANCY AND COMPUTER FACILITIES MANAGEMENT ACTIVITIES',
  area:      'IT INFRASTRUCTURE',
  nossTitle: 'Sovereign IT Infrastructure Operations',
  nossLevel: 'LEVEL 3',
  nossCode:  'IT-020-3:2026'
};

// CU data: title must be UPPERCASE for DOCX, WAs are arrays of {name, code}
const SAMPLE_CUS = [
  {
    cuName: 'PERFORM BASIC COMPUTER SYSTEM INSTALLATION AND CONFIGURATION',
    cuCode: 'CODE CU01',
    cuTitleMD: 'PERFORM BASIC COMPUTER SYSTEM INSTALLATION AND CONFIGURATION',
    cuCodeMD:  'CU01',
    was: [
      { name: 'Prepare computer system set-up components.',     code: 'CODE CU01-WA01', codeMD: 'CU01-WA01' },
      { name: 'Carry out computer system hardware installation.',code: 'CODE CU01-WA02', codeMD: 'CU01-WA02' },
      { name: 'Carry out computer Operating System (OS) software installation.', code: 'CODE CU01-WA03', codeMD: 'CU01-WA03' },
      { name: 'Carry out computer application, peripheral and device driver installation.', code: 'CODE CU01-WA04', codeMD: 'CU01-WA04' },
      { name: 'Configure static IP and wireless network parameters.', code: 'CODE CU01-WA05', codeMD: 'CU01-WA05' },
      { name: 'Prepare computer system installation record.',    code: 'CODE CU01-WA06', codeMD: 'CU01-WA06' }
    ]
  },
  {
    cuName: 'SERVER INSTALLATION & MAINTENANCE',
    cuCode: 'CODE CU03',
    cuTitleMD: 'SERVER INSTALLATION & MAINTENANCE',
    cuCodeMD:  'CU03',
    was: [
      { name: 'Prepare server installation requirements.',      code: 'CODE CU03-WA01', codeMD: 'CU03-WA01' },
      { name: 'Carry out server hardware installation.',        code: 'CODE CU03-WA02', codeMD: 'CU03-WA02' },
      { name: 'Carry out server software and OS installation.', code: 'CODE CU03-WA03', codeMD: 'CU03-WA03' },
      { name: 'Perform server functionality testing and maintenance.', code: 'CODE CU03-WA04', codeMD: 'CU03-WA04' },
      { name: 'Prepare server installation and maintenance records.', code: 'CODE CU03-WA05', codeMD: 'CU03-WA05' }
    ]
  }
];

// ─────────────────────────────────────────────
// HELPER FUNCTIONS
// ─────────────────────────────────────────────

/** Standard text run — Times New Roman 11pt */
function run(text, opts = {}) {
  return new TextRun({ text, font: 'Times New Roman', size: 22, ...opts });
}

/** Paragraph with optional alignment and spacing */
function para(text, align = AlignmentType.CENTER, opts = {}) {
  return new Paragraph({
    children: [run(text, opts)],
    alignment: align,
    spacing: { before: 100, after: 100 }
  });
}

/** Standard bordered cell with colour fill */
function cell(content, bgColor = COLOR_WHITE, colSpan = 1, rowSpan = 1) {
  const children = Array.isArray(content)
    ? content
    : [para(typeof content === 'string' ? content : '', AlignmentType.CENTER)];

  return new TableCell({
    children,
    shading:       { fill: bgColor },
    columnSpan:    colSpan,
    rowSpan:       rowSpan,
    verticalAlign: VerticalAlign.CENTER,
    margins:       { top: 100, bottom: 100, left: 100, right: 100 },
    borders: {
      top:    { style: BorderStyle.SINGLE, size: 4, color: '000000' },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: '000000' },
      left:   { style: BorderStyle.SINGLE, size: 4, color: '000000' },
      right:  { style: BorderStyle.SINGLE, size: 4, color: '000000' }
    }
  });
}

/** Red text cell for metadata values */
function redCell(text, colSpan = 1) {
  return cell(
    [new Paragraph({
      children: [run(text, { color: 'FF0000' })],
      alignment: AlignmentType.CENTER,
      spacing: { before: 100, after: 100 }
    })],
    COLOR_WHITE, colSpan
  );
}

/** Grey label cell for metadata keys */
function greyCell(text) {
  return cell(
    [new Paragraph({
      children: [run(text, { bold: false })],
      alignment: AlignmentType.CENTER,
      spacing: { before: 100, after: 100 }
    })],
    COLOR_GREY
  );
}

// ─────────────────────────────────────────────
// BUILD TABLE 1 — METADATA HEADER
// ─────────────────────────────────────────────

function buildMetadataTable(meta) {
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows: [
      new TableRow({ children: [ greyCell('SECTION'),    redCell(meta.section,   4) ] }),
      new TableRow({ children: [ greyCell('GROUP'),      redCell(meta.group,     4) ] }),
      new TableRow({ children: [ greyCell('AREA'),       redCell(meta.area,      4) ] }),
      new TableRow({ children: [ greyCell('NOSS TITLE'), redCell(meta.nossTitle, 4) ] }),
      new TableRow({ children: [
        greyCell('NOSS LEVEL'),
        redCell(meta.nossLevel),
        greyCell('NOSS CODE'),
        redCell(meta.nossCode, 2)
      ]})
    ]
  });
}

// ─────────────────────────────────────────────
// BUILD TABLE 2 — CPC GRID
// ─────────────────────────────────────────────

function buildCpcGrid(cuList) {
  const rows = [];

  // ── Header row ──────────────────────────────
  rows.push(new TableRow({ children: [
    cell('',               COLOR_WHITE),              // col 0: spacer
    cell('←COMPETENCY UNIT→', COLOR_GREEN),           // col 1: CU header
    cell('←WORK ACTIVITIES→', COLOR_BLUE, 4)          // col 2-5: WA header (colspan=4)
  ]}));

  // ── Blank spacer row ────────────────────────
  rows.push(new TableRow({ children: [ cell('', COLOR_WHITE, 6) ] }));

  // ── Per-CU blocks ───────────────────────────
  cuList.forEach((cu, cuIdx) => {
    const wasFirst   = cu.was.slice(0, 4);   // WAs 1–4
    const wasOverflow = cu.was.slice(4);      // WAs 5+ (overflow)
    const hasOverflow = wasOverflow.length > 0;

    // Orange CORE col rowSpan: 2 rows if ≤4 WAs, 4 rows if >4 WAs
    const coreRowSpan = hasOverflow ? 4 : 2;
    const coreText    = cuIdx === 0 ? 'C\nO\nR\nE' : '';

    // Pad arrays to 4 slots
    const waNameRow1 = [...wasFirst.map(w => w.name), ...Array(4 - wasFirst.length).fill('')];
    const waCodeRow1 = [...wasFirst.map(w => w.code), ...Array(4 - wasFirst.length).fill('')];

    // ── Name row A ──
    rows.push(new TableRow({ children: [
      cell(coreText, COLOR_ORANGE, 1, coreRowSpan), // orange CORE col — rowSpan
      cell(cu.cuName, COLOR_YELLOW),                 // CU title
      ...waNameRow1.map(n => cell(n, COLOR_WHITE))   // WA names 1–4
    ]}));

    // ── Code row A ──
    rows.push(new TableRow({ children: [
      // col 0: vMerge continuation — pass empty cell, rowSpan handled by docx library
      cell(cu.cuCode, COLOR_GREEN),                  // CU code
      ...waCodeRow1.map(c => cell(c, COLOR_BLUE))    // WA codes 1–4
    ]}));

    // ── Overflow rows (if > 4 WAs) ──
    if (hasOverflow) {
      const waNameRow2 = [...wasOverflow.map(w => w.name), ...Array(4 - wasOverflow.length).fill('')];
      const waCodeRow2 = [...wasOverflow.map(w => w.code), ...Array(4 - wasOverflow.length).fill('')];

      rows.push(new TableRow({ children: [
        cell('', COLOR_WHITE),                        // col 1: empty
        ...waNameRow2.map(n => cell(n, COLOR_WHITE))  // WA names 5–8
      ]}));

      rows.push(new TableRow({ children: [
        cell('', COLOR_WHITE),                        // col 1: empty
        ...waCodeRow2.map(c => cell(c, COLOR_BLUE))   // WA codes 5–8
      ]}));
    }

    // ── Spacer row after each CU ──
    rows.push(new TableRow({ children: [ cell('', COLOR_WHITE, 6) ] }));
  });

  return new Table({
    width:  { size: 50, type: WidthType.PERCENTAGE }, // 50% of page width
    layout: 'fixed',
    rows
  });
}

// ─────────────────────────────────────────────
// BUILD MARKDOWN OUTPUT
// ─────────────────────────────────────────────

function buildMarkdown(meta, cuList) {
  const lines = [];

  lines.push('# Competency Profile Chart (CPC)');
  lines.push('');
  lines.push(`| SECTION | ${meta.section} |`);
  lines.push('| :--- | :--- |');
  lines.push(`| **GROUP** | ${meta.group} |`);
  lines.push(`| **AREA** | ${meta.area} |`);
  lines.push(`| **NOSS TITLE** | ${meta.nossTitle} |`);
  lines.push(`| **NOSS LEVEL** | ${meta.nossLevel} |`);
  lines.push(`| **NOSS CODE** | ${meta.nossCode} |`);
  lines.push('');
  lines.push('');
  lines.push('## 🟢 CORE COMPETENCIES');
  lines.push('');
  lines.push('| COMPETENCY UNIT (CU) | WORK ACTIVITIES (WA) |');
  lines.push('| :--- | :--- |');

  cuList.forEach(cu => {
    const cuCell = `**${cu.cuTitleMD}**<br>\`[CODE: ${cu.cuCodeMD}]\``;
    const waEntries = cu.was.map((wa, i) => {
      // Strip trailing period for MD display, keep WA name clean
      const name = wa.name.replace(/\.$/, '');
      return `**${i + 1}.** ${name} \`[${wa.codeMD}]\``;
    });
    const waCell = waEntries.join('<br><br>');
    lines.push(`| ${cuCell} | ${waCell} |`);
  });

  lines.push('');
  lines.push('---');
  lines.push('*Note: This Markdown CPC maps identically to the backend `.agents/skills` registry.*');
  lines.push('');

  return lines.join('\n');
}

// ─────────────────────────────────────────────
// MAIN
// ─────────────────────────────────────────────

(async () => {
  // Build DOCX
  const metadataTable = buildMetadataTable(NOSS_METADATA);
  const gridTable     = buildCpcGrid(SAMPLE_CUS);

  const doc = new Document({
    sections: [{
      properties: {
        page: { margin: { top: 720, right: 720, bottom: 720, left: 720 } }
      },
      children: [
        new Paragraph({ text: '1. Competency Profile Chart (CPC)', heading: HeadingLevel.HEADING_1 }),
        new Paragraph(''),
        metadataTable,
        new Paragraph(''),
        gridTable
      ]
    }]
  });

  const buffer   = await Packer.toBuffer(doc);
  const docxPath = path.join(__dirname, 'example-cpc-output.docx');
  fs.writeFileSync(docxPath, buffer);
  console.log('✓ DOCX written:', docxPath);

  // Build Markdown
  const mdContent = buildMarkdown(NOSS_METADATA, SAMPLE_CUS);
  const mdPath    = path.join(__dirname, 'example-cpc-output.md');
  fs.writeFileSync(mdPath, mdContent, 'utf8');
  console.log('✓ Markdown written:', mdPath);
})();
