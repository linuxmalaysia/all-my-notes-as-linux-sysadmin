---
okf_version: 0.1
type: knowledge_node
title: "Prosedur Pemasangan Ubuntu 26.04 LTS, AlmaLinux 10 & Fedora 43"
timestamp: "2026-08-16T12:05:00Z"
topics: ["installation-procedure", "ubuntu-installation", "almalinux-installation", "fedora-installation", "lvm", "partitioning", "cu01"]
tags: ["linux", "installation", "ubuntu", "almalinux", "fedora", "lvm", "cu01", "noss"]
description: "Panduan amali langkah demi langkah pemasangan sistem operasi Linux (Ubuntu 26.04 LTS, AlmaLinux 10, Fedora 43) serta strategi pembahagian cakeran LVM."
resource: "file:///manual/cu01/prosedur-pemasangan-ubuntu-almalinux.md"
---

# 📀 Prosedur Pemasangan Ubuntu 26.04 LTS, AlmaLinux 10 & Fedora 43

> *"Langkah pertama pentadbir sistem profesional ialah mereka bentuk skema pembahagian storan yang mampan dan boleh dikembangkan."*

Dokumen ini menyediakan panduan terperinci langkah demi langkah untuk proses pemasangan sistem operasi Linux menggunakan tiga edaran kanonik rujukan utama NOSS Malaysia: **Ubuntu 26.04 LTS "Quetzal"** (Desktop/Latihan), **AlmaLinux 10 "Purple Lion"** (Pelayan Perusahaan), dan **Fedora 43** (Bleeding-Edge Workstation).

---

## 1. Strategi Pembahagian Storan Piawai (Partitioning Strategy)

Dalam persekitaran latihan NOSS Level 3 dan pengeluaran pejabat, penggunaan **LVM (Logical Volume Manager)** adalah sangat disyorkan berbanding partition fizikal statik.

### Skema Storan Rujukan (Cakera 100 GB SSD/NVMe)
| Titik Lekap (Mount Point) | Jenis Sistem Fail | Saiz Disyorkan | Keterangan / Fungsi |
| :--- | :--- | :--- | :--- |
| `/boot/efi` | `vfat` (FAT32) | 1,024 MB (1 GB) | Partition Sistem EFI untuk pemuat but UEFI (`shim` & `grub2`) |
| `/boot` | `ext4` / `xfs` | 2,048 MB (2 GB) | Mengandungi fail isirung Linux (`vmlinuz`) & `initramfs` |
| **LVM Volume Group (`vg_system`)** | LVM Physical Volume | Baki Ruang Storan (~97 GB) | Kumpulan Isipadu Logikal LVM |
| ├── `lv_root` (`/`) | `ext4` (Ubuntu) / `xfs` (AlmaLinux) | 30,000 MB (30 GB) | Sistem fail punca (Root OS binaries & libraries) |
| ├── `lv_var` (`/var`) | `ext4` / `xfs` | 20,000 MB (20 GB) | Fail berubah (Log sistem, pangkalan data, fail pelayan web) |
| ├── `lv_home` (`/home`) | `ext4` / `xfs` | 30,000 MB (30 GB) | Storan dokumen & direktori profil pengguna |
| └── `lv_swap` (`swap`) | `swap` | 8,192 MB (8 GB) | Ruang memori maya (Virtual Swap Space) |

---

## 2. Prosedur Pemasangan Ubuntu 26.04 LTS "Quetzal"

1. **Boot daripada USB Live:**
   - Masukkan pemacu USB Live Ubuntu 26.04 LTS dan pilih menu `Try or Install Ubuntu`.
2. **Pilihan Bahasa & Susun Atur Papan Kekunci:**
   - Pilih `Bahasa Melayu` atau `English (US)` untuk sistem, dan `English (US)` untuk papan kekunci.
3. **Pilihan Jenis Pemasangan (Interactive vs Automated):**
   - Pilih `Interactive Installation` → `Default Selection` (Aplikasi asas pejabat dan utiliti).
