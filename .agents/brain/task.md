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
- [x] **Jaminan Kualiti (100% Quality Gate):**
  - **902 ujian Python pytest lulus** (penambahan `tests/test_manual_cu01_wa05_wa06_cu02_content.py` dan `tests/test_manual_cu02_storage_content.py`).
  - **38 ujian Node.js Jest lulus**.
  - Laman web statik `html/` dibina semula dan disahkan bebas amaran.

---

## 🎯 Roadmap Fasa Seterusnya
- [ ] **Fasa 4: Transformasi Silibus Bab 4 (Pentadbiran Pengguna & Keselamatan Endpoint - CU01 & CU05):**
  - [ ] Ekstrak dan modenkan kandungan amali dari `references/manual/bab_04/` ke `manual/cu05/` (Audit akaun pengguna, kebenaran fail/POSIX ACL, pertahanan antimalware, firewall klien, dan kawalan keselamatan fizikal).
  - [ ] Porting kemahiran AI CU05 (`cu05-wa01` hingga `cu05-wa05`).
  - [ ] Kemas kini `openwiki/topic-05-linux-security.md`.
- [ ] **Fasa 5: Transformasi Silibus Bab 5 (Konfigurasi Rangkaian & Servis Pelayan Teras - CU03):**
  - [ ] Ekstrak dari `references/manual/bab_05/` ke `manual/cu03/` (Persediaan pelayan, pemasangan OS pelayan AlmaLinux 10/Ubuntu Server, peranan DNS/DHCP/Web/SSH).
  - [ ] Porting kemahiran AI CU03 (`cu03-wa01` hingga `cu03-wa06`).
- [ ] **Fasa 6: Transformasi Silibus Bab 6 (Automasi Skrip Shell & Troubleshooting - CU04 & CU06):**
  - [ ] Ekstrak dari `references/manual/bab_06/` ke `manual/cu04/` dan `manual/cu06/`.
