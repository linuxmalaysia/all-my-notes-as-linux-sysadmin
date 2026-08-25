---
okf_version: 0.1
type: knowledge_node
title: "Penyulitan Penuh Cakera LUKS2 Pejabat (ISO/IEC 27001 & MAMPU)"
timestamp: "2026-08-16T12:10:00Z"
topics: ["luks2", "full-disk-encryption", "security-compliance", "iso27001", "mampu-circular", "cu01"]
tags: ["linux", "encryption", "luks2", "security", "iso27001", "mampu", "cu01", "noss"]
description: "Panduan penyulitan penuh cakera (Full Disk Encryption) LUKS2 untuk komputer pejabat dan pelayan enterprise mengikut piawaian ISO/IEC 27001 dan Pekeliling MAMPU."
resource: "file:///manual/cu01/penyulitan-cakera-luks2-pejabat.md"
---

# 🔐 Penyulitan Penuh Cakera LUKS2 Pejabat (ISO/IEC 27001 & Pekeliling MAMPU)

> *"Penyulitan data berehat (data-at-rest encryption) bukan lagi pilihan, tetapi syarat wajib bagi pematuhan keselamatan maklumat sektor awam dan korporat."*

Di bawah keperluan **Pekeliling Keselamatan ICT MAMPU / AKNC** dan piawaian **ISO/IEC 27001:2022 (Kawalan A.8.24 - Use of Cryptography)**, semua komputer riba, stesen kerja pejabat, dan pelayan perkhidmatan teras wajib mengoperasikan **Penyulitan Cakera Penuh (Full Disk Encryption - FDE)**.

Di dalam ekosistem Linux, **LUKS2 (Linux Unified Key Setup version 2)** dengan algoritma `AES-XTS-PLAIN64` merupakan standard industri berprestasi tinggi bagi melindungi data sensitif daripada kecurian fizikal atau pencerobohan media storan.

---

## 1. Merekabentuk Lapisan Storan LUKS2 + LVM

Penyulitan LUKS2 dilaksanakan di atas peranti blok fizikal (atau partition) sebelum pembentukan LVM Logical Volume:

```
┌─────────────────────────────────────────────────────────────┐
│                    Sistem Fail (`/` dan `/home`)             │
├─────────────────────────────────────────────────────────────┤
│                 LVM Logical Volumes (`lv_root`, `lv_home`)  │
├─────────────────────────────────────────────────────────────┤
│                  LVM Volume Group (`vg_secure`)             │
├─────────────────────────────────────────────────────────────┤
│        Satu Peranti Terbuka Decrypted (`/dev/mapper/crypt_root`)│
├─────────────────────────────────────────────────────────────┤
│         🔒 Lapisan Penyulitan LUKS2 (AES-256-XTS)           │
├─────────────────────────────────────────────────────────────┤
│          Partition Fizikal Storan (`/dev/nvme0n1p3`)       │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Panduan Konfigurasi Amali LUKS2 pada Peranti Blok

### Langkah A: Memformat Partition dengan LUKS2
Format partition storan (contoh: `/dev/nvme0n1p3`) menggunakan LUKS2 dengan frasa laluan (*passphrase*) tegar.

```bash
# Formatkan partition sasaran dengan LUKS2
sudo cryptsetup luksFormat --type luks2 --cipher aes-xts-plain64 --key-size 512 /dev/nvme0n1p3

# Buka peranti terdiskripsi dan berikan nama pemetaan (contoh: crypt_root)
sudo cryptsetup open /dev/nvme0n1p3 crypt_root

# Sahkan status peranti penyulitan
sudo cryptsetup status crypt_root
```

### Langkah B: Membina LVM di Atas Peranti Terpenyulit
Setelah peranti LUKS2 dibuka di `/dev/mapper/crypt_root`, bina Physical Volume (PV), Volume Group (VG), dan Logical Volume (LV):

```bash
# 1. Cipta LVM Physical Volume
sudo pvcreate /dev/mapper/crypt_root

# 2. Cipta Volume Group
sudo vgcreate vg_secure /dev/mapper/crypt_root

# 3. Cipta Logical Volumes
sudo lvcreate -L 40G -n lv_root vg_secure
sudo lvcreate -L 50G -n lv_home vg_secure
sudo lvcreate -L 8G -n lv_swap vg_secure

# 4. Formatkan sistem fail
sudo mkfs.ext4 /dev/vg_secure/lv_root
sudo mkfs.ext4 /dev/vg_secure/lv_home
sudo mkswap /dev/vg_secure/lv_swap
```

---

## 3. Pengurusan Berbilang Kunci Pengguna (Multi-User LUKS2 Key Slots)

LUKS2 menyediakan sehingga **8 ruang kunci (Key Slots 0 hingga 7)**. Ini membolehkan:
- **Slot 0:** Frasa laluan pengguna / pegawai pemilik komputer riba.
- **Slot 1:** Frasa laluan sandaran (*Master Recovery Key*) Pentadbir IT / SysAdmin Pejabat.
- **Slot 2:** Kunci TPM2 (*Trusted Platform Module*) atau YubiKey FIDO2 untuk nyahkunci automatik perkakasan.

### Arahan Menambah dan Mengurus Slot Kunci LUKS2:

```bash
# 1. Semak maklumat slot kunci LUKS2 terisi
sudo cryptsetup luksDump /dev/nvme0n1p3

# 2. Tambah frasa laluan baharu (contoh: Kunci Sandaran Pegawai IT ke Slot 1)
sudo cryptsetup luksAddKey /dev/nvme0n1p3

# 3. Padam frasa laluan pengguna lama daripada slot (contoh: memadam Slot 0)
sudo cryptsetup luksKillSlot /dev/nvme0n1p3 0
```

---

## 4. Konfigurasi Autonyahkunci `/etc/crypttab` & `/etc/fstab`

Untuk membolehkan prapemuat but (*initramfs/dracut*) meminta frasa laluan semasa but awal:

### Fail `/etc/crypttab`:
```text
# <target name>   <source device>         <key file>      <options>
crypt_root        UUID=a1b2c3d4-e5f6-7890  none            luks,discard
```

### Fail `/etc/fstab`:
```text
/dev/mapper/vg_secure-lv_root  /       ext4    defaults        1 1
/dev/mapper/vg_secure-lv_home  /home   ext4    defaults        1 2
/dev/mapper/vg_secure-lv_swap  none    swap    sw              0 0
```

---

## 5. Pematuhan ISO/IEC 27001 & MAMPU Checklist

| Audit / Standard | Keperluan Tekno-Legal | Tindakan Pelaksanaan Linux |
| :--- | :--- | :--- |
| **ISO/IEC 27001 (A.8.24)** | Pengurusan Kunci Kriptografi & Penyulitan Data | Menggunakan LUKS2 AES-256 dengan PBKDF `argon2id` untuk halangan serangan *brute-force*. |
| **Pekeliling MAMPU ICT** | Perlindungan Storan Komputer Liba / Peranti Mudah Alih | Semua komputer riba kerajaan wajib dipasang LUKS2 FDE sebelum diserahkan kepada pegawai. |
| **Sokongan TPM2 / Secure Boot** | Halangan pembongkaran pemuat but (*bootloader tampering*) | Mempautkan kunci LUKS2 ke cip TPM2 menggunakan `systemd-cryptenroll --tpm2-device=auto`. |

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
