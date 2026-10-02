---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: DSOM reference material
description: Dokumentasi OKF v0.2 bagi index.md.
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
title: "Index"
description: "DSOM Reference document for Index."
type: "reference"
id: "docs/reference/index.md"
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

# DSOM reference material

Welcome to the **Deep State of Mind (DSOM) Reference Material** quadrant, structured according to the **Diátaxis Framework**.

## Information-oriented reference

Reference material provides **highly structured, key factual information** detailing arguments, environment variables, dependencies, inputs, outputs, and programmatic interfaces for *every single Python tool* in the repository.

- **[generate_sitemaps.py](generate_sitemaps.md):** Dynamic sitemap and robots.txt generator.
- **[openwiki_emulator.py](openwiki_emulator.md):** Zero-dependency pure Python OpenWiki emulator CLI.
- **[tools/mcp/server.py](mcp_server.md):** FastMCP server implementation exposing the Palace.
- **[apply_okf_frontmatter.py](apply_okf_frontmatter.md):** OKF YAML frontmatter compliance and enforcement script.
- **[refactor_okf.py](refactor_okf.md):** OKF frontmatter batch re-ordering and UTF-8 validation tool.
- **[bench_brain.py](bench_brain.md):** Spatial context memory access throughput benchmark.
- **[dsom_token_auditor.py](dsom_token_auditor.md):** Tiktoken-based token optimisation and audit calculator.
- **[mkdocs_hooks.py](mkdocs_hooks.md):** Custom MkDocs page hooks for link rewriting and path normalization.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
