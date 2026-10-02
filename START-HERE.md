---
okf_version: '0.2'
type: guide
title: 'START HERE: Titik Mula Linux NOSS Malaysia & DSOM'
topics:
- onboarding
- entry-points
- dsom
- sovereign
- linux
- noss
- malaysia
description: Dokumen panduan permulaan utama untuk pengendali manusia dan ejen AI
  yang menggunakan kerangka DSOM dalam projek Linux NOSS Malaysia.
spec_version: '0.2'
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

# START HERE: Titik Mula Linux NOSS Malaysia & DSOM

Selamat datang ke **Sovereign Markdown Palace: Pangkalan Pengetahuan Linux NOSS Malaysia** menggunakan kerangka **Deep State of Mind (DSOM)**.

Sistem ini direka bentuk sebagai pangkalan pengetahuan Linux tidak rasmi yang berasaskan *National Occupational Skills Standard (NOSS)* Malaysia. Ia disusun rapi mengikut kerangka dokumentasi **Diátaxis** untuk kecekapan manusia dan ejen AI membaca konteks secara spasial dan modular.

!!! tip "💡 Falsafah Titik Mula (Prinsip Diátaxis)"
    **Anda tidak perlu membaca keseluruhan pangkalan pengetahuan ini untuk memahami atau mula menggunakannya secara praktikal.** Malah, kami mengesyorkan agar anda tidak berbuat demikian. Cara terbaik untuk bermula adalah dengan terus mengaplikasikannya — pada satu tugas atau modul amali, sekecil mana sekalipun.

---

## 🌐 Titik Masuk (Entry Points)

Bergantung kepada peranan anda, sila rujuk dokumen berikut sebelum mula membaca fail-fail lain:

| Dokumen | Tujuan / Audiens |
| :--- | :--- |
| **Gateway Ejen AI** | [`AGENTS.md`](AGENTS.md) - Fail amaran dan pengubah hala pertama untuk Ejen AI (Cursor, Claude, dll). |
| **Perlembagaan Penuh AI** | [`.agents/AGENTS.md`](.agents/AGENTS.md) - 27 Undang-undang Konstitusi Ejen AI yang bertindak sebagai pakar Linux NOSS. |
| **Sitemap AI (LLMs)** | [`llms.txt`](llms.txt) - Peta tapak ringkas untuk perangkak AI (AI crawler) luaran. |
| **Penafian Perundangan** | [`LEGAL-NOTICE.md`](LEGAL-NOTICE.md) - Notis penafian bahawa projek ini adalah tidak rasmi (untuk tujuan pembelajaran sahaja). |
| **Notis Hak Cipta & Pihak Ketiga** | [`NOTICE.md`](NOTICE.md) - Kredit kepada OpenSkills, DSOM, dan AgentSkills. |

---

## 📖 Di Mana Mahu Bermula Untuk Manual Linux?

Jika anda pembaca manusia, pelajar TVET, atau pentadbir sistem yang mahu mempelajari sukatan pelajaran amali Linux, berikut adalah panduan titik mula untuk manual Linux:

1. **Pusat Rujukan Utama Manual**:
   - [`manual/index.md`](manual/index.md) — **Pusat Rujukan Manual NOSS Linux Malaysia**. Ini adalah indeks induk yang memetakan keseluruhan 6 Unit Kompetensi (CU01 hingga CU06) dengan Kerangka Diátaxis.

2. **Laluan Mengikut Tahap & Keperluan**:
   - 🔰 **Pemula & Pengguna Baharu Desktop**:
     - Mula dengan [**CU01: Persediaan Sistem Komputer & Desktop Linux**](manual/cu01/index.md).
     - Rujuk juga panduan permulaan amali di [`docs/tutorials/getting-started.md`](docs/tutorials/getting-started.md).
   - 🖥️ **Pentadbir Sistem & Infrastruktur Pelayan**:
     - **Storan & Pemayaan**: Rujuk [**CU02: Pengurusan Storan & Hipervisor Pemayaan**](manual/cu02/index.md).
     - **Pelayan & Servis**: Rujuk [**CU03: Pentadbiran & Perkhidmatan Pelayan Linux**](manual/cu03/index.md).
   - ⚙️ **Automasi, Keselamatan & Khidmat Sokongan**:
     - **Sandaran & Automasi**: Rujuk [**CU04: Automasi, Sandaran & Pemulihan Sistem**](manual/cu04/index.md).
     - **Keselamatan & Pengerasan Sistem**: Rujuk [**CU05: Kawalan Keselamatan Endpoint & Pengerasan Sistem**](manual/cu05/index.md).
     - **Penyelesaian Masalah & Log**: Rujuk [**CU06: Sokongan Pengguna & Penyelesaian Masalah**](manual/cu06/index.md).

---

## 🌟 Kenapa Linux NOSS & DSOM?

- **Penyusunan Sistematik (NOSS)**: Pengetahuan Linux dipetakan terus kepada unit-unit kompetensi piawai industri dalam `manual/`.
- **Pengurangan Token AI (DSOM)**: Penggunaan *OpenWiki* dan Loci (`.agents/brain/wings/`) mengurangkan konteks yang perlu dimuatkan ke dalam tetingkap memori LLM.
- **Tidak Bergantung kepada API Pihak Ketiga**: Semua maklumat berada dalam bentuk fail `.md` tempatan.
- **Sovereign & Sulit**: Tiada kebergantungan kepada perkhidmatan pelayan awan untuk menyusun struktur silibus.

---
*Deep State of Mind (DSOM) For My AI Protocol | Harisfazillah Jamel (LinuxMalaysia)*
*Projek Bebas (Tidak Rasmi) | Untuk Tujuan Pengetahuan Sahaja*

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
