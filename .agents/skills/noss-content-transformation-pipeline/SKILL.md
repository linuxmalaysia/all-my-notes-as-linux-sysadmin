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
1. **Pemetaan Unit Kompetensi NOSS:**
   - Petakan kandungan kepada salah satu unit `CU01` hingga `CU06` dan `WA01` hingga `WA07`.
2. **Penguatkuasaan Piawaian Moden 2026 (Rule 15):**
   - Distribusi Desktop: **Ubuntu 26.04 LTS "Quetzal"** & **Fedora 43**.
   - Distribusi Pelayan / Enterprise: **AlmaLinux 10 "Purple Lion"** (alternatif: Rocky Linux 9).
   - Gantikan teknologi lapuk (MBR, ext2, sysvinit) dengan teknologi moden (GPT, LVM2, systemd, Btrfs/XFS/EXT4).
   - Sertakan panduan **Penyulitan LUKS2** (ISO/IEC 27001 & MAMPU).
3. **Piawaian Bahasa Melayu Baku DBP (Rule 3):**
   - Gunakan Bahasa Melayu profesional, istilah teknikal standard DBP, dan biarkan sintaks CLI dalam Bahasa Inggeris standard.
4. **Pematuhan Format OKF v0.1 (Rule 8):**
   - Pastikan setiap nod bermula dengan YAML frontmatter lengkap (`okf_version: 0.1`, `type`, `title`, `timestamp`, `topics`, `tags`, `description`, `resource`).
   - Akhiri setiap nod dengan tiga seksyen penutup (Rule 16):
     - `## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)`
     - `## 🔗 Bahan Bacaan Lanjut (Rujukan URL)`
     - `## 📚 Buku Boleh Dibeli (Syor Bacaan)`
   - Akhiri dengan Sovereign Dual-License Footer rasmi.

---

## 📤 Fasa 3: Pengedaran Output & Penyegerakan (Output Distribution)
1. **Simpan ke Direktori Sasaran:**
   - Manual Amali: `manual/cuXX/nama-fail.md`
   - Indeks Naratif Silibus: `openwiki/topic-XX-*.md`
2. **Kemas Kini Memori Ruang Ejen:**
   - Kemas kini closet yang berkaitan di `.agents/brain/wings/` dan lejar di `.agents/brain/task.md`.
3. **Jana Semula Peta Memori & Laman Web:**
   ```bash
   uv run scripts/generate_palace_registry.py
   uv run scripts/serve_mkdocs.py --build-only
   ```
4. **Pengesahan 100% Quality Gate (Rule 12):**
   ```bash
   uv run run_all_tests.py
   ```
5. **Penjejakan & Penyegerakan GitOps (Rule 19):**
   ```bash
   git add -A && git commit -m "feat(manual): <huraian-transformasi>"
   git push origin main && git push github main
   ```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
