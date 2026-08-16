---
okf_version: 0.1
name: cu01-wa04-install-computer-desktop-operating-systems
description: Kemahiran amali pemasangan sistem operasi Linux desktop — dikemaskini dengan prosedur terkini 2026 menggunakan Ubuntu 26.04 LTS, Fedora 43, dan AlmaLinux 10.
topics: [noss, cu01, wa04, linux-install, ubuntu, fedora, almalinux]
tags: [linux, pemasangan, desktop, ubuntu, almalinux, fedora, cu01, wa04]
type: procedural_skill
---

# CU01-WA04: Pemasangan Sistem Operasi Linux Desktop

## Tujuan Kemahiran
Kemahiran ini melengkapkan pelajar dengan prosedur pemasangan sistem operasi Linux desktop secara lengkap — daripada menyediakan media pemasangan hinggalah sistem siap digunakan sepenuhnya.

> **💡 Pemikiran Ke Belakang:** Matlamat akhir = sistem Linux fungsional untuk pengguna. Langkah terakhir = log masuk pertama. Maka kita mula dari pembinaan media USB → konfigurasi BIOS/UEFI → partition → pemasangan → but pertama.

---

## Prasyarat
- Sudah memahami ekosistem Linux (CU01-WA00)
- Pemacu kilat USB (minimum 8GB)
- Sambungan internet untuk muat turun fail ISO
- Komputer sasaran dengan ruang storan minimum 25GB

---

## Prosedur Pemasangan

### Fasa 1: Penyediaan Media Pemasangan

**Langkah 1: Muat turun fail ISO**
```bash
# Pilihan distribusi yang disyorkan:

# [1] Ubuntu 26.04 LTS "Quetzal" — DISYORKAN untuk latihan & pengguna umum
# URL: https://ubuntu.com/download/desktop
# SHA256: semak di https://ubuntu.com/download/desktop#verify
# Isirung: Linux 6.14 LTS | Persekitaran Meja: GNOME 48
# Sokongan: sehingga April 2031 (5 tahun)

# [2] AlmaLinux 10 "Purple Lion" (GNOME Desktop) — DISYORKAN untuk pejabat & persekitaran enterprise
# URL: https://almalinux.org/get-almalinux/#AlmaLinux_OS_10
# Pilih: AlmaLinux-10-latest-x86_64-dvd.iso  (DVD ISO, termasuk GNOME penuh)
# SHA256: semak di https://repo.almalinux.org/almalinux/10/isos/x86_64/
# Isirung: Linux 6.12 LTS (RHEL 10-stable) | Persekitaran Meja: GNOME 47
# Sokongan: sehingga 2035 (Enterprise Long-Term)
# Kelebihan: Serasi penuh RHEL 10 / RPM, sijil enterprise, sesuai persekitaran mixed-OS

# [3] Fedora Workstation 43 — Untuk teknologi terkini & pembangun
# URL: https://fedoraproject.org/workstation/download

# [4] Linux Mint 22.1 — Paling mesra pemula
# URL: https://linuxmint.com/download.php
```

**Langkah 2: Tulis ISO ke USB menggunakan Balena Etcher**
```
1. Muat turun Balena Etcher dari https://etcher.balena.io
2. Buka Etcher
3. Pilih "Flash from file" → pilih fail .iso
4. Pilih "Select target" → pilih pemacu USB anda
5. Klik "Flash!" dan tunggu sehingga selesai
```

**Alternatif CLI (Linux/macOS):**
```bash
# Gantikan /dev/sdX dengan pemacu USB anda (semak dengan lsblk)
sudo dd if=ubuntu-26.04-desktop-amd64.iso of=/dev/sdX bs=4M status=progress sync
```

---

### Fasa 2: Konfigurasi BIOS/UEFI

