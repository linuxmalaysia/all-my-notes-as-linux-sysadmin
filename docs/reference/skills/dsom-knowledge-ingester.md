---
title: "Dsom Knowledge Ingester"
description: "DSOM Reference document for Dsom Knowledge Ingester."
type: "reference"
id: "docs/reference/skills/dsom-knowledge-ingester.md"
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

# 📥 DSOM Knowledge Ingester Skill

## When to use this skill
Use this skill when the user provides a new external source (PDF, Markdown, Web Article, Meeting Transcript) and wants to formalize it into the Palace. This embodies the "Ingest" pattern of the LLM WIKI.

## Instructions
1. **Source Discovery:** Ask the user for the path to the raw source document in `raw_sources/` (create this directory if it doesn't exist).
2. **Analysis & Synthesis:**
   - Read the raw document using `view_file`, `pdf-text-extractor`, or `read_url_content`.
   - Synthesize the key concepts, rules, and architectural data.
3. **Wiki Integration (The Palace):**
   - Create a new `.md` file in the appropriate directory (e.g., `docs/governance/`, `hall_facts/`).
   - Format the file according to DSOM Generative Engine Optimization (GEO) standards (atomic chunks, H2 headers, expert tone).
   - Inject the OKF v0.1 frontmatter and the Sovereign Signature using `dsom-signature-injector`.
4. **Ledger & Index Updates:**
   - Add the new file to `SUMMARY.md` and `mkdocs.yml` (Dual Documentation Sync).
   - Add the new file to `.agents/brain/palace_registry.md`.
   - Update `CHANGELOG.md` and `HISTORY.md` to note the new knowledge ingestion.
5. **Confirmation:** Provide the user with a summary of the concepts extracted and the new pages created.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
