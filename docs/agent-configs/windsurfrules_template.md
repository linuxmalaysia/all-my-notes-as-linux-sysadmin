---
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
