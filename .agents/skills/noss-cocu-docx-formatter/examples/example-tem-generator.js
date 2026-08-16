const fs = require('fs');
const path = require('path');
const { Document, Packer, Paragraph, Table, TableRow, AlignmentType, HeadingLevel, WidthType } = require('docx');

// Import the shared template utility
const {
  PAGE_A4_LANDSCAPE,
  MARGIN_DEFAULT,
  COLOR_GREY_MEDIUM,
  createTableCell,
  DEFAULT_DOCUMENT_STYLES
} = require('../../../../scripts/utils/noss-docx-template');

const outputPath = path.join(__dirname, 'Sample-TEM.docx');

function generateSampleTEM() {
  console.log("Generating sample TEM document...");

  const docChildren = [];

  // Title
  docChildren.push(new Paragraph({
    heading: HeadingLevel.HEADING_2,
    children: [
      createTableCell("Tools, Equipment & Materials (TEM) Matrix", { bold: true, size: 24 })
    ],
    spacing: { before: 180, after: 180 }
  }));

  // Matrix Table Setup
  const matrixRows = [];
  const wNo = 955;
  const wItem = 3667;
  const wRatioTotal = 8867;
  const wRatioCol = Math.round(wRatioTotal / 6); // ~1478 dxa per column

  // Header row 1: NO. | ITEM* | RATIO (colSpan=6)
  matrixRows.push(new TableRow({
    children: [
      createTableCell("NO.", { width: wNo, bg: COLOR_GREY_MEDIUM, bold: true, alignment: AlignmentType.CENTER, rowSpan: 2 }),
      createTableCell("ITEM*", { width: wItem, bg: COLOR_GREY_MEDIUM, bold: true, alignment: AlignmentType.CENTER, rowSpan: 2 }),
      createTableCell("RATIO (TEM : Trainees or AR = As Required)", { width: wRatioTotal, bg: COLOR_GREY_MEDIUM, bold: true, alignment: AlignmentType.CENTER, colSpan: 6 })
    ]
  }));

  // Header row 2: C01, C02, C03, C04, C05, C06
  matrixRows.push(new TableRow({
    children: [
      createTableCell("C01", { width: wRatioCol, bg: COLOR_GREY_MEDIUM, bold: true, alignment: AlignmentType.CENTER }),
      createTableCell("C02", { width: wRatioCol, bg: COLOR_GREY_MEDIUM, bold: true, alignment: AlignmentType.CENTER }),
      createTableCell("C03", { width: wRatioCol, bg: COLOR_GREY_MEDIUM, bold: true, alignment: AlignmentType.CENTER }),
      createTableCell("C04", { width: wRatioCol, bg: COLOR_GREY_MEDIUM, bold: true, alignment: AlignmentType.CENTER }),
      createTableCell("C05", { width: wRatioCol, bg: COLOR_GREY_MEDIUM, bold: true, alignment: AlignmentType.CENTER }),
      createTableCell("C06", { width: wRatioCol, bg: COLOR_GREY_MEDIUM, bold: true, alignment: AlignmentType.CENTER })
    ]
  }));

  // Category Helper Row
  function addCategoryRow(title) {
    matrixRows.push(new TableRow({
      children: [
        createTableCell("", { width: wNo, bg: COLOR_GREY_MEDIUM }),
        createTableCell(title, { width: wItem + wRatioTotal, bold: true, colSpan: 7 })
      ]
    }));
  }

  addCategoryRow("A. Tools");
  
  // Add a sample item row
  matrixRows.push(new TableRow({
    children: [
      createTableCell("1", { width: wNo, alignment: AlignmentType.CENTER }),
      createTableCell("Cable stripper", { width: wItem }),
      createTableCell("1:5", { width: wRatioCol, alignment: AlignmentType.CENTER }),
      createTableCell("", { width: wRatioCol }),
      createTableCell("", { width: wRatioCol }),
      createTableCell("", { width: wRatioCol }),
      createTableCell("", { width: wRatioCol }),
      createTableCell("1:5", { width: wRatioCol, alignment: AlignmentType.CENTER })
    ]
  }));

  // Append Table with explicit table width in DXA to prevent collapsing
  docChildren.push(new Table({
    width: { size: 13489, type: WidthType.DXA },
    rows: matrixRows
  }));

  const doc = new Document({
    styles: DEFAULT_DOCUMENT_STYLES,
    sections: [{
      properties: {
        page: {
          size: PAGE_A4_LANDSCAPE,
          margin: MARGIN_DEFAULT,
        },
      },
      children: docChildren
    }]
  });

  Packer.toBuffer(doc).then((buffer) => {
    fs.writeFileSync(outputPath, buffer);
    console.log(`Saved sample TEM to: ${outputPath}`);
  });
}

generateSampleTEM();
