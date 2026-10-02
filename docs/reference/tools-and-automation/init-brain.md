---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: 🧠 Brain Initializer (init-brain.sh)
description: Dokumentasi OKF v0.2 bagi init-brain.md.
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
title: "Init Brain"
description: "DSOM Reference document for Init Brain."
type: "reference"
id: "docs/reference/tools-and-automation/init-brain.md"
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

# 🧠 Brain Initializer (init-brain.sh)

> **"A clean home for a clear mind."** - Initializing the Cognitive State.

## 1. 🏛️ Purpose

**Version:** v4.1 (Root Aware)
**Description:** Safely initializes the `.agents/brain` directory and default artifacts (`task.md`, `walkthrough.md`) to ensure cognitive continuity for AI agents.

## 2. 🛡️ Safety Mechanisms

| Mechanism | Status | Description |
| :--- | :--- | :--- |
| **Idempotency** | ✅ Enforced | Checks `if [ ! -d ]` before creating. Skips existing files. |
| **Exit-on-Error** | ✅ Active | `set -e` injected for safety. |
| **Root Check** | ✅ Active | Fails if not a git repository. |

## 3. ⚙️ Usage

```bash
./tools/init-brain.sh

```

## 4. 🧠 Logic Flow

1. **Repo Check:** Confirms execution within a valid Git repository.
2. **Directory Creation:** Creates `.agents/brain/` if missing.
3. **Artifact Generation:** Populates `task.md`, `walkthrough.md`, `implementation_plan.md`, and `DSOM_TEMPLATE.md` with default boilerplate content *only if they don't exist*.

## 5. 📝 Extracted Comments

>
> "Safely initializes the Deep State of Mind (DSOM) directory and artifacts at the repository root to ensure cognitive continuity for AI agents."

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
