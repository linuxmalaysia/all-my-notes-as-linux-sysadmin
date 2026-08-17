---
okf_version: 0.1
type: documentation
title: "Topik 1: Pengenalan & Asas Ekosistem Linux (CU01) — Dikemaskini 2026"
timestamp: "2026-08-16T00:00:00Z"
topics: ["linux-desktop", "linux-history", "distribusi", "cu01", "pemasangan-linux", "luks2"]
tags: ["linux", "desktop", "sejarah", "distribusi", "cu01", "gpl", "ubuntu", "fedora", "almalinux", "luks2"]
description: "Silibus komprehensif CU01 dikemaskini dengan edaran rujukan 2026 (Ubuntu 26.04 LTS, Fedora 43, AlmaLinux 10), penyulitan LUKS2, dan prosedur pemasangan NOSS Level 3."
resource: "file:///openwiki/topic-01-linux-desktop-and-basics.md"
---

# Topik 1: Pengenalan & Asas Ekosistem Linux (CU01)

## Gambaran Keseluruhan (Overview)

Topik ini membina asas konseptual dan amali yang kukuh mengikut piawaian **NOSS Level 3 (CU01)**. Ia menggabungkan **konteks sejarah, falsafah perisian bebas, landskap distribusi rujukan 2026 (Ubuntu 26.04 LTS, Fedora 43, AlmaLinux 10), prosedur pemasangan sistem operasi, penyulitan penuh cakera LUKS2 pejabat, pengurusan aplikasi & pemacu, konfigurasi rangkaian endpoint, serta penegasan keselamatan pasca-pemasangan**.

> **💡 Kemahiran Kognitif - Peningkatan Tahap Pengabstrakan:**
> Daripada sekadar mempelajari "cara pasang Linux" (spesifik) → fahami "mengapa Linux wujud dan bagaimana struktur storan selamat direka" (corak) → hayati "apakah makna perisian bebas dan kedaulatan data untuk pengkomputeran enterprise" (prinsip universal).

---

## Silibus Utama

### 1. Sejarah & Asal-Usul Linux

- Linus Torvalds, Universiti Helsinki, 1991: Dari hobi kepada infrastruktur global
- Projek GNU & Richard Stallman: Falsafah 4 Kebebasan Perisian
- Evolusi isirung: Linux 0.01 (1991) → Linux 6.14 LTS (2026, ~38 juta baris kod)
- Mengapa Linux menguasai 96.4% pelayan awan dan 100% superkomputer dunia

**📖 Baca Lanjut:** [manual/cu01/pengenalan-linux-dan-sejarah.md](../manual/cu01/pengenalan-linux-dan-sejarah.md)

### 2. Falsafah & Lesen GNU GPL

- Perbezaan antara "perisian bebas" dan "sumber terbuka"
- GNU GPL v2 (isirung Linux), MIT, Apache, CC BY-SA
- Hak pengguna di bawah perisian terbuka
- Implikasi di Malaysia: Akta Hak Cipta 1987

**📖 Baca Lanjut:** [manual/cu01/hakcipta-dan-pelesenan.md](../manual/cu01/hakcipta-dan-pelesenan.md)

### 3. Ekosistem Distribusi Linux 2026 (Piawaian Kanonik)

- **Ubuntu 26.04 LTS "Resolute Raccoon"**: Rujukan utama desktop, latihan, dan awan (Isirung 6.14 LTS, GNOME 48)
- **AlmaLinux 10 "Purple Lion"**: Rujukan pelayan & desktop perusahaan (Isirung 6.12 LTS, GNOME 47, sokongan sehingga 2035)
- **Fedora 43**: Rujukan teknologi terkini (bleeding-edge workstation)
- **Distribusi Khusus**: Kali Linux (keselamatan), Alpine Linux (kontena), Raspberry Pi OS (IoT)

**📖 Baca Lanjut:** [manual/cu01/pecahan-linux-terkini.md](../manual/cu01/pecahan-linux-terkini.md)

### 4. Keperluan Perkakasan & Mod Penimbalan BIOS/UEFI

- Spesifikasi minimum & disyorkan (x86_64, ARM64)
- Perbezaan Legacy BIOS (MBR) vs UEFI (GPT)
- Konfigurasi Secure Boot, CSM, dan penyediaan Bootable Live USB (`dd`, Ventoy)

**📖 Baca Lanjut:** [manual/cu01/keperluan-perkakasan-dan-bios-uefi.md](../manual/cu01/keperluan-perkakasan-dan-bios-uefi.md)

### 5. Prosedur Pemasangan Sistem Operasi & Storan LVM

