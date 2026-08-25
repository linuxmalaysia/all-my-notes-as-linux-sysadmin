---
okf_version: 0.2
type: knowledge_node
title: "Keperluan Perkakasan & Mod Penimbalan BIOS/UEFI"
timestamp: "2026-08-16T12:00:00Z"
topics: ["hardware-requirements", "bios-uefi", "secure-boot", "live-usb", "cu01"]
tags: ["linux", "hardware", "uefi", "bios", "liveusb", "cu01", "noss"]
description: "Nod pengetahuan mengenai spesifikasi perkakasan, perbezaan BIOS vs UEFI, tetapan Secure Boot, dan penyediaan media pemasangan Bootable Live USB."
resource: "file:///manual/cu01/keperluan-perkakasan-dan-bios-uefi.md"
---

# 💻 Keperluan Perkakasan & Mod Penimbalan BIOS/UEFI

> *"Sistem operasi yang hebat bermula daripada persediaan tegar perkakasan dan mod penimbalan peranti yang betul."*

Sebelum memulakan proses pemasangan sistem operasi Linux (sama ada untuk kegunaan desktop latihan mahupun pelayan perusahaan), pentadbir sistem wajib memahami spesifikasi minimum perkakasan serta tatacara konfigurasi tegar tegar (*firmware*) BIOS dan UEFI.

---

## 1. Spesifikasi Minimum & Disyorkan Perkakasan (2026)

Jadual berikut memaparkan keperluan perkakasan untuk tiga edaran kanonik rujukan utama: **Ubuntu 26.04 LTS**, **Fedora 43**, dan **AlmaLinux 10**.

| Keperluan Perkakasan | Ubuntu 26.04 LTS (Desktop) | Fedora 43 (Workstation) | AlmaLinux 10 (Server / Enterprise) |
| :--- | :--- | :--- | :--- |
| **Seni Bina Pemproses** | x86_64 / ARM64 (64-bit) | x86_64-v2 / ARM64 | x86_64-v2 / ARM64 / ppc64le |
| **Peluang Pemproses (CPU)** | 2.0 GHz Dual-Core (Disyorkan 4-Core) | 2.0 GHz Quad-Core | 2.0 GHz Multi-Core |
| **Memori Capaian Rawak (RAM)** | Minimum 4 GB (Disyorkan 8 GB+) | Minimum 4 GB (Disyorkan 8 GB+) | Minimum 2 GB (Disyorkan 4 GB+ tanpa GUI, 8 GB+ dengan GUI) |
| **Storan Cakera (Disk Space)** | Minimum 25 GB SSD/NVMe | Minimum 20 GB SSD/NVMe | Minimum 20 GB (Server), 50 GB+ (Enterprise Workstation) |
| **Paparan Grafik** | Resolusi 1024x768 (Disyorkan Full HD 1920x1080) | Kad grafik dengan sokongan OpenGL 3.3+ | Kad grafik asas atau Mod Teks (Headless) |
| **Media Pemasangan** | Pemacu Kilat USB 8 GB+ | Pemacu Kilat USB 8 GB+ | Pemacu Kilat USB 8 GB+ / ISO Rangkaian (NetInstall) |

---

## 2. Perbezaan Warisan BIOS (Legacy CSB) vs Modern UEFI

Sistem pengkomputeran moden telah beralih daripada **Legacy BIOS** kepada **UEFI (Unified Extensible Firmware Interface)**.

```
                    MOD PENIMBALAN SISTEM (BOOT MODE)
                                   │
         ┌─────────────────────────┴─────────────────────────┐
         ▼                                                   ▼
 🏛️ Legacy BIOS (MBR)                               🚀 UEFI Mode (GPT)
 ├─ Had Pemasangan: Storan Max 2 TB                 ├─ Storan: Menyokong > 2 TB (GPT)
 ├─ Partition: Max 4 Primary Partitions            ├─ Partition: Sehingga 128 Partitions
 ├─ Sektor Boot: Master Boot Record (Sektor 0)     ├─ Sektor Boot: Partition Khas EFI (`/boot/efi`)
 └─ Kelajuan: Perlahan (Real Mode 16-bit)           └─ Kelajuan: Pantas (32-bit / 64-bit Native)
```

### Tetapan Secure Boot & Mod Compatibility Support Module (CSM)
1. **Secure Boot:**
   - Ciri keselamatan UEFI yang menghalang pemuat but (*bootloader*) tidak diiktiraf daripada dijalankan.
   - **Ubuntu 26.04 LTS** dan **AlmaLinux 10** menyokong penuh Secure Boot secara lalai (*out-of-the-box*) melalui tandatangan digital Microsoft `shim`.
   - Untuk pemacu peranti pihak ketiga khas (contohnya pemacu grafik Nvidia proprietary purba), Secure Boot mungkin perlu dilumpuhkan sementara atau kunci MOK (*Machine Owner Key*) mesti didaftarkan.
2. **Nyahaktif CSM (Legacy Mode):**
   - Disyorkan untuk mematikan CSM/Legacy Mode di BIOS/UEFI bagi memastikan sistem beroperasi dalam mod UEFI tulen dengan jadual partitions GPT.

---

## 3. Penyediaan Media Pemasangan Bootable Live USB

Terdapat dua kaedah utama untuk menghasilkan pemacu USB bootable pada Linux:

### Kaedah A: Menggunakan Arahan CLI `dd` (Standard SysAdmin)
Perintah `dd` (*dataset definition*) ialah alatan garisan arahan asas paling pantas pada persekitaran Linux.

> **⚠️ AMARAN PENTING:** Pastikan sasaran pemacu USB (`/dev/sdX` atau `/dev/nvmeXnY`) ditanda dengan tepat. Kesilapan memilih peranti akan memadam data sistem utama anda!

```bash
# 1. Kenal pasti nama peranti pemacu USB anda (contoh: /dev/sdb)
lsblk

# 2. Hantar imej ISO terus ke pemacu USB (contohnya Ubuntu 26.04 LTS)
sudo dd if=ubuntu-26.04-desktop-amd64.iso of=/dev/sdb bs=4M status=progress conv=fdatasync
```

### Kaedah B: Menggunakan Ventoy (Pelbagai-ISO Bootable)
Ventoy membolehkan penyalinan terus fail `.iso` ke dalam pemacu USB tanpa perlu memformat USB setiap kali menukar edaran Linux.

```bash
# Pemasangan Ventoy pada pemacu USB /dev/sdb
sudo ventoy -i /dev/sdb

# Seterusnya, cuma salin mana-mana fail ISO (Ubuntu, AlmaLinux, Fedora) ke partition USB Ventoy
```

---

## 4. Latihan Amali Semakan Sistem

Jalankan perintah berikut pada sesi Live USB untuk memverifikasi sama ada peranti but dalam mod UEFI atau Legacy BIOS:

```bash
# Jika direktori ini wujud, sistem but dalam mod UEFI
ls -d /sys/firmware/efi

# Memeriksa struktur partition dan jenama pemproses
lscpu | grep "Model name\|Architecture"
lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINTS
```

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
