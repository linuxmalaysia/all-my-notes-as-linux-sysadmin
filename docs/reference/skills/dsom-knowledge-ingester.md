---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: 📥 DSOM Knowledge Ingester Skill
description: Dokumentasi OKF v0.2 bagi dsom-knowledge-ingester.md.
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


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
