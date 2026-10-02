---
spec_version: '0.2'
okf_version: '0.2'
type: agent_skill
title: 🚀 DSOM Release Manager
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
okf_version: 0.1
type: agent_skill
title: dsom-release-manager
description: Cuts a formal DSOM release, updates ledgers, tags the repository, and deploys to GitHub/GitLab.
topics: [release, git, tagging, changelog, deployment]
timestamp: 2026-07-12T09:50:00Z
---
# 🚀 DSOM Release Manager

## When to use this skill
Trigger this skill when the user asks to "cut a release", "create release notes", or "do a release for github/gitlab".

## Execution Steps
1. **Changelog Promotion:** Modify `CHANGELOG.md` to promote the `[Unreleased]` section into a formal versioned release block (e.g., `## [10.4.0-governance] - YYYY-MM-DD`). Add an empty `[Unreleased]` block above it.
2. **Ledger Sync:** Ensure the version footer in `HISTORY.md` reflects the new version string.
3. **Mental Anchor:** Create an EOD-style mental anchor in `.agents/brain/checkpoint_summary.txt` summarizing the release.
4. **GitOps Stage:** Commit all changes via `git commit -m "docs: cut release <VERSION>"`.
5. **Tagging:** Create a Git tag via `git tag -a v<VERSION> -m "Release <VERSION>"` and push to all remotes (`git push origin main`, `git push origin v<VERSION>`, `git push gitlab main`, `git push gitlab v<VERSION>`).
6. **Release Notes Generation:** Extract the specific release notes from `CHANGELOG.md` and write them to a temporary file (`.agents/brain/scratch/release_notes.txt`).
7. **Platform Deployment:** 
   - Deploy to GitHub: `gh release create v<VERSION> -F .agents/brain/scratch/release_notes.txt --title "v<VERSION>"`
   - Deploy to GitLab: `glab release create v<VERSION> --name "v<VERSION>" --notes-file .agents/brain/scratch/release_notes.txt`

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia) | 2026-07-12*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | GNU General Public License v3.0*


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
