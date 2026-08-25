---
okf_version: 0.2
type: knowledge-index
title: "Pusat Rujukan Manual NOSS Linux Malaysia (Diátaxis Master Index)"
timestamp: "2026-08-17T00:00:00Z"
topics: ["manual", "noss-linux", "diataxis", "kurikulum", "rujukan-setempat"]
tags: ["manual", "noss", "diataxis", "indeks", "rujukan-setempat"]
description: "Pusat rujukan bersepadu silibus amali NOSS Linux Malaysia mengikut Kerangka Diátaxis merangkumi CU01 hingga CU06."
resource: "file:///manual/index.md"
---

# 📚 Pusat Rujukan Manual NOSS Linux Malaysia (Diátaxis Master Index)

Selamat datang ke **Sovereign Manual NOSS Linux Malaysia**. Halaman ini berfungsi sebagai **pusat rujukan sehenti (*centralised local reference portal*)** bagi pengendali manusia dan ejen AI. 

Kesemua modul pembelajaran disusun secara sistematik mengikut **Piawaian Kemahiran Pekerjaan Kebangsaan (NOSS Level 3)** dan dipadankan dengan **4 Kuadran Kerangka Diátaxis**.

---

## 🗺️ Matriks Integrasi Silibus NOSS & Kerangka Diátaxis

```mermaid
graph TD
    subgraph MANUAL_CU ["UNIT KOMPETENSI SILIBUS (manual/)"]
        CU01["<b>CU01:</b> Sistem Komputer & Desktop Linux"]
        CU02["<b>CU02:</b> Storan & Infrastruktur Pemayaan"]
        CU03["<b>CU03:</b> Pentadbiran & Servis Pelayan"]
        CU04["<b>CU04:</b> Automasi, Sandaran & Pemulihan"]
        CU05["<b>CU05:</b> Keselamatan Endpoint & Hardening"]
        CU06["<b>CU06:</b> Troubleshooting & Khidmat Sokongan"]
    end

    subgraph DIATAXIS_HUB ["INTEGRASI 4 KUADRAN DIÁTAXIS"]
        TUT["<b>1. Tutorials:</b><br><a href='../docs/tutorials/'>docs/tutorials/</a>"]
        HTG["<b>2. How-To Guides:</b><br><a href='../docs/how-to/'>docs/how-to/</a>"]
        REF["<b>3. Reference:</b><br><a href='../docs/reference/'>docs/reference/</a>"]
        EXP["<b>4. Explanation:</b><br><a href='../openwiki/'>openwiki/</a> & <a href='../docs/explanation/'>docs/explanation/</a>"]
    end

    CU01 --> DIATAXIS_HUB
    CU02 --> DIATAXIS_HUB
    CU03 --> DIATAXIS_HUB
    CU04 --> DIATAXIS_HUB
    CU05 --> DIATAXIS_HUB
    CU06 --> DIATAXIS_HUB
```

---

## 📑 Direktori Unit Kompetensi (NOSS Level 3)

