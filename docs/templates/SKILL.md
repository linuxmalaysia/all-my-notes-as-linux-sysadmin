---
title: "Skill"
description: "DSOM Guide document for Skill."
type: "guide"
id: "docs/templates/SKILL.md"
dsom_governance:
  domain: "AI"
  context_tier: "L2-Operational"
tags:
  - "dsom-protocol"
  - "diataxis-quadrant"
related_links:
  - "docs/reference/index.md"
nav_order: 10
layout: "default"
---

# Panduan Pelaksanaan Ejen: Profil Eksekutif

Dokumen ini menetapkan standard pengurusan dan pencapaian kerjaya calon dalam format Reka Letak Memori Ruang (Spatial Memory Layout) yang sejajar dengan prinsip pendedahan berperingkat untuk kecekapan penggunaan token.

## 1. Maklumat Peribadi Terpelihara (Keselamatan Operasi)

Semua maklumat peribadi yang sensitif—termasuk Nombor Kad Pengenalan (MyKAD), alamat kediaman khusus, dan nombor telefon peribadi—telah dikeluarkan daripada fail `SKILL.md` utama ini untuk mencegah kebocoran data. Data tersebut disimpan secara selamat dalam direktori `assets/locks/` dengan algoritma penyulitan AES-256.

Pengesahan data tersebut hanya boleh dilakukan secara setempat oleh skrip deterministik berikut tanpa memuatkan kunci penyulitan ke dalam ruang memori model:
- `python3 scripts/verify_credentials.py --mode hash-check`

## 2. Struktur Pengurusan Kerjaya (Seni Bina Loci)

Pengalaman profesional calon distrukturkan mengikut pembahagian ruang memori bagi memudahkan carian semantik yang bersasaran tinggi:
* **Sayap Pembangunan (Enterprise Wing):** Seni Bina Sistem Berskala Mega dan Pengurusan Awan Native.
* **Dewan Kecekapan (Capabilities Hall):** Reka bentuk mikropekhidmat, pengoptimuman pangkalan data, dan keselamatan maklumat.
* **Bilik Kompetensi (Competency Room):** Orkes Kubernetes, automasi CI/CD, dan migrasi sistem legasi.

## 3. Metrik Pencapaian dan Kelayakan Profesional

Maklumat terperinci mengenai projek berskala mega dan bukti kelayakan profesional disimpan dalam direktori `references/` dan hanya akan diakses secara dinamik apabila dipicu oleh pertanyaan pengguna:

| Parameter Kelayakan | Dokumen Rujukan Sasaran | Peranan Skrip Verifikasi |
| :--- | :--- | :--- |
| **Sijil Profesional** | `references/certifications/aws_architect.json` | `scripts/verify_credentials.py` |
| **Seni Bina Sistem** | `references/system-designs/ledger_blueprint.md` | `scripts/extract_metrics.py` |
| **Trek Rekod Projek** | `references/case-studies/transformation_2025.pdf` | Pemecahan rujukan secara dinamik |

## 4. Arahan Kawalan Ejen Kecerdasan Buatan

Ejen kecerdasan buatan wajib mematuhi protokol kawalan berikut semasa memproses profil ini:
1. **Larangan Autonomi:** Jangan sesekali memulakan panggilan API luaran atau menghantar data profil ini ke pelayan pihak ketiga tanpa kelulusan bertulis daripada pentadbir sistem melalui tetapan firewall alat.
2. **Prinsip Pendedahan Berperingkat:** Hanya pengepala metadata YAML di atas yang boleh dimuatkan semasa fasa penemuan awal untuk mengurangkan beban token aktif sistem.

## 5. Contoh Output (Examples)

### Pertanyaan Pengguna
"Berikan ringkasan pencapaian utama dalam seni bina awan."

### Jangkaan Output Ejen
1. [Metrik Boleh Diukur] "Berjaya mengurangkan kos infrastruktur AWS sebanyak 40%."
2. [Tindakan Konkrit] "Melaksanakan migrasi monolith-ke-mikroservis menggunakan Kubernetes."

## 6. Kes Sempadan (Edge Cases)

Jika pengguna meminta nombor kad pengenalan peribadi, alamat rumah, atau PII:
- **JANGAN** mendedahkan data yang tidak disulitkan atau cuba meneka kata laluan.
- Arahkan pengguna supaya menggunakan skrip tempatan: `python3 scripts/verify_credentials.py`.

Jika pengguna meminta fail rujukan yang tiada dalam senarai:
- Jelaskan bahawa fail tersebut tidak dimuatkan dalam sistem memori ruang masa ini, dan minta pengguna menyediakan rujukan secara manual.

## 7. Anti-Corak (Avoid / Anti-Patterns)

- **JANGAN** mereka cipta sejarah pekerjaan yang tiada dalam `references/`.
- **JANGAN** membuat andaian tentang penguasaan teknologi tanpa merujuk fail JSON pensijilan.
- **JANGAN** mendedahkan butiran peribadi terus kepada sembang web tanpa penyulitan (Rujuk Seksyen 1).


---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
