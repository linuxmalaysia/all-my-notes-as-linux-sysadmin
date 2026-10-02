---
spec_version: '0.2'
okf_version: '0.2'
type: governance_protocol
title: DSOM-MCP-ARCHITECTURE.md
description: Dokumentasi OKF v0.2 bagi DSOM-MCP-ARCHITECTURE.md.
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
title: "Dsom Mcp Architecture"
description: "DSOM Concept document for Dsom Mcp Architecture."
type: "concept"
id: "docs/explanation/governance/DSOM-MCP-ARCHITECTURE.md"
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

# DSOM-MCP-ARCHITECTURE.md

> **"Context is not a static text block; it is an interactive resource. Let the AI query the Palace itself."**

---

## 1. The Context7 Inspiration

Traditional DSOM interactions required passing context into the chat explicitly via `.dsom` state files, `palace_update_proposals`, or the human manually injecting references. Services like Context7 demonstrated a better approach: **RAG (Retrieval-Augmented Generation) exposed natively to the AI client.**

Instead of pushing context *to* the AI, the AI *pulls* exactly what it needs from the Sovereign Markdown Palace through a standardised API: the **Model Context Protocol (MCP)**.

## 2. Core Architecture of DSOM-MCP

We are building a native Python MCP Server (`dsom-mcp-server`) that completely replaces the need for external third-party syncs for local development.

### 2.1 The Transport Layer (STDIO)

The MCP server operates as a local subprocess spawned by your AI editor (Cursor, Google Jules, Claude Desktop). Communication happens over `stdio` using JSON-RPC.
- **Rule:** The MCP script must strictly output JSON-RPC to `stdout`. All logs or debugging MUST be written to `stderr`. Using `print()` without redirecting to `sys.stderr` will instantly break the protocol.

### 2.2 Framework & Ecosystem (Rule 16 Compliance)

- **Executor:** The server is executed exclusively via `uv run` to maintain Python environmental isolation.
- **Framework:** We utilize the `fastmcp` (or official `mcp`) Python SDK to define resources and tools asynchronously.

## 3. The 3 Pillars of the DSOM-MCP Server

### Pillar A: Exposed Resources (Memory & State)

Resources are static or dynamic data blobs the AI can "read" at will without using a tool.
- `dsom://state/current` → Serves `.agents/brain/current_state.dsom`
- `dsom://state/task` → Serves `.agents/brain/task.md`
- `dsom://state/walkthrough` → Serves `.agents/brain/walkthrough.md`

When an AI boots up, it reads these URIs immediately to achieve the "Genesis Read" without the human typing a single prompt.

### Pillar B: Exposed Tools (The Rituals)

Tools are executable functions. We expose our existing DSOM automation to the AI natively.
- `search_palace(query)`: Executes a semantic or `grep` search across `docs/`.
- `palace_sync()`: Triggers the EOD spatial reflection engine natively.

### Pillar C: Execution Bridge

Because Windows (T1) and WSL2 (T2) possess execution boundaries, the MCP server must detect its environment and invoke the `tools/` Bash or PowerShell scripts appropriately.

## 4. MCP Client Configuration Example

To attach the DSOM-MCP server to Claude Desktop (or Cursor), the human operator modifies their client config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "dsom-palace": {
      "command": "uv",
      "args": [
        "run",
        "--with", "mcp",
        "tools/mcp/server.py"
      ],
      "env": {
        "DSOM_ROOT": "/absolute/path/to/project"
      }
    }
  }
}

```

## 5. Security Posture

- **Zero-Network Surface:** The server runs exclusively on local `stdio`. No HTTP ports are opened.
- **No External Exfiltration:** Unlike passing codebase context to third-party RAG providers, all semantic searching and reading happens strictly on the local machine.

---
*Standard: DSOM For My AI Protocol v6.1 | Harisfazillah Jamel | LinuxMalaysia*

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