- Langkah demi langkah pemasangan Ubuntu 26.04 LTS, AlmaLinux 10, dan Fedora 43
- Skema pembahagian storan LVM (`/boot/efi`, `/`, `/var`, `/home`, `swap`)

**📖 Baca Lanjut:** [manual/cu01/prosedur-pemasangan-ubuntu-almalinux.md](../manual/cu01/prosedur-pemasangan-ubuntu-almalinux.md)

### 6. Penyulitan Penuh Cakera LUKS2 Pejabat (ISO/IEC 27001 & MAMPU)

- Konfigurasi LUKS2 FDE dengan algoritma AES-256-XTS
- Pengurusan berbilang slot kunci (*multi-user key slots*) untuk pengguna dan pentadbir IT
- Pematuhan piawaian keselamatan ISO/IEC 27001 (A.8.24) & Pekeliling MAMPU/JDN

**📖 Baca Lanjut:** [manual/cu01/penyulitan-cakera-luks2-pejabat.md](../manual/cu01/penyulitan-cakera-luks2-pejabat.md)

### 7. Pemasangan Aplikasi & Pemacu Peranti Linux (CU01-WA05)

- Pengurusan pakej asli (`apt` pada Ubuntu, `dnf5` pada AlmaLinux/Fedora)
- Pakej berasaskan kontena universal (`Flatpak`, `Snap`)
- Pengesanan dan pemasangan pemacu GPU (NVIDIA/AMD) dan kad peranti

**📖 Baca Lanjut:** [manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md](../manual/cu01/cu01-wa05-pemasangan-aplikasi-dan-pemacu-peranti.md)

### 8. Konfigurasi Sambungan Rangkaian Endpoint (CU01-WA06)

- Pengurusan sambungan berwayar dan Wi-Fi menggunakan NetworkManager (`nmcli`) dan `iproute2`
- Penetapan Alamat IP Statik, DHCP, dan pelayan DNS
- Pengerasan keselamatan profil sambungan dan resolusi nama DNS

**📖 Baca Lanjut:** [manual/cu01/cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint.md](../manual/cu01/cu01-wa06-konfigurasi-sambungan-rangkaian-endpoint.md)

### 9. Tugasan Pasca-Pemasangan & Hardening

- Kemaskini repositori dan pengurusan pakej (`apt`, `dnf`)
- Pengurusan pengguna, kumpulan `sudo`/`wheel`, serta penegasan keselamatan firewall (`ufw`, `firewalld`, SSH)

**📖 Baca Lanjut:** [manual/cu01/pasca-pemasangan-dan-driver.md](../manual/cu01/pasca-pemasangan-dan-driver.md)

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
| **CU01-WA04** | Pasang Sistem Operasi Desktop | [Lihat Skill](../.agents/skills/cu01-wa04-install-computer-desktop-operating-systems/SKILL.md) |
| **CU01-WA05** | Pasang Aplikasi & Pemacu | [Lihat Skill](../.agents/skills/cu01-wa05-install-computer-applications-and-device-drivers/SKILL.md) |
| **CU01-WA06** | Konfigurasi Rangkaian Endpoint | [Lihat Skill](../.agents/skills/cu01-wa06-configure-endpoint-network-connectivity/SKILL.md) |

---

## Eksplorasi Lanjut bersama AI (AI Prompts)

Gunakan *prompt* berikut bersama AI (seperti ChatGPT, Claude, atau Gemini) untuk mendalami topik ini:
1. > "Bolehkah anda terangkan perbezaan antara Kernel Linux dan Sistem Operasi Linux (seperti Ubuntu 26.04 LTS) menggunakan analogi mudah yang boleh difahami oleh pelajar sekolah?"
2. > "Tuliskan skrip Bash ringkas untuk menyemak sama ada peranti but beroperasi dalam mod UEFI atau Legacy BIOS, dan paparkan ruang peranti storan dalam format jadual."
3. > "Bagaimanakah penyulitan cakera penuh LUKS2 melindungi data pada komputer riba pejabat jika peranti tersebut hilang atau dicuri? Terangkan fungsi ruang kunci (key slots) LUKS2."
4. > "Saya seorang pentadbir sistem di agensi kerajaan. Apakah senarai semak keselamatan pasca-pemasangan (hardening checklist) pertama yang wajib saya laksanakan pada AlmaLinux 10?"

---

## Bahan Bacaan Lanjut (Rujukan URL)

- [Dokumentasi Rasmi Ubuntu 26.04 LTS](https://help.ubuntu.com)
- [Dokumentasi Rasmi AlmaLinux 10](https://wiki.almalinux.org)
- [Dokumentasi Fedora Project](https://docs.fedoraproject.org)
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
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
