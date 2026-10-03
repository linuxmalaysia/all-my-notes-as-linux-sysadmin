---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: apply_okf_frontmatter.py reference
description: Dokumentasi OKF v0.2 bagi apply_okf_frontmatter.md.
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
title: "Apply_Okf_Frontmatter"
description: "DSOM Reference document for Apply_Okf_Frontmatter."
type: "reference"
id: "docs/reference/apply_okf_frontmatter.md"
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

# apply_okf_frontmatter.py reference

Authoritative Open Knowledge Format (OKF v0.1) compliance and enforcement engine.

## Description

The `apply_okf_frontmatter.py` tool scans directories and ensures all `.md` files contain the 5 required frontmatter variables. It automatically handles line endings, quotes special values, and writes updates atomically.

## Script path

`tools/apply_okf_frontmatter.py`

## CLI signature

```bash

# Scan and standardise files in a target directory (defaults to current directory)

uv run python tools/apply_okf_frontmatter.py docs/

```

## Mandatory fields enforced

All Markdown files are parsed to assert:
- **okf_version:** Fixed float representation (defaults to `0.1`).
- **type:** Document category, mapped from directory paths.
- **title:** File header string (parsed from H1 tags).
- **timestamp:** UTC ISO 8601 creation string.
- **topics:** Categorized string lists defining index content.

## Dependencies

- **Python:** 3.12+.
- **pyyaml:** Robust SafeLoader parsing configuration.

## Internal Python API

### `get_okf_type(filepath)`

Derives document types dynamically from parent paths.
- **Types returned:** `governance_protocol`, `agent_skill`, `architecture_concept`, `automation_tool`, `infrastructure_playbook`, `documentation`.

### `needs_double_quotes(s)`

Detects if strings contain colons, parentheses, emojis, or spaces, requiring YAML escape double quotes.
- **Returns:** Boolean.

### `atomic_replace_file(filepath, new_content, filename)`

Atomically updates files via temporary sibling structures and `os.replace()`, preserving permissions.
- **Mechanism:** Prevents data truncation in the event of hardware or system execution hangs.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
