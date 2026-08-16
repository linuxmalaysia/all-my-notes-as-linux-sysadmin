# Sovereign Markdown Palace: Linux NOSS Malaysia (DSOM)

Projek ini merupakan sebuah pangkalan pengetahuan Sistem Operasi Linux yang tidak rasmi, disusun berdasarkan Standard Kemahiran Pekerjaan Kebangsaan (NOSS) Malaysia. Ia dibina di atas kerangka seni bina *exocortex* (memori luaran) yang mematuhi protokol **Deep State of Mind (DSOM) v0.1** dan distrukturkan sepenuhnya mengikut **Kerangka Dokumentasi Diátaxis**.

| Pautan Rujukan | Keterangan |
| :--- | :--- |
| 🗃️ [Palace Knowledge Index](.agents/skills/index.md) | Daftar rasmi (Sovereign Root) untuk 105+ modul kemahiran NOSS Linux. |
| 🧭 [Seni Bina Diátaxis & Pelbagai Pelantar](docs/explanation/diataxis-architecture.md) | Panduan seni bina Diátaxis, prinsip Markdown-First, dan penerbitan web. |
| 🛡️ [Tri-Phasic Architecture](docs/explanation/governance/DSOM-TRI-PHASIC-COGNITIVE-ARCHITECTURE.md) | Model pemprosesan kognitif 3-lapis AI (Active, Twilight, Deep State). |
| 📜 [Penyata Hak Cipta AI](NOTICE.md) | Deklarasi CC BY-SA 4.0 dan atribusi Harisfazillah Jamel. |

> **PENAFIAN PENTING**: Repositori ini adalah TIDAK RASMI dan dicipta untuk tujuan pengetahuan / pembelajaran sahaja. Ia tidak mewakili Jabatan Pembangunan Kemahiran (JPK) atau Kementerian Sumber Manusia Malaysia (MOHR). Sila rujuk [`LEGAL-NOTICE.md`](LEGAL-NOTICE.md).

---

## 🏛️ Seni Bina Dokumentasi: Diátaxis & Markdown-First

Dokumentasi repositori ini direka bentuk supaya mempunyai **Format Dwicapaian (Dual-Format Delivery)**:
1. **Capaian Teks Tulen (Pure Markdown `.md`):** Setiap modul boleh dibaca secara terus tanpa penterjemahan di terminal, penyunting teks (VS Code, Vim), aplikasi nota (Obsidian), atau terus dalam repositori GitHub / GitLab.
2. **Laman Web Statik HTML:** Boleh dijana secara automatik kepada laman web HTML pantas, moden, dan mesra peranti menggunakan MkDocs Material.

### 4 Kuadran Kerangka Diátaxis (`docs/`)

Berasaskan spesifikasi rasmi [Diátaxis Framework](https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/explanation/diataxis/), fail-fail dokumentasi diasingkan mengikut niat pengguna:

```text
                           ORIENTASI PENGGUNA
                 Pembelajaran (Learning)      Praktikal (Practical)
               +---------------------------+---------------------------+
               |        1. TUTORIALS       |     2. HOW-TO GUIDES      |
  Pemerolehan  |   (Pembelajaran Berpandu) |  (Panduan Masalah/Tugas)  |
  Kemahiran    |  - Langkah mula pemula    |  - Resipi operasi spesifik|
  (Acquisition)|  - Onboarding amali       |  - Panduan kerja SysAdmin |
               +---------------------------+---------------------------+
               |      3. EXPLANATION       |       4. REFERENCE        |
  Kefahaman    |    (Penerangan Konsep)    |    (Rujukan Fakta/Data)   |
  Mendalam     |  - Falsafah GPL & Sejarah |  - Jadual & Sintaks arahan|
 (Understanding|  - Senibina Isirung/OS    |  - Matriks NOSS CU/WA     |
               +---------------------------+---------------------------+
```

1. **Tutorials ([`docs/tutorials/`](docs/tutorials/)):** Panduan langkah demi langkah untuk pemula membina kemahiran praktikal pertama Linux.
2. **How-To Guides ([`docs/how-to/`](docs/how-to/)):** Panduan berfokus matlamat (*problem-oriented recipes*) bagi menyelesaikan masalah dan tugasan operasi sebenar.
3. **Reference ([`docs/reference/`](docs/reference/) & [`manual/`](manual/)):** Modul silibus NOSS teknikal (CU01–CU06), spesifikasi teknikal, jadual pemetaan CU/WA, dan perincian arahan tanpa naratif meleret.
4. **Explanation ([`docs/explanation/`](docs/explanation/) & [`openwiki/`](openwiki/)):** Penerangan teori, falsafah sumber terbuka (GPL), seni bina isirung, dan konteks industri.

---

## 🌐 Keserasian Penerbitan Pelbagai Pelantar (Multi-Platform Publishing)

Kandungan repositori ini menyokong secara natif pelbagai sasaran penerbitan:

