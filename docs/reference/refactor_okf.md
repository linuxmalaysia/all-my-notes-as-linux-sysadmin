---
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
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip)*
