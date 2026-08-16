---
okf_version: 0.1
type: agent_skill
title: docx-highlight-extractor
name: docx-highlight-extractor
description: Extracts highlighted text and comments from DOCX files, preserving exact page locations and paragraph context, and generates a tracking ledger.
topics: [docx, highlight, comments, audit, tracking, xml]
---

# DOCX Highlight Extractor

Use this skill when the user asks to extract comments, feedback, or highlighted text from a Microsoft Word (`.docx`) document. Standard markdown converters lose the precise context, so this skill utilizes native XML parsing to locate page boundaries, paragraphs, and adjacent contextual text.

## Instructions

1. Identify the target `.docx` file to extract from.
2. Execute the XML extraction script to generate the raw JSON data:
   `uv run .agents/skills/docx-highlight-extractor/scripts/extract_detailed_highlights.py <path_to_input_docx> <path_to_output_json>`
3. Execute the markdown generator script to compile the detailed tracking ledger:
   `uv run .agents/skills/docx-highlight-extractor/scripts/generate_detailed_md.py <path_to_input_json> <path_to_output_md>`
4. Present the generated markdown file to the user as an artifact (e.g. `review_notes_detailed.md`).
5. **Auditing Protocol:** Whenever the user successfully addresses a specific highlight (e.g., `HL-001`), manually append a `Resolution / Replacement` row directly into the markdown table documenting the exact change.

## Constraints & Immutability
- **Tracking ID Immutability:** Once a tracking ledger is generated and `HL-XXX` IDs are assigned, they are considered immutable team references. **NEVER** delete, filter, or re-sequence highlights to "clean up" the document, as this destroys external team alignment.
- **Invisible Highlights:** Raw XML extraction often captures invisible formatting artifacts (e.g., `white` or `lightGray` highlights caused by copy-pasting). Do not delete these from the JSON. Instead, maintain the sequence and explicitly mark them in the markdown `Resolution / Replacement` column as: `⏩ **Skipped:** Invisible formatting artifact. Can safely skip.`
---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia)*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
