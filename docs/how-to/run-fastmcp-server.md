---
spec_version: '0.2'
okf_version: '0.2'
type: guide
title: Run the FastMCP server
description: Dokumentasi OKF v0.2 bagi run-fastmcp-server.md.
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
title: "Run Fastmcp Server"
description: "DSOM Guide document for Run Fastmcp Server."
type: "guide"
id: "docs/how-to/run-fastmcp-server.md"
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

# Run the FastMCP server

This guide explains how to configure, start, and debug the local Model Context Protocol (MCP) server to expose the Sovereign Palace to AI editors.

## Prerequisites

- **Python 3.11+** and **`uv`** must be installed.
- **MCP client** (e.g. Cursor, Claude Desktop, or Windsurf) running locally.

## Step 1: Start the server

Launch the server using `uv run` to isolate and resolve dependencies dynamically. This starts the JSON-RPC interface over standard input/output (`stdio`):

```bash
uv run tools/mcp/server.py

```

## Step 2: Configure AI editors (Cursor / Claude Desktop)

To connect your IDE to the server, append the following configuration block to your client settings.

### Claude Desktop config (`claudedesktopconfig.json`)

Open `~/.code/claude_desktop_config.json` (macOS/Linux) or `%APPDATA%/Claude/claude_desktop_config.json` (Windows) and insert:

```json
{
  "mcpServers": {
    "dsom-palace": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp[cli]>=1.1.2",
        "--with", "fastmcp>=0.1.0",
        "--with", "pyyaml>=6.0",
        "tools/mcp/server.py"
      ],
      "env": {
        "DSOM_ROOT": "/absolute/path/to/deep-state-of-mind-for-my-ai"
      }
    }
  }
}

```

## Step 3: Verify server functionality

Execute the standard test suite to confirm that the server registers all required resources and tools:

```bash
uv run --with pyyaml --with pytest --with mcp==1.2.1 --with fastmcp pytest tests/test_mcp_server.py

```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
