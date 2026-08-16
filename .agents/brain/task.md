# 📋 NOSS Linux Malaysia - Master Task Tracker

## 🌟 Milestone Status: Fasa 1 & Fasa 2 (Penstrukturan Semula Seni Bina DSOM & Silibus Manual) - SELESAI ✅
- [x] **Penstrukturan Semula Direktori Punca `manual/`:**
  - Pengasingan modul amali silibus NOSS (CU01–CU06) daripada Memori Ruang Ejen ke dalam folder `manual/`.
  - Penjanaan rangka nod draf lengkap berformat OKF v0.1 untuk kesemua Aktiviti Kerja (WA01–WA07) bagi CU01 hingga CU06.
- [x] **Pembinaan Semula DSOM Spatial Memory Palace (.agents/brain/wings/):**
  - Penyusunan Sayap `wing_dsom_core` (`hall_facts`, `hall_events`, `hall_discoveries`) dan `wing_noss_linux` (`hall_curriculum`, `hall_governance`).
  - Penjanaan Master Palace Registry di `.agents/brain/palace_registry.md`.
- [x] **Kemas Kini Perlembagaan & Alatan:**
  - Pindaan Peraturan 2 & Peraturan 8 dalam `AGENTS.md` dan `.agents/AGENTS.md`.
  - Pengemaskinian `scripts/serve_mkdocs.py`, `mkdocs.yml`, dan suite ujian pematuhan (`tests/test_okf_compliance.py`, `tests/test_serve_mkdocs.py`, `tests/test_manual_cu01_bab2_content.py`).
  - 100% Quality Gate tercapai (802/802 Python tests, 38/38 Jest tests).

---

## 🎯 Roadmap Fasa Seterusnya: Migrasi Silibus Manual ke NOSS (manual/)
- [x] **Bab 2 (Pemasangan & Konfigurasi Linux Desktop/Server - Selesai):**
  - [x] 4 nod memori dimodenkan dalam `manual/cu01/` (`keperluan-perkakasan-dan-bios-uefi.md`, `prosedur-pemasangan-ubuntu-almalinux.md`, `penyulitan-cakera-luks2-pejabat.md`, `pasca-pemasangan-dan-driver.md`).
  - [x] Kemas kini `openwiki/topic-01-linux-desktop-and-basics.md`.
- [ ] **Bab 3 (Pengurusan Storan, Partisi & Sistem Fail Linux - SASARAN SETERUSNYA):**
  - [ ] Migrasi kandungan amali `references/manual/bab_03/` ke `manual/cu02/` (Partisi GPT/fdisk/parted, LVM2, EXT4, XFS, Btrfs).
  - [ ] Kemas kini `openwiki/topic-02-storage-and-virtualisation.md`.
- [ ] **Bab 4 (Pentadbiran Pengguna, Hak Akses & Keselamatan Asas):**
  - [ ] Migrasi kandungan `references/manual/bab_04/` ke `manual/cu01/` & `manual/cu05/`.
- [ ] **Bab 5 (Pengurusan Rangkaian & Perkhidmatan Pelayan Asas):**
  - [ ] Migrasi kandungan `references/manual/bab_05/` ke `manual/cu03/` (SSH, DNS, DHCP, Web).
- [ ] **Bab 6 (Automasi Skrip Shell & Penyelenggaraan Sistem):**
  - [ ] Migrasi kandungan `references/manual/bab_06/` ke `manual/cu04/` & `manual/cu06/`.
- [ ] **Binaan Semula HTML & Ujian Kualiti (Rule 12 & 18):**
  - [ ] Jalankan `uv run scripts/serve_mkdocs.py --build-only` dan `uv run run_all_tests.py` sebelum setiap komit.
