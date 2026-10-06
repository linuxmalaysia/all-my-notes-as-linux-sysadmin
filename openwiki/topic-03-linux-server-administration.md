---
okf_version: '0.2'
type: explanation
title: 'Topik 3: Pentadbiran Pelayan Linux (CU03)'
timestamp: '2026-08-17T00:00:00Z'
topics:
- linux-server
- cu03
- systemd
- openwiki
- noss
tags:
- linux
- server
- cu03
- systemd
- openwiki
description: Silibus pentadbiran pelayan Linux, pengurusan perkhidmatan systemd, konfigurasi
  teras sistem, dan penyelarasan masa (CU03).
resource: file:///openwiki/topic-03-linux-server-administration.md
spec_version: '0.2'
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:43Z'
sources:
- id: internal-legal-notice
  title: Dokumen Notis Perundangan, Privasi & Penafian / Legal Notice
  author: Harisfazillah Jamel (LinuxMalaysia)
  url: docs/legal-notice.md
  resource: docs/legal-notice.md
- id: google-okf-v02-spec
  title: Open Knowledge Format v0.2 Specification & Trust Signals
  author: Google Cloud Data Analytics
  url: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
  resource: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
- id: redlinesoft-attested-computations
  title: Attested Computations in Open Knowledge Format (OKF v0.2)
  author: RedLineSoft
  url: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
  resource: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
- id: dsom-okf-v02-adoption-skill
  title: OKF v0.2 Adoption Engineer Skill Standard
  author: Deep State of Mind (DSOM)
  url: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
  resource: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
---

# Topik 3: Pentadbiran Pelayan Linux (CU03)

## 📌 Overview (Gambaran Keseluruhan)

Pusat utama ekosistem Linux adalah pelayannya (*Server*). Topik ini menerangkan tentang pengurusan perkhidmatan (*services*), konfigurasi teras pelayan, dan pelaksanaan peranan pelayan enterprise. Ia merupakan pemetaan langsung daripada **NOSS CU03 (Server Setup)**.

---

## 📚 Silibus Utama

1. **Pemasangan & Persediaan OS Pelayan (Server OS)**:
    - Membezakan edisi Desktop vs Server (pemasangan minimum, CLI penuh).
    - *Static IP Configuration* menggunakan Netplan (Ubuntu 26.04 LTS) atau NetworkManager / `nmcli` (AlmaLinux 10 / Fedora 43).
2. **Konfigurasi Teras Pelayan & Systemd**:
    - Pengurusan perkhidmatan menggunakan `systemctl` (start, stop, enable, disable, mask, restart, daemon-reload).
    - Penulisan fail unit perkhidmatan kustom (`/etc/systemd/system/`) dengan parameter pengerasan keselamatan.
    - Audit log sistem terpusat menggunakan `journalctl`.
    - Penyegerakan masa kebangsaan dan zon masa melalui `timedatectl` dan `chronyd`.
    - Navigasi dokumentasi sistem dan halaman manual (`man`, `apropos`, `whatis`, `whereis`, `plocate`).
3. **Capaian Jarak Jauh & Pengerasan SSH (Remote Access Hardening)**:
    - Pemasangan dan konfigurasi `openssh-server`.
    - Log masuk tanpa kata laluan menggunakan kunci SSH (`ssh-keygen`, `ssh-copy-id`, `authorized_keys`).
    - Pengerasan SSH: penutupan root login (`PermitRootLogin no`), pertukaran port, dan `fail2ban`.
4. **Penyedia Khidmat & Peranan Pelayan (Server Roles)**:
    - **Pelayan Web**: Apache (`httpd` / `apache2`) dan Nginx dengan TLS/SSL Let's Encrypt.
    - **Perkongsian Fail**: Samba (SMB/CIFS) untuk interoperabiliti Windows dan NFSv4 untuk persekitaran Linux.
    - **Pangkalan Data**: MariaDB / MySQL enterprise hardening.

---

## 🗺️ Pemetaan Modul Amali & Kemahiran AI (NOSS Mapping)

Silibus ini memandu modul amali di `manual/cu03/` dan kemahiran AI di `.agents/skills/`:

- `manual/cu03/cu03-wa01-persediaan-pemasangan-pelayan.md` ➔ `.agents/skills/cu03-wa01-prepare-server-setup/`
- `manual/cu03/cu03-wa02-pelaksanaan-pemasangan-fizikal-pelayan.md` ➔ `.agents/skills/cu03-wa02-carry-out-server-installation/`
- `manual/cu03/cu03-wa03-pemasangan-sistem-operasi-pelayan.md` ➔ `.agents/skills/cu03-wa03-install-server-operating-system/`
- `manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md` ➔ `.agents/skills/cu03-wa04-perform-core-server-configurations/`
- `manual/cu03/cu03-wa05-pelaksanaan-peranan-dan-servis-pelayan.md` ➔ `.agents/skills/cu03-wa05-implement-server-roles-and-services/`
- `manual/cu03/cu03-wa05-solusi-pangkalan-data-kebolehseediaan-tinggi.md` ➔ `.agents/skills/solusi-pangkalan-data-ha/`
- `manual/cu03/cu03-wa06-pengurusan-perkakasan-dan-antaramuka-pelayan.md` ➔ `.agents/skills/cu03-wa06-manage-server-hardware/`

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Apakah perbezaan ketara antara pengurusan unit systemd pada Ubuntu Server 26.04 LTS dan AlmaLinux 10 dari segi kawalan SELinux/AppArmor?"*
2. *"Hasilkan skrip automasi Bash untuk mengesahkan penyegerakan masa chronyc dan status keaktifan semua perkhidmatan teras pelayan."*
3. *"Bagaimanakah cara mengkonfigurasikan pelayan web Nginx sebagai reverse proxy bersama modul systemd socket activation?"*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Dokumentasi Systemd Official](https://systemd.io/)
- [Panduan Pentadbiran Pelayan Ubuntu Server](https://ubuntu.com/server/docs)
- [AlmaLinux 10 Enterprise Server Administration Wiki](https://wiki.almalinux.org/)
- [Freedesktop.org Systemd Unit Manual](https://www.freedesktop.org/software/systemd/man/systemd.unit.html)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **UNIX and Linux System Administration Handbook (5th Edition)** oleh Evi Nemeth, Garth Snyder, Trent R. Hein, Ben Whaley, Dan Mackin.
- **Mastering systemd** oleh Anish Nath.
- **Panduan Praktikal Pentadbiran Pelayan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
