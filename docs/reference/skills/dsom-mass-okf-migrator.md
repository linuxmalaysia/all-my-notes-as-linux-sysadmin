---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: DSOM Mass OKF Migrator
description: Dokumentasi OKF v0.2 bagi dsom-mass-okf-migrator.md.
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
title: "Dsom Mass Okf Migrator"
description: "DSOM Reference document for Dsom Mass Okf Migrator."
type: "reference"
id: "docs/reference/skills/dsom-mass-okf-migrator.md"
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

# DSOM Mass OKF Migrator

## Overview
This skill instructs the AI on how to perform a mass migration of legacy markdown documents into the highly-structured **Open Knowledge Format (OKF) v0.1** tailored for the Linux NOSS Malaysia project.

It utilises a Python script to deeply copy a directory while rewriting the metadata, URLs, and appending the Sovereign Dual-License footer.

## When to Use
Trigger this skill whenever you need to import external documentation, migrate an older DSOM repository's `docs/` or `openwiki/` folder, or standardise a large batch of markdown files to comply with the project's AI Constitution (AGENTS.md) Rule 8 and 9.

## Requirements
- Python must be executed exclusively via `uv` (as per Rule 9).

## Instructions

1. Identify the absolute path of the **Source Directory** (the legacy docs).
2. Identify the absolute path of the **Destination Directory**.
3. Execute the migration script using `uv run` to maintain environment hygiene:

```powershell
uv run .agents/skills/dsom-mass-okf-migrator/scripts/migrate.py "<SOURCE_DIR>" "<DEST_DIR>"
```

*Note: The script automatically skips overwriting `PERSONALIZATION.md`, `OKF-ADOPTION-GUIDE.md`, and `SKILL-FORMAT.md`.*

## Verification
After the script completes, use the `list_dir` tool to verify the destination directory and `view_file` to ensure the YAML frontmatter (`okf_version: 0.1`) and Sovereign footer were injected correctly.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
