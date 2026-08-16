---
okf_version: 0.1
type: knowledge_node
title: "Pengenalan Linux & Sejarah Pembangunannya"
timestamp: "2026-08-16T10:29:00Z"
topics: ["linux-history", "open-source", "cu01", "ekosistem-linux"]
tags: ["linux", "sejarah", "kernel", "gnu", "cu01", "pengenalan"]
description: "Nod pengetahuan tentang sejarah Linux, tokoh-tokoh kunci, dan falsafah perisian bebas. Dikemaskini dengan fakta terkini 2024-2025."
resource: "file:///palace/cu01/pengenalan-linux-dan-sejarah.md"
---

# 🧠 Pengenalan Linux & Sejarah Pembangunannya

> *"An operating system is not just software. It is a political statement about who controls computing."*
> — Richard Stallman

---

## 1. Apakah Linux?

Linux bukan sekadar sebuah sistem operasi — ia adalah sebuah **pergerakan sosial teknologi** yang mencabar dominasi perisian proprietari. Secara teknikalnya, **Linux** merujuk kepada **isirung (kernel)** sahaja — otak yang berkomunikasi antara perkakasan (hardware) dan perisian (software). Apa yang pengguna kenali sebagai "Linux" sebenarnya adalah **GNU/Linux**: gabungan isirung Linux dengan alatan GNU yang dibangunkan oleh Richard Stallman.

### Prinsip Tunjang Linux
| Prinsip | Penjelasan |
|---------|------------|
| **Sumber Terbuka** | Kod sumber boleh diperiksa, diubah suai, dan diedarkan semula oleh sesiapa sahaja |
| **Berbilang pengguna** | Ramai pengguna boleh beroperasi serentak tanpa mengganggu satu sama lain |
| **Berbilang tugas** | Boleh menjalankan pelbagai proses secara serentak |
| **Keselamatan lapisan** | Model kebenaran Unix dengan pemisahan `root` dan pengguna biasa |
| **Kestabilan jangka panjang** | Pelayan Linux boleh beroperasi selama bertahun-tahun tanpa memerlukan but semula |

---

## 2. Sejarah & Tokoh-Tokoh Tunjang

### 2.1 Linus Benedict Torvalds (1991 - Kini)
**Status terkini (2024)**: Linus Torvalds masih aktif mengetuai pembangunan isirung Linux di bawah naungan **Linux Foundation**. Beliau kini menetap di Amerika Syarikat dan menggunakan workstation berasaskan AMD untuk pembangunan harian.

Pada bulan Ogos 1991, seorang pelajar berusia 21 tahun dari Universiti Helsinki, Finland menghantar mesej bersejarah ke kumpulan berita **comp.os.minix**:

> *"I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu) for 386(486) AT clones."*

Hobi kecil beliau kini telah menjadi kuasa yang menjalankan:
- **96.4%** daripada pelayan-pelayan awan teratas dunia
- **100%** daripada 500 superkomputer terpantas di dunia (Top500, 2024)
- Hampir semua infrastruktur internet global

**Perkembangan Isirung (Kernel):**
| Tahun | Versi Isirung | Pencapaian Penting |
|-------|--------------|-------------------|
| 1991 | 0.01 | Versi pertama, ~10,000 baris kod |
| 1994 | 1.0 | Stabil untuk pengguna am |
| 2003 | 2.6 | Sokong SMP & berbilang seni bina |
| 2011 | 3.0 | Nombor versi dirombak semula |
| 2015 | 4.0 | Tampalan langsung tanpa but semula (live patching) |
| 2022 | 5.19 | Sokong penuh Rust sebagai bahasa pengaturcaraan kedua |
| 2024 | **6.11** | Versi terkini, Rust semakin meluas, sokong perkakasan AI/GPU terkini |

