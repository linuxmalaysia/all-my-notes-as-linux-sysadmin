/**
 * minimal-cp-generator.js
 * ========================
 * NOSS CP DOCX Formatter Skill — Standalone Example
 *
 * Purpose:
 *   Demonstrates the exact docx library API calls required to produce
 *   a CP document matching the CP-Level-3-Generated.docx reference format.
 *
 * Usage:
 *   node minimal-cp-generator.js
 *
 * Output:
 *   ./example-cp-output.md
 *   ./example-cp-output.docx
 *
 * Dependencies:
 *   npm install docx
 */

'use strict';

const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, Table, TableCell, TableRow,
  WidthType, TextRun, HeadingLevel
} = require('docx');

// ─────────────────────────────────────────────
// SAMPLE DATA (replace with parsed profile data)
// ─────────────────────────────────────────────

const NOSS_METADATA = {
  section: '(J) Information and Communication',
  group:   '(620) Computer Programming, Consultancy and Related Activities',
  area:    'Computer System Administration',
  title:   'Sovereign IT Infrastructure Operations',
  level:   'LEVEL 3',
  code:    'IT-020-3:2026'
};

const SAMPLE_CUS = [
  {
    title: 'Server Installation & Maintenance',
    code:  'IT-020-3:2026-CU03',
    desc:
      'Server Installation & Maintenance describes mounting servers in cabinets, ' +
      'deploying server OS, configuring Netplan IPs, checking server room ' +
      'environments, and managing server registries. ' +
      'This activity typically takes place in server environments and is performed ' +
      'to ensure hardware and OS baseline readiness.\n\n' +
      'The person who is competent in this CU should be able to prepare server ' +
      'installation requirements, carry out server hardware installation, carry out ' +
      'server software and OS installation, perform server functionality testing and ' +
      'maintenance, and prepare server installation and maintenance records.\n\n' +
      'The outcome of this CU is a successfully rack-mounted server with a configured ' +
      'base OS and registered inventory details.',
    was: [
      {
        name: 'Prepare server installation requirements',
        code: 'IT-020-3:2026-CU03-WA01',
        steps: [
          'Identify server installation specifications.',
          'Identify server hardware requirements.',
          'Identify server software requirements.',
          'Map server network configuration settings.',
          'Prepare server installation tools and safety equipment.'
        ],
        pcs: [
          'Server installation specifications and deployment requirements analyzed in accordance with the enterprise server installation checklist.',
          'Server physical form factor (tower, rack, or blade unit) and hardware module specs determined in accordance with the hardware inventory record procedure.',
          'Server operating systems, virtualization platforms, and system configuration profiles determined in accordance with software technical specifications.',
          'Pre-installation server configuration details (hostnames, static IPs, subnet masks, DNS settings) mapped in accordance with network addressing scheme.',
          'Server installation tools and hardware handling safety gear prepared in accordance with server environment handling guidelines.'
        ]
      }
    ]
  }
];

// ─────────────────────────────────────────────
// HELPER FUNCTIONS
// ─────────────────────────────────────────────

/**
 * Creates a styled TextRun with Times New Roman 11pt.
 */
function run(text, bold = false) {
  return new TextRun({
    text,
    bold,
    font: 'Times New Roman',
    size: 22            // 22 half-points = 11pt
  });
}

/**
 * Creates a Paragraph containing a single styled TextRun.
 */
function para(text, bold = false) {
  return new Paragraph({ children: [run(text, bold)] });
}

/**
 * Creates a TableCell with standard margins and optional colspan.
 *
 * @param {string|Paragraph|Paragraph[]} content
 * @param {number} widthPct - percentage width (0-100)
 * @param {boolean} bold
 * @param {number} colSpan - number of columns this cell spans
 */
function cell(content, widthPct, bold = false, colSpan = 1) {
  let children;
  if (Array.isArray(content)) {
    children = content.map(c =>
      typeof c === 'string' ? para(c, bold) : c
    );
  } else if (typeof content === 'string') {
    children = [para(content, bold)];
  } else {
    children = [content];
  }

  return new TableCell({
    children,
    width:      { size: widthPct, type: WidthType.PERCENTAGE },
    columnSpan: colSpan,
    margins:    { top: 100, bottom: 100, left: 100, right: 100 }
  });
}

/**
 * Creates a standard full-width table with single borders.
 */
function table(rows) {
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    rows
  });
}

// ─────────────────────────────────────────────
// DOCUMENT BUILDER
// ─────────────────────────────────────────────

