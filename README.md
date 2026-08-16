# Sovereign Markdown Palace: Linux NOSS Malaysia (DSOM)

Projek ini merupakan sebuah pangkalan pengetahuan Sistem Operasi Linux yang tidak rasmi, disusun berdasarkan Standard Kemahiran Pekerjaan Kebangsaan (NOSS) Malaysia. Ia dibina di atas kerangka seni bina *exocortex* (memori luaran) yang mematuhi protokol **Deep State of Mind (DSOM) v0.1**.

Susun atur spatial ini direka khusus untuk kecekapan Ejen AI (seperti Claude, Cursor, Windsurf, Jules) mengekstrak dan membaca silibus teknikal tanpa membebankan konteks memori.

> **PENAFIAN PENTING**: Repositori ini adalah TIDAK RASMI dan dicipta untuk tujuan pengetahuan / pembelajaran sahaja. Ia tidak mewakili Jabatan Pembangunan Kemahiran (JPK) atau Kementerian Sumber Manusia Malaysia (MOHR). Sila rujuk `LEGAL-NOTICE.md`.
## Rujukan Teras (References)

Pembangunan senibina dan standard ejen ini merujuk secara langsung kepada sumber-sumber utama berikut yang membina ekosistem *Agent Skills*:

*   **OpenSkills (Universal Loader)**: [https://github.com/numman-ali/openskills](https://github.com/numman-ali/openskills)
*   **Skills Directory (Marketplace)**: [https://www.skillsdirectory.com/](https://www.skillsdirectory.com/)
*   **AgentSkills Open Standard**: [https://agentskills.io/home](https://agentskills.io/home)
*   **Deep State of Mind**: [https://github.com/linuxmalaysia/deep-state-of-mind-for-my-ai](https://github.com/linuxmalaysia/deep-state-of-mind-for-my-ai)
*   **MemPalace Framework**: [https://github.com/MemPalace/mempalace](https://github.com/MemPalace/mempalace)

## Maklumat Projek (Project Info)

- [`START-HERE.md`](START-HERE.md): **Titik Masuk Utama (Entry Point)**. Sila baca ini dahulu.
- [`llms.txt`](llms.txt): Peta tapak (sitemap) khusus untuk perangkak AI (AI crawler).
- [`HISTORY.md`](HISTORY.md): Menjejaki evolusi dan falsafah awal pembinaan projek ini.
- [`CHANGELOG.md`](CHANGELOG.md): Nota keluaran (Release Notes) rasmi bagi semua versi.
- [`LEGAL-NOTICE.md`](LEGAL-NOTICE.md): **[PENTING]** Penafian NOSS dan ketidakrasmian kandungan.
- [`NOTICE.md`](NOTICE.md): Hak cipta pengarang asal, dan penafian ke atas rujukan pihak ketiga (seperti DSOM, OpenSkills & AgentSkills).

## Struktur Dokumentasi (Manual)

Sila rujuk kepada folder `docs/` untuk tatacara gred pengeluaran (*production-grade*):

1.  [`HOWTO-create-skill.md`](docs/HOWTO-create-skill.md): Manifesto seni bina dan falsafah teras Loci.
2.  [`PROMPTS.md`](docs/PROMPTS.md): Protokol dan amalan keselamatan (OpSec).
3.  [`templates/SKILL.md`](docs/templates/SKILL.md): Templat contoh profil kerjaya eksekutif ejen.
4.  [`BEST-PRACTICES.md`](docs/BEST-PRACTICES.md): Metodologi penggubalan kemahiran ejen yang spesifik.
5.  [`OPTIMIZING-DESCRIPTIONS.md`](docs/OPTIMIZING-DESCRIPTIONS.md): Strategi mencetuskan respons dengan lebih tepat (*triggering*).
6.  [`EVALUATING-SKILLS.md`](docs/EVALUATING-SKILLS.md): Prosedur penilaian gred keluaran sistem.
7.  [`USING-SCRIPTS.md`](docs/USING-SCRIPTS.md): Antara muka skrip pelaksanaan di bahagian ejen.
8.  [`ADDING-SKILLS-SUPPORT.md`](docs/ADDING-SKILLS-SUPPORT.md): Panduan menyokong kemahiran dalam ejen lain.
9.  [`WHAT-ARE-SKILLS.md`](docs/WHAT-ARE-SKILLS.md): Gambaran keseluruhan logik dan peranan *Claude Skills*.
10. [`CREATING-YOUR-FIRST-SKILL.md`](docs/CREATING-YOUR-FIRST-SKILL.md): Tutorial mula bagi membina fail arahan baru.
11. [`WRITING-EFFECTIVE-SKILLS.md`](docs/WRITING-EFFECTIVE-SKILLS.md): Petua mencipta *skills* yang benar-benar berkesan.
12. [`SKILL-FILE-STRUCTURE.md`](docs/SKILL-FILE-STRUCTURE.md): Spesifikasi anatomi fail dan sistem folder.
13. [`USING-REFERENCE-FILES.md`](docs/USING-REFERENCE-FILES.md): Teknik pendedahan secara berperingkat (*Progressive Disclosure*).
14. [`SKILL-FORMAT.md`](docs/SKILL-FORMAT.md): Spesifikasi kod YAML *Frontmatter*.
15. [`OPENSKILLS.md`](docs/OPENSKILLS.md): Rujukan pengaktifan alat CLI `npx openskills`.
16. [`GIT-RELEASE-WORKFLOW.md`](docs/GIT-RELEASE-WORKFLOW.md): Tatacara Git untuk pengepakan keluaran (release packaging) oleh Ejen AI.

## Integrasi Universal

Kerangka ini disokong sepenuhnya oleh fail [`AGENTS.md`](AGENTS.md) dan boleh disegerakkan menerusi alat `openskills` secara universal:

```bash
npx openskills sync
```
