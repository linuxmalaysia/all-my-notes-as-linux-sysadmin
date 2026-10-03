---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: 🌅 Reanimation Engine (reanimate.sh)
description: Dokumentasi OKF v0.2 bagi reanimate.md.
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
title: "Reanimate"
description: "DSOM Reference document for Reanimate."
type: "reference"
id: "docs/reference/tools-and-automation/reanimate.md"
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

# 🌅 Reanimation Engine (reanimate.sh)

> **"Wake up, Neo."** - Ingesting the Project State.

## 1. 🏛️ Purpose

**Version:** v1.5
**Description:** The heart of the Start-of-Day (SOD) ritual. It aggregates ALL core artifacts (`README`, `AI-MASTER-PROTOCOL`, `task.md`, etc.), file topology, and git history into a single text manifest (`sod_manifest.txt`) that brings the AI up to speed instantly.

## 2. 🛡️ Safety Mechanisms

| Mechanism | Status | Description |
| :--- | :--- | :--- |
| **Interactive Input** | ✅ Active | Captures multi-line manual summaries via `cat` and `CTRL+D`. |
| **Sunday Audit** | ✅ Active | Auto-detects if today is Sunday and prompts for Weekly Audit. |
| **System Telemetry** | ✅ Active | Injects OS, Shell, and Date info for context. |
| **Exit-on-Error** | ✅ Active | `set -e` prevents partial manifests. |

## 3. ⚙️ Usage

```bash
./tools/reanimate.sh

```

## 4. 🧠 Logic Flow

1. **Manual Injection:** Prompts user for "EOD Summary" or "Master Prompt" additions.
2. **Context Aggregation:** Concatenates:
    * `README.md`
    * `docs/AI-MASTER-PROTOCOL.md`
    * `.agents/brain/*` (Task, Walkthrough, Plan)
    * `git ls-tree` (Project Structure)
    * `git log` (Recent History)
3. **Governance Warning:** Checks Day-of-Week. Triggers Sunday Audit alert if applicable.
4. **Output:** Generates `sod_manifest_[DATE].txt` in root.

## 5. 📝 Extracted Comments

>
> "Aggregates ALL core DSOM artifacts. Features an interactive multi-line input for EOD summaries."

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