**Langkah 3: Boot dari USB**
```
1. Masukkan USB ke komputer
2. Hidupkan semula dan tekan kekunci BIOS:
   - Dell: F2 atau F12
   - HP: F9 atau F10  
   - Lenovo: F1 atau F12
   - ASUS: F2 atau Del
   - Acer: F2 atau Del
3. Dalam menu BIOS/UEFI:
   - Lumpuhkan Secure Boot (jika perlu)
   - Tetapkan urutan but: USB dahulu
4. Simpan dan keluar (F10)
```

---

### Fasa 3: Pemasangan Ubuntu 26.04 LTS "Quetzal"

**Langkah 4: Mulakan pemasangan**
```
1. Pilih "Try or Install Ubuntu 26.04 LTS"
2. Pilih bahasa: Bahasa Melayu (atau English)
3. Pilih "Install Ubuntu"
4. Sambungan WiFi (jika tersedia)
5. Jenis pemasangan:
   - ☑ Normal installation
   - ☑ Download updates while installing
   - ☑ Install third-party software (penting untuk pemacu!)

Nota Ubuntu 26.04 LTS (Quetzal):
  - Antara muka pemasang: Subiquity (versi terkini, lebih pantas)
  - Sokongan TPM-based Full Disk Encryption diaktifkan secara lalai
  - GNOME 48 dengan Wallpaper AI Generatif (opsional)
  - Snap Firefox dan beberapa aplikasi teras sudah pra-pasang
```

**Langkah 5: Penyulitan Cakera Penuh (Full Disk Encryption) — WAJIB Untuk Pejabat**

> **🔐 Dasar Keselamatan Pejabat:** Semua komputer pejabat yang menyimpan data kerajaan atau korporat MESTI menggunakan penyulitan cakera penuh (Full Disk Encryption / FDE) bagi mematuhi standard **ISO/IEC 27001** dan **Pekeliling Am Bil. 3 Tahun 2000 (MAMPU)**. Sekiranya komputer dicuri atau hilang, data tidak boleh diakses tanpa kata laluan penyulitan.

---

#### 5A. Kaedah GUI — Pilihan Pemasang Ubuntu (Paling Mudah)

Ubuntu 26.04 LTS menawarkan dua pilihan penyulitan melalui antara muka grafik pemasang:

**Pilihan 1: TPM-backed Encryption (Baharu di Ubuntu 26.04)**
```
→ Pilih "Erase disk and install Ubuntu"
→ Klik pilihan: "Advanced features..."
→ Pilih: ☑ "Use TPM-backed Full Disk Encryption" (DIUTAMAKAN untuk pejabat)

Kelebihan:
  ✅ Penyulitan diurus secara automatik melalui cip TPM 2.0
  ✅ Pengguna tidak perlu ingat frasa laluan (passphrase) tambahan
  ✅ Boot automatik jika cip TPM hadir dan sistem tidak diusik
  ✅ Selamat terhadap kecurian fizik

Prasyarat:
  - Komputer mesti mempunyai cip TPM 2.0 (hampir semua komputer pejabat 2020+)
  - UEFI Secure Boot mestilah aktif
```

**Pilihan 2: LUKS dengan Frasa Laluan Manual (Paling Selamat, Disyorkan untuk Data Sangat Sensitif)**
```
→ Pilih "Erase disk and install Ubuntu"
→ Klik: "Advanced features..."
→ Pilih: ☑ "Use LVM with the new Ubuntu installation"
→ TANDAKAN: ☑ "Encrypt the new Ubuntu installation for security"
→ Masukkan Kunci Keselamatan (Security key / LUKS passphrase):
  - Minimum 20 aksara
  - Gabungkan huruf besar, kecil, nombor, dan simbol khas
  - CONTOH FORMAT: PejabatKL-2026!Selamat#Linux
→ ☑ "Overwrite empty disk space" (untuk data yang padam tidak boleh dipulihkan)
```

---

#### 5B. Kaedah Manual LUKS — Partition Tersuai (Pentadbir Sistem Mahir)

Kaedah ini memberikan kawalan penuh dan fleksibiliti untuk senario penyebaran besar (mass deployment) di pejabat.

