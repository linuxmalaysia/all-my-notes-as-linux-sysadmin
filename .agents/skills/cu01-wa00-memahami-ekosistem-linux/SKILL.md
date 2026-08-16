---
okf_version: 0.1
name: cu01-wa00-memahami-ekosistem-linux
description: Kemahiran Asas: Memahami ekosistem Linux, sejarahnya, distribusi terkini, dan falsafah perisian bebas sebagai asas kepada semua CU01 yang seterusnya.
topics: [noss, cu01, wa00, linux-intro, ekosistem]
tags: [linux, pengenalan, sejarah, distribusi, gpl, cu01]
type: foundational_skill
---

# 🐧 CU01-WA00: Memahami Ekosistem Linux

## Tujuan Kemahiran
Kemahiran asas ini mewujudkan pemahaman konseptual dan kontekstual yang kukuh tentang ekosistem Linux sebelum pelajar meneruskan kepada kemahiran praktikal pemasangan dan konfigurasi. Tanpa pemahaman ini, pelajar akan cenderung menjadi "pengguna arahan buta" tanpa memahami mengapa dan bagaimana sistem ini berfungsi.

> **💡 Pemikiran Rantaian Ke Belakang:** Matlamat akhir ialah pentadbir sistem Linux yang mahir. Untuk sampai ke sana, pelajar perlu terlebih dahulu *memahami falsafah* ekosistem — barulah tangan mengikut minda.

---

## Hasil Pembelajaran (Learning Outcomes)

Setelah menyelesaikan kemahiran ini, pelajar berupaya untuk:

1. **Menerangkan** asal-usul dan evolusi Linux daripada projek hobi kepada infrastruktur global
2. **Membezakan** antara isirung Linux (kernel) dengan distribusi Linux lengkap
3. **Mengenalpasti** tokoh-tokoh kunci dalam ekosistem Linux dan sumbangan masing-masing
4. **Menerangkan** prinsip lesen GNU GPL dan kepentingannya kepada komuniti perisian bebas
5. **Memilih** distribusi Linux yang paling sesuai berdasarkan kes penggunaan yang diberikan
6. **Membandingkan** ekosistem Linux 2024 dengan landskap teknologi semasa

---

## Kandungan Silibus

### Modul A: Sejarah & Falsafah
- Kelahiran Linux: Linus Torvalds dan Universiti Helsinki (1991)
- Projek GNU dan Richard Stallman: Mengapa "GNU/Linux" lebih tepat
- Evolusi isirung dari 0.01 (1991) → 6.11 (2024)
- Falsafah perisian bebas vs sumber terbuka (Free Software vs Open Source)

**Nod Palace:** [pengenalan-linux-dan-sejarah.md](../../palace/cu01/pengenalan-linux-dan-sejarah.md)

### Modul B: Lesen & Hak Cipta
- GNU GPL v2 — Lesen isirung Linux
- Perbezaan: GPL, MIT, Apache, CC BY-SA
- Hak pengguna di bawah perisian berlesen terbuka
- Implikasi perundangan di Malaysia (Akta Hak Cipta 1987)

### Modul C: Landskap Distribusi Linux 2024
- Keluarga Debian: Debian, Ubuntu, Linux Mint
- Keluarga Red Hat: Fedora, RHEL, AlmaLinux, Rocky Linux
- Keluarga Arch: Arch Linux, Manjaro
- Keluarga SUSE: openSUSE Leap, Tumbleweed
- Distribusi Khusus: Kali Linux, Alpine, Raspberry Pi OS

**Nod Palace:** [pecahan-linux-terkini.md](../../palace/cu01/pecahan-linux-terkini.md)

### Modul D: Linux dalam Konteks Malaysia
- Dasar Sumber Terbuka Kerajaan Malaysia (OSS Policy 2001)
- MAMPU dan inisiatif perisian bebas sektor awam
- Penggunaan Linux dalam universiti awam Malaysia
- Keperluan NOSS / TVET dan sijil kebangsaan

---

## Penilaian (Assessment)

### Teori (40%)
- Uji Pra: Pengetahuan asas OS sebelum kursus
- Soal Jawab Kelas: Perbincangan tokoh dan falsafah Linux
- Kuiz Ringkas: Padanan distribusi dengan kes penggunaan

### Amali Asas (60%)
```bash
# Aktiviti 1: Kenali sistem anda
cat /etc/os-release
uname -r
hostnamectl

# Aktiviti 2: Semak isirung dan seni bina
uname -a
lscpu | head -20

# Aktiviti 3: Terokai ekosistem dalam terminal
# (Tanpa internet - hanya gunakan man pages)
man intro
man linux
```

---

## Rujukan Nod Palace

| Nod | Pautan | Topik |
|-----|--------|-------|
| Sejarah Linux | [pengenalan-linux-dan-sejarah.md](../../palace/cu01/pengenalan-linux-dan-sejarah.md) | Linus, GNU, GPL |
| Distribusi Terkini | [pecahan-linux-terkini.md](../../palace/cu01/pecahan-linux-terkini.md) | Ubuntu, Fedora, Debian |
| Pemasangan Desktop | [cu01-wa04](../cu01-wa04-install-computer-desktop-operating-systems/SKILL.md) | Pemasangan OS |

---

## Sumber Rujukan Luaran (2024)

- [The Linux Foundation](https://www.linuxfoundation.org)
- [DistroWatch.com](https://distrowatch.com) — Tangga populariti distribusi Linux terkini
- [kernel.org](https://kernel.org) — Muat turun isirung Linux rasmi
- [GNU.org](https://www.gnu.org) — Projek GNU dan lesen GPL
- [MAMPU OSS Portal](https://www.mampu.gov.my) — Dasar OSS Malaysia

---

*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
