---
okf_version: 0.1
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
1. Melaksanakan verifikasi integriti arkib sandaran menggunakan algoritma hash cryptographic `sha256sum` (untuk pengesahan kerosakan tidak sengaja) atau tandatangan GPG terasing (*detached GPG signature* untuk perlindungan usikan).
2. Mengekstrak data terpilih (*selective restoration*) daripada arkib termampat `system_config_20260817.tar.zst` ke lokasi penstoran sementara (`/tmp/recovery_staging`).
3. Melaksanakan pemulihan kebenaran (*permissions*) dan pemilikan fail POSIX (`chown`, `chmod`) selepas data dipulihkan.
4. Memahami alur kerja pemulihan *bare-metal disaster recovery* untuk persekitaran endpoint dan pelayan merentas edaran Ubuntu dan AlmaLinux.

!!! note "Unit Kompetensi NOSS"
    Modul amali ini dipetakan kepada **NOSS CU04 (Backup & Recovery Tools) - WA04: Perform Data and Filesystem Recovery**. Edaran Linux rujukan merangkumi **Ubuntu 26.04 LTS "Resolute Raccoon"** dan **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Garis Panduan Amali & Prosedur

### 1. Verifikasi Integriti Arkib Sandaran (`sha256sum` & `gpg`)

> ℹ️ **Nota Keselamatan Integriti:** Penggunaan `sha256sum` bersama fail manifest bersebelahan (*co-located*) berfungsi untuk mengesan kerosakan tidak sengaja (*corruption detection*) semasa proses pemindahan. Bagi perlindungan daripada usikan berniat jahat (*tamper protection*), tandatangan GPG terasing (`.sig`) atau manifest yang disimpan di lokasi luaran terpisah hendaklah digunakan.

```bash
# A. Mengesahkan integriti fail arkib untuk pengesahan kerosakan (Corruption Detection)
cd /mnt/backup/
sha256sum -c system_config_20260817.tar.zst.sha256

# Output yang sah:
# system_config_20260817.tar.zst: OK

# B. Mengesahkan tandatangan GPG terasing untuk Perlindungan Usikan (Tamper Protection)
gpg --verify system_config_20260817.tar.zst.sig system_config_20260817.tar.zst
```

---

### 2. Pengekstrakan & Pemulihan Data Terpilih (*Selective Restore*)

#### A. Memeriksa Kandungan Arkib Tanpa Mengekstrak
```bash
# Menyenaraikan semua fail dalam arkib dan menapis fail khusus
tar -tvf /mnt/backup/system_config_20260817.tar.zst | grep "netplan"
```

#### B. Mengekstrak Fail Terpilih ke Direktori Pentas Sementara (`/tmp/recovery_staging`)
```bash
# Cipta direktori sementara pemulihan untuk mengelakkan penimpaan tidak sengaja pada sistem hidup
mkdir -p /tmp/recovery_staging

# Mengekstrak hanya fail netplan/01-netcfg.yaml daripada arkib ke lokasi staging
sudo tar -I zstd -xvf /mnt/backup/system_config_20260817.tar.zst \
  -C /tmp/recovery_staging \
  etc/netplan/01-netcfg.yaml

# Semak kandungan fail yang dipulihkan
ls -la /tmp/recovery_staging/etc/netplan/
```

#### C. Memelihara Pemilikan, Kebenaran Fail & Salinan ke Sistem Hidup
> ⚠️ **Amaran Penimpaan Direct Extraction:** Pengekstrakan terus ke direktori punca `/` hanya disyorkan apabila memulihkan sasaran tidak terlekap (*unmounted recovery target*) seperti `/mnt`. Untuk sistem hidup, sentiasa ekstrak ke `/tmp/recovery_staging`, periksa jalur fail, dan salin secara eksplisit.

```bash
# Salin fail yang telah disahkan dari staging ke lokasi sistem live
sudo cp -p /tmp/recovery_staging/etc/netplan/01-netcfg.yaml /etc/netplan/01-netcfg.yaml
```

---

### 3. Pemulihan Arkib Tersulit (`gpg`)

Jika arkib disulitkan dengan GPG (AES-256) mengikut garis panduan JDN/MAMPU:
```bash
# Dekripsikan dan ekstrak aluran tar terus secara paip ke staging
gpg --decrypt /mnt/backup/etc_encrypted.tar.zst.gpg | sudo tar -I zstd -xvf - -C /tmp/recovery_staging/
```

---

### 4. Tatacara Pemulihan Bencana Bare-Metal (*Bare-Metal Recovery*)

Pemulihan bare-metal dilaksanakan mengikut empat laluan khusus mengikut senario perkakasan dan edaran:

