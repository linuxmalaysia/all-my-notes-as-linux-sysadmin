---
spec_version: '0.2'
okf_version: '0.2'
type: agent_skill
title: DSOM Diátaxis Documentation Pipeline
description: Dokumentasi OKF v0.2 bagi SKILL.md.
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
okf_version: 0.1
type: skill
title: "dsom-diataxis-pipeline"
timestamp: "2026-08-16T09:12:00Z"
topics: ["dsom", "diataxis", "pipeline"]
tags: ["script", "automation", "python", "docs"]
description: "Executes the DSOM-Governed Diátaxis & OKF Documentation Pipeline to restructure the repository's docs folder."
resource: "file:///.agents/skills/dsom-diataxis-pipeline/SKILL.md"
---

# DSOM Diátaxis Documentation Pipeline

## Overview
This skill executes the architectural mandate to restructure documentation into the **4 Diátaxis Quadrants** (Tutorials, How-To, Reference, Explanation), injects strict **Google OKF v0.1** schemas, and generates the required AI index `llms.txt` and GitBook index `SUMMARY.md`.

## When to Use
Trigger this skill whenever you perform a major documentation import, create new tools, or need to refresh the `docs/` structure and `llms.txt` root index.

## Instructions
1. Ensure you are at the project root.
2. Execute the pipeline script using `uv run` to satisfy the Python UV Mandate (Rule 9):

```powershell
uv run scripts/build_diataxis_docs.py
```

3. The script will automatically reorganize folders, generate missing reference files for skills, and rebuild `llms.txt`.
4. Verify the output in `docs/SUMMARY.md` and `/llms.txt`.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
