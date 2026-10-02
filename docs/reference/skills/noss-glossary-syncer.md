---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: NOSS Glossary Syncer
description: Dokumentasi OKF v0.2 bagi noss-glossary-syncer.md.
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
title: "Noss Glossary Syncer"
description: "DSOM Reference document for Noss Glossary Syncer."
type: "reference"
id: "docs/reference/skills/noss-glossary-syncer.md"
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

# NOSS Glossary Syncer

Use this skill when the user asks to update, sync, or extract the Glossary of Terms for the current NOSS framework.

## Purpose

The active `glossary.md` file must be continuously updated against technical terms defined in the NOSS baseline.

This skill performs a rigorous **Strict Inclusion Audit**, automatically purging any glossary term that does not physically appear outside of the glossary section in the active CoCU matrix (0 count). It then builds the final OKF v0.1 compliant markdown file and uses a custom Node.js compiler to generate a `.docx` file matching the official JPK visual template (Times New Roman, 3 columns, no headers, faint dotted borders).

## Instructions

1. Ensure the source files exist:
   - Extracted NOSS Document: `noss-l3-latest/references/extracted_noss.md`
2. Execute the bundled python synchronization script to extract and purge:
   Command: `uv run .agents/skills/noss-glossary-syncer/scripts/sync_glossary.py`
3. Execute the custom DOCX Node.js compiler to generate the strict JPK template:
   Command: `node .agents/skills/noss-glossary-syncer/scripts/compile_glossary_docx.js`
4. Convert the DOCX to ODT via Pandoc (optional if the user wants an open format):
   Command: `pandoc noss-l3-latest/addon-knowledge/glossary.docx -o noss-l3-latest/addon-knowledge/glossary.odt`

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia)*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
