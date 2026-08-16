---
title: "Generate Palace Registry"
description: "DSOM Reference document for Generate Palace Registry."
type: "reference"
id: "docs/reference/skills/generate-palace-registry.md"
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

# Generate Palace Registry Skill

## 1. Purpose
Executes the `scripts/generate_palace_registry.js` script to crawl all `SKILL.md` files and update the `index.md` directory map.

## 2. Execution Steps
1. Navigate to the workspace root.
2. Run `node scripts/generate_palace_registry.js`.
3. Verify that `.agents/skills/index.md` was successfully updated and contains a table of skills.


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
