---
okf_version: 0.1
type: knowledge-node
title: "Konfigurasi Teras Pelayan Linux & Pengurusan Perkhidmatan Systemd"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu03", "wa04", "systemd", "systemctl", "journalctl", "timedatectl", "chrony", "man", "editor", "bashrc"]
tags: ["cu03", "systemd", "systemctl", "journalctl", "chrony", "timedatectl", "man", "editor", "bashrc", "noss", "amali"]
description: "Panduan amali konfigurasi teras pelayan Linux, pengurusan unit perkhidmatan systemd, audit log journalctl, penyegerakan masa timedatectl/chrony, penyesuaian $EDITOR/$VISUAL, dan sistem dokumentasi man."
resource: "file:///manual/cu03/cu03-wa04-konfigurasi-teras-pelayan.md"
---

# Konfigurasi Teras Pelayan Linux & Pengurusan Perkhidmatan Systemd

## 🎯 Objektif Pembelajaran

Di akhir modul amali ini, pelatih TVET/NOSS akan dapat:

1. Menguruskan perkhidmatan teras pelayan menggunakan utiliti `systemctl` (mulakan, hentikan, daftar masuk automatik, sekat, dan muat semula pemula).
2. Membina dan menguruskan fail unit perkhidmatan kustom `systemd` (`/etc/systemd/system/*.service`) dengan penerapan parameter pengerasan keselamatan.
3. Melaksanakan pengauditation dan analisis log perkhidmatan secara terperinci menggunakan `journalctl`.
4. Menguruskan zon masa sistem dan penyegerakan masa berprestasi tinggi melalui `timedatectl` dan `chronyd`.
5. Menyelaraskan pemboleh ubah persekitaran shell pentadbiran pelayan (`$EDITOR`, `$VISUAL`, `/etc/environment`, `~/.bashrc`).
6. Memanfaatkan utiliti bantuan dokumentasi sistem Linux (`man`, `apropos`, `whatis`, `whereis`, `plocate`).

> [!NOTE]
> Modul ini dipetakan secara terus kepada standard NOSS **K622-XXX-3:2026-C03 (Server Setup) WA04: Perform Core Server Configurations**. Persekitaran rujukan utama ialah **Ubuntu 26.04 LTS "Resolute Raccoon"** dan **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Garis Panduan Amali & Prosedur

### 1. Keperluan Awal & Pra-Syarat

- Pelayan beroperasi pada **Ubuntu 26.04 LTS** atau **AlmaLinux 10**.
- Akses terminal sebagai pengguna yang mempunyai hak arahan `sudo`.
- Pakej perisian terpasang: `systemd`, `chrony`, `man-db`, `plocate`, `vim`, `nano`.

---

### 2. Pengurusan Perkhidmatan & Unit Servis dengan `systemctl`

Pengurus sistem `systemd` merupakan daemon init utama dalam Linux moden. Semua perkhidmatan, sasaran boot, dan soket diuruskan sebagai unit.

#### A. Arahan Asas Kawalan Perkhidmatan (`systemctl`)

```bash
# Semak status perkhidmatan SSH
sudo systemctl status sshd   # AlmaLinux / Fedora
# atau
sudo systemctl status ssh    # Ubuntu

# Mulakan, hentikan, dan muat semula perkhidmatan
sudo systemctl start sshd
sudo systemctl stop sshd
sudo systemctl restart sshd
sudo systemctl reload sshd   # Muat semula konfigurasi tanpa memutuskan sambungan aktif

# Mengaktifkan atau menyahaktifkan auto-start semasa boot
sudo systemctl enable sshd
sudo systemctl disable sshd

# Mengaktifkan dan memulakan perkhidmatan secara serentak
sudo systemctl enable --now sshd

# Menyekat (mask) perkhidmatan supaya tidak boleh dimulakan secara tidak sengaja
sudo systemctl mask legacy-service
sudo systemctl unmask legacy-service
```

#### B. Pengurusan Sasaran Boot (Target Units)

`systemd` menggantikan tahap larian (runlevel) tradisional dengan **Target Units**:

```bash
# Semak sasaran boot semasa
systemctl get-default

# Tukar sasaran boot lalai kepada mod CLI (multi-user.target) atau GUI (graphical.target)
sudo systemctl set-default multi-user.target

# Tukar sasaran boot serta-merta tanpa reboot
sudo systemctl isolate multi-user.target
```

---

### 3. Pembinaan Fail Unit Perkhidmatan Kustom (`systemd`)

Pembangunan aplikasi enterprise memerlukan penulisan unit servis terkawal di `/etc/systemd/system/`.

