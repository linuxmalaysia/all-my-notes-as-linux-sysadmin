# 📋 Implementation Plan: Fasa 7 (Migrasi & Pemodenan Bab 7 - Penyunting Teks Terminal, Persekitaran Shell & Konfigurasi Sistem)

## 🎯 Objektif & Rasional
Memproses bahan mentah daripada `references/manual/bab_07/` (merangkumi editor teks terminal seperti GNU Emacs, Vim, Pico/Nano, pemboleh ubah persekitaran `$EDITOR`, dan penyesuaian profil shell `.bashrc`/`/etc/profile`) untuk diserapkan secara modular dan moden ke dalam **Sovereign Manual NOSS Linux (CU01, CU03, & CU06)** dan **OpenWiki**, serta menaik taraf kemahiran AI berkaitan.

---

## 🏛️ Pemetaan Silibus NOSS & Penstrukturan Modul

1. **Modul Amali Sovereign Manual (`manual/`):**
   - **`manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md`**: Perkayakan seksyen penyunting teks terminal dengan panduan mendalam Vim (mod arahan, mod sisipan, mod visual, carian/penggantian regex `%s/old/new/g`), Nano (pintasan papan kekunci, konfigurasi `.nanorc`), dan amalan terbaik penyuntingan fail konfigurasi selamat (`visudo`, `sudoedit`).
   - **`manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md`** & **`manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md`**: Masukkan panduan konfigurasi pemboleh ubah persekitaran shell global/pengguna (`$EDITOR`, `$VISUAL`, `/etc/environment`, `~/.bashrc`).

2. **Pangkalan Rujukan OpenWiki (`openwiki/`):**
   - **`openwiki/topic-06-troubleshooting-and-logs.md`** & **`openwiki/topic-01-linux-desktop-and-basics.md`**: Kemas kini dengan sintesis perbandingan penyunting teks (Vim vs Nano vs Emacs), falsafah reka bentuk mod terminal, pengurusan penimbal (*buffers*), dan automasi penyuntingan.

3. **Kemahiran AI Ejen (`.agents/skills/`):**
   - Kemas kini/perkukuh `.agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md` dengan arahan mendalam penyuntingan Vim/Nano.
   - Jana semula Palace Registry dengan `uv run scripts/generate_palace_registry.py`.

4. **Jaminan Kualiti & Ujian (`tests/`):**
   - Tambah/kemas kini suite ujian pengesahan kandungan Bab 7.
   - Jalankan `uv run run_all_tests.py` bagi memastikan 100% kelulusan (pytest + jest).

---

## 🚀 Langkah Pelaksanaan Jules
1. Kaji teks mentah di `references/manual/bab_07/part_01.md` dan `part_02.md`.
2. Kemas kini modul amali di `manual/cu06/` dan `openwiki/` dengan standard Linux 2026 (Ubuntu 26.04 LTS Resolute Raccoon, Fedora 43, AlmaLinux 10).
3. Pastikan frontmatter OKF v0.1 dan pengaki dwi-lesen berdaulat lengkap pada setiap nod.
4. Bina semula tapak web statik dengan `uv run scripts/serve_mkdocs.py --build-only`.
5. Sahkan 100% Quality Gate dengan `uv run run_all_tests.py`.
