---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: 🛡️ Privacy Guardian (privacy-guardian.sh)
description: Dokumentasi OKF v0.2 bagi privacy-guardian.md.
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
title: "Privacy Guardian"
description: "DSOM Reference document for Privacy Guardian."
type: "reference"
id: "docs/reference/tools-and-automation/privacy-guardian.md"
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

# 🛡️ Privacy Guardian (privacy-guardian.sh)

> **"Loose lips sink ships."** - Preventing Data Leaks to AI Models.

## 1. 🏛️ Purpose

**Version:** v1.0
**Description:** A pre-commit and pre-upload scanner that checks the generated `sod_manifest` for sensitive data (PII, API Keys, IPs) to ensure "Sovereign Privacy."

## 2. 🛡️ Safety Mechanisms

| Mechanism | Status | Description |
| :--- | :--- | :--- |
| **Zero-Global Pattern** | ✅ Enforced | Local variable scoping. |
| **Exit-on-Error** | ✅ Active | `set -e` injected. |
| **Heuristic Scan** | ✅ Active | Uses regex for IPv4, Google Keys, Slack Tokens, and Home Paths. |

## 3. ⚙️ Usage

```bash
./tools/privacy-guardian.sh

```

## 4. 🧠 Logic Flow

1. **Target Verification:** Checks if a `sod_manifest_YYYY-MM-DD.txt` exists.
2. **Regex Scanning:** Iterates through an array of dangerous patterns:
    * IPv4 Addresses
    * Emails (Standard Regex)
    * Google API Keys (`AIza...`)
    * AWS Access Keys (`AKIA...`)
    * GitHub Tokens (`ghp...`)
    * OpenAI Keys (`sk-...`)
    * Slack Tokens (`xoxb...`)
    * Private Keys (`-----BEGIN...`)
    * Local User Paths (`/home/user/`)
3. **Reporting:** Exits with `1` if leaks are found, requiring manual remediation.

## 5. 📝 Extracted Comments

>
> "Scans the generated DSOM reanimation manifest for sensitive information before it is uploaded to an external AI model."

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
