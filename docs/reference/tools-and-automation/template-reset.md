---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: ♻️ Template Reset (template-reset.sh)
description: Dokumentasi OKF v0.2 bagi template-reset.md.
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
title: "Template Reset"
description: "DSOM Reference document for Template Reset."
type: "reference"
id: "docs/reference/tools-and-automation/template-reset.md"
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

# ♻️ Template Reset (template-reset.sh)

> **"Tabula Rasa."** - Returning to the beginning.

## 1. 🏛️ Purpose

**Version:** v1.0
**Description:** Prepares a DSOM clone for a new project. It purges old Git history (`.git`) and resets brain artifacts to a blank "Golden Image" state while preserving the Master Protocol and tools.

## 2. 🛡️ Safety Mechanisms

| Mechanism | Status | Description |
| :--- | :--- | :--- |
| **Confirmation Guard** | ✅ Active | Requires explicit `y` input to proceed. |
| **Destructive Warn** | ✅ Active | Clearly warns about Git history deletion. |
| **Exit-on-Error** | ✅ Active | `set -e` injected. |

## 3. ⚙️ Usage

```bash
./tools/template-reset.sh

```

## 4. 🧠 Logic Flow

1. **Repo Check:** Ensures execution inside a git repo.
2. **Confirmation:** Blocks execution until user confirms.
3. **Git Purge:** `rm -rf .git` and `git init`.
4. **Brain Wipe:** Overwrites `task.md`, `walkthrough.md`, `implementation_plan.md` with default "New Project" templates.
5. **Instruction:** Guides user to add files and start fresh history.

## 5. 📝 Extracted Comments

>
> "Prepares a DSOM clone for a new project. It purges old Git history and resets brain artifacts to a 'Golden Image' state."

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