### 2.2 Richard Matthew Stallman (1983 - Kini)
Pengasas **Projek GNU** dan **Free Software Foundation (FSF)**. Stallman memulakan projek GNU pada 1983 dengan matlamat membina sistem operasi bebas sepenuhnya. Beliau memperkenalkan konsep **copyleft** melalui **Lesen GNU GPL (General Public License)**.

**Empat Kebebasan Perisian Bebas** (Prinsip Yang Masih Relevan):
1. Kebebasan untuk **menjalankan** program bagi apa-apa tujuan
2. Kebebasan untuk **mengkaji** cara program berfungsi dan menyesuaikannya
3. Kebebasan untuk **mengedarkan** salinan
4. Kebebasan untuk **meningkatkan** program dan menyebarkan versi yang dipertingkat

> **⚡ Kemaskini 2024:** Stallman masih mengetuai FSF. Projek GNU kini mempunyai lebih 400 pakej perisian aktif.

### 2.3 Alan Cox
Salah seorang penyumbang isirung Linux yang paling berpengaruh, terutama dalam pembangunan sistem rangkaian (networking stack) dan pemprosesan selari (SMP). Beliau adalah "penjaga isirung" (kernel maintainer) tidak rasmi untuk siri isirung 2.x. Banyak berjasa dalam menjadikan Linux stabil di atas perkakasan Intel x86.

### 2.4 Ian Murdock (1973 - 2015)
Pengasas **Debian GNU/Linux** pada tahun 1993. Nama "Debian" berasal daripada gabungan nama beliau dan teman wanitanya, Debra. Falsafah Debian yang mengutamakan kestabilan dan kebebasan telah menjadi asas kepada ratusan distribusi lain termasuk Ubuntu.

> *Ian Murdock meninggal dunia pada 28 Disember 2015. Warisannya hidup melalui Debian yang masih antara distribusi paling berpengaruh.*

---

## 3. GNU GPL & Lesen Hak Cipta Terbuka

Linux dilesenkan di bawah **GNU GPL versi 2 (GPLv2)**. Ini bermakna:

- Anda **boleh** menggunakan Linux secara percuma untuk apa-apa tujuan
- Anda **boleh** melihat dan mengubah suai kod sumber
- Jika anda mengedar versi yang diubah, **anda mesti** juga mengedar kod sumbernya
- Syarikat **tidak boleh** menjadikan Linux proprietari

**Ekosistem Lesen Terbuka (2024):**
| Lesen | Digunakan Oleh | Ciri Khas |
|-------|---------------|-----------|
| GPL v2 | Isirung Linux | "Copyleft" kuat - tular |
| GPL v3 | Kebanyakan alatan GNU | Tambah perlindungan tivoization |
| MIT | Alpine Linux pakej, banyak skrip | Permisif, boleh digabung ke proprietari |
| Apache 2.0 | Android (AOSP) | Permisif dengan klausa paten |
| Creative Commons BY-SA 4.0 | **Projek ini (kandungan)** | Berkongsi dengan pengiktirafan |

---

## 4. Kedudukan Linux di Malaysia

Linux mempunyai peranan yang signifikan dalam ekosistem teknologi Malaysia:

- **MAMPU (Malaysian Administrative Modernisation and Management Planning Unit)**: Telah menggalakkan penggunaan Open Source Software (OSS) dalam sektor awam sejak 2001
- **Universiti awam**: Kebanyakan makmal pengkomputeran universiti menggunakan Linux
- **Awan**: Semua CSP utama (AWS, Azure, GCP) di Malaysia menawarkan mesin maya Linux
- **NOSS & TVET**: Silibus IT kebangsaan kini memasukkan Linux sebagai keperluan mandatori

---

## 5. Latihan Pemahaman

1. Mengapakah Linux dianggap lebih selamat berbanding sistem operasi lain?
2. Apakah perbezaan antara "Linux" dan "GNU/Linux"?
3. Bagaimanakah GPL memastikan Linux kekal sebagai perisian bebas?
4. Senaraikan 3 tokoh yang paling berjasa kepada ekosistem Linux dan terangkan sumbangan masing-masing.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
