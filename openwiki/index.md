---
spec_version: '0.2'
okf_version: '0.2'
type: explanation
title: OpenWiki Master Graph
description: Peta grafik keseluruhan (Master Graph) silibus Linux NOSS di dalam OpenWiki.
status: stable
stale_after: '2027-12-31'
generated:
  by: generate_openwiki_graph.py / OKF v0.2
  at: '2026-10-04T06:16:13Z'
resource: file:///openwiki/index.md
topics:
- openwiki
- noss-linux
- graph
tags:
- index
- mermaid
- map
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

# 🧠 OpenWiki Master Graph (Linux NOSS Syllabus)

Dokumen ini memaparkan gambaran visual dan hierarki bagi kesemua topik NOSS (Level 3) Linux yang sedia ada di dalam pangkalan data `openwiki/`. 
Graf ini dijana secara automatik menggunakan teknologi *Mermaid.js*.

## Peta Topik dan Pemetaan CU

```mermaid
graph TD
    Root(("Silibus Pusat\nLinux NOSS (L3)"))

    T1["Topik 1: Pengenalan & Asas Ekosistem Linux (CU01) — Dikemaskini 2026 <br> <i>(CU01)</i>"]
    T2["Topik 2: Pengurusan Storan, Partisi & Pengmayaan (CU02) — Dikemaskini 2026 <br> <i>(CU02)</i>"]
    T3["Topik 3: Pentadbiran Pelayan Linux (CU03) <br> <i>(CU03)</i>"]
    T4["Topik 4: Automasi Skrip, Sandaran Data & Pemulihan Sistem (CU04) <br> <i>(CU04)</i>"]
    T5["Topik 5: Keselamatan Linux & Kawalan Akses (CU05) <br> <i>(CU05)</i>"]
    T6["Topik 6: Penyelesaian Masalah, Pelekapan Storan, Penapis Teks & Analisis Log <br> <i>(CU06)</i>"]
    Root --> T1
    Root --> T2
    Root --> T3
    Root --> T4
    Root --> T5
    Root --> T6
```

## Perincian Modul

| Topik | Kod CU | Penerangan |
|---|---|---|
| [Topik 1: Pengenalan & Asas Ekosistem Linux (CU01) — Dikemaskini 2026](topic-01-linux-desktop-and-basics.md) | CU01 | Silibus komprehensif CU01 dikemaskini dengan Persekitaran Meja GNOME |
| [Topik 2: Pengurusan Storan, Partisi & Pengmayaan (CU02) — Dikemaskini 2026](topic-02-storage-and-virtualisation.md) | CU02 | Silibus pengurusan storan fizikal dan logikal (GPT, LVM2, EXT4/XFS/Btrfs, LUKS2) serta asas pengmayaan KVM/QEMU (CU02). |
| [Topik 3: Pentadbiran Pelayan Linux (CU03)](topic-03-linux-server-administration.md) | CU03 | Silibus pentadbiran pelayan Linux, pengurusan perkhidmatan systemd, konfigurasi teras sistem, dan penyelarasan masa (CU03). |
| [Topik 4: Automasi Skrip, Sandaran Data & Pemulihan Sistem (CU04)](topic-04-automation-and-backup.md) | CU04 | Silibus automasi skrip Bash, pengarkiban dan pemampatan tar/zstd, penyegerakan rsync, dan penjadualan cron (CU04). |
| [Topik 5: Keselamatan Linux & Kawalan Akses (CU05)](topic-05-linux-security.md) | CU05 | Silibus keselamatan OS Linux komprehensif merangkumi Pentadbiran Pengguna & Kumpulan, Kebenaran Fail & POSIX ACL, Firewall, dan Kawalan Lockdowns (CU05). |
| [Topik 6: Penyelesaian Masalah, Pelekapan Storan, Penapis Teks & Analisis Log](topic-06-troubleshooting-and-logs.md) | CU06 | Silibus penyelesaian masalah sistem, pelekapan storan mount/fstab, penapis teks CLI, dan analisis punca anomali (CU06). |

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-10-04*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