#### A. Contoh Fail Unit Servis Kustom dengan Pengerasan Keselamatan (`/etc/systemd/system/myapp.service`)

```ini
[Unit]
Description=Aplikasi Pengurusan Teras NOSS App
After=network.target remote-fs.target network-online.target nss-lookup.target
Wants=network-online.target

[Service]
Type=simple
User=nossapp
Group=nossapp
ExecStart=/usr/local/bin/myapp --config /etc/myapp/config.conf
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5s

# Parameter Pengerasan Keselamatan (Security Hardening JDN/MAMPU)
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true
NoNewPrivileges=true
CapabilityBoundingSet=CAP_NET_BIND_SERVICE
ReadWritePaths=/var/log/myapp /var/lib/myapp

[Install]
WantedBy=multi-user.target
```

#### B. Mengaktifkan Unit Servis Baharu

```bash
# Buat pengguna sistem khas tanpa akses kelompang interaktif
sudo useradd -r -s /sbin/nologin nossapp

# Muat semula daemon systemd untuk mengesan unit baharu
sudo systemctl daemon-reload

# Memulakan dan semak status
sudo systemctl enable --now myapp.service
sudo systemctl status myapp.service
```

---

### 4. Pengauditan Log Sistem & Perkhidmatan dengan `journalctl`

`journalctl` membaca log binari terpusat yang diuruskan oleh `systemd-journald`.

```bash
# Semak log perkhidmatan secara real-time (follow)
sudo journalctl -u sshd -f

# Filter log mengikut selang masa tertentu
sudo journalctl -u myapp.service --since "2026-08-17 00:00:00" --until "2026-08-17 12:00:00"

# Memaparkan log berkaitan ralat sahaja (Priority level 3 / ERR)
sudo journalctl -u myapp.service -p err..emerg

# Semak log sesi boot terkini
sudo journalctl -b

# Semak saiz penggunaan ruang cakera oleh journal log dan lakukan pembersihan
sudo journalctl --disk-usage
sudo journalctl --vacuum-size=500M
```

---

### 5. Penyesuaian Pemboleh Ubah Persekitaran Shell Pentadbiran (`$EDITOR` & `$VISUAL`)

Dalam pentadbiran pelayan, alatan CLI seperti `systemctl edit`, `visudo`, dan `crontab -e` bergantung secara automatik kepada pemboleh ubah persekitaran `$EDITOR` dan `$VISUAL`.

```bash
# 1. Penetapan profil pentadbir tempatan dalam ~/.bashrc:
export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim

# 2. Penetapan global untuk semua pentadbir pelayan dalam /etc/profile.d/editor.sh:
sudo tee /etc/profile.d/editor.sh << 'EOF'
export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim
EOF
sudo chmod +x /etc/profile.d/editor.sh

# 3. Uji penetapan editor lalai semasa menggunakan systemctl edit
sudo systemctl edit myapp.service
```

---

### 6. Konfigurasi Zon Masa & Penyegerakan Masa (`timedatectl` & `chrony`)

Ketepatan masa adalah kritikal bagi audit keselamatan ISO/IEC 27001 dan pengesyoran Jabatan Digital Negara (JDN).

#### A. Operasi Arahan `timedatectl`

```bash
# Semak status masa, zon masa, dan status NTP
timedatectl status

# Senaraikan zon masa yang sedia ada
timedatectl list-timezones | grep Asia/Kuala_Lumpur

# Tetapkan zon masa rasmi Malaysia
sudo timedatectl set-timezone Asia/Kuala_Lumpur

# Aktifkan penyegerakan masa berasaskan rangkaian (NTP)
sudo timedatectl set-ntp true
```

#### B. Konfigurasi Daemon Chrony (`chronyd`)

Fail konfigurasi `/etc/chrony/chrony.conf` (Ubuntu) atau `/etc/chrony.conf` (AlmaLinux):

```ini
# Rujukan Pelayan Masa Kebangsaan / Standard Pool
server my.pool.ntp.org iburst
server 0.asia.pool.ntp.org iburst
server 1.asia.pool.ntp.org iburst

# Kebenaran audit keselamatan & penyesuaian drift
driftfile /var/lib/chrony/drift
makestep 1.0 3
rtcsync
```

Semakan status penyegerakan:

```bash
# Pastikan perkhidmatan chrony aktif
sudo systemctl enable --now chronyd

# Semak sumber pelayan masa dan status ralat penyegerakan
chronyc sources -v
chronyc tracking
```

---

### 7. Bantuan Dokumentasi & Navigasi Sistem Linux

Sistem Linux menyediakan utiliti dokumentasi luar talian (*offline documentation*) yang komprehensif.

#### A. Halaman Panduan `man` (Manual Pages)

