---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: refactor_okf.py reference
description: Dokumentasi OKF v0.2 bagi refactor_okf.md.
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
title: "Refactor_Okf"
description: "DSOM Reference document for Refactor_Okf."
type: "reference"
id: "docs/reference/refactor_okf.md"
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

# refactor_okf.py reference

Batch refactoring script for Open Knowledge Format (OKF) frontmatter structures.

## Description

The `refactor_okf.py` tool processes files across the repository, strips leading UTF-8 Byte Order Marks (BOM), and enforces proper ordering of YAML variables (such as placing `topics` immediately after `description` in skill schemas).

## Script path

`tools/refactor_okf.py`

## CLI signature

```bash

# Preview expected changes without executing in-place writes

uv run python tools/refactor_okf.py --dry-run

# Refactor and overwrite files with standardised compliance

uv run python tools/refactor_okf.py

```

## Internal Python API

This script imports logic from `tools/apply_okf_frontmatter.py` to preserve consistency:
- **`FRONTMATTER_RE`:** Pattern identifying Markdown fences.
- **`process_file(filepath, root_dir, dry_run)`:** Main orchestrator implementing parsing, normalisation, and atomic replacement.

## Excluded directories

The tool ignores these directories to prevent unnecessary modifications:
- `.git`
- `node_modules`
- `.pytest_cache`
- `.venv`

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
