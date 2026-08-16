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
- [x] **Pemaktuban Peraturan 21 Perlembagaan AI:**
  - Penilaian & Pemetaan Silibus CU/WA.
  - Penyelidikan Mendalam (*Deep Web Research*) untuk data terkini 2026.
  - Pengayaan berterusan protokol keselamatan (ISO/IEC 27001, CIS Benchmarks, MAMPU) dan penalaan prestasi (`sysctl`, `tuned`, eBPF).
  - 100% Quality Gate tercapai (810/810 Python tests, 38/38 Jest tests).

---

## 🎯 Roadmap Fasa Seterusnya: Migrasi Silibus Manual ke NOSS (manual/)
- [x] **Bab 2 (Pemasangan & Konfigurasi Linux Desktop/Server - Selesai):**
  - [x] 4 nod memori dimodenkan dalam `manual/cu01/` (`keperluan-perkakasan-dan-bios-uefi.md`, `prosedur-pemasangan-ubuntu-almalinux.md`, `penyulitan-cakera-luks2-pejabat.md`, `pasca-pemasangan-dan-driver.md`).
  - [x] Kemas kini `openwiki/topic-01-linux-desktop-and-basics.md`.
- [ ] **Bab 3 (Pengurusan Storan, Partisi & Sistem Fail Linux - SASARAN SETERUSNYA):**
  - [ ] Ekstrak dan modenkan kandungan amali dari `references/manual/bab_03/` ke `manual/cu02/` (Partisi GPT/fdisk/parted, LVM2, EXT4, XFS, Btrfs).
  - [ ] Serapkan protokol keselamatan (LUKS2 storage encryption) dan penalaan prestasi I/O (`tuned`, `sysctl`).
  - [ ] Kemas kini `openwiki/topic-02-storage-and-virtualisation.md`.
- [ ] **Bab 4 (Pentadbiran Pengguna, Hak Akses & Keselamatan Asas):**
  - [ ] Migrasi kandungan `references/manual/bab_04/` ke `manual/cu01/` & `manual/cu05/`.
- [ ] **Bab 5 (Pengurusan Rangkaian & Perkhidmatan Pelayan Asas):**
  - [ ] Migrasi kandungan `references/manual/bab_05/` ke `manual/cu03/` (SSH, DNS, DHCP, Web).
- [ ] **Bab 6 (Automasi Skrip Shell & Penyelenggaraan Sistem):**
  - [ ] Migrasi kandungan `references/manual/bab_06/` ke `manual/cu04/` & `manual/cu06/`.
- [ ] **Binaan Semula HTML & Ujian Kualiti (Rule 12 & 18):**
  - [ ] Jalankan `uv run scripts/serve_mkdocs.py --build-only` dan `uv run run_all_tests.py` sebelum setiap komit.
