---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: Proposal DOCX Formatter
description: Dokumentasi OKF v0.2 bagi proposal-docx-formatter.md.
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:43Z'
sources:
- id: internal-legal-notice
  title: Dokumen Notis Perundangan, Privasi & Penafian / Legal Notice
  author: Harisfazillah Jamel (LinuxMalaysia)
  url: docs/legal-notice.md
  resource: docs/legal-notice.md
- id: google-okf-v02-spec
  title: Open Knowledge Format v0.2 Specification & Trust Signals
  author: Google Cloud Data Analytics
  url: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
  resource: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
- id: redlinesoft-attested-computations
  title: Attested Computations in Open Knowledge Format (OKF v0.2)
  author: RedLineSoft
  url: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
  resource: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
- id: dsom-okf-v02-adoption-skill
  title: OKF v0.2 Adoption Engineer Skill Standard
  author: Deep State of Mind (DSOM)
  url: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
  resource: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
---

﻿---
title: "Proposal Docx Formatter"
description: "DSOM Reference document for Proposal Docx Formatter."
type: "reference"
id: "docs/reference/skills/proposal-docx-formatter.md"
dsom_governance:
  domain: "AI"
  context_tier: "L2-Operational"
tags:
  - "dsom-protocol"
  - "diataxis-quadrant"
related_links:
  - "docs/reference/index.md"
nav_order: 10
layout: "default"
---

# Proposal DOCX Formatter

## Purpose

Generates a professionally formatted Microsoft Word (.docx) document from a structured
markdown source file. The formatting standards are adopted from the national
Occupational Skills Standard) document generation system.

## Formatting Standards

### Fonts
- **Font Family:** Times New Roman (exclusively)
- **Cover Title:** 24pt bold, centred
- **Cover Subtitle:** 16pt, centred
- **Heading 1 (`##`):** 14pt bold
- **Heading 2 (`###`):** 12pt bold
- **Heading 3 (`####`):** 11pt bold
- **Body Text:** 12pt, 1.15 line spacing
- **Table Content:** 11pt

### Page Layout
- **Paper Size:** A4 Portrait (210mm × 297mm)
- **Margins:** 1.0 inch (1440 dxa) on all sides
- **Header/Footer:** 0.5 inch (720 dxa)

### Table Styling
- **Borders:** 0.5pt single solid black (`000000`) on all edges
- **Header Row Fill:** Light Grey (`D9D9D9`)
- **Header Row Font:** 11pt bold
- **Body Cell Fill:** White (`FFFFFF`)
- **Cell Padding:** 80 dxa (~4pt) on all sides
- **Vertical Alignment:** Centre

### Colour Palette
| Usage               | Hex Code   |
|:--------------------|:-----------|
| Table header fill   | `D9D9D9`   |
| Sub-header fill     | `BFBFBF`   |
| Borders             | `000000`   |
| Body cells          | `FFFFFF`   |

### Linguistic Rules
- **UK English** mandatory (organisation, modernisation, virtualisation)
- Active voice for procedural descriptions
- Passive voice for formal specifications

## Markdown Source Format

The source markdown file must follow this structure:

```markdown
---
title: "Document Title"
subtitle: "Document Subtitle"
version: "X.Y"
date: "DD Month YYYY"
classification: "CONFIDENTIAL"
---

## 1. Section Heading

Body paragraph text with **bold** inline formatting.

### 1.1. Subsection Heading

- Bullet list item
- Another **bold lead-in:** with description

| Column 1 | Column 2 | Column 3 |
|:---------|:---------|:---------|
| Data     | Data     | Data     |

#### Sub-subsection

1. Numbered list item
2. Another item
```

## Build Command

```powershell
uv run --with python-docx python tools/compile_proposal.py docs/proposal.md docs/proposal.docx
```

*Note: If `tools/compile_proposal.py` or `tools/proposal_docx_template.py` are missing, reconstruct them by reading their blueprints in `docs/tools/compile-engines.md`.*

## Files

| File | Role |
|:-----|:-----|
| `tools/proposal_docx_template.py` | Shared template module (fonts, colours, margins, helpers) |
| `tools/compile_proposal.py` | Markdown-to-DOCX compiler script |
| `docs/proposal.md` | Source markdown (structured with YAML frontmatter) |
| `docs/proposal.docx` | Generated output document |

## Dependencies

- Python 3.10+
- `python-docx` (installed via `uv run --with python-docx`)
- `pyyaml` (installed via `uv run --with pyyaml`)


---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
