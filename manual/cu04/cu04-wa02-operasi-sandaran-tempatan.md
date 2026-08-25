---
okf_version: 0.2
type: knowledge-node
title: "Pelaksanaan Operasi Sandaran Tempatan & Pemampatan Data"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu04", "sandaran", "tar", "rsync", "zstd", "cron", "systemd-timer"]
tags: ["cu04", "linux", "noss", "sandaran", "zstd", "rsync", "systemd", "standard-malaysia"]
description: "Panduan amali pelaksanaan operasi sandaran sistem tempatan, arkib berformat tar dengan pemampat moden zstd/gzip/xz, penyegerakan rsync, automasi cron & systemd.timer, serta pematuhan standard ISO/IEC 27001 dan JDN/MAMPU."
resource: "file:///manual/cu04/cu04-wa02-operasi-sandaran-tempatan.md"
---

# Pelaksanaan Operasi Sandaran Tempatan & Pemampatan Data

## 🎯 Objektif Pembelajaran
Di akhir modul amali ini, pelatih dapat:
1. Menguasai penciptaan dan pengekstrakan arkib data menggunakan utiliti `tar` berasaskan algoritma pemampatan moden seperti `zstd`, `xz`, `gzip`, dan `bzip2`.
2. Melaksanakan penyegerakan direktori berprestasi tinggi menggunakan `rsync -avzP --delete-after` bagi operasi sandaran berperingkat (*incremental backup*).
3. Mengaplikasikan strategi sandaran **3-2-1** mengikut Pekeliling Jabatan Digital Negara (JDN) / MAMPU dan ISO/IEC 27001.
4. Mengautomasikan tugasan sandaran berkala menggunakan `cron` dan unit pemasa `systemd.timer`.

> [!NOTE]
> Modul amali ini dipetakan kepada **NOSS CU04 (Backup & Recovery Tools) - WA02: Perform Local Backup Operations**. Edaran Linux rujukan merangkumi **Ubuntu 26.04 LTS "Resolute Raccoon"** dan **AlmaLinux 10 "Purple Lion"**.

---

## 🛠️ Garis Panduan Amali & Prosedur

### 1. Keperluan Awal & Pra-Syarat
- Persekitaran Linux beroperasi (Ubuntu 26.04 LTS / AlmaLinux 10 / Fedora 43).
- Hak akses pentadbir (`sudo`).
- Ruang storan mencukupi pada pemacu sandaran atau partition dedicated (contoh: `/mnt/backup`).

---

### 2. Pengarkiban & Pemampatan Data Moden (`tar`, `zstd`, `gzip`, `xz`)

#### A. Konsep & Operator `tar`
Utiliti `tar` (*Tape Archive*) digabungkan dengan alatan pemampatan untuk mengecilkan saiz arkib data:
- `-c` (*create*): Membina arkib baharu.
- `-x` (*extract*): Mengekstrak kandungan arkib.
- `-v` (*verbose*): Memaparkan maklumat terperinci semasa proses.
- `-f` (*file*): Menentukan nama fail arkib output.
- `-z` (*gzip*), `-j` (*bzip2*), `-J` (*xz*), `--zstd` (*zstandard*): Pilihan algoritma pemampatan.

#### B. Pelaksanaan Amali Pemampatan `zstd` (Standard 2026)
`zstd` (Zstandard) merupakan algoritma pemampatan masa nyata berasaskan bebenang berbilang (*multi-threaded*) berprestasi tinggi.

```bash
# Membina arkib terpatat zstd daripada direktori /var/log
sudo tar -I 'zstd -T0 -19' -cvf /mnt/backup/logs_backup_$(date +%Y%m%d).tar.zst /var/log

# Memeriksa kandungan fail arkib tanpa mengekstrak
tar -tvf /mnt/backup/logs_backup_*.tar.zst

# Mengekstrak arkib zstd ke direktori sasaran
sudo tar -I zstd -xvf /mnt/backup/logs_backup_*.tar.zst -C /tmp/restored_logs/
```

#### C. Pemampat Tradisional & Moden lain
```bash
# Pemampatan Gzip (.tar.gz)
tar -czvf /mnt/backup/etc_backup.tar.gz /etc

# Pemampatan XZ (.tar.xz) - kadar mampatan tinggi
tar -cJvf /mnt/backup/etc_backup.tar.xz /etc
```

---

