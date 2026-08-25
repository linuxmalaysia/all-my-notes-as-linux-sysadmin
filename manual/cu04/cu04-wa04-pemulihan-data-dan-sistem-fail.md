---
okf_version: 0.2
type: knowledge-node
title: "Pemulihan Data & Verifikasi Integriti Sistem Fail"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu04", "pemulihan", "sha256sum", "bare-metal", "tar"]
tags: ["cu04", "linux", "noss", "pemulihan", "sha256sum", "bare-metal", "standard-malaysia"]
description: "Panduan amali prosedur pemulihan data tempatan dan sistem fail, pengesahan integriti checksum SHA-256, pengekstrakan fail terpilih daripada arkib tar/zstd, dan tatacara pemulihan bare-metal."
resource: "file:///manual/cu04/cu04-wa04-pemulihan-data-dan-sistem-fail.md"
---

# Pemulihan Data & Verifikasi Integriti Sistem Fail

## 🎯 Objektif Pembelajaran
Di akhir modul amali ini, pelatih dapat:
1. Melaksanakan verifikasi integriti arkib sandaran menggunakan algoritma hash cryptographic `sha256sum` sebelum proses pemulihan.
2. Mengekstrak data terpilih (*selective restoration*) daripada arkib termampat `tar.zst` / `tar.gz` tanpa menimpa (*overwrite*) data sedia ada secara tidak sengaja.
3. Melaksanakan pemulihan kebenaran (*permissions*) dan pemilikan fail POSIX (`chown`, `chmod`) selepas data dipulihkan.
4. Memahami alur kerja pemulihan *bare-metal disaster recovery* untuk persekitaran endpoint dan pelayan.

> [!NOTE]
> Modul amali ini dipetakan kepada **NOSS CU04 (Backup & Recovery Tools) - WA04: Perform Data and Filesystem Recovery**. Edaran Linux rujukan merangkumi **Ubuntu 26.04 LTS "Resolute Raccoon"** dan **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Garis Panduan Amali & Prosedur

### 1. Verifikasi Integriti Arkib Sandaran (`sha256sum`)

Sebelum memulakan pemulihan data, pengesahan integriti adalah kritikal bagi memastikan arkib sandaran tidak rosak atau diubah suai (*tampered*).

```bash
# A. Menjana nilai checksum SHA-256 semasa pembinaan sandaran
sha256sum /mnt/backup/etc_backup_20260817.tar.zst > /mnt/backup/etc_backup_20260817.tar.zst.sha256

# B. Mengesahkan integriti fail arkib sebelum pemulihan
cd /mnt/backup/
sha256sum -c etc_backup_20260817.tar.zst.sha256

# Output yang sah:
# etc_backup_20260817.tar.zst: OK
```

---

### 2. Pengekstrakan & Pemulihan Data Terpilih (*Selective Restore*)

#### A. Memeriksa Kandungan Arkib Tanpa Mengekstrak
```bash
# Menyenaraikan semua fail dalam arkib dan menapis fail khusus
tar -tvf /mnt/backup/etc_backup_20260817.tar.zst | grep "netplan"
```

#### B. Mengekstrak Fail Terpilih ke Direktori Sasar
```bash
# Cipta direktori sementara pemulihan untuk mengelakkan penimpaan tidak sengaja
mkdir -p /tmp/recovery_staging

# Mengekstrak hanya fail netplan/01-netcfg.yaml daripada arkib
sudo tar -I zstd -xvf /mnt/backup/etc_backup_20260817.tar.zst \
  -C /tmp/recovery_staging \
  etc/netplan/01-netcfg.yaml

# Semak kandungan fail yang dipulihkan
ls -la /tmp/recovery_staging/etc/netplan/
```

#### C. Memelihara Pemilikan dan Kebenaran Fail (`--same-owner`, `-p`)
Secara lalai, pengekstrakan oleh pengguna `root` mengekalkan pemilikan asal:
```bash
sudo tar -I zstd --same-owner -p -xvf /mnt/backup/etc_backup_20260817.tar.zst -C /
```

---

### 3. Pemulihan Arkib Tersulit (`gpg`)

Jika arkib disulitkan dengan GPG (AES-256) mengikut garis panduan JDN/MAMPU:
```bash
# Dekripsikan dan ekstrak aluran tar terus secara paip
gpg --decrypt /mnt/backup/etc_encrypted.tar.zst.gpg | sudo tar -I zstd -xvf - -C /tmp/recovery_staging/
```

---

### 4. Tatacara Pemulihan Bencana Bare-Metal (*Bare-Metal Recovery*)

Pemulihan bare-metal dilaksanakan apabila sistem mengalami kegagalan penuh peranti storan utama:

1. **But menggunakan Persekitaran Live ISO**:
   - But komputer sasaran menggunakan USB Live Ubuntu 26.04 LTS atau AlmaLinux 10.
2. **Penyediaan Partisi & Sistem Fail Sasar**:
   - Bina skema partisi GPT dan penyulitan LUKS2 / LVM2 (jika berkaitan):
     ```bash
     sudo cryptsetup luksOpen /dev/nvme0n1p3 cryptroot
     sudo vgchange -ay
     sudo mount /dev/ubuntu-vg/ubuntu-lv /mnt
     sudo mount /dev/nvme0n1p2 /mnt/boot
     sudo mount /dev/nvme0n1p1 /mnt/boot/efi
     ```
3. **Pengekstrakan Arkib Bare-Metal Sistem**:
   ```bash
   sudo tar -I zstd -xvf /mnt/backup/full_system_baremetal.tar.zst -C /mnt
   ```
4. **Pemasangan Semula Bootloader GRUB2 & Chroot**:
   ```bash
   for dir in /dev /dev/pts /proc /sys /run; do sudo mount --bind $dir /mnt$dir; done
   sudo chroot /mnt
   grub-install /dev/nvme0n1
   update-grub
   exit
   ```

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)
- [ ] Berjaya menjana dan mengesahkan nilai hash `sha256sum` untuk fail arkib.
- [ ] Berjaya menyenarai dan mengekstrak fail terpilih tanpa mengekstrak keseluruhan arkib.
- [ ] Berjaya melaksanakan dekripsi arkib tersulit `gpg` ke lokasi pemulihan.
- [ ] Memahami alur kerja dan langkah asas pemulihan sistem bare-metal.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Bagaimanakah cara membina skrip pengesahan sha256sum automatik yang menolak pengekstrakan jika nilai checksum tidak sepadan?"*
2. *"Apakah langkah-langkah pemulihan data untuk sistem fail Btrfs atau ZFS snapshot apabila berlaku kegagalan integriti data?"*
3. *"Tunjukkan kaedah memulihkan pangkalan data PostgreSQL daripada fail tar.zst dump tanpa mengganggu perkhidmatan hidup."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
- [GNU Tar Restore & Extraction Manual](https://www.gnu.org/software/tar/manual/html_section/transform.html)
- [Ubuntu Live ISO System Recovery Guide](https://help.ubuntu.com/community/LiveCdRecovery)
- [NIST Special Publication 800-34: Contingency Planning Guide for IT Systems](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
- **Linux Incident Response and Forensics** oleh Kristinn Gudjonsson.
- **Disaster Recovery and Business Continuity** oleh The Open Group.
- **Panduan Pemulihan Data & Pemantauan Sistem Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
