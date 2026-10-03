---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: 🤖 Claude Reanimation (reanimate-claude.sh)
description: Dokumentasi OKF v0.2 bagi reanimate-claude.md.
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
title: "Reanimate Claude"
description: "DSOM Reference document for Reanimate Claude."
type: "reference"
id: "docs/reference/tools-and-automation/reanimate-claude.md"
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

# 🤖 Claude Reanimation (reanimate-claude.sh)

> **"Hello, Claude."** - Provider-Specific Context Injection.

## 1. 🏛️ Purpose

**Version:** v1.0
**Description:** A lightweight variant of the Reanimation Engine specifically optimized for Claude.ai's "Project Knowledge" file size limits. It generates a cleaner, markdown-heavy context file.

## 2. 🛡️ Safety Mechanisms

| Mechanism | Status | Description |
| :--- | :--- | :--- |
| **Fail-Safe Cat** | ✅ Active | Uses `|| echo` fallback if Master Protocol is missing. |
| **Exit-on-Error** | ✅ Active | `set -e` injected. |
| **Fixed Output** | ✅ Active | Targets `DSOM-CLAUDE-INIT.md`. |

## 3. ⚙️ Usage

```bash
./tools/reanimate-claude.sh

```

## 4. 🧠 Logic Flow

1. **Header Generation:** Appends Date and Title.
2. **Protocol Injection:** Injects `AI-MASTER-PROTOCOL.md`.
3. **Brain Dump:** Injects Task, Walkthrough, and Implementation Plan.
4. **Finalization:** Writes to `DSOM-CLAUDE-INIT.md`.

## 5. 📝 Extracted Comments

>
> "Optimized for Claude.ai Project Knowledge Base."

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
