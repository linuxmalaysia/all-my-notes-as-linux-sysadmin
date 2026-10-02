---
spec_version: '0.2'
okf_version: '0.2'
type: architecture_concept
title: '📋 Implementation Plan: Fasa 8 (Migrasi & Pemodenan Bab 8 - Pengurusan Pakej
  & Repositori Lanjutan, Rule 32.43 & Rule 32.44)'
description: Dokumentasi OKF v0.2 bagi implementation_plan.md.
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

# 📋 Implementation Plan: Fasa 8 (Migrasi & Pemodenan Bab 8 - Pengurusan Pakej & Repositori Lanjutan, Rule 32.43 & Rule 32.44)

## 🎯 Objektif & Rasional
Memproses bahan mentah daripada `references/manual/bab_08/` (part_01.md & part_02.md) berkaitan pengurusan pakej RPM/Debian, utiliti CLI (`apt`, `dnf5`, `rpm`, `dpkg`), alat GUI (`gnome-software`, `synaptic`, `packagekit`), kompilasi kod sumber tarball (`.tar.gz`, `.tar.zst`, `.src.rpm`), serta pengukuhan pemboleh ubah persekitaran `$EDITOR` dan `$VISUAL`.

Di samping itu, menyerapkan dua peraturan tatatertib dan amalan terbaik Ansible AI terbaharu:
- **Rule 32.43:** Automated Ansible Playbook Validation Ladder & Idempotence Assertion Standard (berasaskan rujukan KodeKloud 2026).
- **Rule 32.44:** Ansible Community AI-Forge & Red Hat CoP Automation Good Practices Standard (berasaskan rujukan ansible-community/ai-forge & Red Hat CoP).

---

## 🏛️ Pemetaan Silibus NOSS & Penstrukturan Modul

1. **Tadbir Urus Perlembagaan AI (`AGENTS.md` & `.agents/AGENTS.md`):**
   - Penambahan Rule 32.43 dan Rule 32.44 bagi garis panduan automasi Ansible AI.

2. **Modul Amali Sovereign Manual (`manual/`):**
   - **`manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md`**: Pengayaan pengurusan pakej CLI RPM (`-i`, `-U`, `-F`, `-q`, `-V`, `-e`, `--rebuilddb`), binaan SRPM `rpmbuild --rebuild`, kompilasi tarball `./configure`, `make`, `make install` & verifikasi `sha256sum`/`gpg`, alat GUI Synaptic & GNOME Software, serta penetapan `$EDITOR` dan `$VISUAL`.
   - **`manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.md`**: Automasi kemas kini keselamatan pakej, audit CVE, dan integriti `rpm -V` / `dpkg --verify`.

3. **Pangkalan Rujukan OpenWiki (`openwiki/`):**
   - **`openwiki/topic-01-linux-desktop-and-basics.md`** & **`openwiki/topic-05-linux-security.md`**: Sintesis pengurusan pakej, kompilasi kod sumber, dan audit keselamatan.

4. **Kemahiran AI Ejen (`.agents/skills/`):**
   - `.agents/skills/dsom-infrastructure-playbook-documenter/SKILL.md` (Ansible Validation Ladder & Red Hat CoP Standards).
   - `.agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md` & `.agents/skills/cu05-wa04-conduct-application-security-patching/SKILL.md`.

---

## 🚀 Langkah Pelaksanaan Jules
1. Kaji teks mentah di `references/manual/bab_08/part_01.md` dan `part_02.md`.
2. Kemas kini fail perlembagaan dan kemahiran AI ejen.
3. Bina semula tapak web statik dengan `uv run scripts/serve_mkdocs.py --build-only`.
4. Sahkan 100% Quality Gate dengan `uv run --with pytest --with pyyaml --with pytest-cov --with defusedxml python run_all_tests.py`.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
