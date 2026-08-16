---
title: "Noss Abbreviation Syncer"
description: "DSOM Reference document for Noss Abbreviation Syncer."
type: "reference"
id: "docs/reference/skills/noss-abbreviation-syncer.md"
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

# NOSS Abbreviation Syncer

Use this skill when the user asks to update, sync, or extract abbreviations/acronyms for the current NOSS framework.

## Purpose

The active `abbreviations.md` file must be continuously updated against technical acronyms appearing across active CoCU files, while maintaining a strictly verified, alphabetised master list. 

This skill performs a rigorous **Strict Inclusion Audit**, automatically purging any abbreviation that does not physically appear in the active CoCU matrix (0 count). It then builds the final OKF v0.1 compliant markdown file and uses a custom Node.js compiler to generate a `.docx` file matching the official JPK visual template (Times New Roman, 3 columns, no headers, faint dotted borders).

## Instructions

1. Ensure the source files exist:
   - Extracted NOSS Document: `noss-l3-latest/references/extracted_noss.md`
   - Active Abbreviations: `noss-l3-latest/addon-knowledge/abbreviations.md`
   - Legacy Master Abbreviations: `noss-rebuild-v2/addon-knowledge/abbreviations.md`
2. Execute the bundled python synchronization script to merge and purge:
   Command: `uv run .agents/skills/noss-abbreviation-syncer/scripts/sync_abbreviations.py`
3. Execute the custom DOCX Node.js compiler to generate the strict JPK template:
   Command: `node .agents/skills/noss-abbreviation-syncer/scripts/compile_abbrev_docx.js`
4. Convert the DOCX to ODT via Pandoc (optional if the user wants an open format):
   Command: `pandoc noss-l3-latest/addon-knowledge/abbreviations.docx -o noss-l3-latest/addon-knowledge/abbreviations.odt`

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia)*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
