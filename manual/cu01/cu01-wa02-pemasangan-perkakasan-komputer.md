---
okf_version: 0.1
type: knowledge-node
title: "Pemasangan Komponen Perkakasan Komputer"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu01", "panduan-amali", "manual-linux"]
tags: ["cu01", "linux", "noss", "amali", "standard-malaysia"]
description: "Pemasangan papan induk, CPU, memori RAM, pemacu storan NVMe/SSD, dan bekalan kuasa PSU."
resource: "file:///manual/cu01/cu01-wa02-pemasangan-perkakasan-komputer.md"
---

# Pemasangan Komponen Perkakasan Komputer

## 🎯 Objektif Pembelajaran
Pemasangan papan induk, CPU, memori RAM, pemacu storan NVMe/SSD, dan bekalan kuasa PSU.

> [!NOTE]
> Modul ini adalah sebahagian daripada manual teknikal **Linux for NOSS Malaysia (Tahap 3)** bagi unit kompetensi **CU01**.

---

## 🛠️ Garis Panduan Amali & Prosedur

### 1. Perkakasan Sumber Terbuka (OSHW) & Peranti Input Custom (QMK)
Selain komponen stesen kerja standard, ekosistem Linux menyokong penuh **Perkakasan Sumber Terbuka (Open-Source Hardware - OSHW)** seperti papan kekunci mekanikal boleh ubah (*custom keyboard*) yang dikuasai **QMK Firmware**.
- **OSHW Definition:** Reka bentuk fizikal (skematik PCB, CAD, BOM) yang terbuka untuk distudi, diubah suai, dan dibina.
- **QMK Configurator & Rules:** Penggunaan [docs.qmk.fm](https://docs.qmk.fm/) untuk reka bentuk susun atur kekunci (*layout/layers*) dan persediaan peraturan `udev` di Linux untuk kebenaran peranti USB input.
- **Rujukan Tutorial Amali:** [Tutorial Papan Kekunci QMK & OSHW](../../docs/tutorials/opensource-keyboard-qmk.md)

### 2. Keperluan Awal & Pra-Syarat
- Persekitaran rujukan rasmi: **Ubuntu 26.04 LTS "Resolute Raccoon"**, **Fedora 43**, atau **AlmaLinux 10 "Purple Lion"**.
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
1. *"Jelaskan langkah-langkah diagnostik keselamatan lanjut bagi modul Pemasangan Komponen Perkakasan Komputer dalam persekitaran Linux perusahaan."*
2. *"Bagaimanakah cara mengautomasikan konfigurasi Pemasangan Komponen Perkakasan Komputer menggunakan Ansible Playbook?"*
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
