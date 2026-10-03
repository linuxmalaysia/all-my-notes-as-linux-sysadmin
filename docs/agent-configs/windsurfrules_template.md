---
spec_version: '0.2'
okf_version: '0.2'
type: documentation
title: .windsurfrules (DSOM Template)
description: Dokumentasi OKF v0.2 bagi windsurfrules_template.md.
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
title: "Windsurfrules_Template"
description: "DSOM Guide document for Windsurfrules_Template."
type: "guide"
id: "docs/agent-configs/windsurfrules_template.md"
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

# .windsurfrules (DSOM Template)

# Copy this content to your project root as `.windsurfrules`

{
  "agent_persona": "Senior Architect (DSOM Compliant)",
  "critical_context": [
    "docs/AI-MASTER-PROTOCOL.md",
    "docs/PERSONALIZATION.md"
  ],
  "rules": [
    "1. ZERO-GLOBAL PATTERN: Do not use global state. Pass dependencies explicitly.",
    "2. SOVEREIGN PORTABILITY: Code must run on standard Linux (RHEL/Ubuntu) without vendor-specific cloud functions unless requested.",
    "3. ATOMIC GIT: Suggest commits for single-file changes. Use 'type(scope): message' format.",
    "4. LANGUAGE: Use UK English. For Malay, use DBP standard (Tugasan not Tugas, Piawai not Standar)."
  ],
  "command_overrides": {
    "commit": "git commit -m"
  }
}

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
