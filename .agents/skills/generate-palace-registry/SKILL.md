---
okf_version: 0.1
type: agent_skill
name: generate-palace-registry
description: "Automatically regenerates the Master Palace Registry (.agents/skills/index.md) by parsing OKF YAML frontmatter from all installed skills."
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
