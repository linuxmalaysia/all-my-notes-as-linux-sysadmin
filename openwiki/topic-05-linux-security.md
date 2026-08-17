---
okf_version: 0.1
type: documentation
title: "Topik 5: Keselamatan Linux & Kawalan Akses (CU05)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["security", "firewall", "cu05", "users", "permissions", "acl"]
tags: ["linux", "security", "cu05", "noss", "faillock", "visudo"]
description: "Silibus keselamatan OS Linux komprehesif merangkumi Pentadbiran Pengguna & Kumpulan, Kebenaran Fail & POSIX ACL, Firewall, dan Kawalan Lockdowns."
resource: "file:///openwiki/topic-05-linux-security.md"
---

# Topik 5: Keselamatan Linux & Kawalan Akses Endpoint (CU05)

## Overview (Gambaran Keseluruhan)

Keselamatan Linux merangkumi pentadbiran identiti pengguna, sekatan kebenaran fail asas dan lanjutan, penegasan dasar kata laluan, kawalan keistimewaan `sudo`, dinding api (*firewall*), serta perlindungan fizikal konsol. Silibus ini dipetakan secara terperinci kepada Unit Kompetensi **CU05 (User Account and Permissions Audits / Security Lockdowns)** dan **CU01 (Aktiviti Asas Linux)** mengikut standard NOSS Tahap 3 dan piawaian **ISO/IEC 27001** & Pekeliling **Jabatan Digital Negara (JDN) / MAMPU**.

## Silibus Utama

1. **Pengurusan Pengguna, Kumpulan & Fail Identiti**:
    - Penciptaan dan pengurusan akaun (`useradd`, `usermod`, `userdel`, `groupadd`).
    - Struktur fail sistem teras `/etc/passwd`, `/etc/shadow`, `/etc/group`, dan `/etc/gshadow`.
2. **Kebenaran Sistem Fail & Bit Khas (UGO, SUID, SGID, Sticky Bit)**:
    - Konsep UGO (User, Group, Others) dengan `chmod`, `chown`, dan `chgrp`.
    - Tetapan Bit Khas: SUID (Set User ID), SGID (Set Group ID), dan Sticky Bit.
    - Konfigurasi `umask` selamat (`027`).
3. **Senarai Kawalan Akses Lanjutan (POSIX ACL)**:
    - Pengurusan kawalan akses khusus individu/kumpulan dengan `getfacl` dan `setfacl`.
4. **Keistimewaan Pentadbir & Perlindungan Kata Laluan (`visudo` & `faillock`)**:
    - Konfigurasi keistimewaan terhad `sudo` melalui `visudo`.
    - Perlindungan serangan brute-force dan penguncian akaun otomatik dengan `faillock`.
5. **Navigasi Standard FHS, Pencarian Fail & Dokumentasi**:
    - Hierarki sistem fail FHS, pencarian pantas `plocate`, `find`, dan halaman manual `man-db`.
6. **Kawalan Keselamatan Konsol, Sesi Terminal & Penutupan Selamat**:
    - Penetapan pembolehubah `TMOUT` untuk tamat masa sesi tidak aktif.
    - Sekatan kawalan sumber sistem dalam `/etc/security/limits.conf`.
    - Perlindungan bootloader GRUB2 dan prosedur penutupan selamat (`systemctl poweroff`/`shutdown`).
7. **Dinding Api (Firewall & Port Security)**:
    - Konfigurasi Uncomplicated Firewall (`ufw`) di Ubuntu.
    - Konfigurasi `firewalld` di sistem berasaskan Red Hat / AlmaLinux.
8. **Sistem Kawalan Mandatori (MAC)**:
    - Pengenalan dan mod SELinux (Enforcing, Permissive, Disabled) di AlmaLinux/Fedora.
    - Pengenalan kepada AppArmor di Ubuntu.

## Modul Amali Terkait

- [Pentadbiran Pengguna, Kebenaran Fail & Kawalan Akses Endpoint Linux](../manual/cu05/pentadbiran-pengguna-kebenaran-dan-kawalan-akses.md)
- [Audit Akaun Pengguna & Kebenaran Akses Linux (CU05-WA01)](../manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.md)
- [Kawalan Keselamatan Fizikal & Persekitaran Console Endpoint Linux (CU05-WA05)](../manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.md)

## Pemetaan NOSS (NOSS Mapping)

Silibus ini memandu kemahiran Ejen AI berikut:

- `cu05-wa01-perform-user-account-and-permission-audits`
- `cu05-wa03-configure-client-firewall-profiles`
- `cu05-wa05-manage-physical-endpoint-security-lockdowns`

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Apakah amalan terbaik untuk mengaudit kebenaran POSIX ACL dan bit SUID pada sistem Ubuntu 26.04 LTS?"*
2. *"Jelaskan cara mengonfigurasi faillock dan pam_tally2 bagi mematuhi penanda aras CIS Benchmark."*
3. *"Tunjukkan contoh skrip Bash untuk menyemak akaun pengguna yang tidak aktif dan menguncinya secara automatik."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Ubuntu Security Handbook - User Account & Permission Audits](https://ubuntu.com/server/docs/security-users)
- [AlmaLinux 10 System Security and Hardening Guide](https://wiki.almalinux.org/)
- [Red Hat Enterprise Linux 10 Security Guide](https://access.redhat.com/documentation/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **UNIX and Linux System Administration Handbook (5th Edition)** oleh Evi Nemeth et al.
- **Linux Security Cookbook** oleh Daniel J. Barrett, Richard E. Silverman, Robert G. Byrnes.
- **Panduan Praktikal Audit & Keselamatan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
