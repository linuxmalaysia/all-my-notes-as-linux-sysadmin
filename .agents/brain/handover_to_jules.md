# 🤝 Taklimat Penyerahan Sesi: Google Antigravity ➔ Google Jules

**Tarikh:** 2026-08-17 | **Kerangka:** Deep State of Mind (DSOM v0.1)  
**Topik Utama:** Fasa 8 SELESAI ✅ ➔ Fasa 9: Migrasi & Pemodenan Silibus Bab 9

---

## 🏛️ Konteks & Mandat Operasi Jules
Hai Jules! Anda bertindak sebagai **Pakar Pentadbir Sistem Linux & Pendidik NOSS**, menjiwai falsafah kedaulatan digital dan kepakaran **Harisfazillah Jamel (LinuxMalaysia)** di bawah kerangka Deep State of Mind (DSOM v0.1).

### Status Repositori Terkini:
- Fasa 1–8 kurikulum NOSS (CU01–CU06) telah selesai dimodenkan sepenuhnya.
- Rule 32.43 (Ansible Validation Ladder) & Rule 32.44 (Red Hat CoP Standards) telah dikuatkuasakan di `AGENTS.md` & `.agents/AGENTS.md`.
- 2,322 ujian Python pytest & 38 ujian JavaScript Jest melepasi 100% Quality Gate.
- Piawaian edaran rasmi 2026: **Ubuntu 26.04 LTS "Resolute Raccoon"** (Desktop/Latihan), **Fedora 43** (Bleeding-edge), dan **AlmaLinux 10 "Purple Lion"** (Enterprise Server).

---

## 🛠️ Garis Panduan Kualiti Mandatori (Quality Invariants)
1. **Frontmatter OKF v0.1 & Pengaki Berdaulat:** Setiap fail markdown yang diubah suai mesti bermula dengan YAML frontmatter OKF v0.1 dan diakhiri dengan pengaki dwi-lesen rasmi berserta pautan `[Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)`.
2. **Struktur Penutup Wajib (Rule 16):** Pastikan indeks topik merangkumi AI Prompts, Bahan Bacaan Lanjut, dan Syor Buku Boleh Dibeli.
3. **Dynamic Timestamp Validation:** Jangan gunakan cap masa statik dalam ujian baharu. Gunakan regex format ISO-8601.
4. **100% Quality Gate Verification:** Sebelum komit/PR:
   - `uv run scripts/generate_palace_registry.py`
   - `uv run scripts/generate_llms_txt.py && uv run scripts/llms_to_xml.py`
   - `uv run scripts/serve_mkdocs.py --build-only`
   - `uv run --with pytest --with pyyaml --with pytest-cov --with defusedxml python run_all_tests.py` (Mesti lulus 100%).
