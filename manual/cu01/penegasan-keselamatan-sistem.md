---
okf_version: 0.2
type: knowledge-node
title: "Penegasan Keselamatan Sistem Linux (Hardening)"
timestamp: "2026-08-16T00:00:00Z"
topics: ["noss-linux", "cu01", "hardening", "keselamatan", "firewall", "ssh"]
tags: ["cu01", "hardening", "ufw", "firewalld", "ssh", "security"]
description: "Panduan amali penegasan keselamatan asas Linux: konfigurasi firewall (UFW/firewalld) dan pengerasan SSH daemon mengikut ISO/IEC 27001 & JDN/MAMPU."
resource: "file:///manual/cu01/penegasan-keselamatan-sistem.md"
---

# Penegasan Keselamatan Sistem Linux (Hardening)

## 🎯 Objektif Pembelajaran

Menguasai prosedur amali penegasan keselamatan asas (*initial system hardening*) pada sistem operasi Linux mengikut piawaian **NOSS Tahap 3 (CU01)**, Pekeliling Am **Jabatan Digital Negara (JDN) / MAMPU**, dan **ISO/IEC 27001**.

---

## 🛠️ Garis Panduan Amali & Prosedur Kerja

### 1. Konfigurasi Tembok Api (*Firewall*)

#### A. Ubuntu / Debian (UFW - Uncomplicated Firewall)

```bash
# Setkan polisi lalai: halang masuk, benarkan keluar
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Benarkan akses SSH pada port 22 secara khusus
sudo ufw allow 22/tcp comment 'Akses SSH Pejabat'

# Aktifkan firewall dan semak status
sudo ufw enable
sudo ufw status verbose
```

#### B. AlmaLinux 10 / Fedora 43 (firewalld)

```bash
# Aktifkan perkhidmatan firewalld
sudo systemctl enable --now firewalld

# Benarkan servis SSH secara kekal
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
```

---

### 2. Pengerasan Akses Pelayan SSH Daemon (`/etc/ssh/sshd_config.d/99-hardening.conf`)

Cipta fail konfigurasi pengerasan SSH baharu:

```text
# Lumpuhkan log masuk root secara terus melalui SSH
PermitRootLogin no

# Hadkan cubaan log masuk gagal kepada maksimum 3 kali
MaxAuthTries 3

# Nyahaktifkan pengesahan kata laluan selepas memastikan akses kunci SSH telah diuji dan berfungsi
PasswordAuthentication no
```

Lakukan semakan sintaks terlebih dahulu sebelum memuat semula perkhidmatan SSH daemon:

```bash
# 1. Uji kesahan sintaks konfigurasi SSH
sudo sshd -t

# 2. Jika tiada ralat sintaks, muat semula perkhidmatan mengikut edaran:
# Untuk Ubuntu / Debian:
sudo systemctl restart ssh.service

# Untuk AlmaLinux 10 / Fedora 43:
sudo systemctl restart sshd.service
```

---

### 3. Auditing & Semakan Log Keselamatan

```bash
# Semak perkhidmatan sistem yang gagal
systemctl --failed

# Semak log ralat dan keselamatan sistem
sudo journalctl -p err..emerg -n 20
```

---

## 🔒 Pematuhan Keselamatan JDN / MAMPU & ISO/IEC 27001

1. **Prinsip Kebenaran Minimum (Least Privilege):** HANYA buka port rangkaian yang diperlukan secara khusus untuk perkhidmatan perniagaan.
2. **Pengasingan Akaun Root:** Pengguna TIDAK BOLEH log masuk secara terus sebagai `root` melalui SSH; wajib gunakan akaun individu dan `sudo`.

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)

- [ ] Berjaya mengkonfigurasi UFW atau firewalld dengan polisi `deny incoming`.
- [ ] Berjaya melumpuhkan `PermitRootLogin` dalam konfigurasi SSH daemon.
- [ ] Berjaya menyemak log ralat sistem menggunakan `journalctl`.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Bagaimanakah cara mengkonfigurasi fail2ban untuk melindungi pelayan SSH daripada serangan brute-force secara automatik?"*
2. *"Terangkan perbezaan antara mod Enforcing dan Permissive pada SELinux / AppArmor."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Garis Panduan Pengerasan Keselamatan OpenSSH](https://www.openssh.com/)
- [Panduan Keselamatan UFW Canonical Ubuntu](https://ubuntu.com/server/docs/security-firewall)
- [Pekeliling Keselamatan ICT Jabatan Digital Negara (JDN) / MAMPU](https://www.jdn.gov.my/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **Linux Security Fundamentals** oleh Ben Whaley.
- **UNIX and Linux System Administration Handbook, 5th Edition** oleh Evi Nemeth et al.
- **Nota Pentadbiran & Keselamatan Sistem Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
