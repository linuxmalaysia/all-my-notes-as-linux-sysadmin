---
name: cu02-wa01-identify-virtualisation-infrastructure-requirements
description: "Executes NOSS Work Activity: Identify Virtualisation Infrastructure & Storage Partitioning Requirements (GPT, LVM2, Filesystems)"
topics: [noss, cu02, wa01, storage, virtualisation]
tags: [cu02, wa01, gpt, gdisk, parted, lvm2, ext4, xfs, btrfs]
okf_version: 0.1
type: skill
---

# Identify Virtualisation Infrastructure Requirements & Storage Partitioning

*Executes NOSS standard K622-XXX-3:2026-C02 WA01*

## Overview

This skill executes hardware inspection and storage layout planning for virtualization hosts according to NOSS CU02 standards. It covers GPT partition schemes, LVM2 volume group allocation, and filesystem layout (EXT4/XFS/Btrfs).

> [!WARNING]
> **AMARAN OPERASI MEMUSNAHKAN DATA (DESTRUCTIVE OPERATION WARNING):**
> Arahan pemartisian (`parted mklabel`, `gdisk`) dan format sistem fail memadamkan semua data pada peranti sasaran secara kekal. Lakukan semakan pra-syarat (*preflight checks*) wajib:
> 1. Sahkan nama peranti sasaran secara teliti menggunakan `lsblk` (contoh: `/dev/sdb`, BUKAN `/dev/sda`).
> 2. Pastikan semua partisi sasaran telah dinyahlekap (`sudo umount /dev/sdb*`).
> 3. Semak tandatangan peranti menggunakan `sudo wipefs /dev/sdb`.
> 4. Pastikan salinan duaan (backup) data penting telah dibuat.

## Procedure

### 1. Storage & Host Hardware Audit

```bash
lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINTS
sudo blkid
lscpu | grep -iE 'vt-x|amd-v|virtualization'
```

### 2. GPT Partitioning (`gdisk` / `parted`)

```bash
sudo parted /dev/sdb mklabel gpt
sudo parted -a optimal /dev/sdb mkpart primary 1MiB 20GiB
sudo parted /dev/sdb set 1 lvm on
```

### 3. LVM2 Initialization

```bash
sudo pvcreate /dev/sdb1
sudo vgcreate vg_virt /dev/sdb1
sudo lvcreate -L 15G -n lv_kvm_images vg_virt
```

### 4. Filesystem Formatting & `/etc/fstab` Mounting

```bash
sudo mkfs.xfs -f /dev/vg_virt/lv_kvm_images
sudo mkdir -p /var/lib/libvirt/images_custom

UUID=$(sudo blkid -s UUID -o value /dev/vg_virt/lv_kvm_images)
if ! grep -q "$UUID" /etc/fstab; then
  echo "UUID=$UUID /var/lib/libvirt/images_custom xfs defaults,nofail 0 2" | sudo tee -a /etc/fstab
fi
sudo mount -a
```

## Security & Governance

- Enforce UUID mounting in `/etc/fstab` to avoid device mapping errors.
- Secure virtualization storage pools in alignment with ISO/IEC 27001 and JDN/MAMPU guidelines.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
