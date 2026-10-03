---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: tools/mcp/server.py reference
description: Dokumentasi OKF v0.2 bagi mcp_server.md.
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
title: "Mcp_Server"
description: "DSOM Reference document for Mcp_Server."
type: "reference"
id: "docs/reference/mcp_server.md"
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

# tools/mcp/server.py reference

FastMCP Model Context Protocol (MCP) server implementation for the DSOM Palace.

## Description

The `server.py` utility exposes the Sovereign Markdown Palace, active brain assets, and local OpenWiki knowledge indexes directly to AI clients. It serves context via standard JSON-RPC over `stdio`.

## Script path

`tools/mcp/server.py`

## CLI signature

```bash
uv run tools/mcp/server.py

```

## Environment variables

- **DSOM_ROOT:** Overrides project base directory path. Defaults to parent of script path.

## Resources exposed

AI clients can subscribe to and read these standardised read-only streams:
- **dsom://brain/state:** Output of condensed system state `current_state.dsom`.
- **dsom://brain/task:** Real-time session checklists inside `.agents/brain/task.md`.
- **dsom://brain/walkthrough:** Episodic session walkthrough records.
- **dsom://governance/agents:** Complete 27 Sovereign AI constitutional rules.
- **dsom://openwiki/skeleton:** Subsystem structural hierarchy ranking file.
- **dsom://openwiki/quickstart:** Interactive routing table and system entry-points.

## Tools registered

AI clients can execute these tools dynamically:
- **search_palace(query):** Text search across `docs/` Markdown files.
- **search_openwiki(query):** Sub-millisecond OKF metadata search.
- **fetch_context7_stream(tokens):** Retrieves URL pointers to external pre-indexed token streams.

## Dependencies

- **mcp[cli]:** Model Context Protocol Python library.
- **fastmcp:** Modern FastMCP helper wrapper.
- **pyyaml:** YAML loader configuration parser.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
