# 📐 Pelan Pelaksanaan Sesi Jules: Migrasi Bab 2 (Pemasangan Sistem Operasi Linux)

## 1. Objektif Utama
Memindahkan, memodenkan, dan memetakan kandungan arkib manual lama Bab 2 (`references/manual/bab_02/`) ke dalam struktur **Sovereign Markdown Palace (`palace/cu01/`)** dan **OpenWiki (`openwiki/topic-01-linux-desktop-and-basics.md`)** berlandaskan standard NOSS Level 3 dan edaran Linux moden 2026.

---

## 2. Garis Panduan Transformasi & Pematuhan Perlembagaan AI

### A. Piawaian Edaran Linux (Rule 15)
- **Rujukan Desktop/Latihan:** Ubuntu 26.04 LTS "Quetzal" (Isirung 6.14 LTS, GNOME 48).
- **Rujukan Bleeding-Edge:** Fedora 43.
- **Rujukan Pelayan Perusahaan:** AlmaLinux 10 "Purple Lion" (Isirung 6.12 LTS, GNOME 47).
- *Jangan gunakan edaran lapuk:* Red Hat 9 (era 2003), CentOS 7/8, Mandrake.

### B. Keperluan Penyulitan Pejabat (Rule 15)
- Sertakan panduan konfigurasi **Penyulitan Cakera Penuh (Full Disk Encryption) LUKS2** dengan pengurusan berbilang kunci pengguna (*multi-user LUKS slots*) untuk pematuhan **ISO/IEC 27001** dan **Pekeliling Am MAMPU**.

### C. Struktur Penutup Bab Silibus (Rule 16)
Setiap fail indeks topik wajib mengandungi:
1. `## Eksplorasi Lanjut bersama AI (AI Prompts)` (Minimum 3 prompt amali).
2. `## Bahan Bacaan Lanjut (Rujukan URL)` (Pautan rasmi).
3. `## Buku Boleh Dibeli (Syor Bacaan)` (Buku berkaitan dalam Bahasa Melayu/Inggeris).

### D. Format OKF v0.1 & Sovereign Footer (Rule 8)
- Setiap fail `.md` baharu wajib mempunyai pengepala YAML OKF v0.1 dan pengaki dwi-lesen rasmi berserta pautan notis perundangan.

---

## 3. Langkah-Langkah Operasi untuk Jules:
1. **Analisis Bahan Mentah:** Baca fail-fail di `references/manual/bab_02/` (jangan padam fail mentah - Rule 17).
2. **Bina Nod Memori Palace (`palace/cu01/`):**
   - `palace/cu01/keperluan-perkakasan-dan-bios-uefi.md`
   - `palace/cu01/prosedur-pemasangan-ubuntu-almalinux.md`
   - `palace/cu01/penyulitan-cakera-luks2-pejabat.md`
   - `palace/cu01/pasca-pemasangan-dan-driver.md`
3. **Kemas Kini Indeks OpenWiki:** Kemas kini `openwiki/topic-01-linux-desktop-and-basics.md` dengan pautan ke nod-nod baharu.
4. **Bina Semula Laman Web Statik:** Jalankan `uv run scripts/serve_mkdocs.py --build-only` untuk menjana HTML ke `html/`.
5. **Quality Gate (Rule 12):** Jalankan `uv run run_all_tests.py` sehingga 100% lulus.
6. **Git Commit & Dual Push (Rule 19):** Komit perubahan dan tolak ke `origin` (GitLab) dan `github` (GitHub).