function buildDocument(metadata, cuList) {
  const docChildren = [];
  let mdLines = [];

  // ── Heading ──────────────────────────────────
  docChildren.push(
    new Paragraph({ text: '1. Competency Profile (CP)', heading: HeadingLevel.HEADING_1 })
  );
  docChildren.push(new Paragraph(''));

  mdLines.push('# 1. Competency Profile (CP)');
  mdLines.push('');

  // ── Header Metadata Table ─────────────────────
  docChildren.push(table([
    new TableRow({ children: [
      cell('SECTION',    25, true),
      cell(metadata.section, 75, true, 3)
    ]}),
    new TableRow({ children: [
      cell('GROUP',      25, true),
      cell(metadata.group,   75, true, 3)
    ]}),
    new TableRow({ children: [
      cell('AREA',       25, true),
      cell(metadata.area,    75, true, 3)
    ]}),
    new TableRow({ children: [
      cell('NOSS TITLE', 25, true),
      cell(metadata.title,   75, true, 3)
    ]}),
    new TableRow({ children: [
      cell('NOSS LEVEL', 25, true),
      cell(metadata.level,   25),
      cell('NOSS CODE',  25, true),
      cell(metadata.code,    25)
    ]})
  ]));
  docChildren.push(new Paragraph(''));

  mdLines.push(`| SECTION | ${metadata.section} | | |`);
  mdLines.push(`| :---- | :---- | :---- | :---- |`);
  mdLines.push(`| GROUP | ${metadata.group} | | |`);
  mdLines.push(`| AREA | ${metadata.area} | | |`);
  mdLines.push(`| NOSS TITLE | ${metadata.title} | | |`);
  mdLines.push(`| NOSS LEVEL | ${metadata.level} | NOSS CODE | ${metadata.code} |`);
  mdLines.push('');

  // ── Per-CU Blocks ─────────────────────────────
  for (const cu of cuList) {

    // CU Header Table (DOCX)
    docChildren.push(table([
      new TableRow({ children: [
        cell('CU TITLE & CU CODE', 25, true),
        cell(`${cu.title} (${cu.code})`, 75, true)
      ]}),
      new TableRow({ children: [
        cell('CU DESCRIPTOR', 25, true),
        // Descriptor: one Paragraph per `\n\n` separated block
        cell(
          cu.desc.split('\n\n').map(block => para(block, false)),
          75, false
        )
      ]})
    ]));
    docChildren.push(new Paragraph(''));

    // CU Header Table (MD)
    const descMD = cu.desc.replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>');
    mdLines.push(`| CU TITLE & CU CODE | ${cu.title} (${cu.code}) |`);
    mdLines.push(`| :---- | :---- |`);
    mdLines.push(`| CU DESCRIPTOR | ${descMD} |`);
    mdLines.push('');

    // WA Matrix Table (DOCX)
    const waRows = [
      new TableRow({ children: [
        cell('WORK ACTIVITIES',     30, true),
        cell('WORK STEPS',          35, true),
        cell('PERFORMANCE CRITERIA',35, true)
      ]})
    ];

    // WA Matrix Table (MD)
    mdLines.push(`| WORK ACTIVITIES | WORK STEPS | PERFORMANCE CRITERIA |`);
    mdLines.push(`| ----- | ----- | ----- |`);

    cu.was.forEach((wa, waIdx) => {
      const waNum = waIdx + 1;

      // DOCX: one Paragraph per step/PC
      const stepParas = wa.steps.map((s, i) => para(`${waNum}.${i+1} ${s}`));
      const pcParas   = wa.pcs.map(  (p, i) => para(`${waNum}.${i+1} ${p}`));

      waRows.push(new TableRow({ children: [
        cell(`${wa.name}.\n(${wa.code})`, 30, false),
        cell(stepParas, 35),
        cell(pcParas,   35)
      ]}));

      // MD: steps and PCs joined with <br>
      const stepsMD = wa.steps.map((s, i) => `${waNum}.${i+1} ${s}`).join('<br>');
      const pcsMD   = wa.pcs.map(  (p, i) => `${waNum}.${i+1} ${p}`).join('<br>');
      mdLines.push(`| ${wa.name}..<br>(${wa.code}) | ${stepsMD} | ${pcsMD} |`);
    });

    docChildren.push(table(waRows));
    docChildren.push(new Paragraph('\n'));
    mdLines.push('');
  }

  return { docChildren, mdContent: mdLines.join('\n') };
}

// ─────────────────────────────────────────────
// MAIN
// ─────────────────────────────────────────────

(async () => {
  const { docChildren, mdContent } = buildDocument(NOSS_METADATA, SAMPLE_CUS);

  // Write Markdown
  const mdPath = path.join(__dirname, 'example-cp-output.md');
  fs.writeFileSync(mdPath, mdContent, 'utf8');
  console.log(`✓ Markdown written: ${mdPath}`);

  // Write DOCX
  const doc = new Document({
    sections: [{
      properties: {
        page: { margin: { top: 720, right: 720, bottom: 720, left: 720 } }
      },
      children: docChildren
    }]
  });

  const buffer = await Packer.toBuffer(doc);
  const docxPath = path.join(__dirname, 'example-cp-output.docx');
  fs.writeFileSync(docxPath, buffer);
  console.log(`✓ DOCX written:     ${docxPath}`);
})();
