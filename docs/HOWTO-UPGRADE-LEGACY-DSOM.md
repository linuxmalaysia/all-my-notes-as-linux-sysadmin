---
title: "Howto Upgrade Legacy Dsom"
description: "DSOM Guide document for Howto Upgrade Legacy Dsom."
type: "guide"
id: "docs/HOWTO-UPGRADE-LEGACY-DSOM.md"
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

# HOWTO: Upgrade Legacy DSOM Projects

> **Entry Point 5:** This document serves as the Legacy Upgrade Entry Point. See [START-HERE.md](START-HERE.md) for the master onboarding roadmap.

If you are operating a legacy DSOM project and need to modernize it to the current master architectural baseline, you must systematically inject the following modern protocols to achieve compliance.

## The 5-Step Modernization Path

1. **Adopt `llms.txt`:** Create an `llms.txt` file at the root of your project to map your critical governance documents for external AI crawlers.
2. **Inject OKF YAML Frontmatter:** All existing `.md` files in your `brain/` and `docs/` directories must be retroactively updated to include OKF v0.2 YAML frontmatter (metadata routing).
3. **Mandate the Sovereign Signature:** Pull the `dsom-signature-injector` skill from the master baseline and execute it across your legacy repository to ensure all scripts (`.sh`, `.ps1`) and playbooks (`.yml`) carry standard developer metadata headers and GPL v3.0 licenses.
4. **Transition to `uv`:** Audit your existing Python automation scripts. Adopt the `PYTHON-UV-ENVIRONMENT-GUIDE.md` and migrate away from global `pip` installations to isolated `uv` environments to prevent dependency conflicts.
5. **Establish the Audit Ledger:** Generate an `AUTOMATION-AUDIT-LIST.md` in your `docs/governance/` directory to catalog all legacy `.sh` and `.ps1` scripts for centralized human security auditing.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
