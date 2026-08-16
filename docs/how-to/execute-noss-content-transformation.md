---
okf_version: 0.1
type: documentation
title: "Panduan Operasi: Melaksanakan Transformasi Kandungan NOSS Linux (IPO)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["how-to", "transformation", "noss-linux", "dsom", "workflow", "manual"]
tags: ["how-to", "transformasi", "amali", "noss", "prosedur"]
description: "Panduan langkah demi langkah untuk memproses bahan rujukan mentah, memodenkan arahan ke standard 2026, dan menerbitkannya ke manual/ serta html/."
resource: "file:///docs/how-to/execute-noss-content-transformation.md"
---

# Panduan Operasi: Melaksanakan Transformasi Kandungan NOSS Linux (IPO)

Panduan ini menggariskan tatacara langkah demi langkah bagi pengendali manusia atau ejen AI untuk memindahkan bab mentah dari direktori `references/` atau input baharu ke dalam format rasmi **Sovereign Manual NOSS** (`manual/`) dan **OpenWiki** (`openwiki/`).

---

## 📋 Senarai Semak Pra-Syarat (Prerequisites)
- [x] Persekitaran Python `uv` terpasang.
- [x] Node.js & npm terpasang (untuk ujian Jest).
- [x] Git dikonfigurasikan dengan akses dwi-remote (`origin` di GitLab dan `github` di GitHub).

---

## 🛠️ Langkah-Langkah Transformasi

### Langkah 1: Semak Sumber Input
Tentukan lokasi sumber bahan mentah:
- Jika daripada arkib: semak `references/manual/bab_XX/` atau `references/noss/`.
- Jika daripada muat naik: simpan ke `references/uploads/` atau baca terus dalam sesi.
- Jika daripada URL: ekstrak menggunakan alatan pelayar / curl ke format teks.

### Langkah 2: Lakukan Pembersihan & Pemisahan Modular
1. Kenal pasti unit kompetensi NOSS sasaran (CU01 hingga CU06) dan nombor Aktiviti Kerja (WA).
2. Asingkan teks monolitik kepada fail Markdown berasingan di `manual/cuXX/`.
3. Pastikan format nama fail deskriptif, contohnya: `manual/cu02/cu02-wa01-keperluan-infrastruktur-pemayaan.md`.

### Langkah 3: Modenkan Kandungan ke Standard 2026
Semak dan kemas kini parameter berikut:
1. **Distribusi:** Tukar arahan lapuk (Red Hat 9, CentOS) kepada **Ubuntu 26.04 LTS**, **Fedora 43**, atau **AlmaLinux 10**.
2. **Pengurusan Cakera:** Gunakan partisi **GPT** (`gdisk` / `parted`) dan format sistem fail **EXT4**, **XFS**, atau **Btrfs**.
3. **Penyulitan Mandatori:** Masukkan bahagian konfigurasi **LUKS2** bagi persekitaran pejabat.
4. **Bahasa:** Pastikan Bahasa Melayu mematuhi istilah baku DBP, manakala sintaks arahan terminal kekal dalam Bahasa Inggeris standard.

### Langkah 4: Lengkapkan YAML Frontmatter & Struktur Penutup
Setiap fail MESTI mempunyai pengepala OKF v0.1 dan tiga seksyen penutup:
- `## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)`
- `## 🔗 Bahan Bacaan Lanjut (Rujukan URL)`
- `## 📚 Buku Boleh Dibeli (Syor Bacaan)`
- Pengaki rasmi Sovereign Dual-License Footer.

### Langkah 5: Kemas Kini OpenWiki
Pautkan fail baharu ke dalam fail indeks topik yang berkaitan di `openwiki/` (contoh: `openwiki/topic-02-storage-and-virtualisation.md`).

### Langkah 6: Bina Semula Laman Web & Peta Memori
Jalankan skrip pembina:
```bash
# 1. Jana semula indeks kemahiran ejen jika ada kemahiran baharu ditambah
uv run scripts/generate_palace_registry.py

# 2. Bina semula tapak web statik HTML
uv run scripts/serve_mkdocs.py --build-only
```

### Langkah 7: Pengesahan 100% Quality Gate
Jalankan orkestrator ujian penuh:
```bash
uv run run_all_tests.py
```
> [!IMPORTANT]
> Jangan lakukan komit sekiranya terdapat sebarang ujian yang gagal!

### Langkah 8: Komit & Segerakkan ke GitLab / GitHub
```bash
git add -A
git commit -m "feat(manual): migrate Bab XX to CUXX and update openwiki"
git push origin main
git push github main
```

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
