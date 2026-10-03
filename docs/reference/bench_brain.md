---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: bench_brain.py reference
description: Dokumentasi OKF v0.2 bagi bench_brain.md.
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
title: "Bench_Brain"
description: "DSOM Reference document for Bench_Brain."
type: "reference"
id: "docs/reference/bench_brain.md"
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

# bench_brain.py reference

Spatial brain performance benchmarking utility.

## Description

The `bench_brain.py` tool measures read latency and byte throughput across brain assets and custom skills, calibrating performance multipliers for native OS and simulated mobile FUSE environments.

## Script path

`tools/bench_brain.py`

## CLI signature

```bash
uv run python tools/bench_brain.py

```

## Inputs

Scans two target paths:
- `.agents/brain`
- `.agents/skills`

## Outputs

Telemetry results printed directly to the shell terminal:
- Count of scanned files and total parsed byte volumes.
- Total read times for native OS (in milliseconds).
- Estimated mobile (Samsung Note 10) Termux FUSE latency extrapolations (using a default `3.5x` multiplier).

## Dependencies

- **Python:** Standard library only (no external packages required).

## Internal Python API

### `get_files(directories, extension)`

Recursively gathers matching files.
- **Arguments:** `directories` (string list), `extension` (string, defaults to `.md`).
- **Returns:** String path list.

### `bench_read(files)`

Evaluates overall reading performance.
- **Returns:** Tuple containing `(total_bytes, elapsed_seconds)`.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
