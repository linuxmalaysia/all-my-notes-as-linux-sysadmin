/**
 * generate-audit-example-docx.js
 * ================================
 * Generates the example audit report DOCX for the noss-linguistic-auditor skill.
 * This creates a reference document showing PASS and FAIL audit findings
 * in the same table format used in the CP documents.
 *
 * Usage (one-time, to regenerate the example):
 *   node generate-audit-example-docx.js
 *
 * Output:
 *   ./audit-example-report.docx
 */

'use strict';

const fs   = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, Table, TableCell, TableRow,
  WidthType, TextRun, HeadingLevel, AlignmentType, BorderStyle
} = require('docx');

// ─── Colours ───────────────────────────────────────────────────
const GREEN  = 'C6EFCE'; // light green — PASS
const RED    = 'FFC7CE'; // light red   — FAIL
const YELLOW = 'FFEB9C'; // light amber — warning/fix
const GREY   = 'D9D9D9'; // grey        — header
const WHITE  = 'FFFFFF';

// ─── Helper functions ──────────────────────────────────────────
function run(text, opts = {}) {
  return new TextRun({ text, font: 'Times New Roman', size: 22, ...opts });
}

function para(text, align = AlignmentType.LEFT, opts = {}) {
  return new Paragraph({
    children: [run(text, opts)],
    alignment: align,
    spacing: { before: 60, after: 60 }
  });
}

function cell(content, fill = WHITE, colSpan = 1) {
  const children = Array.isArray(content) ? content : [para(content)];
  return new TableCell({
    children,
    shading: { fill },
    columnSpan: colSpan,
    margins: { top: 80, bottom: 80, left: 100, right: 100 },
    borders: {
      top:    { style: BorderStyle.SINGLE, size: 4, color: '000000' },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: '000000' },
      left:   { style: BorderStyle.SINGLE, size: 4, color: '000000' },
      right:  { style: BorderStyle.SINGLE, size: 4, color: '000000' }
    }
  });
}

function table(rows) {
  return new Table({ width: { size: 100, type: WidthType.PERCENTAGE }, rows });
}

function heading(text, level = HeadingLevel.HEADING_2) {
  return new Paragraph({ text, heading: level, spacing: { before: 200, after: 100 } });
}

function gap() {
  return new Paragraph({ text: '', spacing: { before: 80, after: 80 } });
}

// ─── Build the document ────────────────────────────────────────
const children = [];

// Title
children.push(new Paragraph({
  text: 'NOSS Linguistic Audit — Example Report',
  heading: HeadingLevel.HEADING_1
}));
children.push(gap());

// ── SECTION 1: Quality Gates Summary ──────────────────────────
children.push(heading('Quality Gates Reference'));
children.push(table([
  new TableRow({ children: [
    cell('Gate', GREY), cell('Name', GREY), cell('Applied To', GREY), cell('Rule', GREY)
  ]}),
  new TableRow({ children: [
    cell('G1'), cell('Active Voice'), cell('Work Steps'),
    cell('Must begin with present-tense action verb. No past-tense (-ed) starters.')
  ]}),
  new TableRow({ children: [
    cell('G2'), cell('Passive Voice'), cell('Performance Criteria'),
    cell('Must contain whitelist passive verb + end with "in accordance with [reference]".')
  ]}),
  new TableRow({ children: [
    cell('G3'), cell('1-to-1 Mapping'), cell('Per WA block'),
    cell('Step count must exactly equal Criteria count.')
  ]}),
  new TableRow({ children: [
    cell('G4'), cell('Language Cleanliness'), cell('All content'),
    cell('No vague phrases. No wrong-platform commands. No awk/sed/multi-pipe in trainee steps.')
  ]})
]));
children.push(gap());

// ── SECTION 2: Example A — PASS ───────────────────────────────
children.push(heading('Example A — CU03-WA01 (PASS)'));
children.push(para('WA: Prepare server installation requirements | IT-020-3:2026-CU03-WA01 | Platform: Linux'));
children.push(gap());

