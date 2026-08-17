---
okf_version: 0.1
type: knowledge-node
title: "Konfigurasi Pelekapan Storan, Peranti Luaran & Pengoperasian Media"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu06", "mount", "umount", "findmnt", "fstab", "storan"]
tags: ["cu06", "linux", "noss", "mount", "fstab", "nvme", "usb", "standard-malaysia"]
description: "Panduan amali konfigurasi pelekapan storan, penangguhan media luaran, pengurusan entri /etc/fstab dengan parameter pengerasan keselamatan JDN/MAMPU, dan diagnostik peranti luaran."
resource: "file:///manual/cu06/cu06-wa04-konfigurasi-dan-troubleshooting-peranti-luaran.md"
---

# Konfigurasi Pelekapan Storan, Peranti Luaran & Pengoperasian Media

## 🎯 Objektif Pembelajaran

Di akhir modul amali ini, pelatih dapat:
1. Memahami penamaan nod peranti moden dalam Linux (`/dev/nvmeXn1`, `/dev/sdX`, `/dev/sr0`, USB) berpandukan piawaian Filesystem Hierarchy Standard (FHS).
2. Melaksanakan pelekapan (*mounting*) dan penangguhan (*unmounting*) sistem fail secara manual menggunakan `mount`, `umount`, dan `findmnt`.
3. Mengkonfigurasi entri pelekapan kekal automatik dalam `/etc/fstab` menggunakan UUID (*Universally Unique Identifier*).
4. Menerapkan pilihan pengerasan keselamatan storan (`nodev,nosuid,noexec`) mengikut Pekeliling Jabatan Digital Negara (JDN) / MAMPU dan ISO/IEC 27001.

!!! note "Unit Kompetensi NOSS"
    Modul amali ini dipetakan kepada **NOSS CU06 (End-User Support & System Maintenance) - WA04: Configure and Troubleshoot Peripheral Connections**. Edaran Linux rujukan merangkumi **Ubuntu 26.04 LTS "Resolute Raccoon"** dan **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Garis Panduan Amali & Prosedur

### 1. Pengecaman Peranti Storan & Struktur Nod (`/dev/`)

#### A. Konvensyen Penamaan Nod Peranti Moden (2026):
- **NVMe SSD**: `/dev/nvme0n1` (Pemacu 1), `/dev/nvme0n1p1` (Partisi 1).
- **SATA / USB Storage**: `/dev/sda` (Pemacu A), `/dev/sdb1` (Partisi 1 Pemacu B).
- **Pemacu Optik (CD/DVD)**: `/dev/sr0` (pautan simbolik `/dev/cdrom`).
- **Media Luaran**: Terlekap di bawah `/media/$USER/` atau `/mnt/`.

#### B. Pemeriksaan Peranti Storan
```bash
# Menyenaraikan semua blok peranti beserta UUID dan sistem fail
lsblk -f

# Menganalisis UUID khusus bagi partisi storan luaran /dev/sdb1
sudo blkid /dev/sdb1
```

---

### 2. Pelekapan & Penangguhan Storan Manual (`mount`, `umount`, `findmnt`)

#### A. Melakukan Pelekapan Sistem Fail
```bash
# Cipta titik pelekap (mount point) di bawah /mnt
sudo mkdir -p /mnt/usb_flash

# Pelekap sistem fail tanpa memaksa jenis ext4 (menyokong vfat, exfat, ext4)
sudo mount /dev/sdb1 /mnt/usb_flash

# Verifikasi status pelekapan dan hierarki
findmnt /mnt/usb_flash
```

#### B. Penangguhan Media Luaran & Pengeluaran Selamat Peranti (`umount`, `eject`, `udisksctl`)
```bash
# Memastikan tiada proses sedang menggunakan direktori sebelum umount
sudo umount /mnt/usb_flash

# Pengeluaran selamat bagi peranti USB (Whole-disk node /dev/sdb)
sudo udisksctl power-off -b /dev/sdb

# Pengeluaran media optik CD/DVD sahaja
eject /dev/sr0
```

---

### 3. Konfigurasi Pelekapan Automatik Kekal (`/etc/fstab`)

Fail `/etc/fstab` (*File System Table*) mengawal pelekapan partition semasa proses but sistem.

#### A. Dapatkan UUID Partisi
```bash
sudo blkid /dev/nvme0n1p3
# Contoh UUID: 550e8400-e29b-41d4-a716-446655440000
```

#### B. Menambah Entri Dalam `/etc/fstab`
Pengerasan keselamatan mewajibkan tetapan `nodev,nosuid,noexec` pada media luaran atau partition muat naik data mengikut Pekeliling Am JDN/MAMPU & ISO/IEC 27001:

##### Entri Storan Wajib (Internal System Disk):
```ini
UUID=550e8400-e29b-41d4-a716-446655440000 /mnt/sec_storage   ext4    defaults                      0       2
```

##### Entri Storan Pilihan / Media Boleh Alih (Optional Removable Media):
```ini
UUID=a1b2c3d4-e5f6-7890-abcd-1234567890ab /mnt/usb_media     ext4    defaults,nofail,x-systemd.device-timeout=5s,nodev,nosuid,noexec  0  2
```

#### C. Menguji Konfigurasi `/etc/fstab`
```bash
# Uji entri fstab baharu tanpa mereboot sistem (ELAKKAN ralat but!)
sudo mount -a

# Sahkan titik pelekapan baharu aktif
findmnt /mnt/sec_storage
```

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)
- [ ] Berjaya mengenal pasti nod peranti NVMe, SATA, dan USB menggunakan `lsblk` & `blkid`.
- [ ] Berjaya melekap dan menangguhkan peranti storan serta membuat safe-removal peranti USB.
- [ ] Berjaya mengkonfigurasi entri automatik kekal dalam `/etc/fstab` untuk storan wajib dan storan pilihan (`nofail`).
- [ ] Berjaya menerapkan opsi pengerasan keselamatan `nodev,nosuid,noexec` pada partition berkenaan.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Mengapakah penggunaan UUID lebih selamat berbanding nama nod peranti /dev/sdb1 di dalam fail /etc/fstab?"*
2. *"Apakah langkah penyelesaian masalah jika sistem gagal but (enter emergency mode) disebabkan ralat sintaks pada /etc/fstab?"*
3. *"Bagaimanakah cara melekap imej fail ISO secara loop device menggunakan arahan mount -o loop?"*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
- [Ubuntu Storage & FHS Management Guide](https://ubuntu.com/server/docs)
- [Systemd Mount Units & fstab Documentation](https://www.freedesktop.org/software/systemd/man/systemd.mount.html)
- [Arch Linux fstab & UUID Reference](https://wiki.archlinux.org/title/fstab)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
- **Linux Filesystem Essentials** oleh Practical Linux Series.
- **System Modernization and Storage Management in Linux** oleh W. John.
- **Pentadbiran Storan & Sistem Fail Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