**Struktur partition yang disyorkan untuk desktop pejabat:**
```
┌──────────────────────────────────────────────────────────────────┐
│                    CAKERA FIZIKAL (SSD/HDD)                       │
├─────────┬──────────────────────────────────────────────────────────┤
│ 1 GB    │ /boot/efi  → EFI (TIDAK disulitkan — diperlukan untuk but)│
│ 1 GB    │ /boot      → ext4 (TIDAK disulitkan — kernel & initrd)    │
│ Baki    │ LUKS Container (DISULITKAN sepenuhnya)                   │
│         │   ├── LVM Volume Group                                   │
│         │   │     ├── 60 GB → / (root) — ext4                     │
│         │   │     ├── 2×RAM → swap (tersulit dalam LUKS)           │
│         │   │     └── Baki  → /home — ext4                        │
└─────────┴──────────────────────────────────────────────────────────┘
```

**Arahan terminal untuk setup LUKS manual:**
```bash
# ⚠️ AMARAN: Arahan berikut akan MEMADAMKAN semua data di cakera!
# Gantikan /dev/nvme0n1 dengan nama cakera anda (semak dengan: lsblk)

# 1. Buat partition menggunakan gdisk
sudo gdisk /dev/nvme0n1

# 2. Format dan aktifkan LUKS pada partition data utama
sudo cryptsetup luksFormat --type luks2 \
    --cipher aes-xts-plain64 \
    --key-size 512 \
    --hash sha512 \
    --iter-time 5000 \
    /dev/nvme0n1p3

# 3. Buka kontena LUKS
sudo cryptsetup luksOpen /dev/nvme0n1p3 pejabat-disk

# 4. Buat LVM di dalam kontena LUKS
sudo pvcreate /dev/mapper/pejabat-disk
sudo vgcreate vg-pejabat /dev/mapper/pejabat-disk
sudo lvcreate -L 60G -n lv-root vg-pejabat
sudo lvcreate -L 8G  -n lv-swap vg-pejabat
sudo lvcreate -l 100%FREE -n lv-home vg-pejabat

# 5. Format partition logik
sudo mkfs.ext4 /dev/vg-pejabat/lv-root
sudo mkfs.ext4 /dev/vg-pejabat/lv-home
sudo mkswap /dev/vg-pejabat/lv-swap
```

---

#### 5C. Penambahan Kunci Penyulitan untuk Pengguna Lain (Multi-User LUKS)

LUKS2 menyokong sehingga **32 slot kunci** — sesuai untuk persekitaran pejabat di mana lebih dari satu pentadbir perlu akses pemulihan.

```bash
# Lihat slot kunci sedia ada
sudo cryptsetup luksDump /dev/nvme0n1p3

# Tambah kunci pemulihan untuk Pentadbir IT (slot 1)
sudo cryptsetup luksAddKey /dev/nvme0n1p3
# (masukkan kunci sedia ada dahulu, kemudian kunci baharu pentadbir)

# Tambah fail kunci (keyfile) untuk pengguna tertentu — slot 2
sudo dd if=/dev/urandom bs=512 count=4 of=/root/keyfile-it.bin
sudo chmod 400 /root/keyfile-it.bin
sudo cryptsetup luksAddKey /dev/nvme0n1p3 /root/keyfile-it.bin

# Senarai semua slot kunci aktif
sudo cryptsetup luksDump /dev/nvme0n1p3 | grep ENABLED

# Cabut slot kunci jika pekerja berhenti (slot 2 sebagai contoh)
sudo cryptsetup luksKillSlot /dev/nvme0n1p3 2
```

> **⚠️ AMARAN PENTING:** Simpan sekurang-kurangnya satu kunci pemulihan (recovery key) dalam peti besi fizikal atau pengurus kata laluan berpusat seperti **Vault (HashiCorp)** atau **Bitwarden Enterprise**. Sekiranya semua kunci hilang, data TIDAK BOLEH dipulihkan.

---

