---
spec_version: '0.2'
okf_version: '0.2'
type: guide
title: Check and apply OKF compliance
description: Dokumentasi OKF v0.2 bagi audit-and-apply-frontmatter.md.
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
title: "Audit And Apply Frontmatter"
description: "DSOM Guide document for Audit And Apply Frontmatter."
type: "guide"
id: "docs/how-to/audit-and-apply-frontmatter.md"
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

# Check and apply OKF compliance

This guide explains how to audit, standardise, and auto-correct Markdown files to ensure compliance with the **Open Knowledge Format (OKF v0.1)**.

## Prerequisites

- **Python 3.12+** and **`uv`** must be installed on your environment.
- **`pyyaml`** dependency is required.

## Step 1: Scan and standardise directory frontmatter

Run the `apply_okf_frontmatter.py` tool pointing directly to your documentation folder. This script automatically injects the five required frontmatter variables (`okf_version`, `type`, `title`, `timestamp`, `topics`) and strips Byte Order Marks (BOM).

```bash
uv run --with pyyaml python tools/apply_okf_frontmatter.py docs/

```

## Step 2: Batch re-order metadata fields

To format skill schemas or re-align metadata ordering (placing `topics` immediately after `description` in skill documents), use the `refactor_okf.py` tool.

### Dry run check

Verify planned modifications without making changes on disk:

```bash
uv run --with pyyaml python tools/refactor_okf.py docs/ --dry-run

```

### In-place execution

Apply standard formatting and reordering rules atomically:

```bash
uv run --with pyyaml python tools/refactor_okf.py docs/

```

## Step 3: Verify the output

To confirm that the changes were executed successfully and no Byte Order Marks remain, use the standard test suite:

```bash
uv run --with pyyaml --with pytest pytest tests/test_okf_frontmatter_bom_reorder.py

```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
