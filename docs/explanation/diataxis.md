---
spec_version: '0.2'
okf_version: '0.2'
type: explanation
title: Diátaxis framework adoption in DSOM
description: Dokumentasi OKF v0.2 bagi diataxis.md.
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
title: "Diataxis"
description: "DSOM Concept document for Diataxis."
type: "concept"
id: "docs/explanation/diataxis.md"
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

# Diátaxis framework adoption in DSOM

An architectural overview explaining the adoption, structure, and benefits of the Diátaxis documentation framework in the DSOM project.

## What is Diátaxis?

The **Diátaxis Framework** is a systematic approach to technical documentation. It categorises files based on their purpose and user intent, separating content into four distinct quadrants:

```text
               USER INTENT
        Learning        Practical
      +---------------+---------------+
      |   TUTORIALS   | HOW-TO GUIDES |
Acq.  |  (Learning-   |  (Problem-    |
      |   oriented)   |   oriented)   |
      +---------------+---------------+
      |  EXPLANATION  |   REFERENCE   |
Und.  |  (Concept-    |  (Information-|
      |   oriented)   |   oriented)   |
      +---------------+---------------+

```

## Why adopt Diátaxis in DSOM?

Historically, AI agent tool documentation was mixed with procedural runbooks. This led to high cognitive load and excessive token consumption.

Adopting Diátaxis provides three main benefits:
- **Reduces token costs:** Separate reference files allow AI agents to fetch precise factual details without reading conversational or tutorial text.
- **Speeds up onboarding:** Human developers can follow step-by-step lessons without getting bogged down in low-level arguments.
- **Clarifies purpose:** Developers and writers know exactly where a new document belongs based on the user's intent.

## Quadrant mappings in DSOM

Our documentation Palace is structured cleanly inside `docs/` using the four Diátaxis folders:

1. **Tutorials (`docs/tutorials/`):**
   - Guided learning lessons for beginners.
   - Example: [Getting Started with DSOM Tools](../tutorials/getting-started.md).

2. **How-To Guides (`docs/how-to/`):**
   - Goal-oriented, step-by-step instructions for specific real-world tasks.
   - Example: [Run the FastMCP Server](../how-to/run-fastmcp-server.md).

3. **Reference (`docs/reference/`):**
   - Factual description, API signatures, and configurations for all 8 Python scripts.
   - Example: [apply_okf_frontmatter.py Reference](../reference/apply_okf_frontmatter.md).

4. **Explanation (`docs/explanation/`):**
   - Context, architecture, and design rationale behind our components.
   - Example: [OpenWiki & FastMCP Architecture](openwiki-mcp-architecture.md).

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
