# CPC Format Reference — Annotated DOCX Structure

## Document: CPC-Level-3-Generated.docx

Derived from direct XML inspection of the reference file.

---

## Key Differences from CP Format

| Feature | CP | CPC |
| :------ | :-- | :-- |
| Tables | 13 (1 header + 2 per CU) | **2 total** |
| Table width | 100% | Header: 100%, Grid: **50%** |
| Width units | Percentage | **DXA (twips)** for grid cells |
| Cell colours | None (white only) | Multiple colours (orange/yellow/green/blue/white) |
| Text colour | Black | Labels: black, Values: **red FF0000** |
| Cell merging | colspan only | **rowSpan (vMerge)** on orange column |
| Layout type | auto | Grid: **fixed** |

---

## Table 1 — Metadata Header XML

```xml
<w:tblPr>
  <w:tblW w:w="5000" w:type="pct"/>   <!-- 100% width -->
</w:tblPr>
```

### Label Cell (grey EFEFEF fill)
```xml
<w:tcPr>
  <w:tcW w:w="2616" w:type="dxa"/>
  <w:tcBorders>
    <w:top    w:val="single" w:sz="4" w:space="0" w:color="000000"/>
    <w:start  w:val="single" w:sz="4" w:space="0" w:color="000000"/>
    <w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>
    <w:end    w:val="single" w:sz="4" w:space="0" w:color="000000"/>
  </w:tcBorders>
  <w:shd w:fill="EFEFEF" w:val="clear"/>
  <w:vAlign w:val="center"/>
</w:tcPr>
<w:p>
  <w:pPr>
    <w:spacing w:before="100" w:after="100"/>
    <w:jc w:val="center"/>
  </w:pPr>
  <w:r>
    <w:rPr>
      <w:rFonts w:eastAsia="Times New Roman" w:cs="Times New Roman"/>
      <w:b w:val="false"/>
      <w:bCs w:val="false"/>
      <w:sz w:val="22"/>
      <w:szCs w:val="22"/>
    </w:rPr>
    <w:t>SECTION</w:t>
  </w:r>
</w:p>
```

### Value Cell (white FFFFFF fill, red FF0000 text, colSpan=4 → gridSpan=3 in 5-col grid)
```xml
<w:tcPr>
  <w:tcW w:w="7850" w:type="dxa"/>
  <w:gridSpan w:val="3"/>
  <w:tcBorders> ... same borders ... </w:tcBorders>
  <w:shd w:fill="FFFFFF" w:val="clear"/>
  <w:vAlign w:val="center"/>
</w:tcPr>
<w:p>
  <w:r>
    <w:rPr>
      <w:rFonts w:eastAsia="Times New Roman" w:cs="Times New Roman"/>
      <w:color w:val="FF0000"/>
      <w:sz w:val="22"/>
      <w:szCs w:val="22"/>
    </w:rPr>
    <w:t>K62 COMPUTER PROGRAMMING...</w:t>
  </w:r>
</w:p>
```

---

## Table 2 — CPC Grid XML

```xml
<w:tblPr>
  <w:tblW w:w="5000" w:type="pct"/>     <!-- 50% of page -->
  <w:jc w:val="start"/>                  <!-- left-aligned -->
  <w:tblInd w:w="0" w:type="dxa"/>
  <w:tblLayout w:type="fixed"/>          <!-- fixed layout! -->
  <w:tblCellMar>
    <w:top    w:w="100" w:type="dxa"/>
    <w:start  w:w="100" w:type="dxa"/>
    <w:bottom w:w="100" w:type="dxa"/>
    <w:end    w:w="100" w:type="dxa"/>
  </w:tblCellMar>
</w:tblPr>
<w:tblGrid>
  <w:gridCol w:w="1744"/>
  <w:gridCol w:w="1744"/>
  <w:gridCol w:w="1744"/>
  <w:gridCol w:w="1745"/>
  <w:gridCol w:w="1744"/>
  <w:gridCol w:w="1745"/>
</w:tblGrid>
```

### vMerge START (orange column, first row of CU block)
```xml
<w:tcPr>
  <w:tcW w:w="1744" w:type="dxa"/>
  <w:vMerge w:val="restart"/>
  <w:tcBorders> ... </w:tcBorders>
  <w:shd w:fill="FFC000" w:val="clear"/>
  <w:vAlign w:val="center"/>
</w:tcPr>
```

### vMerge CONTINUATION (orange column, subsequent rows)
```xml
<w:tcPr>
  <w:tcW w:w="1744" w:type="dxa"/>
  <w:vMerge/>   <!-- no w:val = continuation -->
  <w:tcBorders> ... </w:tcBorders>
  <!-- no shd fill in continuation cells -->
  <w:vAlign w:val="center"/>
</w:tcPr>
```

---

## Complete Row-by-Row Map (CU01 example, 6 WAs)

```
Row 0 (header):
  [col0: 1744 WHITE empty] [col1: 1744 GREEN "←COMPETENCY UNIT→"] [col2-5: 6978 BLUE gs=4 "←WORK ACTIVITIES→"]

Row 1 (spacer):
  [col0-5: 10466 WHITE gs=6 empty]

Row 2 (CU01 name row A):
  [col0: 1744 ORANGE vMerge:START "C\nO\nR\nE"]
  [col1: 1744 YELLOW "PERFORM BASIC COMPUTER SYSTEM INSTALLATION AND CONFIGURATION"]
  [col2: 1744 WHITE "Prepare computer system set-up components."]
  [col3: 1745 WHITE "Carry out computer system hardware installation."]
  [col4: 1744 WHITE "Carry out computer Operating System (OS) software installation."]
  [col5: 1745 WHITE "Carry out computer application, peripheral and device driver installation."]

Row 3 (CU01 code row A):
  [col0: 1744 vMerge:CONT empty]
  [col1: 1744 GREEN "CODE CU01"]
  [col2: 1744 BLUE "CODE CU01-WA01"]
  [col3: 1745 BLUE "CODE CU01-WA02"]
  [col4: 1744 BLUE "CODE CU01-WA03"]
  [col5: 1745 BLUE "CODE CU01-WA04"]

Row 4 (CU01 name row B — overflow WA5,6):
  [col0: 1744 vMerge:CONT empty]
  [col1: 1744 WHITE empty]
  [col2: 1744 WHITE "Configure static IP and wireless network parameters."]
  [col3: 1745 WHITE "Prepare computer system installation record."]
  [col4: 1744 WHITE empty]
  [col5: 1745 WHITE empty]

Row 5 (CU01 code row B — overflow codes):
  [col0: 1744 vMerge:CONT empty]
  [col1: 1744 WHITE empty]
  [col2: 1744 BLUE "CODE CU01-WA05"]
  [col3: 1745 BLUE "CODE CU01-WA06"]
  [col4: 1744 BLUE empty]
  [col5: 1745 BLUE empty]

Row 6 (CU01 spacer):
  [col0-5: 10466 WHITE gs=6 empty]
```

---

## Colour Reference Table

| Name | Hex | Used for |
| :--- | :-- | :------- |
| ORANGE | `FFC000` | CORE column (col 0) |
| YELLOW | `FFFF00` | CU Title (col 1, name rows) |
| GREEN  | `92D050` | CU Code (col 1, code rows) + header |
| BLUE   | `DDEBF7` | WA Codes (cols 2–5, code rows) + header |
| WHITE  | `FFFFFF` | WA Titles (cols 2–5, name rows) + spacers |
| GREY   | `EFEFEF` | Metadata label cells (Table 1 only) |
| RED text | `FF0000` | All metadata values (Table 1 only) |
