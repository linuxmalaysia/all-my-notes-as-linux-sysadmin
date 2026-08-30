---
okf_version: 0.1
type: knowledge-node
title: "CU01-WA04: Pemasangan OS Desktop Linux & Persekitaran Meja GNOME"
timestamp: "2026-08-17T00:00:00Z"
topics: ["noss-linux", "cu01", "wa04", "gnome", "nautilus", "applet", "workspace", "luks2"]
tags: ["cu01", "wa04", "gnome", "nautilus", "applet", "workspace", "ubuntu", "almalinux", "fedora", "luks2"]
description: "Panduan amali NOSS CU01-WA04 bagi pemasangan OS desktop Linux (Ubuntu 26.04 LTS, Fedora 43, AlmaLinux 10), penyulitan LUKS2, dan pengendalian Persekitaran Meja GNOME (Pengurus Fail Nautilus, aplet panel, penukar ruang kerja, dan penyesuaian desktop)."
resource: "file:///manual/cu01/cu01-wa04-pemasangan-os-desktop-linux.md"
---

# CU01-WA04: Pemasangan OS Desktop Linux & Persekitaran Meja GNOME

## 🎯 Objektif Pembelajaran

Menguasai prosedur amali pemasangan sistem operasi Linux desktop, penyulitan cakera LUKS2, serta navigasi dan penyesuaian **Persekitaran Meja GNOME (GNOME 48 pada Ubuntu 26.04 LTS / GNOME 47 pada AlmaLinux 10)** mengikut piawaian **NOSS Tahap 3 (CU01-WA04)**.

Setelah menyempurnakan modul ini, pelatih akan dapat:

1. Melaksanakan pemasangan OS desktop Linux (**Ubuntu 26.04 LTS "Resolute Raccoon"**, **AlmaLinux 10 "Purple Lion"**, dan **Fedora 43**) berserta penyulitan penuh cakera LUKS2.
2. Mengendalikan komponen teras Persekitaran Meja GNOME: **Pengurus Fail Nautilus**, Panel Top/Dash, Aplet Sistem, dan Penukar Ruang Kerja (*Workspace Switcher*).
3. Melaksanakan pengurusan fail moden di Nautilus: Navigasi paparan pepohon (*tree view*), kawalan gambaran kecil (*thumbnails*), carian fail, serta operasi heret-dan-lepas (*drag-and-drop*).
4. Menyelaraskan tetapan desktop GNOME (paparan, latar belakang, pintasan papan kekunci, dan sambungan rangkaian) mengikut garis panduan kelestarian dan keselamatan Jabatan Digital Negara (JDN) / MAMPU.

---

## 🛠️ Garis Panduan Amali & Prosedur Kerja

### 1. Pemasangan OS Desktop Linux & Penyulitan Cakera LUKS2

#### A. Prosedur Pemasangan Ubuntu 26.04 LTS & AlmaLinux 10
- **Ubuntu 26.04 LTS "Resolute Raccoon"**: Gunakan pemasang Subiquity dengan mod penyulitan TPM-backed FDE atau penyulitan manual LUKS2.
- **AlmaLinux 10 "Purple Lion"**: Pilih kumpulan pakej *Workstation* (GNOME Desktop) dalam pemasang Anaconda dan aktifkan penyulitan LUKS2.

#### B. Pengurusan Penyulitan LUKS2 Manual & Slot Kunci Multi-Pengguna
```bash
# Semak status penyulitan LUKS2 pada partition cakera
sudo cryptsetup luksDump /dev/nvme0n1p3

# Tambah kunci pemulihan pentadbir IT ke slot kunci 1
sudo cryptsetup luksAddKey /dev/nvme0n1p3
```

---

### 2. Pengendalian Persekitaran Meja GNOME (GNOME 48 / 47)

GNOME menyediakan persekitaran grafik berasaskan Wayland / X11 yang fleksibel untuk kegunaan pengkomputeran pejabat dan enterprise.

#### A. Komponen Utama Meja Kerja GNOME
- **Panel Atas (Top Bar / Panel)**: Menampilkan menu *Activities* (Aktiviti), jam/kalendar, status rangkaian, kelantangan suara, dan menu kawalan sesi (Log Out, Lock, Power Off).
- **Penukar Ruang Kerja (Workspace Switcher)**: Membenarkan pengasingan tetingkap aplikasi ke dalam pelbagai meja kerja maya. Pintasan papan kekunci: `Ctrl + Alt + [Panah Atas/Bawah]` atau `Super + PageUp/PageDown`.
- **Aplet Panel & Pelancar (Panel Applets & Launchers)**: Aplet pemberitahuan (seperti pengemas kini perisian, status VPN, kawalan media) yang berjalan di panel untuk pemantauan terus.

#### B. Pengurus Fail Nautilus (GNOME Files)

Nautilus merupakan shell pengurusan fail visual bersepadu di bawah GNOME:

1. **Pengeluaran & Navigasi**:
   - Membuka Nautilus: Klik ikon *Files* pada panel/dock atau tekan `Super` lalu taip `Nautilus`.
   - Mod Paparan: Paparan Ikon, Paparan Senarai (*List View*), dan Paparan Pepohon (*Tree View* - muat turun navigasi hierarki).
2. **Ciri Gambaran Kecil (Thumbnails)**:
   - Paparan gambaran kecil automatik untuk imej dan dokumen teks.
   - Penyesuaian prestasi: Dalam Tetapan Nautilus (*Preferences* ➔ *Performance*), tetapkan penciptaan thumbnail kepada *Local Files Only* atau *Never* bagi mengoptimumkan kelajuan pemprosesan cakera pada sistem enterprise.
