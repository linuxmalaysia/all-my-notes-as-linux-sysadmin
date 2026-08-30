---
okf_version: 0.1
type: documentation
title: "Topik 1: Pengenalan & Asas Ekosistem Linux (CU01) — Dikemaskini 2026"
timestamp: "2026-08-17T00:00:00Z"
topics: ["linux-desktop", "gnome", "nautilus", "synaptic", "gnome-software", "tarball", "cu01", "pemasangan-linux", "luks2", "editor", "bashrc"]
tags: ["linux", "desktop", "gnome", "nautilus", "synaptic", "gnome-software", "tarball", "sejarah", "distribusi", "cu01", "gpl", "ubuntu", "fedora", "almalinux", "luks2", "editor", "bashrc"]
description: "Silibus komprehensif CU01 dikemaskini dengan Persekitaran Meja GNOME (GNOME 48/47), Pengurus Fail Nautilus, pengurusan pakej GUI (Synaptic, GNOME Software), pengompilan tarball, edaran rujukan 2026 (Ubuntu 26.04 LTS, Fedora 43, AlmaLinux 10), penyulitan LUKS2, dan konfigurasi $EDITOR/$VISUAL."
resource: "file:///openwiki/topic-01-linux-desktop-and-basics.md"
---

# Topik 1: Pengenalan & Asas Ekosistem Linux (CU01)

## Gambaran Keseluruhan (Overview)

Topik ini membina asas konseptual dan amali yang kukuh mengikut piawaian **NOSS Level 3 (CU01)**. Ia menggabungkan **konteks sejarah, falsafah perisian bebas, landskap distribusi rujukan 2026 (Ubuntu 26.04 LTS, Fedora 43, AlmaLinux 10), persekitaran meja grafik GNOME (GNOME 48/47), pengurus fail Nautilus, pengurusan perisian GUI & CLI (APT, DNF5, Synaptic, GNOME Software, Flatpak, Snap, pengompilan Tarball), penyulitan penuh cakera LUKS2 pejabat, penyesuaian pemboleh ubah persekitaran shell ($EDITOR/$VISUAL), serta penegasan keselamatan pasca-pemasangan**.

> **💡 Kemahiran Kognitif - Peningkatan Tahap Pengabstrakan:**
> Daripada sekadar mempelajari "cara pasang Linux" (spesifik) → fahami "mengapa Linux wujud dan bagaimana struktur storan serta persekitaran grafik selamat direka" (corak) → hayati "apakah makna perisian bebas dan kedaulatan data untuk pengkomputeran enterprise" (prinsip universal).

---

## Silibus Utama

### 1. Sejarah & Asal-Usul Linux

- Linus Torvalds, Universiti Helsinki, 1991: Dari hobi kepada infrastruktur global
- Projek GNU & Richard Stallman: Falsafah 4 Kebebasan Perisian
- Evolusi isirung: Linux 0.01 (1991) → Linux 6.14 LTS (2026, ~38 juta baris kod)
- Mengapa Linux menguasai 96.4% pelayan awan dan 100% superkomputer dunia

**📖 Baca Lanjut:** [manual/cu01/pengenalan-linux-dan-sejarah.md](../manual/cu01/pengenalan-linux-dan-sejarah.md)

### 2. Falsafah, Perkakasan Sumber Terbuka (OSHW) & Lesen GNU GPL

