---
spec_version: '0.2'
okf_version: '0.2'
type: guide
title: Getting started with DSOM tools
description: Dokumentasi OKF v0.2 bagi getting-started.md.
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:44Z'
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
title: "Getting Started"
description: "DSOM Tutorial document for Getting Started."
type: "tutorial"
id: "docs/tutorials/getting-started.md"
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

# Getting started with DSOM tools

A step-by-step tutorial guiding you through running, auditing, and integrating the DSOM workspace toolchain.

## Learning objectives

By completing this tutorial, you will:
- **Initialise** the local OpenWiki documentation hub.
- **Audit and repair** OKF v0.1 metadata frontmatter.
- **Spin up** and test the local Model Context Protocol (MCP) server.

---

## Lesson 1: Initialise your OpenWiki hub

Let's start by materialising the local OpenWiki workspace and knowledge graphs.

1. Open your terminal at the project root.
2. Run the initialisation command:

   ```bash
   uv run --with pyyaml python tools/openwiki_emulator.py --init
   ```

3. Open `./openwiki/graph.html` in your web browser. You should see an interactive visualiser map representing the active documentation.

---

## Lesson 2: Audit and repair frontmatter metadata

Now we will verify that all Markdown documentation satisfies the strict Open Knowledge Format (OKF v0.1).

1. Execute the compliance scanning command:

   ```bash
   uv run --with pyyaml python tools/apply_okf_frontmatter.py docs/
   ```

2. The script automatically scans all files. If any fields are missing, it adds them. If formatting is incorrect, it fixes it atomically.
3. Check one of your files to see the newly standardised headers:

   ```bash
   head -n 8 docs/tutorials/index.md
   ```

---

## Lesson 3: Start the FastMCP server

Let's publish our documentation Palace directly to AI clients.

1. Launch the server over `stdio`:

   ```bash
   uv run tools/mcp/server.py
   ```

2. The server sits waiting for JSON-RPC requests.
3. In a separate terminal, run the MCP verification tests to make sure everything communicates properly:

   ```bash
   uv run --with pyyaml --with pytest --with mcp==1.2.1 --with fastmcp pytest tests/test_mcp_server.py
   ```

**Congratulations!** You have completed the getting started tutorial for DSOM.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
