---
name: "noss-content-transformation-pipeline"
okf_version: 0.1
type: skill
title: "NOSS Linux Content Transformation Pipeline (IPO Protocol)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["transformation", "pipeline", "noss-linux", "dsom", "ipo"]
tags: ["pipeline", "transformation", "noss", "skills", "ipo"]
description: "Protokol automasi dan panduan operasi bagi ejen AI untuk memproses bahan rujukan mentah (references/), memodenkannya ke standard NOSS Linux 2026, menyuntik OKF v0.1, mengesahkan 100% Quality Gate, dan menerbitkan ke manual/, openwiki/, serta html/."
resource: "file:///.agents/skills/noss-content-transformation-pipeline/SKILL.md"
---

# 🚀 NOSS Linux Content Transformation Pipeline (IPO Protocol)

## 📌 Pengenalan & Peranan Kemahiran
Kemahiran ini membimbing mana-mana Ejen AI (Google Jules, Google Antigravity, dsb.) untuk melaksanakan transformasi ilmu secara sistematik mengikut model **Input-Proses-Output (IPO)** yang mematuhi Perlembagaan AI NOSS Linux Malaysia.

---

## 📥 Fasa 1: Pengendalian Input (Input Intake)
1. **Kenal Pasti Punca Bahan:**
   - **Arkib Tempatan:** Periksa fail mentah di `references/manual/` atau `references/noss/`.
   - **Bahan Muat Naik Sesi:** Fail dokumen yang dibekalkan oleh pengguna dalam sesi interaktif.
   - **URL Luaran:** Kandungan dokumentasi rasmi melalui alat pembacaan web.
2. **Patuhi Rule 17 (Raw Archive Preservation):**
   - **DILARANG** memadam sebarang fail di `references/manual/`. Ia merupakan arkib kekal.
   - Bersihkan teks pengepala lama yang berulang secara memori tanpa merosakkan integriti fail asal di `references/`.

---

## ⚙️ Fasa 2: Pemprosesan & Transformasi (Core Processing)

Ejen AI MESTI memproses maklumat melalui 3 langkah teras:

1. **Penilaian Input & Pemetaan Silibus CU/WA:**
   - Baca dan nilai kandungan topik bahan input.
   - Petakan secara tepat kepada Unit Kompetensi NOSS (**CU01 hingga CU06**) dan nombor Aktiviti Kerja (**WA01 hingga WA07**).
