---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: openwiki_emulator.py reference
description: Dokumentasi OKF v0.2 bagi openwiki_emulator.md.
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
title: "Openwiki_Emulator"
description: "DSOM Reference document for Openwiki_Emulator."
type: "reference"
id: "docs/reference/openwiki_emulator.md"
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

# openwiki_emulator.py reference

Zero-binary, pure Python CLI tool emulating the OpenWiki documentation environment.

## Description

The `openwiki_emulator.py` script replaces external Node.js binaries and cloud APIs with localised, offline execution. It compiles 9 markdown wiki pages, repairs Mermaid schemas, and exports an interactive graph visualiser.

## Script path

`tools/openwiki_emulator.py`

## CLI options

```bash

# Initialise and compile the full OpenWiki workspace (default action)

uv run python tools/openwiki_emulator.py --init

# Retrieve recent Git changes and update context history

uv run python tools/openwiki_emulator.py --update

# Perform search against OpenWiki YAML metadata

uv run python tools/openwiki_emulator.py --search "ansible"

# Export a standalone offline HTML interactive knowledge graph

uv run python tools/openwiki_emulator.py --export-graph

```

## Inputs

- **Git status:** System porcelain variables used to determine modified workspace files.
- **Planned pages map:** Hardcoded schemas defining initial wiki content and layouts.

## Outputs

All workspace files created inside `./openwiki/`:
- **INSTRUCTIONS.md:** Standard CLI operating procedures and rules.
- **_skeleton.md:** Ranking matrices and structural subsystems mapping.
- **graph.html:** Interactive standalone knowledge visualization layout.
- **quickstart.md / architecture / automation / memory:** Structured markdown documents.
- **.last-update.json:** Dynamic JSON execution tracker log.

## Dependencies

- **Python:** 3.12+ (standard `uv` environment).
- **pyyaml:** YAML data loading engine.

## Internal Python API

### `validate_mermaid_diagram(code)`

Validates Mermaid diagram layout syntax, bracket matches, and unescaped quotes.
- **Arguments:** `code` (raw string of the diagram block).
- **Returns:** `(bool, reason)` tuple representing valid status and description.

### `process_markdown_file(filepath)`

Scans a markdown file, detects corrupted or plain code fences, and repairs them.
- **Arguments:** `filepath` (absolute target file `pathlib.Path`).
- **Mechanism:** Degrades blocks in place with errors; heals corrected blocks back to active schemas.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