children.push(table([
  new TableRow({ children: [
    cell('#', GREY), cell('Work Step', GREY),
    cell('Performance Criterion', GREY), cell('Result', GREY)
  ]}),
  new TableRow({ children: [
    cell('1.1'),
    cell('Identify server installation specifications.'),
    cell('Server installation specifications analyzed in accordance with the enterprise server installation checklist.'),
    cell('✅ PASS', GREEN)
  ]}),
  new TableRow({ children: [
    cell('1.2'),
    cell('Identify server hardware requirements.'),
    cell('Hardware requirements determined in accordance with the hardware inventory record procedure.'),
    cell('✅ PASS', GREEN)
  ]}),
  new TableRow({ children: [
    cell('1.3'),
    cell('Identify server software requirements.'),
    cell('Server software requirements determined in accordance with software technical specifications.'),
    cell('✅ PASS', GREEN)
  ]}),
  new TableRow({ children: [
    cell('1.4'),
    cell('Map server network configuration settings.'),
    cell('Pre-installation server configuration details mapped in accordance with network addressing scheme.'),
    cell('✅ PASS', GREEN)
  ]}),
  new TableRow({ children: [
    cell('1.5'),
    cell('Prepare server installation tools and safety equipment.'),
    cell('Server installation tools and safety gear prepared in accordance with server environment handling guidelines.'),
    cell('✅ PASS', GREEN)
  ]})
]));
children.push(gap());
children.push(table([
  new TableRow({ children: [
    cell('AUDIT RESULT: ✅ PASS — IT-020-3:2026-CU03-WA01   Steps: 5 | Criteria: 5 | G1 ✓ | G2 ✓ | G3 ✓ | G4 ✓', GREEN, 4)
  ]})
]));
children.push(gap());

// ── SECTION 3: Example B — FAIL ───────────────────────────────
children.push(heading('Example B — CU03-WA02 (FAIL — Multiple Violations)'));
children.push(para('WA: Carry out server hardware installation | IT-020-3:2026-CU03-WA02 | Platform: Linux'));
children.push(gap());

children.push(table([
  new TableRow({ children: [
    cell('#', GREY), cell('Work Step', GREY), cell('Issue', GREY), cell('Gate', GREY)
  ]}),
  new TableRow({ children: [
    cell('2.1'), cell('Server chassis was unpacked and inspected for damage.', RED),
    cell('Starts with passive "was unpacked". Must use active voice.', RED), cell('G1 ❌', RED)
  ]}),
  new TableRow({ children: [
    cell('2.2'), cell('Assembled server processors, cooling modules, memory.', RED),
    cell('Past-tense "Assembled" — must be "Assemble".', RED), cell('G1 ❌', RED)
  ]}),
  new TableRow({ children: [
    cell('2.3'), cell('Mount server chassis on rack rails and secure it.', GREEN),
    cell('✅ OK — "Mount" is active voice.', GREEN), cell('G1 ✅', GREEN)
  ]}),
  new TableRow({ children: [
    cell('2.4'), cell('Make sure the cables are all plugged in properly.', YELLOW),
    cell('"Make sure" and "properly" are vague language.', YELLOW), cell('G4a ❌', RED)
  ]}),
  new TableRow({ children: [
    cell('2.5'), cell('Use ipconfig to check server IP after boot.', RED),
    cell('ipconfig is a Windows command — forbidden in Linux content.', RED), cell('G4b ❌', RED)
  ]})
]));
children.push(gap());

