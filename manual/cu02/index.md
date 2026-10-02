---
okf_version: '0.2'
type: reference
title: 'CU02: Pengurusan Storan & Infrastruktur Pemayaan'
timestamp: '2026-08-17T00:00:00Z'
topics:
- noss-linux
- cu02
- kurikulum-tvet
- manual-linux
tags:
- cu02
- linux
- noss
- modul-amali
- standard-malaysia
description: Modul NOSS Level 3 untuk pengurusan partisi cakera, sistem fail Linux,
  LVM, dan pelaksanaan pemayaan Jenis 2 (KVM / QEMU / VirtualBox).
resource: file:///manual/cu02/index.md
spec_version: '0.2'
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:45Z'
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

# CU02: Pengurusan Storan & Infrastruktur Pemayaan

## 📖 Pengenalan Unit Kompetensi
Modul NOSS Level 3 untuk pengurusan partisi cakera, sistem fail Linux, LVM, dan pelaksanaan pemayaan Jenis 2 (KVM / QEMU / VirtualBox).

---

## 📑 Senarai Aktiviti Kerja (Work Activities - WA)

- [**Mengenal Pasti Keperluan Infrastruktur Pemayaan**](cu02-wa01-keperluan-infrastruktur-pemayaan.md) — *Analisis keperluan CPU virtualization (VT-x/AMD-V), RAM, dan storan bagi persekitaran VM.*
- [**Pemasangan & Konfigurasi Platform Hipervisor**](cu02-wa02-pemasangan-hipervisor-jenis-2.md) — *Pemasangan KVM/QEMU, virt-manager, dan hypervisor desktop pada Linux.*
- [**Penyebaran Mesin Maya Tetamu (Guest VMs)**](cu02-wa03-penyebaran-mesin-maya-tetamu.md) — *Penyediaan imej ISO, konfigurasi perkakasan maya, pemacu VirtIO, dan rangkaian bridged/NAT.*
- [**Penyediaan Rekod Konfigurasi Pemayaan**](cu02-wa04-rekod-konfigurasi-pemayaan.md) — *Penyusunan log topologi VM, rekod peruntukan sumber storan dan alamat IP VM.*
- [**Pengurusan Storan, Partisi & Sistem Fail Linux**](pengurusan-storan-partisi-dan-sistem-fail.md) — *Panduan amali GPT/MBR (fdisk/parted), LVM2 (PV/VG/LV), dan sistem fail EXT4, XFS, serta Btrfs.*

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Apakah kemahiran utama yang dinilai dalam unit kompetensi CU02 bagi pensijilan NOSS Malaysia?"*
2. *"Cadangkan satu projek amali berasaskan industri untuk menguji kefahaman pelajar dalam CU02."*
3. *"Bagaimanakah teknologi kontena dan awan mengintegrasikan konsep dalam CU02 hari ini?"*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
- [Portal Rasmi JPK - NOSS](https://www.dsd.gov.my/)
- [Dokumentasi Rasmi Linux Kernel](https://docs.kernel.org/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
- **UNIX and Linux System Administration Handbook** oleh Evi Nemeth.
- **Nota Sistem Linux Malaysia** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
