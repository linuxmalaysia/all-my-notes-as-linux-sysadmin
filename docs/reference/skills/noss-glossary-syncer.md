---
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

This skill performs a rigorous **Strict Inclusion Audit**, automatically purging any glossary term that does not physically appear outside of the glossary section in the active CoCU matrix (0 count). It then builds the final OKF v0.2 compliant markdown file and uses a custom Node.js compiler to generate a `.docx` file matching the official JPK visual template (Times New Roman, 3 columns, no headers, faint dotted borders).

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