- Perbezaan antara "perisian bebas" (*free software*) dan "sumber terbuka" (*open source*)
- **Perkakasan Sumber Terbuka (Open-Source Hardware - OSHW)**: Skematik, CAD, dan BOM fizikal awam (contoh: Papan kekunci mekanikal QMK Firmware & QMK Configurator di [docs.qmk.fm](https://docs.qmk.fm/))
- GNU GPL v2 (isirung Linux), MIT, Apache, CC BY-SA
- Hak pengguna di bawah perisian & perkakasan terbuka
- Implikasi di Malaysia: Akta Hak Cipta 1987

**📖 Baca Lanjut (Lesen):** [manual/cu01/hakcipta-dan-pelesenan.md](../manual/cu01/hakcipta-dan-pelesenan.md)
**📖 Tutorial Amali OSHW & QMK:** [docs/tutorials/opensource-keyboard-qmk.md](../docs/tutorials/opensource-keyboard-qmk.md)

### 3. Ekosistem Distribusi Linux 2026 (Piawaian Kanonik)

- **Ubuntu 26.04 LTS "Resolute Raccoon"**: Rujukan utama desktop, latihan, dan awan (Isirung 6.14 LTS, GNOME 48)
- **AlmaLinux 10 "Purple Lion"**: Rujukan pelayan & desktop perusahaan (Isirung 6.12 LTS, GNOME 47, sokongan sehingga 2035)
- **Fedora 43**: Rujukan teknologi terkini (bleeding-edge workstation)
- **Distribusi Khusus**: Kali Linux (keselamatan), Alpine Linux (kontena), Raspberry Pi OS (IoT)

**📖 Baca Lanjut:** [manual/cu01/pecahan-linux-terkini.md](../manual/cu01/pecahan-linux-terkini.md)

### 4. Keperluan Perkakasan, BIOS/UEFI & Persekitaran Meja GNOME (CU01-WA04)

- Spesifikasi minimum & disyorkan (x86_64, ARM64)
- Perbezaan Legacy BIOS (MBR) vs UEFI (GPT)
- Konfigurasi Secure Boot, CSM, dan penyediaan Bootable Live USB (`dd`, Ventoy)
- **Persekitaran Meja GNOME (GNOME 48 / 47)**:
  - Komponen Meja Kerja: Panel Atas (*Top Bar*), Menu Aktiviti (*Activities*), Aplet Sistem, dan Penukar Ruang Kerja (*Workspace Switcher*).
  - **Pengurus Fail Nautilus (GNOME Files)**: Navigasi hierarki pepohon (*tree view*), kawalan prestasi gambaran kecil (*thumbnail*), dan operasi heret-dan-lepas (*drag-and-drop*).

**📖 Baca Lanjut (BIOS/UEFI):** [manual/cu01/keperluan-perkakasan-dan-bios-uefi.md](../manual/cu01/keperluan-perkakasan-dan-bios-uefi.md)
**📖 Baca Lanjut (OS & GNOME):** [manual/cu01/cu01-wa04-pemasangan-os-desktop-linux.md](../manual/cu01/cu01-wa04-pemasangan-os-desktop-linux.md)

### 5. Prosedur Pemasangan Sistem Operasi & Storan LVM

- Langkah demi langkah pemasangan Ubuntu 26.04 LTS, AlmaLinux 10, dan Fedora 43
- Skema pembahagian storan LVM (`/boot/efi`, `/`, `/var`, `/home`, `swap`)

**📖 Baca Lanjut:** [manual/cu01/prosedur-pemasangan-ubuntu-almalinux.md](../manual/cu01/prosedur-pemasangan-ubuntu-almalinux.md)

### 6. Penyulitan Penuh Cakera LUKS2 Pejabat (ISO/IEC 27001 & MAMPU)

- Konfigurasi LUKS2 FDE dengan algoritma AES-256-XTS
- Pengurusan berbilang slot kunci (*multi-user key slots*) untuk pengguna dan pentadbir IT
- Pematuhan piawaian keselamatan ISO/IEC 27001 (A.8.24) & Pekeliling MAMPU/JDN

**📖 Baca Lanjut:** [manual/cu01/penyulitan-cakera-luks2-pejabat.md](../manual/cu01/penyulitan-cakera-luks2-pejabat.md)

### 7. Pemasangan Aplikasi, Pemacu Peranti & Persekitaran Shell (CU01-WA05)

- **Perbandingan Format Pembungkusan & Utiliti GUI/CLI**:
  - Pakej Binari Asli CLI: Debian/Ubuntu (`.deb` / DEB via `apt`/`dpkg`), Red Hat/AlmaLinux/Fedora (`.rpm` / RPM via `dnf5`/`rpm`). Operasi asas `rpm`: `-ivh`, `-Uvh`, `-q`, `-V`, `-e`, `--rebuilddb`.
  - Pakej Perisian Grafik GUI: **GNOME Software**, **Synaptic Package Manager**, **PackageKit**.
  - Pakej aplikasi universal dengan pengasingan: `Flatpak` (Flathub) dan `Snap` (Canonical) untuk pengasingan persekitaran pejabat.
  - Kod Sumber Tarball: Arkib `.tar.gz` / `.tar.zst`. Semak README/INSTALL untuk sistem binaan (seperti Autotools `./configure`, `make`, `sudo make install`).
  - Pakej Sumber RPM (`.src.rpm`): Binaan semula `rpmbuild --rebuild` selepas penyelesaian `BuildRequires`.
- **Penyesuaian Pemboleh Ubah Persekitaran Shell**: `$EDITOR` & `$VISUAL` dalam `~/.bashrc`, `/etc/environment`, `/etc/profile.d/editor.sh`.
- **Pengesahan dan Pemasangan Pemacu GPU (NVIDIA/AMD) & Kad Peranti**:
  - Deteksi perkakasan: `lspci`.
  - Ubuntu/NVIDIA: `ubuntu-drivers` dan `nvidia-smi`.
  - Fedora/AlmaLinux/NVIDIA: RPM Fusion, `dnf install akmod-nvidia`, dan `nvidia-smi`.
  - AMD Radeon: Pemacu sumber terbuka `Mesa`/`amdgpu` dengan pengesahan `glxinfo`.

**📖 Baca Lanjut:** [manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md](../manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md)

### 8. Konfigurasi Sambungan Rangkaian Endpoint (CU01-WA06)

- Pengurusan sambungan berwayar dan Wi-Fi menggunakan NetworkManager (`nmcli`) dan `iproute2`
- Penetapan Alamat IP Statik, DHCP, dan pelayan DNS
- Pengerasan keselamatan profil sambungan dan resolusi nama DNS

**📖 Baca Lanjut:** [manual/cu01/cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint.md](../manual/cu01/cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint.md)

### 9. Tugasan Pasca-Pemasangan & Hardening

- Konfigurasi tembok api (*firewall*) UFW dan firewalld
- Pengerasan perkhidmatan SSH daemon dan auditing log keselamatan

**📖 Baca Lanjut:** [manual/cu01/penegasan-keselamatan-sistem.md](../manual/cu01/penegasan-keselamatan-sistem.md)

### 10. Soal Jawab (FAQ) & Direktori Perisian Alternatif

- Soalan lazim pengguna baharu Linux
- Padanan aplikasi Windows ke Linux (CAD, Pelayar Web, RDBMS)

**📖 Baca Lanjut (FAQ):** [manual/cu01/soal-jawab-linux.md](../manual/cu01/soal-jawab-linux.md)
**📖 Baca Lanjut (Direktori):** [manual/cu01/direktori-sumber-rujukan.md](../manual/cu01/direktori-sumber-rujukan.md)

---

## Pemetaan CU & WA

| Kod | Nama | Status |
|-----|------|--------|
| **CU01-WA00** | Memahami Ekosistem Linux | [Lihat Skill](../.agents/skills/cu01-wa00-memahami-ekosistem-linux/SKILL.md) |
| **CU01-WA04** | Pasang OS Desktop & GNOME | [Lihat Skill](../.agents/skills/cu01-wa04-install-computer-desktop-operating-systems/SKILL.md) |
| **CU01-WA05** | Pasang Aplikasi & Pemacu | [Lihat Skill](../.agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md) |
| **CU01-WA06** | Konfigurasi Rangkaian Endpoint | [Lihat Skill](../.agents/skills/cu01-wa06-configure-endpoint-network-connectivity/SKILL.md) |

---

## Eksplorasi Lanjut bersama AI (AI Prompts)

Gunakan *prompt* berikut bersama AI (seperti ChatGPT, Claude, atau Gemini) untuk mendalami topik ini:
1. > "Bolehkah anda terangkan perbezaan antara Kernel Linux dan Persekitaran Meja GNOME (seperti GNOME 48 di Ubuntu 26.04 LTS) menggunakan analogi mudah yang boleh difahami oleh pelajar sekolah?"
2. > "Tuliskan skrip Bash ringkas untuk menyemak sama ada peranti but beroperasi dalam mod UEFI atau Legacy BIOS, dan paparkan ruang peranti storan dalam format jadual."
3. > "Bagaimanakah pengurus fail Nautilus menguruskan paparan thumbnail dan struktur paparan pepohon (tree view) untuk mempercepatkan carian fail di stesen kerja enterprise?"
4. > "Saya seorang pentadbir sistem di agensi kerajaan. Apakah senarai semak keselamatan pasca-pemasangan (hardening checklist) pertama yang wajib saya laksanakan pada AlmaLinux 10?"

---

## Bahan Bacaan Lanjut (Rujukan URL)

- [Dokumentasi Rasmi Ubuntu 26.04 LTS](https://help.ubuntu.com)
- [Dokumentasi Rasmi AlmaLinux 10](https://wiki.almalinux.org)
- [Dokumentasi Fedora Project](https://docs.fedoraproject.org)
- [Dokumentasi Rasmi GNOME Desktop](https://help.gnome.org)
- [Dokumentasi Synaptic Package Manager Guide](https://help.ubuntu.com/community/SynapticHowto)
- [Sejarah Lengkap Linux (Wikipedia BM)](https://ms.wikipedia.org/wiki/Linux)
- [Projek GNU dan Maksud Perisian Bebas](https://www.gnu.org/philosophy/free-sw.ms.html) — (Tersedia dalam Bahasa Melayu)
- [DistroWatch.com](https://distrowatch.com) — Tangga & statistik distribusi Linux terkini dunia
- [kernel.org](https://kernel.org) — Repositori rasmi Isirung Linux
- [Jabatan Digital Negara (JDN) / MAMPU Malaysia](https://www.jdn.gov.my) — Dasar OSS & Pekeliling Keselamatan ICT sektor awam Malaysia
- [The Linux Foundation](https://www.linuxfoundation.org)

---

## Buku Boleh Dibeli (Syor Bacaan)

Jika anda ingin membina pemahaman yang lebih mendalam, berikut adalah senarai buku yang disyorkan:

**Bahasa Melayu:**
1. *Asas Sistem Operasi Linux* oleh Harisfazillah Jamel — Sesuai untuk pemula yang ingin memahami konsep asas dalam konteks Malaysia.
2. *Panduan Mudah Ubuntu Linux* — Buku panduan amali langkah-demi-langkah.

**English (Antarabangsa):**
1. *How Linux Works, 3rd Edition: What Every Superuser Should Know* oleh Brian Ward — Sangat disyorkan untuk memahami komponen dalaman Linux.
2. *The Linux Command Line, 2nd Edition* oleh William Shotts — Buku asas terbaik untuk menguasai terminal (tersedia percuma secara dalam talian, atau boleh dibeli fizikal).
3. *UNIX and Linux System Administration Handbook, 5th Edition* oleh Evi Nemeth, Garth Snyder, Trent R. Hein, Ben Whaley, Dan Mackin — Kitab rujukan utama pentadbir sistem profesional.
4. *Just for Fun: The Story of an Accidental Revolutionary* oleh Linus Torvalds & David Diamond — Autobiografi pencipta Linux yang santai dan memberi inspirasi.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
