---
spec_version: '0.2'
okf_version: '0.2'
type: documentation
title: Changelog
description: Dokumentasi OKF v0.2 bagi CHANGELOG.md.
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:42Z'
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

# Changelog

Semua perubahan ketara kepada projek ini akan direkodkan dalam fail ini. 

Format ini berdasarkan kepada [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), 
dan projek ini mematuhi spesifikasi [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added (Penambahan)
- **Open Knowledge Format (OKF v0.2) Adoption**: Upgraded repository frontmatter schema across all Markdown files to OKF v0.2 (`spec_version: "0.2"`, `okf_version: "0.2"`, trust signals `generated`/`verified`/`status`/`stale_after`, and `sources` provenance listing `resource` paths and public URLs).
- **Code Health & Tooling**: Enhanced `scripts/apply_okf_v02.py` with safe `verified` field normalization, string source conversion to resource dicts, and scalar string validation for `id` and `resource` fields.
- **AI Constitution & Adoption Guide**: Updated Rule 8 in `AGENTS.md` and `.agents/AGENTS.md` and comprehensively updated `docs/OKF-ADOPTION-GUIDE.md` to reflect OKF v0.2 trust signals, actor conventions (`<producer>/<version>`, `human:<id>`, `process:<id>`), index/log reserved file rules, and Attested Computations.
- **Fasa 8 Migrasi Silibus Bab 8**: Ekstraksi dan pemodenan kandungan amali `references/manual/bab_08/` ke dalam `manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md` dan `manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.md`.
- **Governance Rules**: Added **Rule 32.43** (*Automated Ansible Playbook Validation Ladder & Idempotence Assertion Standard*) and **Rule 32.44** (*Ansible Community AI-Forge & Red Hat CoP Automation Good Practices Standard*) to `AGENTS.md` and `.agents/AGENTS.md`.
- **Skill Extensions**: Extended `.agents/skills/dsom-infrastructure-playbook-documenter/SKILL.md` (Phases 4l & 4m), `.agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md`, and `.agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md`.
- **OpenWiki**: Updated `openwiki/topic-01-linux-desktop-and-basics.md` and `openwiki/topic-05-linux-security.md` with package management and security audit synthesis.
- **Governance**: Adopted the *Tri-Phasic Mind Cognitive Architecture* blueprint, injecting Tech Stack and Implementation Roadmap into `docs/explanation/governance/DSOM-TRI-PHASIC-COGNITIVE-ARCHITECTURE.md`.
- **Rules**: Added Rule 11 to AI Constitution (`.agents/AGENTS.md`) governing Tri-Phasic execution state constraints.

## [1.0.4] - 2026-05-24

### Added (Penambahan)
- Fail `NOTICE.md` berserta klausa atribusi perundangan pihak ketiga bagi mengiktiraf lesen pengarang asal sumber luar (OpenSkills, AgentSkills, DSPy).
- Seksyen penafian keselamatan pada pautan `README.md`.

## [1.0.3] - 2026-05-24

### Added (Penambahan)
- Lesen Terbuka (Open Source License) menggunakan **MIT License** bagi membolehkan repositori ini digunakan secara bebas sebagai templat gred pengeluaran.

## [1.0.2] - 2026-05-24

### Added (Penambahan)
- Fail `HISTORY.md` yang merakam sejarah, evolusi dan falsafah projek.
- Fail `CHANGELOG.md` untuk mengurus nota keluaran dan log perubahan rasmi secara berpusat.

### Changed (Perubahan)
- Indeks rujukan dalam `README.md` dikemas kini untuk memuatkan senarai sejarah dan changelog terbaru.

## [1.0.1] - 2026-05-24

### Added (Penambahan)
- Integrasi *Universal Loader* dengan membina `AGENTS.md` di root folder.
- Dokumen rujukan `docs/OPENSKILLS.md` bagi panduan penggunaan `npx openskills`.
- Dokumen aliran kerja `docs/GIT-RELEASE-WORKFLOW.md` sebagai SOP pembuatan fail versi.
- Tambahan dua rujukan repo rasmi (*Deep State of Mind*, *MemPalace Framework*) ke dalam `README.md`.

## [1.0.0] - 2026-05-24

### Added (Penambahan)
- Struktur direktori awal *Method of Loci* (`palace/wings/halls/rooms/drawers/closets`, `scripts`, `references`, `assets/locks`).
- Fail manifesto `docs/HOWTO-create-skill.md` dan keselamatan `docs/PROMPTS.md`.
- Fail penapis `gitignore` untuk mengelak kebocoran PII.
- Templat teras eksekutif dalam `docs/templates/SKILL.md`.
- Rangkaian luas perpustakaan dokumen untuk format Agent Skills (`BEST-PRACTICES`, `WHAT-ARE-SKILLS`, `CREATING-YOUR-FIRST-SKILL`, `WRITING-EFFECTIVE-SKILLS`, `SKILL-FILE-STRUCTURE`, `USING-REFERENCE-FILES`, `SKILL-FORMAT`, dll).
- Direktori `releases/` untuk penyimpanan fail-fail versi keluaran (zip).

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
