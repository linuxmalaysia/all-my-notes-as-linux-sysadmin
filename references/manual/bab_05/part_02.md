---
okf_version: '0.2'
name: Bab 5 - Bahagian 2
topics:
- linux
- manual
- references
- chapter-5
tags:
- noss
- dbp
spec_version: '0.2'
type: reference
title: Bab 5 - Bahagian 2
description: Dokumentasi OKF v0.2 bagi part_02.md.
status: stable
stale_after: '2027-12-31'
generated:
  by: OKF v0.2 Adoption Tooling / Gemini 2.5 Pro
  at: '2026-10-02T08:43:42Z'
sources:
- id: internal-legal-notice
  title: Dokumen Notis Perundangan, Privasi & Penafian / Legal Notice
  author: Harisfazillah Jamel (LinuxMalaysia)
  url: docs/legal-notice.md
  resource: docs/legal-notice.md
- id: google-okf-v02-spec
  title: Open Knowledge Format v0.2 Specification & Trust Signals
  author: Google Cloud Data Analytics
  url: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
  resource: https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals
- id: redlinesoft-attested-computations
  title: Attested Computations in Open Knowledge Format (OKF v0.2)
  author: RedLineSoft
  url: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
  resource: https://blog.redlinesoft.net/posts/attested-computations-in-open-knowledge-format/
- id: dsom-okf-v02-adoption-skill
  title: OKF v0.2 Adoption Engineer Skill Standard
  author: Deep State of Mind (DSOM)
  url: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
  resource: https://deep-state-of-mind-for-my-ai.readthedocs.io/en/latest/.agents/skills/okf-v02-adoption-engineer/SKILL/
---

# Bab 5 - Bahagian 2

ata dengan menggunakan
arahan makewhatis, ia boleh di dapati di /usr/sbin direktori. anda harus log masuk (login)
sebagai “root”.
# makewhatis

14.12 Mendapatkan Bantuan Dengan man
Kesemua pecahan Linux datang dengan manual yang mengandungi informasi mengenai
program, utiliti, arahan dan program sistem.
Dengan menggunakan man anda boleh mencetak halaman manual untuk mendapatkan
arahan, file. Sebagai contoh anda boleh membaca lebih banyak mengenai man melalui
beberapa arahan.
# man man
Arahan ini akan menghantar halaman manual terus kepada skrin. anda terpaksa
menggunakan "less pager" untuk "scroll" isi kandungannya. Ingat halaman manual
merupakan fail "text" yang di tulis menggunakan format-format yang tertentu.
Untuk membaca format halaman, gunakan pilihan "section" yang di dapati di
/usr/man/man7 seperti yang di tunjuk di bawah
# man 7 man
Halaman manual dan dokumentasi boleh di dapati di /usr/man. Rujukan 5.1 menunjukkan
seksyen halaman man
Seksyen Jenis Dokumentasi
1 Arahan Global
2 Panggilan Sistem Isirung (kernel)
3 Panggilan Perpustakaan
4 Fail Khas
5 Format Fail (/etc/passwd dan sebagainya)
6 Permainan

7 Format Makro (format halaman man)
8 Pengendalian Sistem (utiliti root)
9 Rutin Isirung (kernel)
Jadual 12 : Jenis dokumentasi
Fail dari setiap halaman manual dinamakan dengan sambungan satu digit dan akan di
simpan di sub-direktori /usr/man. Halaman manual untuk Red Hat Linux arahan akan
disalin kepada cakera komputer semasa proses pemuatan.
Anda juga boleh mendapatkan maklumat terperinci mengenai dokumentasi Linux arahan
di direktori /usr/doc. Di situ juga terdapat FAQ (Frequently Asked Questios),
Dokumentasi How-To, Dokumentasi HTML dan sebagainya.
14.13 Kumpulan Arahan Linux
Kesemua arahan yang telah dikumpulkan ini merupakan arahan-arahan yang banyak
digunakan di dalam Linux. Untuk mendapatkan penjelasan yang lebih komprehensif anda
dinasihati merujuk kepada halaman man.
14.13.1 Araha n Informasi Sistem
Arahan Ulasan
Date Mengubah atau memberikan tarikh sistem
Who Menunjukkan pengguna yang telah log masuk
Whois Program pencari IP/Domain
W Menunjukkan pengguna yang telah log masuk
Jadual 13 : Arahan informasi sistem

14.13.2 Arahan Berhubungan Fail
Arahan Ulasan
Ls Melayari kandungan sesebuah lipatan
Pwd Memberitahu lipatan semasa
Cp Salin fail atau lipatan
Rm Buang fail atau lipatan
Mkdir Buat lipatan
Cat Menulis kandungan fail kepada monitor
Vi Menjalankan teks editor
Jadual 14 : Arahan perhubungan fail
14.13.3 Arahan Akses
Arahan Ulasan
Chmod Mengubah penetapan akses pada fail dan lipatan
Chown Mengubah kepunyaan pengguna pada fail dan lipatan
Chgrp Mengubah kepunyaan kumpulan pengguna pada fail dan lipatan
Umask Set lapangan mod asas
Jadual 15 : Arahan akses
14.13.4 Arahan Proses
Arahan Ulasan
& Mengarahkan sesuatu proses supaya dijalankan secara sembunyi
Ps Melaporkan status proses
Kill Membu nuh proses berdasarkan PID
Nice Pr ogram yang boleh mengubah keutamaan proses yang berjalan
Top Menunjukkan proses kemuncak yang dijalankan CPU
Vmstat Melaporkan statistik memori maya
Jadual 16 : Arahan proses

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
