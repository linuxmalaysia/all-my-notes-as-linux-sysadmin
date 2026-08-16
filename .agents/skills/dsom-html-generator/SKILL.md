---
okf_version: 0.1
name: dsom-html-generator
description: Skrip automasi untuk menjana tapak web statik HTML ke dalam direktori /html daripada keseluruhan struktur fail Markdown repositori (DSOM-Safe).
topics: [web, html, static-site, automation, scripts]
tags: [html, web, generator, dsom, scripts, static]
type: operational_skill
---

# 🌐 Penjana Tapak Web Statik (DSOM HTML Generator)

## Bilakah kemahiran ini patut digunakan?
Gunakan kemahiran ini selepas penambahan atau pengemaskinian struktur dokumen Markdown yang besar di dalam repositori (contohnya penghasilan nota Bab baharu atau penyuntingan fail amali `SKILL.md`). Ini bertujuan untuk memperbaharui tapak web paparan awam supaya sentiasa selari dengan pangkalan pengetahuan sedia ada.

## Peringatan Keselamatan
Skrip ini beroperasi dalam mod **Baca Sahaja (Read-Only)** terhadap struktur *Sovereign Markdown Palace*. Ia meronda dokumen, menukar ekstensi `.md` kepada `.html` bagi pemautan dalaman (internal linking), merender format Markdown menjadi HTML asli berserta fail CSS, dan meletakkan output hanya di dalam direktori `html/`.

### Peraturan Reka Bentuk (Design Constraint)
1. **Metadata OKF Tersembunyi:** Metadata YAML hadapan (OKF frontmatter) daripada dokumen Markdown mestilah **TIDAK** dirender secara visual di skrin pelayar web. Ia mesti disembunyikan sebagai Komentar HTML (`<!-- OKF Metadata: ... -->`) di dalam kod sumber. Ini memastikan pelawat awam hanya melihat nota Markdown yang bersih, tetapi pentadbir masih boleh melakukan "View Source" untuk mengesahkan pematuhan.

## Langkah-Langkah Pelaksanaan

### Menjana Laman Web Statik
Jalankan arahan skrip Python ini di terminal dari direktori akar (root) projek:
```powershell
uv run scripts/generate_html_site.py
```
> **Nota Teknikal:** Penggunaan `uv run` memastikan pakej dependensi (seperti `markdown` dan `jinja2`) dimuat turun hanya semasa waktu perjalanan (runtime) menerusi piawai PEP-723 tanpa memasangnya ke dalam persekitaran hos tempatan.

**Apa yang berlaku:**
1. Direktori `/html/` asal akan dipadam (diset semula).
2. Fail-fail `.md` yang disenaraikan oleh pengindeks akan dibaca.
3. Templat CSS generik dicipta (`html/assets/style.css`).
4. Fail-fail `*.html` yang meniru sepenuhnya hierarki asal (termasuk folder CU dan WA dari `palace/` dan `.agents/skills/`) akan dijana.
5. Anda akan menjumpai halaman direktori utama (`index.html`) yang menyatukan semua pautan tersebut.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
