---
okf_version: 0.1
type: knowledge_node
title: "Tugasan Pasca-Pemasangan, Pemacu Peranti & Penegasan Keselamatan"
timestamp: "2026-08-16T12:15:00Z"
topics: ["post-installation", "package-management", "gpu-drivers", "system-hardening", "user-management", "cu01"]
tags: ["linux", "post-install", "apt", "dnf", "nvidia", "security", "cu01", "noss"]
description: "Panduan amali tugasan pasca-pemasangan: pengurusan repositori pakej (apt/dnf), pemasangan pemacu GPU, penetapan akaun pengguna, dan penegasan keselamatan asas."
resource: "file:///manual/cu01/pasca-pemasangan-dan-driver.md"
---

# 🛠️ Tugasan Pasca-Pemasangan, Pemacu Peranti & Penegasan Keselamatan

> *"Pemasangan OS yang baru selesai hanyalah kanvas kosong; penegasan keselamatan dan konfigurasi pemacu peranti menentukan kebolehgunaannya di persekitaran pengeluaran."*

Selepas proses pemasangan sistem operasi Linux selesai dan sistem dibut semula buat kali pertama, pentadbir sistem perlu menyempurnakan beberapa tugasan amali pasca-pemasangan (*post-installation tasks*) untuk memastikan sistem sentiasa dikemaskini, berprestasi tinggi, dan selamat.

---

## 1. Kemaskini Repositori & Pakej Perisian

Pengurusan pakej berbeza mengikut keluarga edaran Linux:

### Keluarga Debian / Ubuntu (`apt`):
```bash
# Kemaskini indeks repositori dan naik taraf pakej sistem
sudo apt update && sudo apt upgrade -y

# Bersihkan pakej yang tidak diperlukan lagi
sudo apt autoremove -y && sudo apt clean
```

### Keluarga Red Hat / AlmaLinux / Fedora (`dnf`):
```bash
# Kemaskini indeks repositori dan naik taraf pakej
sudo dnf check-update
sudo dnf upgrade -y

# Bersihkan simpanan cache DNF
sudo dnf clean all
```

---

## 2. Pemasangan Pemacu Grafik Proprietary (Nvidia / AMD)

Untuk stesen kerja grafik (CAD, pemprosesan video, atau pembelajaran mesin AI):

### Pada Ubuntu 26.04 LTS:
```bash
# Semak kad grafik dan pemacu yang disyorkan
ubuntu-drivers devices

# Pasang pemacu proprietary Nvidia secara automatik
sudo ubuntu-drivers install

# Reboot sistem
sudo reboot
```

### Pada AlmaLinux 10 / Fedora 43:
```bash
# Aktifkan repositori RPM Fusion Non-Free
sudo dnf install https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-10.noarch.rpm \
                    https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-10.noarch.rpm -y

# Pasang pemacu grafik Nvidia
sudo dnf install akmod-nvidia xorg-x11-drv-nvidia-cuda -y
```

---

## 3. Pengurusan Pengguna & Kebenaran `sudo`

Menambah akaun pengguna baharu untuk kakitangan pejabat dan memberikan akses pentadbir berjadual melalui `sudo` (Rule 3 DBP / English command parameters):

```bash
# 1. Cipta pengguna baharu (contoh: user 'ali')
sudo useradd -m -s /bin/bash ali

# 2. Tetapkan kata laluan tegar untuk pengguna ali
sudo passwd ali

# 3. Masukkan pengguna ke kumpulan pentadbir
# Pada Ubuntu: kumpulan 'sudo'
sudo usermod -aG sudo ali

# Pada AlmaLinux / Fedora: kumpulan 'wheel'
sudo usermod -aG wheel ali
```

---

## 4. Penegasan Keselamatan Asas (Initial Hardening)

### A. Konfigurasi Tembok Api (*Firewall*):
```bash
# Untuk Ubuntu (UFW - Uncomplicated Firewall):
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp comment 'SSH Access'
sudo ufw enable
sudo ufw status verbose

# Untuk AlmaLinux / Fedora (Firewalld):
sudo systemctl enable --now firewalld
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
sudo firewall-cmd --list-all
```

### B. Keselamatan SSH Daemon (`/etc/ssh/sshd_config.d/99-hardening.conf`):
```text
# Lumpuhkan log masuk root secara terus melalui SSH
PermitRootLogin no

# Hadkan cubaan log masuk gagal
MaxAuthTries 3

# Niahaktifkan autentikasi kata laluan jika menggunakan kunci SSH
PasswordAuthentication yes
```

```bash
# Muat semula perkhidmatan SSH
sudo systemctl restart sshd
```

---

## 5. Pengesahan Ringkasan Persekitaran Pasca-Pemasangan

Gunakan alatan diagnostik sistem berikut untuk verifikasi akhir:

```bash
# Semak maklumat ringkasan sistem
fastfetch || neofetch || hostnamectl

# Semak perkhidmatan sistem yang gagal
systemctl --failed

# Semak log keselamatan sistem
sudo journalctl -p err..emerg -n 20
```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
