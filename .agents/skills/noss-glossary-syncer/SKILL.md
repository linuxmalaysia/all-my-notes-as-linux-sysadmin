---
okf_version: 0.1
type: agent_skill
title: noss-glossary-syncer
name: noss-glossary-syncer
description: Automates glossary syncing by extracting terms from the core NOSS document, purging zero-count entries, and generating JPK-compliant DOCX and OKF Markdown glossaries.
topics: [noss, glossary, extraction, sync, terminology]
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
