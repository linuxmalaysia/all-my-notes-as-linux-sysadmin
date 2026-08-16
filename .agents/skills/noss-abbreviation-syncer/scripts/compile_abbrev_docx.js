/**
 * @file compile_abbrev_docx.js
 * @description Highly detailed JSDoc comments for compile_abbrev_docx.js.
 * Provides module operations and internal functions.
 */
const fs = require("fs");
const path = require("path");
const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  Table,
  TableRow,
  TableCell,
  WidthType,
  AlignmentType,
  BorderStyle,
  TableLayoutType
} = require("docx");

// Read from the JSON dumped by the Python sync script
const rawData = fs.readFileSync(path.join(__dirname, "../../../../noss-l3-latest/scripts/abbreviations_data.json"), "utf8");
const data = JSON.parse(rawData);

// The faint blue dotted borders matching the standard
const TABLE_BORDERS = {
  top: { style: BorderStyle.DOTTED, size: 4, color: "88B4DE" },
  bottom: { style: BorderStyle.DOTTED, size: 4, color: "88B4DE" },
  left: { style: BorderStyle.DOTTED, size: 4, color: "88B4DE" },
  right: { style: BorderStyle.DOTTED, size: 4, color: "88B4DE" },
  insideHorizontal: { style: BorderStyle.DOTTED, size: 4, color: "88B4DE" },
  insideVertical: { style: BorderStyle.DOTTED, size: 4, color: "88B4DE" },
};

const rows = [];

for (let i = 0; i < data.length; i++) {
  const item = data[i];
  rows.push(
    new TableRow({
      children: [
        new TableCell({
          width: { size: 1000, type: WidthType.DXA },
          children: [
            new Paragraph({
              children: [new TextRun({ text: (i + 1).toString(), font: "Times New Roman", size: 24 })],
            }),
          ],
        }),
        new TableCell({
          width: { size: 2500, type: WidthType.DXA },
          children: [
            new Paragraph({
              children: [new TextRun({ text: item.acronym, font: "Times New Roman", size: 24 })],
            }),
          ],
        }),
        new TableCell({
          width: { size: 6000, type: WidthType.DXA },
          children: [
            new Paragraph({
              children: [new TextRun({ text: item.definition, font: "Times New Roman", size: 24 })],
            }),
          ],
        }),
      ],
    })
  );
}

const doc = new Document({
  sections: [
    {
      properties: {},
      children: [
        new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({
              text: "Abbreviation",
              bold: true,
              font: "Times New Roman",
              size: 24, // 12pt
            }),
          ],
          spacing: { after: 200 },
        }),
        new Table({
          layout: TableLayoutType.FIXED,
          columnWidths: [1000, 2500, 6000],
          borders: TABLE_BORDERS,
          rows: rows,
        }),
      ],
    },
  ],
});

Packer.toBuffer(doc).then((buffer) => {
  const outputPath = path.join(__dirname, "../../../../noss-l3-latest/addon-knowledge/abbreviations.docx");
  fs.writeFileSync(outputPath, buffer);
  console.log(`✅ Compiled JPK-compliant abbreviations.docx successfully at ${outputPath}`);
});
