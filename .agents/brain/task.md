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

---

## 🌟 Milestone Status: Fasa 3 (Audit Bab 1–2, Knowledge-to-Skill Porting, & Migrasi Bab 3 Storan) - SELESAI ✅ (Google Jules PR #4 Merged)
- [x] **Audit & Semakan Semula Bab 1 & Bab 2 (`manual/cu01/`):**
  - Penyempurnaan `manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md` (APT, DNF5, Flatpak, Snap, Pemacu NVIDIA/AMD).
  - Penyempurnaan `manual/cu01/cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint.md` (NetworkManager, `nmcli`, IP statik/DHCP, Wi-Fi, `systemd-resolved`).
  - Penciptaan nod `manual/cu01/penegasan-keselamatan-sistem.md` (Pengerasan SSH, UFW, `firewalld`, audit log).
  - Pengemaskinian `openwiki/topic-01-linux-desktop-and-basics.md` dengan silibus bernombor 10 seksyen.
- [x] **Mandat Porting Pengetahuan ke Kemahiran AI (*Knowledge-to-Skill Porting*):**
  - Naik taraf `.agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md` ke format `type: skill`.
  - Naik taraf `.agents/skills/cu01-wa06-configure-endpoint-network-connectivity/SKILL.md` ke format `type: skill`.
  - Naik taraf `.agents/skills/cu02-wa01-identify-virtualisation-infrastructure-requirements/SKILL.md` ke format `type: skill`.
  - Pengemaskinian Master Palace Registry (`.agents/skills/index.md`).
- [x] **Migrasi Silibus Bab 3: Storan, Partisi & Sistem Fail (`references/manual/bab_03/` ➔ `manual/cu02/`):**
  - Penciptaan nod `manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md` (Partisi GPT `gdisk`/`parted`, LVM2 `pvcreate`/`vgcreate`/`lvcreate`, sistem fail EXT4/XFS/Btrfs, `/etc/fstab`, dan penyulitan LUKS2).
  - Pengemaskinian `openwiki/topic-02-storage-and-virtualisation.md`.

---

## 🌟 Milestone Status: Fasa 4 (Migrasi Silibus Bab 4: Pentadbiran Pengguna & Keselamatan Endpoint CU05) - SELESAI ✅ (Google Jules PR #6 Merged)
- [x] **Penyempurnaan Modul Amali `manual/cu05/`:**
  - Penciptaan nod `manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.md` (Pengurusan Pengguna/Kumpulan, `/etc/shadow`, `visudo`, `pam_faillock`, `chmod`/`chown`, SUID/SGID/Sticky bit, POSIX ACL `getfacl`/`setfacl`, FHS, pencarian `plocate`/`find`, dan penutupan selamat).
  - Kemas kini `manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.md` & `manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.md`.
  - Kemas kini `openwiki/topic-05-linux-security.md`.
- [x] **Porting Kemahiran AI CU05 (`.agents/skills/`):**
  - Naik taraf `.agents/skills/cu05-wa01-perform-user-account-and-permission-audits/SKILL.md` ke format `type: skill` penuh.
  - Naik taraf `.agents/skills/cu05-wa05-manage-physical-endpoint-security-lockdowns/SKILL.md` ke format `type: skill` penuh.

---

## 🌟 Milestone Status: Fasa 5 (Migrasi Silibus Bab 5: Konfigurasi Teras Pelayan CU03 & Pemantauan Prestasi CU06) - SELESAI ✅ (Google Jules PR #9 Merged)
- [x] **Penyempurnaan Modul Amali `manual/cu03/` & `manual/cu06/`:**
  - Penyempurnaan `manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md` (Pengurusan unit servis `systemd`, `systemctl`, `journalctl`, `timedatectl`/`chrony`, FHS, dan halaman `man`).
  - Penyempurnaan `manual/cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md` (Pemantauan proses `ps`/`top`/`htop`/`vmstat`/`iostat`, penamatan isyarat SIGTERM/SIGKILL, penalaan keutamaan `nice`/`renice`, dan cgroups v2).
  - Kemas kini `openwiki/topic-03-linux-server-administration.md` & `openwiki/topic-06-troubleshooting-and-logs.md`.
- [x] **Porting Kemahiran AI CU03 & CU06 (`.agents/skills/`):**
  - Naik taraf `.agents/skills/cu03-wa04-perform-core-server-configurations/SKILL.md` ke format `type: skill` penuh.
  - Cipta `.agents/skills/cu06-wa05-optimize-system-performance-and-storage/SKILL.md` ke format `type: skill` penuh.
  - Naik taraf `.agents/skills/cu06-wa05-perform-system-optimisation-and-disk-management/SKILL.md` ke format `type: skill` penuh.
- [x] **Jaminan Kualiti (100% Quality Gate):**
  - **917 ujian Python pytest lulus** (penambahan `tests/test_manual_cu03_cu06_process_server_content.py`).
  - **38 ujian Node.js Jest lulus**.
  - Laman web statik `html/` dibina semula dan disegerakkan.

---

## 🎯 Roadmap Fasa Seterusnya
- [ ] **Fasa 6: Transformasi Silibus Bab 6 (Automasi Skrip Shell, Sandaran & Troubleshooting - CU04 & CU06):**
  - [ ] Ekstrak dan modenkan kandungan amali dari `references/manual/bab_06/` ke `manual/cu04/` (Sandaran `rsync`/`tar`/`restic`, Automasi Cron/Systemd Timers, Pemulihan Data) dan `manual/cu06/` (Diagnostik Anomali, Analisis Log, RCA).
  - [ ] Porting kemahiran AI CU04 (`cu04-wa01` hingga `cu04-wa05`) dan CU06 (`cu06-wa01` hingga `cu06-wa07`).
  - [ ] Kemas kini `openwiki/topic-04-automation-and-backup.md` dan `openwiki/topic-06-troubleshooting-and-logs.md`.