- **Penggunaan Terus Tanpa Build (`git pull`):** Direktori [`html/`](html/) telah disediakan secara **prabina (pre-built)** dan dijejak terus di dalam Git. Pengguna boleh terus membuka `html/index.html` pada pelayar web atau menghalakan pelayan web tanpa perlu membina semula projek.
- **GitHub Pages / GitLab Pages:** Boleh diterbitkan terus daripada folder `html/` melalui tetapan repositori atau *pipeline* CI/CD.
- **Read the Docs:** Dikonfigurasikan secara langsung melalui [`mkdocs.yml`](mkdocs.yml).
- **GitBook:** Disokong melalui indeks navigasi Diátaxis [`docs/SUMMARY.md`](docs/SUMMARY.md).
- **Pelayan Nginx & Apache:** Halakan *DocumentRoot* terus ke direktori `html/` (disokong penuh oleh mod URL berkait luar talian).
- **Panduan Terperinci:** Rujuk panduan operasi amali di [**`docs/how-to/deploy-and-serve-html.md`**](docs/how-to/deploy-and-serve-html.md).
- **Konteks AI / LLM:** Disokong melalui [`llms.txt`](llms.txt), `llms-full.txt`, dan skema **Google OKF v0.1**.

---

## 🚀 Arahan Pantas (Quickstart Commands)

```bash
# 1. Bina / Segerakkan struktur Diátaxis dan llms.txt
uv run scripts/build_diataxis_docs.py

# 2. Bina tapak web statik HTML ke folder html/
uv run scripts/serve_mkdocs.py --build-only

# 3. Jalankan pelayan pembangunan tempatan (Live Preview)
uv run scripts/serve_mkdocs.py

# 4. Jalankan ujian pematuhan kualiti 100% (Quality Gate)
uv run run_all_tests.py
```

---

## 🎯 Misi Projek (Project Mission)

Objektif utama repositori ini adalah untuk **memanfaatkan ilmu Sistem Operasi Linux kepada awam (public benefit)**:
1. Digunakan secara bebas oleh sesiapa sahaja (Ejen AI, pendidik, institusi TVET, mahupun industri).
2. Menjadi pangkalan rujukan teknikal yang kukuh untuk membantu usaha pembinaan dan pemetaan silibus **NOSS Malaysia**.
3. Menyumbang semula kepada komuniti perisian sumber terbuka (Open Source) tempatan dan menyokong matlamat kemahiran pendigitalan negara.

---

## 📚 Maklumat Projek (Project Info)

- [`START-HERE.md`](START-HERE.md): **Titik Masuk Utama (Entry Point)**. Sila baca ini dahulu.
- [`.agents/AGENTS.md`](.agents/AGENTS.md): **Perlembagaan & Garis Panduan Ejen AI (DSOM v0.1)**.
- [`.agents/brain/`](.agents/brain/): **Memori Episodik & Penyerahan Ejen (Task, Plan, Walkthrough)**.
- [`llms.txt`](llms.txt): Peta tapak (sitemap) khusus untuk perangkak AI (AI crawler).
- [`HISTORY.md`](HISTORY.md): Menjejaki evolusi dan falsafah awal pembinaan projek ini.
- [`CHANGELOG.md`](CHANGELOG.md): Nota keluaran (Release Notes) rasmi bagi semua versi.
- [`LEGAL-NOTICE.md`](LEGAL-NOTICE.md): **[PENTING]** Penafian NOSS dan ketidakrasmian kandungan.
- [`NOTICE.md`](NOTICE.md): Hak cipta pengarang asal, dan penafian ke atas rujukan pihak ketiga.

---

## 🔗 Rujukan Teras & Penghargaan (References & Attributions)

* **Deep State of Mind (DSOM)**: Pengasas & Pengarang: **Harisfazillah Jamel (LinuxMalaysia)** — [https://github.com/linuxmalaysia/deep-state-of-mind-for-my-ai](https://github.com/linuxmalaysia/deep-state-of-mind-for-my-ai)
* **MemPalace Framework**: Pencipta & Pengarang Asal: **Milla Jovovich & Ben Sigman** (Konsep Memori Ruang / *Method of Loci* yang diadaptasikan ke dalam DSOM) — [https://github.com/milla-jovovich/mempalace](https://github.com/milla-jovovich/mempalace)
* **OpenSkills (Universal Loader)**: Numman Ali & Komuniti OpenSkills — [https://github.com/numman-ali/openskills](https://github.com/numman-ali/openskills)
* **AgentSkills Open Standard**: Anthropic & Komuniti AgentSkills — [https://agentskills.io/home](https://agentskills.io/home)
* **Diátaxis Documentation Framework**: Daniele Procida — [https://diataxis.fr/](https://diataxis.fr/)
* **Skills Directory**: [https://www.skillsdirectory.com/](https://www.skillsdirectory.com/)

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
