---
okf_version: 0.1
type: skill
title: "dsom-mass-okf-migrator"
timestamp: "2026-08-16T08:57:00Z"
topics: ["dsom", "okf", "migration"]
tags: ["script", "automation", "python"]
description: "Automatically migrates a directory of markdown files to the OKF v0.1 format, replacing obsolete URLs and injecting the Sovereign Dual-License Footer."
resource: "file:///.agents/skills/dsom-mass-okf-migrator/SKILL.md"
---

# DSOM Mass OKF Migrator

## Overview
This skill instructs the AI on how to perform a mass migration of legacy markdown documents into the highly-structured **Open Knowledge Format (OKF) v0.1** tailored for the Linux NOSS Malaysia project.

It utilises a Python script to deeply copy a directory while rewriting the metadata, URLs, and appending the Sovereign Dual-License footer.

## When to Use
Trigger this skill whenever you need to import external documentation, migrate an older DSOM repository's `docs/` or `openwiki/` folder, or standardise a large batch of markdown files to comply with the project's AI Constitution (AGENTS.md) Rule 8 and 9.

## Requirements
- Python must be executed exclusively via `uv` (as per Rule 9).

## Instructions

1. Identify the absolute path of the **Source Directory** (the legacy docs).
2. Identify the absolute path of the **Destination Directory**.
3. Execute the migration script using `uv run` to maintain environment hygiene:

```powershell
uv run .agents/skills/dsom-mass-okf-migrator/scripts/migrate.py "<SOURCE_DIR>" "<DEST_DIR>"
```

*Note: The script automatically skips overwriting `PERSONALIZATION.md`, `OKF-ADOPTION-GUIDE.md`, and `SKILL-FORMAT.md`.*

## Verification
After the script completes, use the `list_dir` tool to verify the destination directory and `view_file` to ensure the YAML frontmatter (`okf_version: 0.1`) and Sovereign footer were injected correctly.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip)*