4. **Pemasangan Perisian Pihak Ketiga & Pemacu:**
   - Tandakan pilihan `Install third-party software for graphics and Wi-Fi hardware` dan `Download & install support for additional media formats`.
5. **Konfigurasi Storan & Pembahagian manual (Manual Partitioning):**
   - Pilih `Manual Partitioning` (atau `Advanced Features` → `Use LVM`).
   - Cipta `/boot/efi` (1 GB, FAT32).
   - Cipta `/boot` (2 GB, ext4).
   - Cipta Physical Volume (PV) LVM untuk baki ruang dan bentuk Volume Group `vg_system`.
   - Bahagikan Logical Volume (`lv_root`, `lv_var`, `lv_home`, `lv_swap`).
6. **Akaun Pengguna & Zon Masa:**
   - Tetapkan Zon Masa kepada `Asia/Kuala_Lumpur`.
   - Masukkan Nama Pengguna (contoh: `sysadmin`) dan Kata Laluan Tegar.
7. **Selesai & But Semula:**
   - Tunggu proses pemasangan selesai, cabut pemacu USB apabila diarahkan, dan tekan `Enter` untuk boot semula.

---

## 3. Prosedur Pemasangan AlmaLinux 10 "Purple Lion"

1. **Boot Pemuat But Anaconda:**
   - Masukkan media ISO AlmaLinux 10 dan pilih `Install AlmaLinux 10.0`.
2. **Pemilihan Bahasa:**
   - Pilih `English (United States)` / `Bahasa Melayu`.
3. **Papan Pemuka Pemasangan (Installation Summary):**
   - **Software Selection:** Pilih `Server with GUI` untuk persekitaran makmal latihan atau `Minimal Install` untuk pelayan pengeluaran.
   - **Installation Destination:**
     - Pilih disk sasaran.
     - Di bawah *Storage Configuration*, pilih `Custom`.
     - Tetapkan skema ke `LVM`.
     - Cipta `/boot/efi` (1 GB, Standard Partition, xfs/vfat).
     - Cipta `/boot` (2 GB, Standard Partition, xfs).
     - Baki ruang diletakkan bawah LVM VG `almalinux` dan dipisahkan kepada `/` (xfs), `/home` (xfs), `/var` (xfs), dan `swap`.
   - **Network & Host Name:**
     - Tetapkan Hostname (contoh: `srv-noss01.my`).
     - Aktifkan kad rangkaian (Ethernet / Wi-Fi).
   - **Root Password & User Creation:**
     - Tetapkan kata laluan `root`.
     - Cipta akaun pentadbir pengguna biasa (tandakan `Make this user administrator` untuk akses `sudo`).
4. **Mulakan Pemasangan (Begin Installation):**
   - Klik `Begin Installation`. Setelah selesai, klik `Reboot System`.

---

## 4. Prosedur Pemasangan Fedora 43 (Workstation / Btrfs)

1. **Boot Fedora Live Desktop:**
   - Jalankan `Install to Hard Drive` daripada desktop GNOME 48 Fedora 43.
2. **Pengurusan Partition Btrfs Lalai:**
   - Fedora 43 secara lalai menggunakan **Btrfs** dengan subvolume (`@` untuk `/` dan `@home` untuk `/home`).
   - Bagi kegunaan stesen kerja pembangun, model subvolume Btrfs membolehkan ciri tangkapan skrin pantas (*snapshots*) menggunakan utiliti `snapper` atau `timeshift`.

---

## 5. Pengesahan Pasca-Pemasangan Storan

Setelah but semula ke dalam sistem baharu, jalankan perintah berikut di terminal untuk memverifikasi struktur LVM dan sistem fail:

```bash
# Memeriksa Physical Volume LVM
sudo pvs

# Memeriksa Volume Group LVM
sudo vgs

# Memeriksa Logical Volume LVM
sudo lvs

# Memeriksa status lekapan sistem fail & ruang tersedia
df -hT

# Memeriksa entri automatik lekapan sistem
cat /etc/fstab
```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