2. **Penyelidikan Mendalam & Pengesahan Fakta Web (Deep Research):**
   - Ejen AI MESTI menjalankan carian web berautoriti (*deep research*) untuk mengesahkan:
     - Sintaks arahan CLI, pilihan bendera (*flags*), dan pakej perisian terkini.
     - Dokumentasi rasmi kernel Linux ([kernel.org](https://docs.kernel.org/)), [Ubuntu 26.04 Docs](https://ubuntu.com/server/docs), [AlmaLinux 10 Wiki](https://wiki.almalinux.org/), dan [systemd.io](https://systemd.io/).
     - Garis panduan keselamatan Jabatan Digital Negara (JDN) / MAMPU dan penanda aras CIS Benchmark.
     - Istilah rasmi Dewan Bahasa dan Pustaka (DBP).
   - **DILARANG** berhalusinasi atau mengekalkan konfigurasi lapuk yang tidak disahkan.
3. **Penguatkuasaan Piawaian Moden 2026 (Rule 15):**
   - Distribusi Desktop: **Ubuntu 26.04 LTS "Quetzal"** & **Fedora 43**.
   - Distribusi Pelayan / Enterprise: **AlmaLinux 10 "Purple Lion"** (alternatif: Rocky Linux 9).
   - Gantikan teknologi lapuk (MBR, ext2, sysvinit) dengan teknologi moden (GPT, LVM2, systemd, Btrfs/XFS/EXT4).
   - Sertakan panduan **Penyulitan LUKS2** (ISO/IEC 27001 & Pekeliling JDN/MAMPU).
4. **Penyepaduan Protokol Keselamatan & Penalaan Prestasi (Continuous Enrichment):**
   - **Keselamatan:** CIS Benchmark, kawalan integriti audit `auditd`, SSH hardening, perlindungan firewall (`ufw`/`firewalld`), dan pematuhan ISO/IEC 27001 & Pekeliling Jabatan Digital Negara (JDN) / MAMPU.
   - **Prestasi (*Performance Tuning*):** Penalaan parameter kernel `sysctl`, konfigurasi profil `tuned`, pemantauan eBPF/bpftrace, dan pengoptimuman I/O cakera serta rangkaian.
5. **Piawaian Bahasa Melayu Baku DBP (Rule 3):**
   - Gunakan Bahasa Melayu profesional, istilah teknikal standard DBP, dan biarkan sintaks CLI dalam Bahasa Inggeris standard.
6. **Pematuhan Format OKF v0.1 (Rule 8 & 16):**
   - Pastikan setiap nod bermula dengan YAML frontmatter lengkap (`okf_version: 0.1`, `type`, `title`, `timestamp`, `topics`, `tags`, `description`, `resource`).
   - Akhiri setiap nod dengan tiga seksyen penutup:
     - `## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)`
     - `## 🔗 Bahan Bacaan Lanjut (Rujukan URL)`
     - `## 📚 Buku Boleh Dibeli (Syor Bacaan)`
   - Akhiri dengan Sovereign Dual-License Footer rasmi.

---

## 📤 Fasa 3: Pengedaran Output & Penyegerakan (Output Distribution)

Ejen AI MESTI memastikan setiap hasil transformasi menyokong **4 Kuadran Diátaxis** dan bersedia dijana ke dalam pelbagai format:

1. **Pengagihan Mengikut Kuadran Diátaxis:**
   - **Tutorials (`docs/tutorials/`):** Panduan pembelajaran langkah demi langkah untuk pemula.
   - **How-To Guides (`docs/how-to/`):** Resipi penyelesaian masalah dan konfigurasi operasi khusus.
   - **Reference (`manual/cuXX/` & `docs/reference/`):** Spesifikasi teknikal, jadual NOSS, dan modul amali standard.
   - **Explanation (`openwiki/topic-XX-*.md` & `docs/explanation/`):** Huraian konsep mendalam, perbandingan teknologi, dan sejarah.

2. **Sokongan Pelbagai Format Output (Multi-Artifact Deliverables):**
   - **Markdown OKF v0.1:** Modul teks berdaulat di `manual/` dan `openwiki/`.
   - **Tapak Web Statik HTML:** Direktori `html/` dijana melalui `uv run scripts/serve_mkdocs.py --build-only`.
   - **Kurikulum Rasmi DOCX:** Menggunakan kemahiran `.agents/skills/noss-cocu-docx-formatter/` untuk menghasilkan matriks CoCU & TEM.
   - **Slaid Pembentangan PPTX/ODP:** Menggunakan `.agents/skills/odp-slide-generator/` untuk modul slaid TVET.
   - **Buku / Dokumen Cadangan PDF:** Menggunakan `.agents/skills/latex-proposal-compiler/`.
   - **Konteks AI / FastMCP:** Suapan `llms.txt`, `llms-full.txt`, dan pelayan FastMCP.
   - **Templat Pengeluaran DevOps:** Konfigurasi Nginx, Apache, Podman Quadlet, dan Ansible Playbook.

3. **Kemas Kini Memori Ruang Ejen:**
   - Kemas kini closet yang berkaitan di `.agents/brain/wings/` dan lejar di `.agents/brain/task.md`.

4. **Jana Semula Peta Memori & Laman Web:**
   ```bash
   uv run scripts/generate_palace_registry.py
   uv run scripts/serve_mkdocs.py --build-only
   ```

5. **Pengesahan 100% Quality Gate (Rule 12):**
   ```bash
   uv run run_all_tests.py
   ```

6. **Penjejakan & Penyegerakan GitOps (Rule 19):**
   ```bash
   git add -A && git commit -m "feat(manual): <huraian-transformasi>"
   git push origin main && git push github main
   ```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
