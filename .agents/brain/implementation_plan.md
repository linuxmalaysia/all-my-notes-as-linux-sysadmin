# 📐 Pelan Pelaksanaan Google Jules: Migrasi Silibus Bab 3 (Pengurusan Storan, Partisi & Sistem Fail ke manual/cu02/)

## 1. Objektif Utama
Memindahkan, memodenkan, menyelidik secara mendalam (*Deep Web Research*), dan memetakan kandungan arkib manual lama **Bab 3 (`references/manual/bab_03/`)** ke dalam direktori **`manual/cu02/`** dan **`openwiki/topic-02-storage-and-virtualisation.md`** berlandaskan standard **NOSS Level 3 (CU02 - Storan & Hipervisor Pemayaan)**, piawaian kanonik Linux 2026, 4 kuadran Diátaxis, dan arahan keselamatan **Jabatan Digital Negara (JDN) / MAMPU**.

---

## 2. Garis Panduan Transformasi & Pematuhan Perlembagaan AI

### A. Kitaran Mandatori Peraturan 21 (Deep Research & CU/WA Mapping)
1. **Penilaian Silibus:** Memetakan bahan partisi, sistem fail, dan pengurusan volum kepada:
   - `CU02-WA01`: Keperluan Infrastruktur Pemayaan & Storan.
   - `CU02-WA02` hingga `CU02-WA04`: Pengurusan storan bare-metal, partisi, volum maya, dan sandaran fail.
2. **Penyelidikan Mendalam (*Deep Web Research*):**
   - Rujuk dokumentasi rasmi kernel Linux ([kernel.org](https://docs.kernel.org/)), [Ubuntu 26.04 Docs](https://ubuntu.com/server/docs), [AlmaLinux 10 Wiki](https://wiki.almalinux.org/), [systemd.io](https://systemd.io/), dan PRPM DBP.
   - Sahkan sintaks arahan CLI terkini (`parted`, `gdisk`, `lsblk`, `pvcreate`, `vgcreate`, `lvcreate`, `mkfs.ext4`, `mkfs.xfs`, `mkfs.btrfs`, `cryptsetup`).
3. **Pengayaan Keselamatan & Penalaan Prestasi:**
   - Masukkan prosedur penyulitan volum storan menggunakan **LUKS2** (ISO/IEC 27001 & JDN/MAMPU).
   - Penalaan I/O cakera, scheduler (`bfq`/`none` untuk NVMe), dan parameter kernel `sysctl` (`vm.dirty_ratio`, `vm.dirty_background_ratio`).
4. **Penyusunan Output Terstruktur:**
   - Hasilkan nod modular di `manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md` dan kemas kini nod WA berkaitan di `manual/cu02/`.

### B. Piawaian Edaran Linux Moden 2026 (Rule 15)
- **Rujukan Desktop/Latihan:** Ubuntu 26.04 LTS "Quetzal" (Isirung 6.14 LTS, GNOME 48).
- **Rujukan Bleeding-Edge:** Fedora 43.
- **Rujukan Pelayan Perusahaan:** AlmaLinux 10 "Purple Lion" (Isirung 6.12 LTS, GNOME 47) / Rocky Linux 9.
- *JANGAN gunakan edaran lapuk:* Red Hat 9 (era 2003), CentOS 7/8, Mandrake.

### C. Pemuliharaan Arkib Mentah (Rule 17)
- **DILARANG MEMADAM** sebarang fail di `references/manual/bab_03/`. Arkib kekal terpelihara.

### D. Struktur Penutup Wajib & Footer (Rule 8 & 16)
Setiap nod Markdown baharu mesti mematuhi skema OKF v0.1 dan ditutup dengan:
- `## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)` (Minimum 3 prompt berfokus).
- `## 🔗 Bahan Bacaan Lanjut (Rujukan URL)` (Pautan rasmi).
- `## 📚 Buku Boleh Dibeli (Syor Bacaan)` (Buku Bahasa Melayu/Inggeris berkaitan).
- Pengaki rasmi Sovereign Dual-License Footer dengan pautan Notis Perundangan.

---

## 3. Langkah Operasi Langkah Demi Langkah untuk Jules

```bash
# 1. Baca arkib mentah Bab 3
# references/manual/bab_03/ (fdisk, partisi, filesystem, lvm, quota)

# 2. Tulis nod amali moden ke manual/cu02/
# manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md
# Kemas kini manual/cu02/index.md

# 3. Pautkan ke OpenWiki
# openwiki/topic-02-storage-and-virtualisation.md

# 4. Jana indeks suapan konteks AI
uv run scripts/generate_llms_txt.py
uv run scripts/llms_to_xml.py

# 5. Bina tapak web statik HTML
uv run scripts/serve_mkdocs.py --build-only

# 6. Jalankan Quality Gate (100% Wajib Lulus)
uv run run_all_tests.py

# 7. Komit dan tolak ke kedua-dua remote
git add -A
git commit -m "feat(manual): migrate Bab 3 storage and file systems to manual/cu02"
git push origin main
git push github main
```