3. **Operasi Salin & Pindah (Drag-and-Drop / Cut-Copy-Paste)**:
   - Gunakan tetikus untuk mengheret fail dari satu lokasi ke lokasi lain. Pegang kekunci `Ctrl` semasa mengheret untuk menyalin fail.
   - Pintasan: `Ctrl + C` (Salin), `Ctrl + X` (Potong), `Ctrl + V` (Tampal), `Ctrl + N` (Buka Tetingkap Nautilus Baharu).

```bash
# Membuka Pengurus Fail Nautilus dari terminal
nautilus ~

# Membuka Nautilus sebagai pentadbir (jika disokong melalui admin://)
nautilus admin:///etc/
```

#### C. Kelebihan Desktop Linux GNOME Berbanding Windows 11 & Penggunaan Google Antigravity Desktop

- **Kelebihan GNOME Desktop Berbanding Windows 11**:
  1. **Kawalan Kedaulatan Data & Bebas Telemetri**: Dalam konfigurasi lalai Ubuntu 26.04 LTS dan AlmaLinux 10 Workstation, GNOME menyediakan persekitaran desktop tanpa keperluan akaun mandatori dalam talian serta kawalan privasi data selaras dengan panduan keselamatan Jabatan Digital Negara (JDN) / MAMPU dan amalan ISO/IEC 27001.
  2. **Pengurusan Sumber Prestasi Tinggi**: Sesi Wayland pada GNOME 48/47 memaparkan kecekapan pengurusan memori (sebagai contoh, saiz penggunaan memori *idle* am dianggarkan sekitar 1.1GB–1.5GB bergantung pada perkhidmatan latar belakang) berbanding sistem pengendalian komersial yang memuatkan pelbagai aplikasi terbina (*bloatware*).
  3. **Penyulitan & Keselamatan Bersepadu**: Penyulitan cakera LUKS2 menyediakan kawalan keselamatan data pegun (*data-at-rest encryption*) dan pengurusan slot kunci bertingkat untuk perlindungan peranti fizikal.
- **Penggunaan Google Antigravity Desktop pada Linux**:
  Persekitaran pembantu AI Google Antigravity menyokong alur kerja pembangunan pada persekitaran Linux GNOME Desktop melalui integrasi terminal CLI dan ejen autonomi berstruktur.

#### D. Penyesuaian Tetapan GNOME & Tetapan Sistem (`gnome-control-center` / `gsettings`)

```bash
# Membuka Pusat Kawalan Tetapan GNOME GUI
gnome-control-center

# Penyesuaian gsettings melalui CLI (contoh: aktifkan tema gelap)
gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true
```

---

## 🔒 Pematuhan Keselamatan JDN / MAMPU & ISO/IEC 27001

1. **Kunci Skrin Automatik (Screen Lockout):** Tetapkan pengunci skrin automatik selepas 5 minit tidak aktif menerusi *Settings* ➔ *Privacy & Security* ➔ *Screen Lock*.
2. **Pengasingan Akaun Pengguna (Unprivileged User):** Elakkan daripada menjalankan sesi grafik GNOME terus sebagai pengguna `root`. Sentiasa log masuk sebagai pengguna biasa dan gunakan `sudo` bagi tugas pentadbiran.
3. **Log Keluar & Penutupan Selamat:** Pengguna wajarkan menggunakan fungsi *Log Out* atau *Power Off* menerusi menu sistem GNOME sebelum meninggalkan stesen kerja pejabat.

---

## 📋 Senarai Semak Kompetensi (Competency Checklist)

- [ ] Berjaya melaksanakan pemasangan OS desktop Linux berserta penyulitan LUKS2.
- [ ] Berjaya mengendalikan persekitaran GNOME (menu Aktiviti, Aplet Panel, dan Penukar Ruang Kerja).
- [ ] Berjaya menguruskan fail menggunakan Nautilus (paparan senarai/pepohon, thumbnail, heret-dan-lepas).
- [ ] Berjaya menyesuaikan tetapan GNOME menggunakan `gnome-control-center` dan `gsettings`.
- [ ] Mengaktifkan fungsi kunci skrin automatik demi keselamatan maklumat pejabat.

---

## 💡 Eksplorasi Lanjut bersama AI (AI Prompts)

1. *"Bagaimanakah cara mengkonfigurasi gsettings dalam skrip Bash untuk menetapkan kertas dinding dan kunci skrin secara automatik bagi semua pengguna GNOME di pejabat?"*
2. *"Bandingkan kelebihan kecekapan ruang kerja (workspaces) GNOME 48 berbanding tetingkap aplikasi bertindih dari sudut produktiviti pentadbir sistem."*
3. *"Apakah langkah-langkah untuk menyematkan pelancar aplikasi tersuai (.desktop file) pada panel Dash GNOME?"*

---

## 🔗 Bahan Bacaan Lanjut (Rujukan URL)

- [Dokumentasi Rasmi GNOME Desktop](https://help.gnome.org/)
- [Panduan Pengguna Pengurus Fail Nautilus](https://wiki.gnome.org/Apps/Nautilus)
- [Dokumentasi Ubuntu Desktop 26.04 LTS](https://help.ubuntu.com/community/GraphicalUserInterface)
- [AlmaLinux Workstation Desktop Guide](https://wiki.almalinux.org/)

---

## 📚 Buku Boleh Dibeli (Syor Bacaan)

- **GNOME Desktop Administration Guide** oleh GNOME Documentation Team.
- **The Linux Command Line, 2nd Edition** oleh William Shotts.
- **Nota Pentadbiran Sistem & Desktop Linux Malaysia** oleh Harisfazillah Jamel.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