| Kod Unit | Tajuk Kompetensi NOSS | Modul Amali & Aktiviti Kerja | Rujukan Diátaxis Terpaut |
| :--- | :--- | :--- | :--- |
| [**CU01**](cu01/index.md) | **Persediaan Sistem Komputer & Desktop Linux** | - [Pemasangan OS Desktop](cu01/cu01-wa04-pemasangan-os-desktop-linux.md)<br>- [Penyulitan LUKS2](cu01/penyulitan-cakera-luks2-pejabat.md)<br>- [Perkakasan & BIOS/UEFI](cu01/keperluan-perkakasan-dan-bios-uefi.md)<br>- [Pasca Pemasangan](cu01/pasca-pemasangan-dan-driver.md) | **Explanation:** [OpenWiki Topik 1](../openwiki/topic-01-linux-desktop-and-basics.md)<br>**Tutorial:** [Getting Started](../docs/tutorials/getting-started.md) |
| [**CU02**](cu02/index.md) | **Pengurusan Storan & Hipervisor Pemayaan** | - [Keperluan Pemayaan](cu02/cu02-wa01-keperluan-infrastruktur-pemayaan.md)<br>- [Pemasangan Hipervisor](cu02/cu02-wa02-pemasangan-hipervisor-jenis-2.md)<br>- [Penyebaran VM Tetamu](cu02/cu02-wa03-penyebaran-mesin-maya-tetamu.md)<br>- [Storan & LVM2](cu02/pengurusan-storan-partisi-dan-sistem-fail.md) | **Explanation:** [OpenWiki Topik 2](../openwiki/topic-02-storage-and-virtualisation.md) |
| [**CU03**](cu03/index.md) | **Pentadbiran & Perkhidmatan Pelayan Linux** | - [Persediaan Pelayan](cu03/cu03-wa01-persediaan-pemasangan-pelayan.md)<br>- [Pemasangan OS Pelayan](cu03/cu03-wa03-pemasangan-sistem-operasi-pelayan.md)<br>- [Konfigurasi Teras & SSH](cu03/cu03-wa04-konfigurasi-teras-pelayan.md)<br>- [Servis Web, DNS, Samba](cu03/cu03-wa05-pelaksanaan-peranan-dan-servis-pelayan.md) | **Explanation:** [OpenWiki Topik 3](../openwiki/topic-03-linux-server-administration.md) |
| [**CU04**](cu04/index.md) | **Automasi, Sandaran & Pemulihan Sistem** | - [Alatan Sandaran & Rsync](cu04/cu04-wa01-persediaan-alatan-sandaran-dan-pemulihan.md)<br>- [Sandaran Rangkaian](cu04/cu04-wa03-sandaran-berasaskan-rangkaian.md)<br>- [Pemulihan Bare-Metal](cu04/cu04-wa05-pemulihan-bare-metal-endpoint.md) | **Explanation:** [OpenWiki Topik 4](../openwiki/topic-04-automation-and-backup.md) |
| [**CU05**](cu05/index.md) | **Kawalan Keselamatan Endpoint & Hardening** | - [Audit Pengguna & Sudo](cu05/cu05-wa01-audit-akaun-pengguna-dan-kebenaran.md)<br>- [Antivirus & ClamAV](cu05/cu05-wa02-konfigurasi-pertahanan-antivirus-dan-antimalware.md)<br>- [Profil UFW / Firewalld](cu05/cu05-wa03-konfigurasi-profil-firewall-klien.md)<br>- [Tampalan Keselamatan](cu05/cu05-wa04-pengurusan-tampalan-dan-kemas-kini-keselamatan.md) | **Explanation:** [OpenWiki Topik 5](../openwiki/topic-05-linux-security.md) |
| [**CU06**](cu06/index.md) | **Sokongan Pengguna & Troubleshooting** | - [Khidmat Bantuan IT](cu06/cu06-wa01-keperluan-perkhidmatan-sokongan-pengguna.md)<br>- [Diagnostik Perkakasan](cu06/cu06-wa03-diagnostik-dan-troubleshooting-perkakasan.md)<br>- [Prestasi & Pengoptimuman](cu06/cu06-wa05-pengoptimuman-prestasi-sistem-dan-cakera.md)<br>- [Analisis Punca (RCA)](cu06/cu06-wa07-analisis-punca-anomali-dan-dokumentasi-rca.md) | **Explanation:** [OpenWiki Topik 6](../openwiki/topic-06-troubleshooting-and-logs.md) |

---

## 🌐 Navigasi Pantas 4 Kuadran Diátaxis

- 🎓 **[Tutorials (Pembelajaran Berpandu)](../docs/tutorials/index.md):** Sesuai untuk pemula memulakan langkah praktikal pertama.
- 🛠️ **[How-To Guides (Panduan Operasi)](../docs/how-to/execute-noss-content-transformation.md):** Resipi pantas bagi pentadbir sistem menyelesaikan isu harian.
- 📖 **[Reference (Spesifikasi & Standard)](../docs/reference/index.md):** Spesifikasi teknikal, senarai arahan, dan kemahiran AI.
- 💡 **[Explanation (Kefahaman & Falsafah)](../openwiki/index.md):** Analisis teori, perbandingan teknologi, dan falsafah sumber terbuka.

---
*Linux for NOSS Malaysia (Sovereign Manual) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-17*  
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