Halaman manual dibahagikan kepada 9 seksyen standard:
- **Seksyen 1:** Arahan Pengguna Global (cth: `ls`, `cd`, `ps`).
- **Seksyen 2:** Panggilan Sistem Isirung Kernel (cth: `fork`, `exec`).
- **Seksyen 3:** Panggilan Perpustakaan C (cth: `printf`).
- **Seksyen 4:** Fail Khas & Peranti (cth: `/dev/null`, `/dev/sda`).
- **Seksyen 5:** Format Fail Konfigurasi (cth: `/etc/passwd`, `/etc/fstab`).
- **Seksyen 6:** Permainan & Pembantu.
- **Seksyen 7:** Format Makro & Standard Sistem.
- **Seksyen 8:** Arahan Pentadbiran Sistem & Root (cth: `systemctl`, `fdisk`).
- **Seksyen 9:** Rutin Isirung (Kernel Routines).

```bash
# Membaca halaman man bagi perkhidmatan systemctl
man systemctl

# Membaca format fail konfigurasi fstab (Seksyen 5)
man 5 fstab

# Membaca arahan pentadbiran useradd (Seksyen 8)
man 8 useradd
```

#### B. Utiliti Carian Bantuan (`apropos`, `whatis`, `whereis`, `plocate`)

```bash
# Cari arahan berkaitan kata kunci menggunakan pangkalan data whatis
apropos "systemctl"
apropos "network configuration"

# Dapatkan gambaran ringkas satu baris fungsi arahan
whatis systemctl
whatis chronyd

# Cari lokasi fail binari, sumber, dan halaman man bagi sesuatu arahan
whereis systemctl
whereis chronyc

# Kemas kini pangkalan data fail dan cari lokasi fail dengan pantas
sudo updatedb
plocate chrony.conf
```

---

## 🔒 Pengerasan Keselamatan & Pematuhan JDN / MAMPU

1. **Prinsip Perkhidmatan Minimum (Service Minimisation):** Matikan dan *mask* semua perkhidmatan yang tidak diperlukan (seperti `telnet`, `ftp`, `rsh`) untuk mengurangkan permukaan serangan (*attack surface*).
2. **Pengasingan Hak Akses Unit Servis:** Setiap perkhidmatan kustom MESTI dijalankan di bawah akaun pengguna sistem berasingan (`/sbin/nologin` atau `/bin/false`).
3. **Audit Log Berpusat:** Log `journalctl` hendaklah dipastikan mempunyai kebenaran akses terhad (`/var/log/journal/`) dan dihantar ke pelayan log berpusat (Syslog/SIEM) untuk pematuhan ISO/IEC 27001.

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)

- [ ] Berjaya menguruskan status, mula, henti, dan auto-start perkhidmatan dengan `systemctl`.
- [ ] Berjaya menetapkan sasaran boot sistem (`multi-user.target`).
- [ ] Berjaya menulis, menguji, dan memuat semula fail unit servis kustom di `/etc/systemd/system/`.
- [ ] Berjaya membuat analisis log perkhidmatan secara terperinci berasaskan julat masa menggunakan `journalctl`.
- [ ] Berjaya mengkonfigurasi pemboleh ubah `$EDITOR` dan `$VISUAL` bagi perkhidmatan pentadbiran pelayan.
- [ ] Berjaya menetapkan zon masa `Asia/Kuala_Lumpur` dan mengesahkan penyegerakan masa `chronyc tracking`.
- [ ] Berjaya mengendalikan carian dokumentasi sistem menggunakan `man`, `apropos`, `whatis`, dan `plocate`.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Jelaskan langkah-langkah mereka bentuk fail unit systemd drop-in override (/etc/systemd/system/service.d/override.conf) untuk mengubah had memori tanpa mengubah fail unit asal."*
2. *"Bagaimanakah pemboleh ubah persekitaran $EDITOR mempengaruhi tingkah laku arahan systemctl edit dan visudo?"*
3. *"Berikan arahan journalctl komprehensif untuk mengesan percubaan pencerobohan SSH yang gagal pada persekitaran pelayan Ubuntu 26.04 LTS."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Systemd Official Documentation & Index](https://systemd.io/)
- [Ubuntu Server Guide - Systemd Services](https://ubuntu.com/server/docs)
- [AlmaLinux 10 System Administration & Chrony Guide](https://wiki.almalinux.org/)
- [Freedesktop.org - Journalctl Reference](https://www.freedesktop.org/software/systemd/man/journalctl.html)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **Linux System Programming** oleh Robert Love.
- **The Linux Command Line (2nd Edition)** oleh William Shotts.
- **Panduan Praktikal Pentadbiran Pelayan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
