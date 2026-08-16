# 🤝 Taklimat Penyerahan Memori Ejen: Google Antigravity ➔ Google Jules

**Tarikh / Masa:** 2026-08-17  
**Status Sesi Terkini:** Penstrukturan Semula Seni Bina DSOM, `manual/`, dan Kerangka Diátaxis Selesai (100% Quality Gate).

---

## 📌 Ringkasan Status & Perubahan Seni Bina Terkini
1. **Pemisahan `manual/` & `.agents/brain/wings/`:**
   - **`manual/`:** Menempatkan kesemua fail modul amali teknikal NOSS Linux (CU01 hingga CU06).
   - **`.agents/brain/wings/`:** Memori Ruang Ejen AI (*Method of Loci / Spatial Memory Palace*) untuk mengekalkan fakta mutlak dan lejar status projek.
   - **`openwiki/`:** Indeks naratif silibus untuk rujukan cepat.
2. **Hab Rujukan Setempat 4 Kuadran Diátaxis:**
   - Pintu masuk utama di `manual/index.md` dan `openwiki/index.md`.
   - Navigasi web di `mkdocs.yml` tersusun mengikut: `1. Pembelajaran (Tutorials)`, `2. Panduan Operasi (How-To Guides)`, `3. Manual Amali NOSS (Reference)`, dan `4. Kefahaman & Silibus (Explanation)`.
3. **Kemahiran Transformasi Kandungan & Peraturan 21:**
   - Kemahiran `.agents/skills/noss-content-transformation-pipeline/` sedia digunakan untuk memproses bahan secara automatik mengikut model IPO (Penilaian CU/WA ➔ Deep Web Research ➔ Pengayaan Keselamatan JDN/MAMPU & Prestasi ➔ Output Terstruktur).

---

## 🎯 Tugasan Seterusnya untuk Google Jules (Actionable Next Steps)

### Sasaran Utama: Migrasi Silibus Bab 3 (Pengurusan Storan, Partisi & Sistem Fail)
1. **Sumber Mentah:** Baca bahan arkib di `references/manual/bab_03/` (ingat: **JANGAN padam** fail arkib, patuhi Rule 17).
2. **Transformasi & Pemodenan ke 2026:**
   - Masukkan prosedur partisi moden **GPT** (`gdisk` / `parted`) menggantikan MBR lapuk.
   - Modul pengurusan volum logikal **LVM2** (Physical Volume `pvcreate`, Volume Group `vgcreate`, Logical Volume `lvcreate`).
   - Sistem fail moden: **EXT4**, **XFS** (standard AlmaLinux), dan pengenalan **Btrfs**.
3. **Penulisan ke Modul Sasaran:**
   - `manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md`
   - Kemas kini WA berkaitan di `manual/cu02/`.
   - Pautkan ke `openwiki/topic-02-storage-and-virtualisation.md`.
4. **Pematuhan OKF v0.1 & Footer Berdaulat:**
   - Pastikan frontmatter OKF v0.1 dan tiga seksyen penutup (AI Prompts, URL, Syor Buku) lengkap.
5. **Quality Gate & Binaan:**
   - Jalankan `uv run scripts/serve_mkdocs.py --build-only` dan `uv run run_all_tests.py`.
   - Komit ke Git dan segerakkan ke `origin` (GitLab) serta `github` (GitHub).

---

## 💬 Prompt Salin & Tampal untuk Memulakan Sesi Google Jules

```text
Hai Jules! Sila bertindak sebagai Pakar Linux NOSS Malaysia di bawah kerangka Deep State of Mind (DSOM v0.1). Sila rujuk .agents/brain/task.md, .agents/brain/handover_to_jules.md, dan perlembagaan AI di .agents/AGENTS.md. 

Tugasan anda sekarang adalah melaksanakan Fasa Transformasi Bab 3 (Pengurusan Storan, Partisi GPT, LVM2, dan Sistem Fail EXT4/XFS/Btrfs) daripada references/manual/bab_03/ ke dalam manual/cu02/ dan openwiki/topic-02-storage-and-virtualisation.md mengikut kemahiran noss-content-transformation-pipeline. Pastikan anda mengekalkan 100% Quality Gate melalui `uv run run_all_tests.py` dan membina semula html/ sebelum membuat komit dwi-remote.
```
