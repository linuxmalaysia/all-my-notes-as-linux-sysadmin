---
okf_version: 0.1
type: knowledge-node
title: "Pengurusan Tampalan & Kemas Kini Keselamatan"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu05", "panduan-amali", "manual-linux"]
tags: ["cu05", "linux", "noss", "amali", "standard-malaysia"]
description: "Automasi keselamatan pakej (unattended-upgrades / dnf-automatic) dan audit CVE."
resource: "file:///manual/cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.md"
---

# Pengurusan Tampalan & Kemas Kini Keselamatan

## 🎯 Objektif Pembelajaran
Automasi keselamatan pakej (unattended-upgrades / dnf-automatic) dan audit CVE.

> [!NOTE]
> Modul ini adalah sebahagian daripada manual teknikal **Linux for NOSS Malaysia (Tahap 3)** bagi unit kompetensi **CU05**.

---

## 🛠️ Garis Panduan Amali & Prosedur

### 1. Keperluan Awal & Pra-Syarat
- Persekitaran rujukan rasmi: **Ubuntu 26.04 LTS "Resolute Raccoon"**, **Fedora 43**, atau **AlmaLinux 10 "Purple Lion"**.
- Hak akses pentadbir (`sudo`).
- Dokumentasi dan rekod inventori yang teratur.

### 2. Langkah-Langkah Operasi
1. Melakukan semakan status dan kesediaan perkakasan atau perkhidmatan.
2. Melaksanakan konfigurasi mengikut piawaian industri dan tadbir urus keselamatan.
3. Mengesahkan hasil kerja menggunakan ujian diagnostik dan verifikasi sistem.

### 2. Automasi Tampalan Keselamatan Pakej (Unattended Upgrades & DNF Automatic)

#### A. Debian / Ubuntu (unattended-upgrades)

Pada **Ubuntu 26.04 LTS**, automasi pemutakhiran tampalan keselamatan dipasang dan dikonfigurasikan seperti berikut:

```bash
# 1. Pasang pakej unattended-upgrades
sudo apt update
sudo apt install -y unattended-upgrades apt-config-auto-update

# 2. Aktifkan perkhidmatan automasi tampalan keselamatan secara interaktif atau pemprosesan automatik
sudo dpkg-reconfigure --priority=low unattended-upgrades

# 3. Pengesahan fail konfigurasi di /etc/apt/apt.conf.d/50unattended-upgrades dan /etc/apt/apt.conf.d/20auto-upgrades
cat /etc/apt/apt.conf.d/20auto-upgrades

# 4. Semak log aktiviti kemas kini automatik
sudo tail -n 50 /var/log/unattended-upgrades/unattended-upgrades.log
```

#### B. Red Hat / AlmaLinux / Fedora (dnf-automatic)

Pada **AlmaLinux 10** dan **Fedora 43**, kemas kini keselamatan secara automatik dilaksanakan menggunakan `dnf-automatic`:

```bash
# 1. Pasang pakej dnf-automatic
sudo dnf install -y dnf-automatic

# 2. Sunting konfigurasi di /etc/dnf/automatic.conf untuk mengaplikasikan kemas kini keselamatan
# Tetapkan apply_updates = yes dan upgrade_type = security
sudo sed -i 's/upgrade_type = default/upgrade_type = security/' /etc/dnf/automatic.conf
sudo sed -i 's/apply_updates = no/apply_updates = yes/' /etc/dnf/automatic.conf

# 3. Aktifkan dan jalankan Systemd timer bagi dnf-automatic
sudo systemctl enable --now dnf-automatic.timer
sudo systemctl status dnf-automatic.timer
```

---

### 3. Semakan Integriti Fail Pakej & Audit CVE (`rpm -V` & `dpkg --verify`)

Untuk memastikan fail biner dan fail konfigurasi perisian tidak diubah atau dicemari oleh sebarang pencerobohan:

```bash
# A. Semakan integriti pada sistem berasaskan Red Hat / AlmaLinux / Fedora:
# Semak kesemua pakej terpasang bagi sebarang perubahan saiz, checksum MD5/SHA256, atau kebenaran fail
sudo rpm -Va

# Semak integriti fail bagi pakej spesifik (contoh: openssh-server)
sudo rpm -V openssh-server

# B. Semakan integriti pada sistem berasaskan Debian / Ubuntu:
sudo dpkg --verify

# C. Audit kelemahan dan keselamatan pakej (CVE auditing):
# Menggunakan debsecan / dnf audit jika tersedia
sudo dnf updateinfo list security
```

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)
- [ ] Memahami teori dan konsep asas yang terlibat.
- [ ] Berjaya melaksanakan prosedur kerja secara amali tanpa ralat.
- [ ] Menyediakan rekod verifikasi atau dokumentasi penyerahan tugas.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Jelaskan langkah-langkah diagnostik keselamatan lanjut bagi modul Pengurusan Tampalan & Kemas Kini Keselamatan dalam persekitaran Linux perusahaan."*
2. *"Bagaimanakah cara mengautomasikan konfigurasi Pengurusan Tampalan & Kemas Kini Keselamatan menggunakan Ansible Playbook?"*
3. *"Berikan senarai semak pengerasan (hardening checklist) untuk perkhidmatan yang berkaitan dengan topik ini."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
- [Dokumentasi Rasmi Ubuntu](https://ubuntu.com/server/docs)
- [Dokumentasi AlmaLinux Wiki](https://wiki.almalinux.org/)
- [Panduan Pentadbiran Fedora](https://docs.fedoraproject.org/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
- **Linux Administration Handbook (Edisi Terkini)** oleh Evi Nemeth et al.
- **The Linux Command Line** oleh William Shotts.
- **Panduan Praktikal Pentadbiran Sistem Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
