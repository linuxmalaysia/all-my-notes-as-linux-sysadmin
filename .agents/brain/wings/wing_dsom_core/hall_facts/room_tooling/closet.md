---
okf_version: '0.2'
type: architecture_concept
title: 'Fact Closet: Tooling & Automation'
timestamp: '2026-08-17T00:00:00Z'
topics:
- dsom
- tooling
- automation
- quality-gate
tags:
- dsom-core
- tools
- memory-closet
description: Fakta alatan pembangunan, penjanaan laman web statik MkDocs, dan orkestrator
  ujian 100% pematuhan.
resource: file:///.agents/brain/wings/wing_dsom_core/hall_facts/room_tooling/closet.md
spec_version: '0.2'
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

# Fact Closet: Tooling & Automation

## Absolute Facts
- **Binaan Laman Web Statik:** `uv run scripts/serve_mkdocs.py --build-only` menjana laman web ke direktori `html/` yang dijejak dalam Git.
- **Ujian Pematuhan Penuh:** `uv run run_all_tests.py` merangkumi Pytest (Python, OKF compliance, cross-platform filesystem) dan Jest (JavaScript).
- **Piawaian Penjanaan Symlink/Junction:** Menggunakan `mklink /J` di Windows dan `os.symlink` di POSIX.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
