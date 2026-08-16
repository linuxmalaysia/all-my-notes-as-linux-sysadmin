---
okf_version: 0.1
type: knowledge-node
title: "Penyebaran Mesin Maya Tetamu (Guest VMs)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu02", "panduan-amali", "manual-linux"]
tags: ["cu02", "linux", "noss", "amali", "standard-malaysia"]
description: "Penyediaan imej ISO, konfigurasi perkakasan maya, pemacu VirtIO, dan rangkaian bridged/NAT."
resource: "file:///manual/cu02/cu02-wa03-penyebaran-mesin-maya-tetamu.md"
---

# Penyebaran Mesin Maya Tetamu (Guest VMs)

## 🎯 Objektif Pembelajaran
Penyediaan imej ISO, konfigurasi perkakasan maya, pemacu VirtIO, dan rangkaian bridged/NAT.

> [!NOTE]
> Modul ini adalah sebahagian daripada manual teknikal **Linux for NOSS Malaysia (Tahap 3)** bagi unit kompetensi **CU02**.

---

## 🛠️ Garis Panduan Amali & Prosedur

### 1. Keperluan Awal & Pra-Syarat
- Persekitaran rujukan rasmi: **Ubuntu 26.04 LTS "Quetzal"**, **Fedora 43**, atau **AlmaLinux 10 "Purple Lion"**.
- Hak akses pentadbir (`sudo`).
- Dokumentasi dan rekod inventori yang teratur.

### 2. Langkah-Langkah Operasi
1. Melakukan semakan status dan kesediaan perkakasan atau perkhidmatan.
2. Melaksanakan konfigurasi mengikut piawaian industri dan tadbir urus keselamatan.
3. Mengesahkan hasil kerja menggunakan ujian diagnostik dan verifikasi sistem.

```bash
# Contoh arahan verifikasi status sistem
uname -r
systemctl status
```

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)
- [ ] Memahami teori dan konsep asas yang terlibat.
- [ ] Berjaya melaksanakan prosedur kerja secara amali tanpa ralat.
- [ ] Menyediakan rekod verifikasi atau dokumentasi penyerahan tugas.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Jelaskan langkah-langkah diagnostik keselamatan lanjut bagi modul Penyebaran Mesin Maya Tetamu (Guest VMs) dalam persekitaran Linux perusahaan."*
2. *"Bagaimanakah cara mengautomasikan konfigurasi Penyebaran Mesin Maya Tetamu (Guest VMs) menggunakan Ansible Playbook?"*
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
