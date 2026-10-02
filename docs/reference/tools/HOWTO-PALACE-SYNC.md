---
spec_version: '0.2'
okf_version: '0.2'
type: automation_tool
title: 'HOWTO: palace-sync — Kingdom Spatial Mapping'
description: Dokumentasi OKF v0.2 bagi HOWTO-PALACE-SYNC.md.
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
title: "Howto Palace Sync"
description: "DSOM Reference document for Howto Palace Sync."
type: "reference"
id: "docs/reference/tools/HOWTO-PALACE-SYNC.md"
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

# HOWTO: palace-sync — Kingdom Spatial Mapping

# docs/tools/HOWTO-PALACE-SYNC.md

> **Standard: DSOM For My AI Protocol v6.1 | Palace v1.0 | Core Engine**
> **Tools:** `palace-sync.ps1`, `palace-sync.sh`
> **Platforms:** Windows Native (T1), Linux/WSL2 (T2)

---

## 1. Purpose

`palace-sync` is the **Spatial Parser** of the Sovereign Markdown Palace. It bridges the gap between raw Git commits and high-density cognitive closets. By analyzing the path of changed files in git, it automatically maps updates to the correct "Room" in the Palace hierarchy.

**Use it to:**
- Automatically categorize git history since the last sync.
- Generate a **Palace Update Proposal** for AI review.
- Perform a full-history backfill to populate a new Palace from scratch.
- Maintain the spatial integrity of the `wings/` directory.

**Location:** 
- `tools/palace-sync.ps1` (Windows)
- `tools/palace-sync.sh` (Linux/WSL2)

---

## 2. Prerequisites

| Requirement | Minimum | Notes |
|:---|:---|:---|
| Protocol Level | Palace v1.0 | Requires the `wings/` directory structure. |
| Sync Marker | `.palace-sync-marker` | Automatically created to track the last sync date. |
| Closets | `closet.md` | Rooms must have a closet file to receive updates. |

---

## 3. Usage

### 3.1 Incremental Sync (EOD Fashion)

```powershell
.\tools\palace-sync.ps1

```

```bash
bash tools/palace-sync.sh

```

Analyzes commits since the date stored in `.palace-sync-marker`. Used during every End-of-Day ritual.

### 3.2 Full History Backfill

```powershell
.\tools\palace-sync.ps1 -Backfill

```

```bash
bash tools/palace-sync.sh --backfill

```

Scans the **entire git history** from the first commit. Essential for onboarding an existing repository into the Palace architecture.

---

## 4. Reading the Output & Status Codes

| Label | Meaning | Action |
|:---|:---|:---|
| `✅ No new commits` | The Palace is already up to date. | None needed. |
| `📝 Building Proposal` | Mapping detected changes. | Wait for the generator to finish. |
| `📄 File: palace_update_proposal...` | Success. | Share this file with the AI for closet updates. |

---

## 5. Implementation Logic (Path Mapping)

The tool uses regex patterns to map files to Rooms:

| Path | Wing | Hall | Room |
|:---|:---|:---|:---|
| `playbooks/`, `roles/` | `wing_dsom_core` | `hall_events` | `room_sovereign_fabric` |
| `.agents/brain/` | `wing_dsom_core` | `hall_events` | `room_brain_artifacts` |
| `tools/` | `wing_dsom_core` | `hall_facts` | `room_tooling` |
| `docs/` | `wing_dsom_core` | `hall_facts` | `room_dsom_protocol` |
| `CHANGELOG.md` | `wing_dsom_core` | `hall_events` | `room_ledger` |

---

## 6. Related Documents

| Document | Purpose |
|:---|:---|
| [`docs/HOWTO-PALACE-ONBOARDING.md`](../HOWTO-PALACE-ONBOARDING.md) | Guide for first-time Palace setup. |
| [`docs/MIRROR-OF-KNOWLEDGE.md`](../MIRROR-OF-KNOWLEDGE.md) | Understanding the underlying memory theory. |

---

*Standard: DSOM For My AI Protocol v6.1 | Palace v1.0 | Harisfazillah Jamel*
*Document Version: v1.0 | Created: 2026-04-08*

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