### 3. Penyegerakan Data Pintar & Incremental Backup (`rsync`)

`rsync` (*Remote Sync*) hanya menyalin blok fail yang telah berubah, menjimatkan masa dan penggunaan I/O cakera.

```bash
# Parameter utama rsync:
# -a (archive mode): Memelihara kebenaran, pemilik, dan pautan simbolik
# -v (verbose): Memaparkan perincian
# -z (compress): Mermampatkan data semasa pemindahan
# -P (progress & partial): Memaparkan bar kemajuan dan membolehkan resume
# --delete-after: Memadam fail di destinasi jika ia dipadam di sumber (penyegerakan tepat)

sudo rsync -avzP --delete-after /home/user/documents/ /mnt/backup/documents_mirror/
```

---

### 4. Strategi Sandaran 3-2-1 & Pengerasan Keselamatan JDN/MAMPU

#### A. Prinsip 3-2-1:
- **3** salinan data (1 data asal + 2 salinan sandaran).
- **2** jenis media storan berbeza (contoh: NVMe SSD tempatan + NAS/LUKS Encrypted External Volume).
- **1** salinan ditempatkan di luar premis (*offsite / cloud / secondary DC*).

#### B. Penyulitan Arkib Sandaran
Mengikut Pekeliling Am JDN/MAMPU, data sensitif mesti disulitkan sebelum disimpan:
```bash
# Menyalurkan arkib tar zstd terus ke penyulitan Symmetric GPG
tar -I zstd -cvf - /etc | gpg --symmetric --cipher-algo AES256 -o /mnt/backup/etc_encrypted.tar.zst.gpg
```

---

### 5. Automasi Jadual Sandaran (`cron` & `systemd.timer`)

#### A. Automasi Tradisional menerusi `crontab`
```bash
# Menyunting jadual cron pengguna root
sudo crontab -e

# Format crontab: [Minit] [Jam] [Hari/Bulan] [Bulan] [Hari/Minggu] [Arahan]
# Contoh: Menjalankan skrip sandaran setiap hari pada jam 2:00 pagi
0 2 * * * /usr/local/bin/system_backup.sh >> /var/log/backup.log 2>&1
```

#### B. Automasi Moden menerusi Unit `systemd.service` & `systemd.timer`
Mewujudkan servis sandaran di `/etc/systemd/system/local-backup.service`:
```ini
[Unit]
Description=Servis Sandaran Sistem Tempatan CU04
After=network.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/system_backup.sh
```

Mewujudkan pemasa di `/etc/systemd/system/local-backup.timer`:
```ini
[Unit]
Description=Pemasa Sandaran Harian CU04

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

Mengaktifkan pemasa `systemd`:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now local-backup.timer
sudo systemctl list-timers
```

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)
- [ ] Berjaya membina dan mengekstrak arkib `.tar.zst` dan `.tar.gz`.
- [ ] Berjaya menyegerakkan direktori menggunakan `rsync` dengan opsi `--delete-after`.
- [ ] Memahami dan mengaplikasikan prinsip sandaran 3-2-1.
- [ ] Mampu mengkonfigurasi automasi sandaran berkala menerusi `cron` atau `systemd.timer`.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)
1. *"Apakah perbezaan prestasi dari segi saiz dan masa pemprosesan antara zstd, xz, dan gzip apabila mermampatkan log bersaiz 10GB?"*
2. *"Tunjukkan skrip Bash lengkap yang merangkumi pengarkiban tar.zst, semakan integriti sha256sum, dan penghantaran laporan e-mel/journalctl."*
3. *"Bagaimanakah cara mengkonfigurasi systemd.timer untuk menjalankan sandaran hanya apabila sistem berada dalam keadaan idle?"*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)
- [Dokumentasi Rasmi GNU Tar](https://www.gnu.org/software/tar/manual/)
- [Panduan Pemampatan Zstandard (zstd)](https://facebook.github.io/zstd/)
- [Rsync Official Documentation & Manual](https://rsync.samba.org/)
- [Systemd Timers Wiki & Guide](https://wiki.archlinux.org/title/Systemd/Timers)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)
- **Linux Administration Handbook (5th Edition)** oleh Evi Nemeth, Garth Snyder, Trent R. Hein, Ben Whaley.
- **Mastering Linux System Administration** oleh Christine Bresnahan & Richard Blum.
- **Panduan Praktikal Pentadbiran & Sandaran Pelayan Linux** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
