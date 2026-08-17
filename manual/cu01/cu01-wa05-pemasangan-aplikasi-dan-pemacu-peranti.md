---
okf_version: 0.1
type: knowledge-node
title: "CU01-WA05: Pemasangan Aplikasi & Pemacu Peranti Linux"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu01", "wa05", "pengurusan-pakej", "pemacu-peranti", "editor", "bashrc"]
tags: ["cu01", "wa05", "apt", "dnf", "flatpak", "snap", "nvidia", "driver", "editor", "bashrc"]
description: "Panduan amali NOSS CU01-WA05 bagi pengurusan pakej perisian (APT, DNF, Flatpak, Snap), penyesuaian pemboleh ubah persekitaran $EDITOR/$VISUAL, dan pemasangan pemacu peranti GPU/pemacu proprietari di Linux."
resource: "file:///manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md"
---

# CU01-WA05: Pemasangan Aplikasi & Pemacu Peranti Linux

## 🎯 Objektif Pembelajaran

Menguasai prosedur amali pengurusan aplikasi, pakej perisian, penyesuaian persekitaran shell, serta pemasangan dan konfigurasi pemacu peranti (*device drivers*) pada sistem operasi Linux desktop mengikut piawaian **NOSS Tahap 3 (CU01-WA05)**.

Setelah menyempurnakan modul ini, pelajar akan dapat:

1. Menguruskan repositori dan pakej perisian menggunakan pengurus pakej asli (**APT** pada Ubuntu 26.04 LTS, **DNF5** pada AlmaLinux 10 dan Fedora 43).
2. Memasang dan menguruskan aplikasi berasaskan kontena universal (**Flatpak** dan **Snap**).
3. Menguruskan pemboleh ubah persekitaran shell pengguna dan sistem (`$EDITOR`, `$VISUAL`, `/etc/environment`, `~/.bashrc`).
4. Mengesan, memasang, dan mengesahkan pemacu peranti proprietari dan terbuka (GPU NVIDIA, AMD Radeon, serta kad peranti rangkaian tanpa wayar).
5. Mematuhi garis panduan keselamatan Jabatan Digital Negara (JDN) / MAMPU dan ISO/IEC 27001 mengenai integriti perisian dan tandatangan digital (*GPG key verification*).

---

## 🛠️ Garis Panduan Amali & Prosedur Kerja

### 1. Pengurusan Pakej Asli (APT & DNF5)

#### A. Debian/Ubuntu (APT - Advanced Package Tool)

Pada **Ubuntu 26.04 LTS "Resolute Raccoon"**, pengurusan pakej dilakukan menggunakan arahan `apt`:

```bash
# 1. Kemas kini indeks repositori dan senaraikan pakej yang boleh dinaik taraf
sudo apt update

# 2. Naik taraf kesemua pakej sistem ke versi terkini secara selamat
sudo apt upgrade -y

# 3. Cari dan pasang aplikasi (contoh: cURL, Git, VLC, Vim, Nano)
sudo apt search vlc
sudo apt install -y curl git vlc vim nano

# 4. Buang pakej yang tidak diperlukan beserta fail konfigurasi sisa
sudo apt purge -y vlc
sudo apt autoremove -y
```

#### B. Red Hat/AlmaLinux/Fedora (DNF5 / DNF)

Pada **AlmaLinux 10 "Purple Lion"** dan **Fedora 43**, pengurus pakej generasi baharu **DNF5** digunakan:

```bash
# 1. Semak kemas kini pakej dan naik taraf sistem
sudo dnf check-upgrade || true
sudo dnf upgrade -y

# 2. Pasang aplikasi dan kumpulan perisian (Package Groups)
sudo dnf install -y htop wget vim nano
sudo dnf groupinstall -y "Development Tools"

# 3. Pengurusan repositori EPEL pada AlmaLinux 10
sudo dnf install -y epel-release
sudo dnf config-manager --enable epel
```

---

### 2. Pemasangan Pakej Universal (Flatpak & Snap)

Untuk aplikasi desktop moden yang terpencil (*sandboxed*) demi keselamatan persekitaran pejabat:

#### A. Flatpak (Flathub Repository)

```bash
# 1. Pastikan perkhidmatan Flatpak terpasang dan tambah repositori Flathub
sudo apt install -y flatpak   # Ubuntu
# sudo dnf install -y flatpak # AlmaLinux / Fedora

sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# 2. Pasang dan jalankan aplikasi (contoh: LibreOffice / GIMP)
flatpak install flathub org.gimp.GIMP -y
flatpak run org.gimp.GIMP
```

#### B. Snap (Ubuntu Canonical Ecosystem)

```bash
# 1. Semak status dan pasang aplikasi Snap
snap list
sudo snap install code --classic  # VS Code
sudo snap install chromium
```

---

### 3. Konfigurasi Pemboleh Ubah Persekitaran `$EDITOR` & `$VISUAL`

Pemboleh ubah persekitaran menentukan aplikasi lalai yang digunakan oleh utiliti sistem (seperti `git`, `crontab`, `visudo`) apabila membuka editor teks.

#### A. Konfigurasi Persekitaran Pengguna Indivdu (`~/.bashrc`)
Gunakan penyunting teks untuk menambah eksport pemboleh ubah dalam fail profil pengguna:

```bash
# Tetapkan Vim atau Nano sebagai editor CLI lalai pengguna
export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim

# Muat semula fail .bashrc untuk menguji perubahan
source ~/.bashrc

# Sahkan nilai pemboleh ubah persekitaran
echo $EDITOR
echo $VISUAL
```

#### B. Konfigurasi Persekitaran Sistem Global (`/etc/environment` & `/etc/profile.d/editor.sh`)
Untuk menetapkan penyunting lalai bagi kesemua pengguna pelayan/desktop sektor awam:

```bash
# 1. Menyunting /etc/environment (format kependudukan pemboleh ubah tetap):
# Tambahkan baris berikut menggunakan sudoedit:
EDITOR="/usr/bin/vim"
VISUAL="/usr/bin/vim"

# 2. Sebagai alternatif, cipta skrip profil global di /etc/profile.d/editor.sh:
sudo tee /etc/profile.d/editor.sh << 'EOF'
export EDITOR=/usr/bin/vim
export VISUAL=/usr/bin/vim
EOF

sudo chmod +x /etc/profile.d/editor.sh
```

---

### 4. Pengesanan & Pemasangan Pemacu Peranti (GPU & Rangkaian Tanpa Wayar)

#### A. Pengesanan Perkakasan Peranti

```bash
# Senaraikan peranti PCI (GPU, Rangkaian, Pengawal Storan)
lspci -nnk | grep -A3 -i vga
lspci -nnk | grep -A3 -i network

# Senaraikan peranti USB
lsusb

# Semak modul isirung (kernel modules) yang diloadkan
lsmod | grep -iE 'nvidia|amdgpu|iwlwifi'
```

#### B. Pemasangan Pemacu NVIDIA GPU pada Ubuntu 26.04 LTS

```bash
# 1. Kesan pemacu yang disyorkan oleh peranti
ubuntu-drivers devices

# 2. Pasang pemacu NVIDIA terkini secara automatik
sudo ubuntu-drivers install

# 3. Sahkan pemacu NVIDIA berfungsi selepas but semula
nvidia-smi
```

#### C. Pemasangan Pemacu NVIDIA pada Fedora 43 & AlmaLinux 10 (RPM Fusion)

```bash
# Untuk Fedora 43:
sudo dnf install -y https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install -y https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

# Untuk AlmaLinux 10:
# sudo dnf install -y https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-10.noarch.rpm
# sudo dnf install -y https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-10.noarch.rpm

# Pasang pemacu akmod-nvidia:
sudo dnf install -y akmod-nvidia xorg-x11-drv-nvidia-cuda
```

#### D. Pengesanan & Konfigurasi Pemacu AMD Radeon & Kad Rangkaian Tanpa Wayar

```bash
# Pemacu AMD Radeon (Sumber Terbuka disertakan secara asal dalam Isirung Linux):
sudo apt install -y mesa-vulkan-drivers mesa-utils   # Ubuntu
# sudo dnf install -y mesa-dri-drivers mesa-vulkan-drivers # AlmaLinux / Fedora
glxinfo | grep "OpenGL vendor"

# Pemacu Kad Rangkaian Tanpa Wayar (Wi-Fi Firmwares):
sudo apt install -y linux-firmware                   # Ubuntu
# sudo dnf install -y linux-firmware                 # AlmaLinux / Fedora
```

---

## 🔒 Pematuhan Keselamatan JDN / MAMPU & ISO/IEC 27001

1. **Verifikasi Kunci GPG APT:** Bagi repositori pihak ketiga pada sistem Debian/Ubuntu, gunakan fail kunci tersimpan di `/etc/apt/keyrings/` dengan opsyen `[signed-by=/etc/apt/keyrings/...]` dalam fail `.list` repositori.
2. **Pengesahan Kunci DNF:** Tetapkan `gpgcheck=1` pada semua repositori DNF untuk mengelakkan suntikan pakej yang tidak disahkan.
3. **Pakej Berdaftar Sahaja:** HANYA pasang perisian daripada repositori rasmi atau Flathub berverifikasi di komputer pejabat sektor awam.
4. **Audit Pemasangan:** Simpan log pemasangan di `/var/log/dpkg.log` atau `/var/log/dnf.log` sebagai sebahagian daripada audit keselamatan ISO 27001.

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)

- [ ] Berjaya mengemaskini repositori dan menaik taraf pakej sistem menggunakan APT dan DNF.
- [ ] Berjaya memasang aplikasi desktop menerusi Flatpak/Snap.
- [ ] Berjaya menetapkan pemboleh ubah persekitaran `$EDITOR` dan `$VISUAL` dalam `~/.bashrc` dan `/etc/environment`.
- [ ] Berjaya mengenal pasti cip grafik dan kad Wi-Fi menggunakan `lspci` serta memasang pemacu peranti berkaitan.
- [ ] Mengesahkan modul pemacu dimuatkan ke dalam isirung Linux (`lsmod` / `nvidia-smi` / `glxinfo`).

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Bandingkan kelebihan dan kekurangan seni bina pembungkusan pakej APT/RPM berbanding ketersendirian kontena Flatpak dan Snap dari sudut keselamatan sektor awam."*
2. *"Apakah perbezaan antara pemboleh ubah persekitaran $EDITOR dan $VISUAL mengikut standard POSIX dan utiliti Linux?"*
3. *"Tuliskan skrip Bash untuk menyemak sama ada pemacu peranti NVIDIA atau AMD telah dimuatkan dengan betul dalam Kernel Linux 6.14."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Dokumentasi Pengurusan Pakej Ubuntu](https://ubuntu.com/server/docs/package-management)
- [Dokumentasi Rasmi DNF5 Fedora / AlmaLinux](https://dnf5.readthedocs.io/)
- [Panduan Pengurusan Flathub](https://flathub.org/)
- [Garis Panduan Keselamatan Perisian MAMPU / JDN](https://www.jdn.gov.my/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **Linux Administration Handbook (Edisi Terkini)** oleh Evi Nemeth et al.
- **The Linux Command Line, 2nd Edition** oleh William Shotts.
- **Nota Pentadbiran Sistem Linux Malaysia** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