children.push(table([
  new TableRow({ children: [
    cell('#', GREY), cell('Performance Criterion', GREY), cell('Issue', GREY), cell('Gate', GREY)
  ]}),
  new TableRow({ children: [
    cell('2.1'), cell('Server chassis unpacked and modules inspected in accordance with safety guidelines.', GREEN),
    cell('✅ OK — passive verbs present.', GREEN), cell('G2 ✅', GREEN)
  ]}),
  new TableRow({ children: [
    cell('2.2'), cell('The technician assembles server hardware and checks it is working.', RED),
    cell('Active voice. Starts with "The technician". No "in accordance with".', RED), cell('G2 ❌', RED)
  ]}),
  new TableRow({ children: [
    cell('2.3'), cell('Server chassis mounted in accordance with datacenter mounting specs.', GREEN),
    cell('✅ OK', GREEN), cell('G2 ✅', GREEN)
  ]}),
  new TableRow({ children: [
    cell('2.4'), cell('All cables plugged in.', RED),
    cell('No passive verb from whitelist. No "in accordance with" reference.', RED), cell('G2 ❌', RED)
  ]}),
  new TableRow({ children: [
    cell('2.5 — MISSING', RED, 3),
  ]})
]));
children.push(gap());

children.push(table([
  new TableRow({ children: [
    cell('AUDIT RESULT: ❌ FAIL — IT-020-3:2026-CU03-WA02   Steps: 5 | Criteria: 4 | G1 ❌ | G2 ❌ | G3 ❌ | G4 ❌', RED, 4)
  ]})
]));
children.push(gap());

// ── SECTION 4: Corrected Version ──────────────────────────────
children.push(heading('Example C — CU03-WA02 Corrected (PASS)'));
children.push(table([
  new TableRow({ children: [
    cell('#', GREY), cell('Work Step (corrected)', GREY),
    cell('Performance Criterion (corrected)', GREY), cell('Result', GREY)
  ]}),
  new TableRow({ children: [
    cell('2.1'),
    cell('Unpack server chassis and inspect modules for damage.'),
    cell('Server chassis unpacked and internal modules inspected for damage in accordance with server safety guidelines.'),
    cell('✅ PASS', GREEN)
  ]}),
  new TableRow({ children: [
    cell('2.2'),
    cell('Assemble server processors, cooling modules, and memory channels.'),
    cell('Server processors, cooling modules, and memory channels assembled in accordance with server hardware installation manuals.'),
    cell('✅ PASS', GREEN)
  ]}),
  new TableRow({ children: [
    cell('2.3'),
    cell('Mount server chassis on rack rails and secure within the enclosure.'),
    cell('Server chassis mounted on rack rails and secured within the server rack enclosure in accordance with datacenter mounting specifications.'),
    cell('✅ PASS', GREEN)
  ]}),
  new TableRow({ children: [
    cell('2.4'),
    cell('Connect server interface cables firmly to the designated ports.'),
    cell('Server physical interface connections connected firmly in accordance with cabling protocols.'),
    cell('✅ PASS', GREEN)
  ]}),
  new TableRow({ children: [
    cell('2.5'),
    cell('Boot up the server and verify the POST status output.'),
    cell('Server Power-On Self-Test (POST) status verified without errors in accordance with controller BIOS specifications.'),
    cell('✅ PASS', GREEN)
  ]})
]));
children.push(gap());
children.push(table([
  new TableRow({ children: [
    cell('AUDIT RESULT: ✅ PASS — IT-020-3:2026-CU03-WA02 (corrected)   Steps: 5 | Criteria: 5 | G1 ✓ | G2 ✓ | G3 ✓ | G4 ✓', GREEN, 4)
  ]})
]));

// ─── Write output ──────────────────────────────────────────────
const doc = new Document({
  sections: [{
    properties: { page: { margin: { top: 720, right: 720, bottom: 720, left: 720 } } },
    children
  }]
});

(async () => {
  const buf = await Packer.toBuffer(doc);
  const outPath = path.join(__dirname, 'audit-example-report.docx');
  fs.writeFileSync(outPath, buf);
  console.log('✓ DOCX written:', outPath);
})();