**Langkah 6: Maklumat pengguna**
```
- Nama anda: [Nama Penuh]
- Nama komputer: [hostname-pejabat-ringkas]  # cth: ws-it-001-kl
- Nama pengguna: [pengguna-kecil-tanpa-spasi] # cth: ali.hassan
- Kata laluan: [minimum 16 aksara untuk akaun pejabat]
- ☑ Require password to log in
- ☑ Use Active Directory (jika domain pejabat tersedia)
```

---

### Fasa 4: Selepas Pemasangan

**Langkah 7: Kemas kini sistem (kewajiban)**
```bash
# Kemas kini semua pakej
sudo apt update && sudo apt upgrade -y

# Pasang alatan asas
sudo apt install -y \
    curl wget git vim \
    htop neofetch tree \
    build-essential

# Semak versi isirung
uname -r

# Semak maklumat sistem
neofetch
```

**Langkah 8: Konfigurasi bahasa Melayu (opsional)**
```bash
# Pasang sokongan bahasa Melayu
sudo apt install -y language-pack-ms language-pack-ms-base

# Kemaskini setempat (locale)
sudo update-locale LANG=ms_MY.UTF-8
```

---

### Fasa 5: Pemasangan AlmaLinux 10 "Purple Lion" Desktop (Pejabat & Enterprise)

> **🏢 Konteks Penggunaan:** AlmaLinux 10 desktop sesuai untuk persekitaran pejabat yang memerlukan keserasian dengan ekosistem Red Hat Enterprise Linux (RHEL 10), pengurusan pakej `dnf`/`rpm`, atau penggunaan perisian enterprise seperti IBM, Oracle, dan SAP yang diperakui pada platform RHEL-compatible.

**Ciri Khusus AlmaLinux 10 "Purple Lion" Desktop:**
```
✅ Serasi binari 1:1 dengan RHEL 10 (tanpa perlu langganan berbayar)
✅ Sokongan sehingga 2035 (lebih panjang dari AlmaLinux 9)
✅ SELinux diaktifkan secara lalai (keselamatan peringkat enterprise)
✅ Isirung 6.12 LTS — sokongan perkakasan terkini (PCIe 6, NVMe 2.0, GPU AI)
✅ Pengurus pakej DNF5 (lebih pantas dari DNF4 pada AlmaLinux 9)
✅ GNOME 47 dengan antara muka moden
✅ FIPS 140-3 compliance untuk agensi kerajaan
✅ Sokongan Rust-based kernel modules (keselamatan memori)
```

**Langkah A: Pemasangan melalui pemasang Anaconda (GUI)**
```
1. But dari USB → Pilih "Install AlmaLinux 10"
2. Pilih bahasa: English (United States) atau Malay
3. Dalam "Installation Summary":

   📦 SOFTWARE SELECTION:
   → Pilih: "Workstation" (atau "Custom Operating System" untuk minimal)
   → Tambahan: ☑ "GNOME Applications"
                ☑ "Office Suite and Productivity"
                ☑ "Development Tools" (jika diperlukan)

   💾 INSTALLATION DESTINATION:
   → Pilih cakera sasaran
   → "Storage Configuration": Custom
   → ☑ "Encrypt my data" (LUKS — WAJIB untuk pejabat)
   → Masukkan frasa laluan LUKS (minimum 20 aksara)

   🌐 NETWORK & HOSTNAME:
   → Tetapkan hostname: ws-alma-[nombor]-[lokasi]  # cth: ws-alma-001-kl
   → Aktifkan sambungan rangkaian

4. Klik "Begin Installation"
5. Tetapkan kata laluan root dan buat akaun pengguna pejabat
```

**Langkah B: Konfigurasi Selepas Pemasangan AlmaLinux 10**
```bash
# Kemas kini sistem
sudo dnf update -y

# DNF5 digunakan secara lalai pada AlmaLinux 10
# (sintaks arahan kekal sama, tetapi prestasi lebih pantas)

# Aktifkan repositori EPEL 10 (Extra Packages for Enterprise Linux)
sudo dnf install -y epel-release
sudo dnf update -y

# Pasang alatan pejabat asas
sudo dnf install -y \
    libreoffice \
    thunderbird \
    firefox \
    vlc \
    htop \
    neofetch \
    git curl wget

# Aktifkan Flatpak (untuk aplikasi yang tidak ada dalam repo)
sudo dnf install -y flatpak
sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# Semak status SELinux (seharusnya "enforcing" untuk pejabat)
getenforce
sudo sestatus
```

