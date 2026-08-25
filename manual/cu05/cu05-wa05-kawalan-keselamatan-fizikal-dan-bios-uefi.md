---
okf_version: 0.2
type: knowledge-node
title: "Kawalan Keselamatan Fizikal & Persekitaran Console Endpoint Linux (CU05-WA05)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu05", "wa05", "panduan-amali", "manual-linux", "security-lockdown"]
tags: ["cu05", "wa05", "linux", "noss", "amali", "physical-security", "lockdown", "tmout", "grub", "systemd", "luks2", "uefi"]
description: "Panduan amali kawalan keselamatan fizikal, penguncian firmware UEFI/BIOS, penyulitan LUKS2, bootloader GRUB2, kawalan konsol maya VT, tamat masa sesi TMOUT, dan penutupan selamat."
resource: "file:///manual/cu05/cu05-wa05-kawalan-keselamatan-fizikal-dan-bios-uefi.md"
---

# Kawalan Keselamatan Fizikal & Persekitaran Console Endpoint Linux (CU05-WA05)

## 🎯 Objektif Pembelajaran

Mengurangkan risiko capaian fizikal tidak sah menerusi penegasan firmware UEFI/BIOS, penyulitan cakera penuh LUKS2, perlindungan bootloader GRUB2, sekatan konsol maya (Virtual Terminals getty@tty), kawalan tamat masa sesi shell (`TMOUT`), dan kawalan penutupan sistem selamat mengikut piawaian **NOSS CU05 WA05** dan penanda aras **CIS Benchmarks / JDN MAMPU**.

> [!NOTE]
> Modul ini dipetakan daripada Unit Kompetensi **CU05 (Kawalan Keselamatan Endpoint & Audit)** bagi Aktiviti Kerja **WA05 (Manage Physical Endpoint Security Lockdowns)** pada **Ubuntu 26.04 LTS "Resolute Raccoon"** dan **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Prosedur & Arahan Amali

### 1. Penegasan Firmware UEFI/BIOS & Penyulitan Cakera LUKS2

- **Penguncian Firmware UEFI/BIOS:** Tetapkan kata laluan pentadbir UEFI/BIOS dan matikan kebolehan boot dari USB/peranti luaran untuk menghalang pelancaran live OS tanpa kebenaran.
- **Penyulitan Cakera Penuh LUKS2:** Pastikan partition sistem disulitkan dengan LUKS2 untuk melindungi data berehat (*data-at-rest*).
  ```bash
  # Semak status penyulitan LUKS2 pada peranti blok sistem
  sudo cryptsetup status /dev/mapper/dm_crypt-0
  ```

### 2. Perlindungan Bootloader GRUB2 dengan Kata Laluan

Melarang pengubahsuaian parameter isirung (`init=/bin/bash` atau `single`) di menu bootloader tanpa pengesahan pentadbir.

- **Pada AlmaLinux 10 / Fedora 43:**
  ```bash
  sudo grub2-setpassword
  sudo grub2-mkconfig -o /boot/grub2/grub.cfg
  ```

- **Pada Ubuntu 26.04 LTS:**
  ```bash
  # Hasilkan PBKDF2 hash kata laluan
  grub-mkpasswd-pbkdf2

  # Tambahkan konfigurasi pengguna superuser di /etc/grub.d/40_custom
  # cat << 'EOF' | sudo tee -a /etc/grub.d/40_custom
  # set superusers="admin"
  # password_pbkdf2 admin grub.pbkdf2.sha512...
  # EOF

  # Kemas kini konfigurasi GRUB2
  sudo update-grub
  ```

### 3. Penguatkuasaan Tamat Masa Sesi Terminal Otomatik (`TMOUT`)

Mengunci atau menamatkan sesi terminal tidak aktif secara automatik selepas 15 minit (900 saat).

```bash
# Cipta fail skrip penguatkuasaan TMOUT secara global
cat << 'EOF' | sudo tee /etc/profile.d/timeout.sh
readonly TMOUT=900
export TMOUT
EOF
sudo chmod +x /etc/profile.d/timeout.sh
```

### 4. Kawalan Konsol Maya (Virtual Terminals) & Had Sumber

```bash
# Matikan perkhidmatan getty pada VT yang tidak digunakan (contoh: tty3)
sudo systemctl disable --now getty@tty3.service
sudo systemctl mask getty@tty3.service

# Prosedur pemulihan (rollback) jika tty3 diperlukan semula:
# sudo systemctl unmask getty@tty3.service
# sudo systemctl enable --now getty@tty3.service

# Konfigurasi had sumber sistem di /etc/security/limits.conf
# Menyertakan larangan coredump dan had maxlogins
cat << 'EOF' | sudo tee -a /etc/security/limits.conf
*          hard    core            0
*          hard    maxlogins       3
EOF
```

### 5. Prosedur Penutupan & Ulang But Selamat

Arahan penutupan terjadual dan penutupan serta-merta adalah pilihan alternatif mengikut keperluan operasi:

```bash
# Pilihan A: Hantar mesej amaran dan jadualkan penutupan sistem secara teratur
sudo shutdown -h +2 "Penyelenggaraan sistem fizikal dalam masa 2 minit."

# Pilihan B: Matikan sistem serta-merta menggunakan systemd
sudo systemctl poweroff
```

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)

- [ ] Verifikasi kuncian UEFI/BIOS dan penyulitan cakera LUKS2.
- [ ] Pengesahan perlindungan kata laluan pada menu bootloader GRUB2.
- [ ] Penguatkuasaan pembolehubah `TMOUT` terbukti berfungsi pada shell bash.
- [ ] Pengurusan unit `getty@ttyN.service` dan penegasan `/etc/security/limits.conf`.
- [ ] Penggunaan alternatif prosedur penutupan selamat (`shutdown` vs `systemctl poweroff`).

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Bagaimanakah cara mengunci firmware UEFI/BIOS pada perkakasan pelayan pelbagai vendor (Dell, HP, Lenovo) secara automatik?"*
2. *"Terangkan kesan penetapan maxlogins dalam /etc/security/limits.conf terhadap sesi SSH dan Konsol."*
3. *"Tulis skrip periksa pematuhan CIS Benchmark untuk keselamatan bootloader dan kawalan konsol fizikal."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Ubuntu Security Lockdowns Guide](https://ubuntu.com/server/docs/security)
- [AlmaLinux Hardening & Physical Security](https://wiki.almalinux.org/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **Hardening Linux System Security** oleh Chey Cobb.
- **Panduan Penegasan Keselamatan Fizikal Pelayan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
