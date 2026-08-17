---
okf_version: 0.1
type: knowledge-node
title: "Audit Akaun Pengguna & Kebenaran Akses Linux (CU05-WA01)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu05", "wa01", "panduan-amali", "manual-linux", "security-audit"]
tags: ["cu05", "wa01", "linux", "noss", "amali", "user-audit", "permissions", "visudo", "faillock"]
description: "Panduan amali audit akaun pengguna, pemeriksaan /etc/passwd dan /etc/shadow, pengurusan privilesej sudoers, kebenaran UGO/POSIX ACL, serta penguncian faillock."
resource: "file:///manual/cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.md"
---

# Audit Akaun Pengguna & Kebenaran Akses Linux (CU05-WA01)

## 🎯 Objektif Pembelajaran
Melaksanakan audit menyeluruh ke atas akaun pengguna sistem, keahlian kumpulan, integriti fail pengesahan (`/etc/passwd`, `/etc/shadow`), konfigurasi keistimewaan `sudo` (`visudo`), matriks kebenaran fail UGO dan POSIX ACL, serta penguatkuasaan dasar kunci kata laluan (`faillock`) mengikut piawaian **NOSS CU05 WA01**, **ISO/IEC 27001**, dan Pekeliling **Jabatan Digital Negara (JDN) / MAMPU**.

> [!NOTE]
> Modul ini dipetakan daripada Unit Kompetensi **CU05 (Kawalan Keselamatan Endpoint & Audit)** bagi Aktiviti Kerja **WA01 (Perform User Account and Permission Audits)** pada platform **Ubuntu 26.04 LTS "Quetzal"** dan **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Prosedur & Arahan Amali

### 1. Audit Integriti Fail Pengguna & Kumpulan (`/etc/passwd` & `/etc/shadow`)
Akaun tanpa kata laluan atau UID 0 tidak sah merupakan risiko keselamatan kritikal.

```bash
# 1. Semak sebarang akaun selain 'root' yang mempunyai UID 0 (Akses Superuser Tidak Sah)
awk -F: '($3 == "0") { print $1 }' /etc/passwd

# 2. Cari akaun tanpa kata laluan atau akaun terkunci dalam /etc/shadow
sudo awk -F: '($2 == "" || $2 == "!") { print $1 }' /etc/shadow

# 3. Semak integriti fail passwd dan shadow dengan alat pwck
sudo pwck -r
```

### 2. Audit & Pengurusan Kebenaran Privilesej Pentadbir (`visudo`)
Log masuk terus sebagai `root` dilarang. Semua tindakan pentadbiran mesti diaudit menerusi `sudo`.

```bash
# Audit fail konfigurasi /etc/sudoers dan direktori /etc/sudoers.d/
sudo visudo -c

# Senaraikan keistimewaan sudo untuk pengguna semasa atau pengguna tertentu
sudo -l -U ahmad
```

### 3. Audit Kebenaran Fail & POSIX ACL
```bash
# Semak kebenaran fail asas dan pemilik
ls -la /srv/projek_sec/

# Semak Senarai Kawalan Akses POSIX (POSIX ACL)
getfacl /srv/projek_sec/dokumen.pdf

# Tetapkan kebenaran ACL khusus pengguna
sudo setfacl -m u:zarith:rw- /srv/projek_sec/dokumen.pdf
```

### 4. Semakan & Pemulihan Penguncian Akaun (`faillock`)
```bash
# Semak sejarah kegagalan log masuk pengguna
sudo faillock --user ahmad

# Nyahkunci akaun yang terkunci akibat salah kata laluan
sudo faillock --user ahmad --reset
```

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)
- [ ] Pengesahan tiada akaun UID 0 yang tidak sah.
- [ ] Semakan kegagalan pwck melepasi 100%.
- [ ] Audit keistimewaan sudoers menggunakan `visudo -c`.
- [ ] Penetapan dan verifikasi POSIX ACL menggunakan `getfacl` / `setfacl`.
- [ ] Pentadbiran kunci kata laluan `faillock`.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Tulis skrip audit Bash untuk mengesan pengguna sistem dengan shell log masuk aktif yang tidak pernah log masuk."*
2. *"Jelaskan cara mengonfigurasi faillock supaya mengunci akaun selama 30 minit selepas 3 percubaan berturut-turut gagal."*
3. *"Bagaimanakah cara mengaudit perubahan pada /etc/passwd menggunakan auditd?"*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
- [Ubuntu Security Handbook - User Auditing](https://ubuntu.com/server/docs/security-users)
- [AlmaLinux PAM & Security Audit Guide](https://wiki.almalinux.org/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
- **Linux Auditing and Hardening** oleh Master Technical Series.
- **Panduan Praktikal Audit Keselamatan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