**Langkah C: Penyulitan LUKS pada AlmaLinux (Jika Tiada Semasa Pasang)**
```bash
# Semak sama ada penyulitan sudah aktif
lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT
sudo dmsetup status

# Semak maklumat LUKS pada partition (gantikan sda3 dengan partition anda)
sudo cryptsetup luksDump /dev/sda3

# Tambah kunci pemulihan untuk Pentadbir IT (multi-user slot)
sudo cryptsetup luksAddKey /dev/sda3
# Masukkan kunci sedia ada → masukkan kunci pentadbir baharu

# Semak semua slot kunci aktif
sudo cryptsetup luksDump /dev/sda3 | grep -A2 'Keyslot'
```

**Langkah D: Konfigurasi Bahasa Melayu pada AlmaLinux**
```bash
# Pasang sokongan locale Melayu
sudo dnf install -y glibc-langpack-ms

# Semak locale tersedia
locale -a | grep ms

# Tetapkan locale sistem ke Bahasa Melayu Malaysia
sudo localectl set-locale LANG=ms_MY.UTF-8
sudo localectl set-keymap ms  # papan kekunci standard Malaysia

# Sahkan perubahan
localectl status
```

**Langkah E: Senarai Semak Pengesahan AlmaLinux Desktop**
```bash
# Pengesahan lengkap selepas pemasangan
echo "=== Maklumat Sistem ==="     && hostnamectl
echo "=== Versi Isirung ==="       && uname -r
echo "=== Versi AlmaLinux ==="     && cat /etc/almalinux-release
echo "=== SELinux Status ==="      && getenforce
echo "=== Status LUKS ==="         && lsblk -o NAME,FSTYPE | grep -i crypt
echo "=== Ruang Storan ==="        && df -h /
echo "=== Rangkaian ==="           && ip addr show
echo "=== Repositori Aktif ==="    && sudo dnf repolist
```

---

## Pengesahan Kejayaan Pemasangan

```bash
# Senarai semak selepas pemasangan
echo "=== Maklumat Sistem ==="     && hostnamectl
echo "=== Versi Isirung ==="       && uname -r
echo "=== Ruang Storan ==="        && df -h /
echo "=== Memori ==="              && free -h
echo "=== Rangkaian ==="           && ip addr show

# Pengesahan LUKS (jika penyulitan diaktifkan)
echo "=== Status Penyulitan LUKS ==="
lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT | grep -E 'crypt|luks|dm-'
sudo dmsetup status

# Sahkan LUKS digunakan pada cakera sistem
sudo cryptsetup status $(lsblk -o NAME,FSTYPE | grep crypto | awk '{print $1}') 2>/dev/null || \
    echo "Semak secara manual: sudo cryptsetup luksDump /dev/<partition>"
```

Pemasangan dianggap berjaya apabila semua arahan di atas mengembalikan output yang sah.

---

## Rujukan

- [Panduan Rasmi Ubuntu 26.04 LTS](https://help.ubuntu.com)
- [Nota Keluaran Ubuntu 26.04](https://discourse.ubuntu.com/c/release/18)
- [Dokumentasi AlmaLinux 10](https://wiki.almalinux.org)
- [Nota Keluaran AlmaLinux 10](https://wiki.almalinux.org/release-notes/10.0.html)
- [Panduan Pemasangan AlmaLinux 10](https://wiki.almalinux.org/documentation/installation-guide.html)
- [AlmaLinux EPEL 10 Setup](https://wiki.almalinux.org/repos/Extras.html)
- [Dokumentasi Fedora 43](https://docs.fedoraproject.org)
- [Balena Etcher](https://etcher.balena.io)
- [Rufus (Windows)](https://rufus.ie) — Alternatif Etcher untuk Windows

---

*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
