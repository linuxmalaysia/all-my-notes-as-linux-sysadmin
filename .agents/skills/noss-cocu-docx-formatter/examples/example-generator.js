const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, Table, TableRow, AlignmentType, HeadingLevel } = require('docx');

// Import the shared template utility
const {
  PAGE_A4_PORTRAIT,
  PAGE_A4_LANDSCAPE,
  MARGIN_DEFAULT,
  COLOR_GREY_LIGHT,
  TABLE_WIDTHS,
  createTableCell,
  createMetadataRow,
  DEFAULT_DOCUMENT_STYLES
} = require('../../../../scripts/utils/noss-docx-template');

const outputPath = path.join(__dirname, 'Sample-CoCU.docx');

function generateSample() {
  console.log("Generating sample CoCU document...");

  const sections = [];

  // 1. Portrait Section: Cover Page
  sections.push({
    properties: {
      page: {
        size: PAGE_A4_PORTRAIT,
        margin: MARGIN_DEFAULT,
      },
    },
    children: [
      new Paragraph({ text: "", spacing: { before: 2000 } }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [
          createTableCell("NOSS DOCUMENT COMPILATION SAMPLE", { bold: true, size: 28 })
        ]
      })
    ]
  });

  // 2. Landscape Section: CoCU Matrix Table
  const landscapeChildren = [];

  // Title
  landscapeChildren.push(new Paragraph({
    heading: HeadingLevel.HEADING_2,
    children: [
      createTableCell("CU01: Perform Computer Installation", { bold: true, size: 24 })
    ],
    spacing: { before: 180, after: 180 }
  }));

  // Metadata Header Table
  const metadataRows = [
    createMetadataRow("SECTION", "K62 COMPUTER PROGRAMMING..."),
    createMetadataRow("GROUP", "622 COMPUTER CONSULTANCY..."),
    createMetadataRow("AREA", "Information Technology Operation"),
    createMetadataRow("CU CODE", "K622-XXX-3:2026-C01"),
  ];

  landscapeChildren.push(new Table({
    rows: metadataRows,
    spacing: { after: 300 }
  }));

  // Matrix Table
  const matrixRows = [
    // Header Row
    new TableRow({
      children: [
        createTableCell("WORK ACTIVITIES", { width: TABLE_WIDTHS.COCU_MATRIX[0], bg: COLOR_GREY_LIGHT, bold: true, alignment: AlignmentType.CENTER }),
        createTableCell("RELATED KNOWLEDGE", { width: TABLE_WIDTHS.COCU_MATRIX[1], bg: COLOR_GREY_LIGHT, bold: true, alignment: AlignmentType.CENTER }),
        createTableCell("RELATED SKILLS", { width: TABLE_WIDTHS.COCU_MATRIX[2], bg: COLOR_GREY_LIGHT, bold: true, alignment: AlignmentType.CENTER }),
        createTableCell("ATTITUDE/ SAFETY/ ENVIRONMENT", { width: TABLE_WIDTHS.COCU_MATRIX[3], bg: COLOR_GREY_LIGHT, bold: true, alignment: AlignmentType.CENTER }),
        createTableCell("ASSESSMENT CRITERIA", { width: TABLE_WIDTHS.COCU_MATRIX[4], bg: COLOR_GREY_LIGHT, bold: true, alignment: AlignmentType.CENTER }),
      ]
    }),
    // Data Row
    new TableRow({
      children: [
        createTableCell("1. Prepare computer setup.", { width: TABLE_WIDTHS.COCU_MATRIX[0] }),
        createTableCell("1.1 OS requirements:<br>• CPU specs<br>• RAM requirements", { width: TABLE_WIDTHS.COCU_MATRIX[1] }),
        createTableCell("1.1 Check OS version.", { width: TABLE_WIDTHS.COCU_MATRIX[2] }),
        createTableCell("**ATTITUDE**<br>1.1 Precise alignment checking.", { width: TABLE_WIDTHS.COCU_MATRIX[3] }),
        createTableCell("**COGNITIVE**<br>• Hardware specs explained.", { width: TABLE_WIDTHS.COCU_MATRIX[4] }),
      ]
    })
  ];

  landscapeChildren.push(new Table({
    rows: matrixRows
  }));

  sections.push({
    properties: {
      page: {
        size: PAGE_A4_LANDSCAPE,
        margin: MARGIN_DEFAULT,
      },
    },
    children: landscapeChildren
  });

  const doc = new Document({
    styles: DEFAULT_DOCUMENT_STYLES,
    sections: sections
  });

  Packer.toBuffer(doc).then((buffer) => {
    fs.writeFileSync(outputPath, buffer);
    console.log(`Saved sample CoCU to: ${outputPath}`);
  });
}

generateSample();
