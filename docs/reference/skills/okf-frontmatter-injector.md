---
title: "Okf Frontmatter Injector"
description: "DSOM Reference document for Okf Frontmatter Injector."
type: "reference"
id: "docs/reference/skills/okf-frontmatter-injector.md"
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

# 💉 OKF Frontmatter Injector

## When to use this skill
Use this skill when the user asks to ensure documentation is OKF (Open Knowledge Format) compliant, or when importing new markdown files that lack standard YAML frontmatter headers.

## Instructions
1. This skill utilises a Python script embedded in `scripts/apply_okf.py`.
2. Ask the user for the target directory to scan (default is the project root `.`).
3. Execute the script using your terminal tools:
   ```bash
   python .agents/skills/okf-frontmatter-injector/scripts/apply_okf.py <TARGET_DIRECTORY>
   ```
4. The script will automatically skip files that already possess frontmatter. It categorizes files dynamically based on their folder structure (e.g. `agent_skill`, `governance_protocol`, etc.).
5. Inform the user of the total number of files modified based on the script's output.


---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*
