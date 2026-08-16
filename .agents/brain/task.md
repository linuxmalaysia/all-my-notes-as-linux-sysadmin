# 📋 NOSS Linux Malaysia - Master Task Tracker

## 🌟 Milestone Status: Fasa 1 (Asas, Tadbir Urus & Pengedaran Multi-Pelantar) - SELESAI ✅
- [x] Konfigurasi Laman Web Statik MkDocs Material dengan pautan berkait (`use_directory_urls: false`) untuk pembacaan luar talian (`file:///`).
- [x] Pembersihan Pukal Teks Lapuk dalam Arkib Mentah `references/manual/` (Rule 17).
- [x] Pelaksanaan Seni Bina Diátaxis (4 Kuadran) di `docs/` dan penerangan dalam `docs/explanation/diataxis-architecture.md` (Rule 18).
- [x] Dokumentasi Sejarah Modul ISL9 KPM 2004 (`docs/explanation/sejarah-dokumen-asal-linux-kpm.md`).
- [x] Dokumentasi Sejarah OSCC MAMPU 2004–2020 (`docs/explanation/sejarah-oscc-mampu-malaysia.md`).
- [x] Dokumentasi Sejarah Malaysia Open Source Conference / MOSCMY (`docs/explanation/sejarah-mosc-malaysia.md`).
- [x] Penjejakan Direktori `html/` Prabina di dalam Git untuk kegunaan terus tanpa build.
- [x] Konfigurasi Pelayan Pengeluaran: Nginx, Apache HTTP Server, `docker-compose.yml`, Podman Pod (Kube YAML & Quadlet), dan Ansible Playbook (`deploy/ansible/`).
- [x] Pembetulan Invarian Atribusi: Deep State of Mind (Harisfazillah Jamel) vs MemPalace Framework (Milla Jovovich & Ben Sigman).
- [x] Konfigurasi Dwi-Pelantar GitOps (GitLab `origin` & GitHub `github`).

---

## 🎯 Roadmap Fasa 2 (Tugasan Google Jules): Migrasi Silibus Manual ke NOSS & Palace
- [ ] **Bab 2 (Pemasangan & Konfigurasi Linux Desktop/Server):**
  - [ ] Ekstrak dan modenkan kandungan dari `references/manual/bab_02/` ke piawaian 2026: Ubuntu 26.04 LTS, Fedora 43, AlmaLinux 10 (Rule 15).
  - [ ] Wujudkan nod memori modular dalam `palace/cu01/` dan kemas kini `openwiki/topic-01-linux-desktop-and-basics.md`.
  - [ ] Masukkan elemen keselamatan: Penyulitan Penuh Cakera LUKS2 (ISO/IEC 27001 & Pekeliling MAMPU).
  - [ ] Lengkapkan seksyen penutup: AI Prompts, Pautan Rujukan Web, dan Syor Buku Boleh Dibeli (Rule 16).
- [ ] **Bab 3 (Pengurusan Storan, Partisi & Sistem Fail Linux):**
  - [ ] Migrasi kandungan `references/manual/bab_03/` ke `palace/cu02/` (LVM, XFS, EXT4, ZFS/Btrfs basics).
- [ ] **Bab 4 (Pentadbiran Pengguna, Hak Akses & Keselamatan Asas):**
  - [ ] Migrasi kandungan `references/manual/bab_04/` ke `palace/cu01/` & `palace/cu05/`.
- [ ] **Bab 5 (Pengurusan Rangkaian & Perkhidmatan Pelayan Asas):**
  - [ ] Migrasi kandungan `references/manual/bab_05/` ke `palace/cu03/` (SSH, DNS, DHCP, Web).
- [ ] **Bab 6 (Automasi Skrip Shell & Penyelenggaraan Sistem):**
  - [ ] Migrasi kandungan `references/manual/bab_06/` ke `palace/cu04/` & `palace/cu06/`.
- [ ] **Binaan Semula HTML & Ujian Kualiti (Rule 12 & 18):**
  - [ ] Jalankan `uv run scripts/serve_mkdocs.py --build-only` dan `uv run run_all_tests.py` sebelum setiap komit.
