---
spec_version: '0.2'
okf_version: '0.2'
type: reference
title: 🔄 Cross-Platform Translator Skill
description: Dokumentasi OKF v0.2 bagi cross-platform-translator.md.
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
title: "Cross Platform Translator"
description: "DSOM Reference document for Cross Platform Translator."
type: "reference"
id: "docs/reference/skills/cross-platform-translator.md"
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

# 🔄 Cross-Platform Translator Skill

## When to use this skill
Use this skill when a new automation script is created in one shell language, and the workspace Constitution requires its equivalent to be generated for cross-platform compliance.

## Instructions
1. **Analyze Source:** Read the source script (e.g., `tools/myscript.ps1`) to understand its exact logical flow, variable assignments, standard output formats, and error handling.
2. **Determine Target:** If the source is `.ps1`, the target is `.sh` (Bash). If the source is `.sh`, the target is `.ps1` (PowerShell).
3. **Translation Rules:**
   - **Banners:** Preserve the exact DSOM banner text and colors (using ANSI escape codes in Bash, or `Write-Host -ForegroundColor` in PowerShell).
   - **Paths:** Ensure path separators are idiomatic (use `/` or `\` appropriately, though PowerShell often accepts `/`).
   - **Error Handling:** Map PowerShell's `try/catch` or `$ErrorActionPreference = "Stop"` to Bash's `set -e` or specific `if ! command; then ... fi` checks.
   - **Dependencies:** If the script calls another script, ensure it calls the correct extension for its platform (e.g., a `.ps1` script should call `reanimate.ps1`, not `reanimate.sh`).
4. **Output Generation:** Write the translated script to the target file.
5. **Update Documentation:** If the script is documented in `docs/tools/`, ensure the documentation accurately lists both the `.ps1` and `.sh` file names.


---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
