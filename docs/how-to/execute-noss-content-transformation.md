---
okf_version: 0.2
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

### Langkah 1: Penilaian Sumber Input & Pemetaan CU/WA
1. Tentukan lokasi sumber bahan (arkib `references/`, muat naik sesi, atau pautan URL).
2. Baca dan nilai kandungan untuk memadankannya secara tepat kepada Unit Kompetensi NOSS (**CU01–CU06**) dan Aktiviti Kerja (**WA01–WA07**).
3. Asingkan teks kepada struktur nod modular di `manual/cuXX/` (contoh: `manual/cu02/cu02-wa01-keperluan-infrastruktur-pemayaan.md`).

### Langkah 2: Penyelidikan Mendalam & Pengesahan Fakta (Deep Web Research)
Lakukan carian web berautoriti untuk mengesahkan kesahihan teknikal:
1. **Rujukan Rasmi:** Semak dokumentasi terkini [Ubuntu Docs](https://ubuntu.com/server/docs), [AlmaLinux Wiki](https://wiki.almalinux.org/), [Kernel.org](https://docs.kernel.org/), dan [systemd.io](https://systemd.io/).
2. **Piawaian Keselamatan:** Semak CIS Benchmark dan Pekeliling Am Jabatan Digital Negara (JDN) / MAMPU bagi keperluan penyulitan LUKS2 dan pengerasan SSH/Firewall.
3. **Piawaian Istilah DBP:** Semak istilah teknikal melalui Pusat Rujukan Persuratan Melayu (PRPM DBP).

### Langkah 3: Modenkan Kandungan ke Standard 2026
Semak dan kemas kini parameter berikut:
1. **Distribusi Kanonik:** Gantikan versi lapuk dengan **Ubuntu 26.04 LTS "Resolute Raccoon"**, **Fedora 43**, atau **AlmaLinux 10 "Purple Lion"**.
2. **Pengurusan Cakera & Storan:** Gunakan partisi **GPT** (`gdisk` / `parted`), pengurusan volum **LVM2**, dan format sistem fail **EXT4**, **XFS**, atau **Btrfs**.
3. **Penyulitan Mandatori:** Sertakan prosedur **LUKS2** bagi persekitaran pejabat/perusahaan.
4. **Bahasa:** Pastikan teks penjelasan menggunakan Bahasa Melayu baku DBP, manakala sintaks arahan terminal kekal dalam Bahasa Inggeris standard.

### Langkah 4: Lengkapkan YAML Frontmatter OKF v0.2 & Struktur Penutup
Setiap fail MESTI mempunyai pengepala OKF v0.2 dan tiga seksyen penutup:
- `## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)`
- `## 🔗 Bahan Bacaan Lanjut (Rujukan URL)`
- `## 📚 Buku Boleh Dibeli (Syor Bacaan)`
- Pengaki rasmi Sovereign Dual-License Footer.

### Langkah 5: Kemas Kini Hab Rujukan Setempat OpenWiki & Manual
Pautkan fail baharu ke dalam `openwiki/topic-XX-*.md` dan kemas kini `manual/cuXX/index.md` serta `manual/index.md`.

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
