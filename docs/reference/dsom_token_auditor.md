---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: dsom_token_auditor.py reference
description: Dokumentasi OKF v0.2 bagi dsom_token_auditor.md.
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
title: "Dsom_Token_Auditor"
description: "DSOM Reference document for Dsom_Token_Auditor."
type: "reference"
id: "docs/reference/dsom_token_auditor.md"
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

# dsom_token_auditor.py reference

Tiktoken-based token efficiency and context load calculation script.

## Description

The `dsom_token_auditor.py` script compares non-DSOM "Bloated" context loads against optimised DSOM configurations (which utilise episodic resumes and progressive disclosures). It calculates savings percentages.

## Script path

`tools/dsom_token_auditor.py`

## CLI signature

```bash
uv run --with tiktoken python tools/dsom_token_auditor.py

```

## Outputs

Prints an analysis report:
- Token counts for bloated scenario structures.
- Token counts for progressive disclosure scenario structures.
- Percentage and absolute token savings achieved per execution turn.

## Dependencies

- **tiktoken:** Fast BPE tokenization library.

## Internal Python API

### `count_tokens(text, model="gpt-4")`

Counts tokens for a given string using optimised tokenisation with the specified model's encoder.
- **Arguments:** `text` (raw string), `model` (defaults to `"gpt-4"`).
- **Returns:** Integer representation of token count.

### `generate_bloated_context()`

Generates a raw string simulating chat history and massive file loads.

### `generate_dsom_context()`

Generates a raw string simulating episodic records and relative link references.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
