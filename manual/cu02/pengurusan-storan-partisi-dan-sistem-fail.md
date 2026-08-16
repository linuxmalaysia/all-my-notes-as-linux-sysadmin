---
okf_version: 0.1
type: knowledge-node
title: "CU02: Pengurusan Storan, Partisi GPT, LVM2 & Sistem Fail Linux"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu02", "storan", "lvm2", "gpt", "sistem-fail"]
tags: ["cu02", "linux", "noss", "partisi", "gdisk", "parted", "lvm", "ext4", "xfs", "btrfs"]
description: "Panduan amali komprehesif bagi pengurusan storan fizikal dan logikal, jadual partisi GPT, LVM2 (PV/VG/LV), sistem fail EXT4/XFS/Btrfs, /etc/fstab, dan penyulitan LUKS2 mengikut NOSS CU02."
resource: "file:///manual/cu02/pengurusan-storan-partisi-dan-sistem-fail.md"
---

# CU02: Pengurusan Storan, Partisi GPT, LVM2 & Sistem Fail Linux

## 🎯 Objektif Pembelajaran
Menguasai prosedur amali pengurusan storan fizikal dan logikal pada Linux mengikut piawaian **NOSS Tahap 3 (CU02)**.

Setelah menyempurnakan modul amali ini, pelajar akan dapat:
1. Menganalisis dan mengecam peranti storan blok menggunakan alatan `lsblk`, `blkid`, dan `fdisk -l`.
2. Menjana jadual partisi **GPT (GUID Partition Table)** menggunakan `gdisk` dan `parted` (menggantikan MBR/fdisk lama).
3. Menguruskan Pengurusan Volum Logikal **LVM2** (*Physical Volumes*, *Volume Groups*, *Logical Volumes*) serta peluasan volum secara dalam talian (*online volume expansion*).
4. Format sistem fail moden (**EXT4**, **XFS**, **Btrfs**) dan mengkonfigurasi pautan kekal di `/etc/fstab` menggunakan `UUID`.
5. Melaksanakan penyulitan storan peringkat blok **LUKS2** untuk pematuhan **ISO/IEC 27001** dan **Pekeliling Am Jabatan Digital Negara (JDN) / MAMPU**.

---

## 🛠️ Garis Panduan Amali & Prosedur Kerja

### 1. Pemerhatian & Analisis Cakera Storan Blok
Gunakan arahan berikut untuk memeriksa peranti blok yang disambungkan pada sistem:

```bash
# 1. Senaraikan peranti blok, saiz, dan titik lekap (mount points)
lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINTS

# 2. Semak UUID (Universally Unique Identifier) bagi setiap blok
sudo blkid

# 3. Semak saiz penggunaan ruang cakera sistem fail secara mesra manusia
df -hT
```

---

### 2. Pembahagian Partisi GPT (GUID Partition Table)
Modenkan sistem storan daripada MBR (had 2TB, maksimum 4 partisi utama) kepada **GPT** (menyokong sehingga 9.4 ZB dan 128 partisi):

#### A. Menggunakan `gdisk` (CLI Interaktif untuk GPT)
```bash
# Buka peranti cakera baharu (contoh: /dev/sdb atau /dev/nvme1n1)
sudo gdisk /dev/sdb

# Arahan interaktif gdisk:
# n  -> Tambah partisi baharu
# Partition number: 1
# First sector: [Default]
# Last sector: +20G  (Mencipta partisi 20 GB)
# Hex code or GUID: 8e00 (Linux LVM) atau 8300 (Linux filesystem)
# w  -> Tulis jadual partisi ke cakera dan keluar
```

#### B. Menggunakan `parted` (Mod Skrip / Non-Interactive)
```bash
# 1. Cipta label jadual partisi GPT baharu pada cakera
sudo parted /dev/sdb mklabel gpt

# 2. Cipta partisi utama 10GB untuk LVM
sudo parted -a optimal /dev/sdb mkpart primary 1MiB 10GiB
sudo parted /dev/sdb set 1 lvm on
```

---

### 3. Pengurusan Volum Logikal (LVM2 - Logical Volume Management)

LVM2 membolehkan pengurusan storan fleksibel yang boleh digabung, dibesarkan, atau dipotong tanpa menghentikan perkhidmatan.

```
+------------------------------------------------------------------+
|                   Logical Volume (LV): /dev/vg_data/lv_storan    |
+------------------------------------------------------------------+
|                     Volume Group (VG): vg_data                   |
+------------------------------------------------------------------+
| Physical Volume (PV): /dev/sdb1  |  Physical Volume (PV): /dev/sdc1|
+------------------------------------------------------------------+
```

#### Step 1: Cipta Physical Volumes (PV)
```bash
sudo pvcreate /dev/sdb1 /dev/sdc1
sudo pvs
```

#### Step 2: Cipta Volume Group (VG)
```bash
# Cipta Volume Group dinamakan 'vg_data' menggabungkan kedua-dua PV
sudo vgcreate vg_data /dev/sdb1 /dev/sdc1
sudo vgs
```

