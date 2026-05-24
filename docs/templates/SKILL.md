---
name: profil-eksekutif-seni-bina-sistem-awan
description: >
  Mengandungi profil profesional, kompetensi teknikal, dan metrik pencapaian strategik calon.
  Gunakan kemahiran ini apabila ejen memerlukan data peribadi yang telah dinyahsensitasikan
  atau pengesahan kelayakan profesional untuk peranan teknologi tinggi di Malaysia.
disable-model-invocation: true
user-invocable: false
metadata:
  version: 10.0.0-palace
  license: GPL-3.0-or-later
---

# Panduan Pelaksanaan Ejen: Profil Eksekutif

[cite_start]Dokumen ini menetapkan standard pengurusan dan pencapaian kerjaya calon dalam format Reka Letak Memori Ruang (Spatial Memory Layout) yang sejajar dengan prinsip pendedahan berperingkat untuk kecekapan penggunaan token[cite: 108].

## 1. Maklumat Peribadi Terpelihara (Keselamatan Operasi)
[cite_start]Semua maklumat peribadi yang sensitif—termasuk Nombor Kad Pengenalan (MyKAD), alamat kediaman khusus, dan nombor telefon peribadi—telah dikeluarkan daripada fail `SKILL.md` utama ini untuk mencegah kebocoran data[cite: 111]. [cite_start]Data tersebut disimpan secara selamat dalam direktori `assets/locks/` dengan algoritma penyulitan AES-256[cite: 111, 112].

[cite_start]Pengesahan data tersebut hanya boleh dilakukan secara setempat oleh skrip deterministik berikut tanpa memuatkan kunci penyulitan ke dalam ruang memori model[cite: 111, 113]:
- `python3 scripts/verify_credentials.py --mode hash-check`

## 2. Struktur Pengurusan Kerjaya (Seni Bina Loci)
[cite_start]Pengalaman profesional calon distrukturkan mengikut pembahagian ruang memori bagi memudahkan carian semantik yang bersasaran tinggi[cite: 113]:
* [cite_start]**Sayap Pembangunan (Enterprise Wing):** Seni Bina Sistem Berskala Mega dan Pengurusan Awan Native[cite: 113].
* [cite_start]**Dewan Kecekapan (Capabilities Hall):** Reka bentuk mikropekhidmat, pengoptimuman pangkalan data, dan keselamatan maklumat[cite: 113].
* [cite_start]**Bilik Kompetensi (Competency Room):** Orkes Kubernetes, automasi CI/CD, dan migrasi sistem legasi[cite: 113].

## 3. Metrik Pencapaian dan Kelayakan Profesional
[cite_start]Maklumat terperinci mengenai projek berskala mega dan bukti kelayakan profesional disimpan dalam direktori `references/` dan hanya akan diakses secara dinamik apabila dipicu oleh pertanyaan pengguna[cite: 113, 114]:

| Parameter Kelayakan | Dokumen Rujukan Sasaran | Peranan Skrip Verifikasi |
| :--- | :--- | :--- |
| **Sijil Profesional** | `references/certifications/aws_architect.json` | [cite_start]`scripts/verify_credentials.py` [cite: 116] |
| **Seni Bina Sistem** | `references/system-designs/ledger_blueprint.md` | [cite_start]`scripts/extract_metrics.py` [cite: 116] |
| **Trek Rekod Projek** | `references/case-studies/transformation_2025.pdf` | [cite_start]Pemecahan rujukan secara dinamik [cite: 116, 117] |

## 4. Arahan Kawalan Ejen Kecerdasan Buatan
Ejen kecerdasan buatan wajib mematuhi protokol kawalan berikut semasa memproses profil ini:
1.  [cite_start]**Larangan Autonomi:** Jangan sesekali memulakan panggilan API luaran atau menghantar data profil ini ke pelayan pihak ketiga tanpa kelulusan bertulis daripada pentadbir sistem melalui tetapan firewall alat[cite: 118].
2.  [cite_start]**Prinsip Pendedahan Berperingkat:** Hanya pengepala metadata YAML di atas yang boleh dimuatkan semasa fasa penemuan awal untuk mengurangkan beban token aktif sistem[cite: 119].
