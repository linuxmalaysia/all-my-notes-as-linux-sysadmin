---
spec_version: '0.2'
okf_version: '0.2'
type: guide
title: Operate the OpenWiki emulator
description: Dokumentasi OKF v0.2 bagi use-openwiki-emulator.md.
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
title: "Use Openwiki Emulator"
description: "DSOM Guide document for Use Openwiki Emulator."
type: "guide"
id: "docs/how-to/use-openwiki-emulator.md"
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

# Operate the OpenWiki emulator

This guide explains how to initialise, update, and query the local OpenWiki documentation and knowledge graph.

## Prerequisites

- **Python 3.12+** and **`uv`** must be configured.
- **`pyyaml`** dependency is required.

## Step 1: Initialise the wiki directory

Recompile standard directories, create index skeletons, self-heal Mermaid diagrams, and export standalone interactive HTML graphs:

```bash
uv run --with pyyaml python tools/openwiki_emulator.py --init

```

## Step 2: Query metadata from terminal

Use the search command to perform fast frontmatter variable checks on compiled wiki pages:

```bash
uv run --with pyyaml python tools/openwiki_emulator.py --search "ansible"

```

## Step 3: Sync changes from Git history

Before saving and finalizing work, pull updated Git changes into the wiki logs and refresh indices:

```bash
uv run --with pyyaml python tools/openwiki_emulator.py --update

```

## Step 4: Run diagram validation tests

Verify standard self-healing logic and schema parsing engines using unit tests:

```bash
uv run --with pyyaml --with pytest pytest tests/test_openwiki_emulator.py

```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
