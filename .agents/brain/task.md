# 📋 NOSS Linux Malaysia - Master Task Tracker

## 🌟 Milestone Status: Fasa 1 & Fasa 2 (Penstrukturan Semula Seni Bina DSOM & Silibus Manual) - SELESAI ✅
- [x] **Penstrukturan Semula Direktori Punca `manual/`:**
  - Pengasingan modul amali silibus NOSS (CU01–CU06) daripada Memori Ruang Ejen ke dalam folder `manual/`.
  - Penjanaan rangka nod draf lengkap berformat OKF v0.1 untuk kesemua Aktiviti Kerja (WA01–WA07) bagi CU01 hingga CU06.
- [x] **Pembinaan Semula DSOM Spatial Memory Palace (`.agents/brain/wings/`):**
  - Penyusunan Sayap `wing_dsom_core` (`hall_facts`, `hall_events`, `hall_discoveries`) dan `wing_noss_linux` (`hall_curriculum`, `hall_governance`).
  - Penjanaan Master Palace Registry di `.agents/brain/palace_registry.md`.
- [x] **Penguatkuasaan 4 Kuadran Diátaxis & Hab Rujukan Setempat:**
  - Pewujudan pusat rujukan sehenti di `manual/index.md` dan `openwiki/index.md`.
  - Penstrukturan navigasi web `mkdocs.yml` mengikut 4 kuadran Diátaxis rasmi.
  - Dokumentasi seni bina IPO (`docs/explanation/workflow-input-process-output.md`) dan panduan amali (`docs/how-to/execute-noss-content-transformation.md`).
  - Kemahiran Ejen AI: `noss-content-transformation-pipeline` (`.agents/skills/noss-content-transformation-pipeline/SKILL.md`).
- [x] **Pemaktuban Peraturan 21 Perlembagaan AI & Penjajaran JDN:**
  - Penilaian & Pemetaan Silibus CU/WA.
  - Penyelidikan Mendalam (*Deep Web Research*) untuk data terkini 2026.
  - Pengayaan berterusan protokol keselamatan (**Jabatan Digital Negara (JDN) / MAMPU**, ISO/IEC 27001, CIS Benchmarks) dan penalaan prestasi (`sysctl`, `tuned`, eBPF).
  - 100% Quality Gate tercapai (810/810 Python tests, 38/38 Jest tests).

---

## 🎯 Roadmap Fasa Seterusnya untuk Google Jules
- [ ] **Fasa 1: Audit & Semakan Semula Bab 1 & Bab 2 (manual/cu01/):**
  - [ ] Sahkan pematuhan penuh Bab 1 & 2 kepada proses IPO dan Peraturan 21.
  - [ ] Port/kemas kini modul ilmu yang telah siap kepada AI Agent Skills di `.agents/skills/` (khususnya `cu01-wa05` pemacu/aplikasi dan `cu01-wa06` rangkaian endpoint).
- [ ] **Fasa 2: Migrasi Silibus Bab 3 (Pengurusan Storan, Partisi & Sistem Fail):**
  - [ ] Ekstrak dan modenkan kandungan amali dari `references/manual/bab_03/` ke `manual/cu02/` (Partisi GPT/fdisk/parted, LVM2, EXT4, XFS, Btrfs).
  - [ ] Tukar kandungan Bab 3 kepada kemahiran AI CU02 (`cu02-wa01` hingga `cu02-wa04`).
  - [ ] Kemas kini `openwiki/topic-02-storage-and-virtualisation.md`.
- [ ] **Fasa 3: Kemas Kini Indeks Palace & Quality Gate (Rule 8, 12, 18):**
  - [ ] `uv run scripts/generate_palace_registry.py`
  - [ ] `uv run scripts/serve_mkdocs.py --build-only`
  - [ ] `uv run run_all_tests.py`
  - [ ] Komit dan penolakan dwi-remote ke GitLab (`origin`) dan GitHub (`github`).
