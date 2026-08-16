---
title: "Palace Auditor"
description: "DSOM Reference document for Palace Auditor."
type: "reference"
id: "docs/reference/skills/palace-auditor.md"
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
