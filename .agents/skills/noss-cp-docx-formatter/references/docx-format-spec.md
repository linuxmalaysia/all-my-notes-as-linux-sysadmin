# CP Format Reference — Annotated Structure

## Document: CP-Level-3-Generated.docx

This file documents the **exact XML/DOCX structure** derived from inspecting
`noss-rebuild/references/CP-Level-3-Generated.docx`.

---

## Table Properties (all tables)

```xml
<w:tblPr>
  <w:tblW w:type="pct" w:w="100%"/>
  <w:tblBorders>
    <w:top    w:val="single" w:color="auto" w:sz="4"/>
    <w:left   w:val="single" w:color="auto" w:sz="4"/>
    <w:bottom w:val="single" w:color="auto" w:sz="4"/>
    <w:right  w:val="single" w:color="auto" w:sz="4"/>
    <w:insideH w:val="single" w:color="auto" w:sz="4"/>
    <w:insideV w:val="single" w:color="auto" w:sz="4"/>
  </w:tblBorders>
</w:tblPr>
```

## Cell Properties (all cells)

```xml
<w:tcPr>
  <w:tcW w:type="pct" w:w="NN%"/>
  <w:gridSpan w:val="N"/>  <!-- only when colspan > 1 -->
  <w:tcMar>
    <w:top    w:type="dxa" w:w="100"/>
    <w:left   w:type="dxa" w:w="100"/>
    <w:bottom w:type="dxa" w:w="100"/>
    <w:right  w:type="dxa" w:w="100"/>
  </w:tcMar>
</w:tcPr>
```

## Run Properties (all text runs)

```xml
<w:rPr>
  <w:rFonts w:ascii="Times New Roman"
            w:cs="Times New Roman"
            w:eastAsia="Times New Roman"
            w:hAnsi="Times New Roman"/>
  <w:b/>    <!-- present for bold cells only -->
  <w:bCs/>  <!-- present for bold cells only -->
  <w:sz   w:val="22"/>   <!-- 11pt = 22 half-points -->
  <w:szCs w:val="22"/>
</w:rPr>
```

For non-bold cells within a bold section, the generator explicitly sets:
```xml
<w:b w:val="false"/>
<w:bCs w:val="false"/>
```

---

## Table 1 — Header / Metadata (4-column grid)

```
SECTION (25%, bold)  | (J) Information and Communication (75%, bold, colspan=3)
GROUP   (25%, bold)  | (620) Computer Programming...     (75%, bold, colspan=3)
AREA    (25%, bold)  | Computer System Administration    (75%, bold, colspan=3)
NOSS TITLE (25%,b)   | Sovereign IT Infrastructure...    (75%, bold, colspan=3)
NOSS LEVEL (25%,b)   | LEVEL 3 (25%) | NOSS CODE (25%,b) | IT-020-3:2026 (25%)
```

Grid definition: `<w:gridCol w:w="100"/>` × 4 (equal columns, % overrides apply)

---

## Table 2 — CU Header (2-column grid, per CU)

```
CU TITLE & CU CODE (25%, bold) | <Title> (<Code>)  (75%, bold)
CU DESCRIPTOR      (25%, bold) | <descriptor text> (75%, NOT bold)
```

Descriptor text uses `\n` (newline) for paragraph breaks in DOCX,
NOT `<br>` tags. The docx library renders each `\n` as a new paragraph
within the same cell.

---

## Table 3 — WA Matrix (3-column grid, per CU)

```
WORK ACTIVITIES (30%, bold) | WORK STEPS (35%, bold) | PERFORMANCE CRITERIA (35%, bold)
<WA Name>.\n(<WA Code>)     | [Paragraph per step]   | [Paragraph per PC]
```

- WA column: single TextRun with `\n` between name and code, NOT bold
- Steps column: **one Paragraph per step**, each with its own TextRun
- PC column: **one Paragraph per PC**, each with its own TextRun

---

## docx Library Mapping

| Concept | docx API |
| :------ | :------- |
| Table | `new Table({ width: { size: 100, type: WidthType.PERCENTAGE }, rows: [...] })` |
| Row | `new TableRow({ children: [...] })` |
| Cell | `new TableCell({ children: [...], width: { size: N, type: WidthType.PERCENTAGE }, columnSpan: N, margins: {...} })` |
| Text | `new Paragraph({ children: [new TextRun({ text, bold, font: "Times New Roman", size: 22 })] })` |
| Bold label | `bold: true` in TextRun |
| Non-bold override | `bold: false` in TextRun |
| Heading | `new Paragraph({ text: "...", heading: HeadingLevel.HEADING_1 })` |
| Page margin | `sections[0].properties.page.margin = { top:720, right:720, bottom:720, left:720 }` |
