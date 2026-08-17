# 🤝 Taklimat Penyerahan Sesi: Google Antigravity ➔ Google Jules

**Tarikh:** 2026-08-17 | **Kerangka:** Deep State of Mind (DSOM v0.1)  
**Topik Utama:** Fasa 7: Migrasi & Pemodenan Silibus Bab 7 (Penyunting Teks Terminal, Persekitaran Shell & Konfigurasi Sistem - CU01, CU03, & CU06)

---

## 🏛️ Konteks & Mandat Operasi Jules
Hai Jules! Anda bertindak sebagai **Pakar Pentadbir Sistem Linux & Pendidik NOSS**, menjiwai falsafah kedaulatan digital dan kepakaran **Harisfazillah Jamel (LinuxMalaysia)** di bawah kerangka Deep State of Mind (DSOM v0.1).

### Status Repositori Terkini:
- Fasa 1–6 kurikulum NOSS (CU01–CU06) telah selesai dimodenkan sepenuhnya.
- 982 ujian Python pytest & 38 ujian JavaScript Jest melepasi 100% Quality Gate.
- Piawaian edaran rasmi 2026: **Ubuntu 26.04 LTS "Resolute Raccoon"** (Desktop/Latihan), **Fedora 43** (Bleeding-edge), dan **AlmaLinux 10 "Purple Lion"** (Enterprise Server).

---

## 🎯 Tugasan Utama Fasa 7 (Migrasi Bab 7)

### 1. Sumber Mentah:
- Arkib rujukan: `references/manual/bab_07/part_01.md` dan `part_02.md`.
- Topik mentah: Penggunaan editor teks terminal (GNU Emacs, XEmacs, VIM, Pico/Nano), konfigurasi pemboleh ubah persekitaran `$EDITOR`, dan fail konfigurasi pengguna (`~/.bashrc`, `/etc/profile`).

### 2. Modul Sasaran:
- **`manual/cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md`**:
  - Perkayakan bahagian editor teks terminal dengan perbandingan mendalam dan amali praktikal bagi **Vim/Neovim** (mod navigasi, mod sisipan, mod visual, operasi regex `%s/asal/ganti/g`, makro) dan **GNU Nano** (pintasan `Ctrl+O`, `Ctrl+X`, `Ctrl+W`, konfigurasi sintaks `~/.nanorc`).
  - Sertakan prosedur keselamatan penyuntingan fail konfigurasi kritikal sistem (`sudoedit`, `visudo`, pengesahan sintaks sebelum simpan).
- **`manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md`** & **`manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md`**:
  - Panduan penyesuaian pemboleh ubah persekitaran `$EDITOR` dan `$VISUAL` dalam `/etc/environment` dan `~/.bashrc`.
- **`openwiki/topic-06-troubleshooting-and-logs.md`** & **`openwiki/topic-01-linux-desktop-and-basics.md`**:
  - Sintesis perbandingan editor teks Linux (Vim vs Nano vs Emacs) serta amalan pengurusan fail konfigurasi sistem.
- **Kemahiran AI Ejen (`.agents/skills/`)**:
  - Kemas kini `.agents/skills/cu06-wa07-resolve-system-anomalies-and-document-rca/SKILL.md` bagi merangkumi keupayaan penyuntingan teks terminal lanjutan.

---

## 🛠️ Garis Panduan Kualiti Mandatori (Quality Invariants)
1. **Frontmatter OKF v0.1 & Pengaki Berdaulat:** Setiap fail markdown yang diubah suai mesti bermula dengan YAML frontmatter OKF v0.1 dan diakhiri dengan pengaki dwi-lesen rasmi berserta pautan `[Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)`.
2. **Struktur Penutup Wajib (Rule 16):** Pastikan indeks topik merangkumi AI Prompts, Bahan Bacaan Lanjut, dan Syor Buku Boleh Dibeli.
3. **Dynamic Timestamp Validation:** Jangan gunakan cap masa statik dalam ujian baharu. Gunakan regex format ISO-8601.
4. **100% Quality Gate Verification:** Sebelum komit/PR:
   - `uv run scripts/generate_palace_registry.py`
   - `uv run scripts/generate_llms_txt.py && uv run scripts/llms_to_xml.py`
   - `uv run scripts/serve_mkdocs.py --build-only`
   - `uv run run_all_tests.py` (Mesti lulus 100%).
