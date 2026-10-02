---
spec_version: '0.2'
okf_version: '0.2'
type: agent_skill
title: odp-slide-generator
description: Dokumentasi OKF v0.2 bagi SKILL.md.
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:44Z'
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
okf_version: 0.1
type: agent_skill
title: odp-slide-generator
name: odp-slide-generator
description: Generates highly styled 3-column Corporate Presentation slides (PPTX/ODP format) based on a specific HTML/CSS theme using python-pptx.
topics: [presentation, pptx, odp, python-pptx, slides]
---

# odp-slide-generator

## When to use this skill
Use this skill when you need to generate a LibreOffice Impress / Microsoft PowerPoint presentation that strictly adheres to the custom 3-column corporate theme (deep blue, vibrant orange accents, grid layout).

## Format Rules

The slide generator (`tools/compile_3col_slides.py`) expects a highly specific Markdown format to populate the complex geometric shapes.

1. Create a markdown file with the following exact structure:
   - `# [Main Slide Title]` (Must be Top Level)
   - `## [Slide Subtitle]` (Optional Subtitle)
   - `### [Column Label]` (e.g. Stage 01: Source)
   - `**[Box Header Text]**` (e.g. Direct Extraction)
   - `- [Bullet point 1]`
   - `- [Bullet point 2]`
   - `> "[Footer Quote Text]"` (Optional footer quote block)

### Example Markdown:
```markdown
# Achieving Zero-Downtime Cutover
## Near-Real-Time Delta Sync (CDC) Architecture

### Stage 01: Source
**Direct Extraction**
- Native connection to PostgreSQL Write-Ahead Logs (WAL).
- Row-level mutation tracking without database triggers.

### Stage 02: Transport
**Streaming Fabric**
- Apache Kafka (KRaft Mode) for high-throughput event bus.
- Debezium Connect for automated change capture.

### Stage 03: Target
**Instant Mirroring**
- Near-instant transaction mirroring to Percona target.
- Continuous data validation during sync phase.

> "By streaming row-level mutations in real-time, we compress the final production cutover window."
```

## Execution

1. Write the target markdown file (e.g., `docs/slide_data.md`).
2. Run the compiler using `uv`:
   ```powershell
   uv run --with python-pptx python tools/compile_3col_slides.py docs/slide_data.md docs/my_presentation.pptx
   ```
3. The resulting `.pptx` file is 100% natively compatible with LibreOffice Impress and will retain all shape geometries, exact RGB colors, and custom fonts.


---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
