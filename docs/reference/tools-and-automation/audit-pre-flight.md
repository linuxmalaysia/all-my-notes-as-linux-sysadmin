---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: 📜 Audit Pre-Flight (audit-pre-flight.sh)
description: Dokumentasi OKF v0.2 bagi audit-pre-flight.md.
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
title: "Audit Pre Flight"
description: "DSOM Reference document for Audit Pre Flight."
type: "reference"
id: "docs/reference/tools-and-automation/audit-pre-flight.md"
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

# 📜 Audit Pre-Flight (audit-pre-flight.sh)

> **"Trust, but Verify."** - The physical reality check before the AI wakes up.

## 1. 🏛️ Purpose

**Version:** v4.1 (Root Aware)
**Description:** Enforces synchronization between the physical environment, Git state, and the AI's "External Brain" before starting a development session.

## 2. 🛡️ Safety Mechanisms

| Mechanism | Status | Description |
| :--- | :--- | :--- |
| **Zero-Global Pattern** | ✅ Enforced | Uses local variables for pathing. |
| **Exit-on-Error** | ✅ Active | `set -e` flag prevents zombie execution. |
| **Root-Aware** | ✅ Active | Auto-detects git root via `git rev-parse`. |

## 3. ⚙️ Usage

```bash
./tools/audit-pre-flight.sh

```

## 4. 🧠 Logic Flow (The Algorithm)

1. **Brain Check:** Verifies existence of `task.md` and `walkthrough.md` in `.agents/brain/`.
2. **Git Drift Check:** Compares local `HEAD` vs remote `@{u}`. Warns if out of sync.
3. **Environment Discovery:** Detects project type (PHP/Node/Python) based on manifest files (`composer.json`, etc.).
4. **Governance Check:** Ensures `AI-MASTER-PROTOCOL.md` and `README.md` are present.

## 5. 📝 Extracted Comments

>
> "Enforces synchronization between the physical environment, Git state, and the AI's 'External Brain' before starting a development session."

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
