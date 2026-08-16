---
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
