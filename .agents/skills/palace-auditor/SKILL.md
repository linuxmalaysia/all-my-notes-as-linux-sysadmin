---
spec_version: '0.2'
okf_version: '0.2'
type: agent_skill
title: 🕵️ Palace Auditor Skill
description: Dokumentasi OKF v0.2 bagi SKILL.md.
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:45Z'
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
name: palace-auditor
description: A diagnostic skill that crawls the workspace to verify index.md links, identify undocumented scripts in tools/, and propose structural cleanups to maintain the Sovereign Memory Palace.
topics: [palace, audit, brain, index, cleanup]
okf_version: 0.1
---

# 🕵️ Palace Auditor Skill

## When to use this skill
Use this skill when the user requests a workspace audit, health check, or when preparing for a major structural release to ensure the `.agents` palace is pristine.

## Instructions
1. **Diagnostic Check:** Run `.\tools\diagnostic.ps1` (or `./tools/diagnostic.sh` on Linux) and capture the output. Ensure all dependencies (`uv`, `node`, `git`) and paths are healthy.
2. **Index Verification:** Read `.agents/brain/index.md`. Verify that every `closet.md` or `.md` file listed under `Path:` actually exists in the filesystem.
3. **Toolchain Audit:**
   - List all files in the `tools/` directory.
   - List all documentation files in `docs/tools/`.
   - Identify any `.ps1`, `.sh`, `.py`, or `.js` script in `tools/` that does NOT have a corresponding structural blueprint in `docs/tools/`.
   - Identify any script that lacks either its `.ps1` or `.sh` cross-platform twin.
4. **Report Generation:** Create a report artifact for the user summarizing:
   - System Diagnostic Health.
   - Broken links in `index.md` (if any).
   - Undocumented scripts.
   - Scripts violating the Cross-Platform Mandate.
5. **Propose Actions:** Suggest specific actions to resolve the findings.


---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