#### Laluan A: Ubuntu 26.04 LTS (UEFI Mode)
1. But Live USB Ubuntu 26.04 LTS.
2. Buka volum penyulitan LUKS2 dan LVM (jika wujud), kemudian lekapkan partition sasaran:
   ```bash
   sudo cryptsetup luksOpen /dev/nvme0n1p3 cryptroot
   sudo vgchange -ay
   sudo mount /dev/ubuntu-vg/ubuntu-lv /mnt
   sudo mount /dev/nvme0n1p2 /mnt/boot
   sudo mount /dev/nvme0n1p1 /mnt/boot/efi
   ```
3. Lekapkan sumber sandaran dan ekstrak:
   ```bash
   sudo mkdir -p /mnt/backup_source
   sudo mount /dev/sdb1 /mnt/backup_source
   sudo tar -I zstd -xvf /mnt/backup_source/system_config_20260817.tar.zst -C /mnt
   ```
4. Bind mount & pasang semula GRUB2 UEFI:
   ```bash
   for dir in /dev /dev/pts /proc /sys /run; do sudo mount --bind $dir /mnt$dir; done
   sudo chroot /mnt
   grub-install --target=x86_64-efi --efi-directory=/boot/efi /dev/nvme0n1
   update-grub
   exit
   ```

#### Laluan B: Ubuntu 26.04 LTS (Legacy BIOS Mode)
1. But Live USB, bina/lekapkan partition ext4 pada `/mnt` dan boot pada `/mnt/boot`.
2. Ekstrak arkib ke `/mnt`.
3. Pemasangan GRUB BIOS:
   ```bash
   for dir in /dev /dev/pts /proc /sys /run; do sudo mount --bind $dir /mnt$dir; done
   sudo chroot /mnt
   grub-install /dev/nvme0n1
   update-grub
   exit
   ```

#### Laluan C: AlmaLinux 10 (UEFI Mode)
1. But Live ISO AlmaLinux 10, lekapkan LV root ke `/mnt`, `/boot` ke `/mnt/boot`, dan ESP ke `/boot/efi`.
2. Ekstrak arkib ke `/mnt`.
3. Reinstall GRUB2 & bina semula konfigurasi AlmaLinux:
   ```bash
   for dir in /dev /dev/pts /proc /sys /run; do sudo mount --bind $dir /mnt$dir; done
   sudo chroot /mnt
   grub2-install --target=x86_64-efi --efi-directory=/boot/efi /dev/nvme0n1
   grub2-mkconfig -o /boot/efi/EFI/almalinux/grub.cfg
   exit
   ```

#### Laluan D: AlmaLinux 10 (Legacy BIOS Mode)
1. But Live ISO, bina/lekapkan partition sasaran ke `/mnt`.
2. Ekstrak arkib ke `/mnt`.
3. Pemasangan GRUB2 BIOS AlmaLinux:
   ```bash
   for dir in /dev /dev/pts /proc /sys /run; do sudo mount --bind $dir /mnt$dir; done
   sudo chroot /mnt
   grub2-install /dev/nvme0n1
   grub2-mkconfig -o /boot/grub2/grub.cfg
   exit
   ```

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)
- [ ] Berjaya mengesahkan fail checksum `sha256sum` dan tandatangan GPG terasing.
- [ ] Berjaya mengekstrak data ke `/tmp/recovery_staging` sebelum memindahkan ke sistem live.
- [ ] Berjaya melaksanakan dekripsi arkib tersulit `gpg` ke lokasi pemulihan.
- [ ] Memahami 4 laluan pemulihan bare-metal (Ubuntu vs AlmaLinux / UEFI vs BIOS).

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Apakah perbezaan antara sha256sum bersebelahan dengan tandatangan GPG terasing dari sudut keselamatan?"*
2. *"Bagaimanakah cara menjana semula imej initramfs (update-initramfs / dracut) selepas pemulihan bare-metal?"*
3. *"Tunjukkan kaedah memulihkan pangkalan data PostgreSQL daripada fail tar.zst dump tanpa mengganggu perkhidmatan hidup."*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
- [GNU Tar Restore & Extraction Manual](https://www.gnu.org/software/tar/manual/html_section/transform.html)
- [Ubuntu Live ISO System Recovery Guide](https://help.ubuntu.com/community/LiveCdRecovery)
- [AlmaLinux System Recovery Wiki](https://wiki.almalinux.org/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
- **Linux Incident Response and Forensics** oleh Kristinn Gudjonsson.
- **Disaster Recovery and Business Continuity** oleh The Open Group.
- **Panduan Pemulihan Data & Pemantauan Sistem Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
