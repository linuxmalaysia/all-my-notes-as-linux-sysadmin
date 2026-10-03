---
spec_version: '0.2'
okf_version: '0.2'
type: agent_skill
title: OpenWiki Graph Generator
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
type: skill
title: "openwiki-graph-generator"
timestamp: "2026-08-16T09:12:00Z"
topics: ["openwiki", "noss-linux", "graph"]
tags: ["script", "automation", "python", "mermaid"]
description: "Generates the OpenWiki Master Graph (Mermaid.js) mapping NOSS Linux Topics to Competency Units (CU)."
resource: "file:///.agents/skills/openwiki-graph-generator/SKILL.md"
---

# OpenWiki Graph Generator

## Overview
This skill instructs the AI on how to rebuild the visual hierarchy and relationship mapping of NOSS Linux syllabus topics inside the `openwiki/` directory.

The python script reads all `topic-*.md` files, extracts their OKF metadata and NOSS mappings (e.g., CU01, CU02), and compiles them into a dynamically generated **Mermaid.js** graph within `openwiki/index.md`.

## When to Use
Trigger this skill whenever a new topic is added to the `openwiki/` folder, or when existing topics undergo major re-mapping of their Competency Units.

## Instructions
1. Ensure you are at the project root.
2. Execute the generator script using `uv run` to satisfy the Python UV Mandate (Rule 9):

```powershell
uv run scripts/generate_openwiki_graph.py
```

3. Verify that the file `openwiki/index.md` has been successfully updated and the Mermaid syntax is valid.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