#### Step 3: Cipta Logical Volume (LV) & Luaskan Secara Dinamik
```bash
# 1. Cipta Logical Volume bernilai 15GB dinamakan 'lv_storan'
sudo lvcreate -L 15G -n lv_storan vg_data
sudo lvs

# 2. Peluasan LV secara dalam talian (Online Expansion +10G)
sudo lvextend -L +10G /dev/vg_data/lv_storan
```

---

### 4. Format Sistem Fail (EXT4, XFS, Btrfs) & Pemasangan Kekal (`/etc/fstab`)

#### A. Format Sistem Fail
```bash
# Format EXT4 (Sesuai untuk Linux am/desktop)
sudo mkfs.ext4 -L "DATA_EXT4" /dev/vg_data/lv_storan

# Format XFS (Sesuai untuk Pelayan Perusahaan AlmaLinux 10 / Pangkalan Data)
sudo mkfs.xfs -f -L "DATA_XFS" /dev/sdb2

# Format Btrfs (Sesuai untuk Salinan Snapshot & Fedora 43 Workstation)
sudo mkfs.btrfs -f -L "DATA_BTRFS" /dev/sdc2
```

#### B. Konfigurasi Pemasangan Kekal (`/etc/fstab`)
Setiap lekap storan kekal **MESTI** menggunakan `UUID` untuk mengelakkan ralat nama peranti yang berubah semasa but.

```bash
# 1. Dapatkan UUID peranti
sudo blkid /dev/vg_data/lv_storan
# Contoh Output: UUID="a1b2c3d4-e5f6-7890-abcd-ef1234567890"

# 2. Cipta direktori titik lekap (mount point)
sudo mkdir -p /mnt/storan_pejabat

# 3. Tambahkan rekod ke /etc/fstab
echo 'UUID=a1b2c3d4-e5f6-7890-abcd-ef1234567890 /mnt/storan_pejabat ext4 defaults,nofail 0 2' | sudo tee -a /etc/fstab

# 4. Uji pemasangan fstab tanpa but semula
sudo mount -a
df -h /mnt/storan_pejabat
```

---

### 5. Penyulitan Storan Blok LUKS2 (Standard JDN / MAMPU & ISO 27001)

Untuk persekitaran pejabat/perusahaan yang mengendalikan data sensitif:

```bash
# 1. Format pemacu/volum dengan LUKS2
sudo cryptsetup luksFormat --type luks2 /dev/vg_data/lv_storan

# 2. Buka pemacu tersulit dan cipta pemetaan peranti (device mapper)
sudo cryptsetup open /dev/vg_data/lv_storan storan_terkunci

# 3. Format peranti tersulit yang dibuka (/dev/mapper/storan_terkunci)
sudo mkfs.ext4 /dev/mapper/storan_terkunci
```

---

## 🔒 Pematuhan Keselamatan JDN / MAMPU & ISO/IEC 27001
1. **Penggunaan UUID:** Sentiasa gunakan `UUID` dalam `/etc/fstab` dan elakkan rujukan langsung `/dev/sdX` bagi mengelakkan kegagalan but (*boot failure*).
2. **Flag `nofail`:** Gunakan parameter `nofail` pada disk tambahan dalam `/etc/fstab` supaya pelayan kekal but walaupun disk luaran tidak disambungkan.
3. **Penyulitan LUKS2:** Storan luaran (USB HDD/SSD) dan volum LVM2 yang menyimpan fail terperingkat Wajib disulitkan menggunakan LUKS2 dengan frasa laluan sekurang-kurangnya 16 aksara.

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)
- [ ] Berjaya memeriksa peranti storan menggunakan `lsblk` dan `blkid`.
- [ ] Berjaya membina jadual partisi GPT menggunakan `gdisk` atau `parted`.
- [ ] Berjaya membina struktur LVM2 (PV, VG, LV) dan meluaskan saiz LV.
- [ ] Berjaya format sistem fail EXT4/XFS/Btrfs dan membuat pautan kekal `/etc/fstab` melalui UUID.
- [ ] Berjaya membina volum LUKS2 tersulit mengikut piawaian keselamatan.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Apakah perbezaan prestasi dan ciri ketahanan (redundancy/snapshots) antara sistem fail EXT4, XFS, dan Btrfs dalam persekitaran pelayan enterprise?"*
2. *"Tuliskan skrip Bash untuk menyemak tahap kesihatan S.M.A.R.T. cakera keras dan menghantar amaran jika terdapat kerosakan sektor fizikal."*
3. *"Bagaimanakah cara mengkonfigurasi kunci LUKS2 automatik menggunakan TPM2 (Trusted Platform Module) pada Linux?"*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
- [Dokumentasi LVM2 Linux RedHat/AlmaLinux](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_logical_volumes/index)
- [Dokumentasi GNU Parted Manual](https://www.gnu.org/software/parted/manual/)
- [Panduan Btrfs Wiki Documentation](https://btrfs.readthedocs.io/)
- [Pekeliling Keselamatan ICT JDN / MAMPU](https://www.jdn.gov.my/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
- **Storage Systems: Organization, Performance, Coding, Reliability, and Statistics** oleh Alexander Thomasian.
- **UNIX and Linux System Administration Handbook, 5th Edition** oleh Evi Nemeth et al.
- **Nota Pentadbiran Storan & Pelayan Linux Malaysia** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
