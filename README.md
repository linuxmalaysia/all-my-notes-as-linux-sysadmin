# Sovereign Markdown Palace AI Agents

Projek ini merupakan sebuah kerangka seni bina *exocortex* (memori luaran) berasaskan format Reka Letak Memori Ruang (*Spatial Memory Layout* / Loci) bagi pengurusan modal kognitif dan kerjaya. Ia dikhususkan untuk penggunaan lancar bersama mana-mana ejen AI seperti Claude Code, Cursor, Windsurf, dan Aider.

## Rujukan Teras (References)

Pembangunan senibina dan standard ejen ini merujuk secara langsung kepada sumber-sumber utama berikut yang membina ekosistem *Agent Skills*:

*   **OpenSkills (Universal Loader)**: [https://github.com/numman-ali/openskills](https://github.com/numman-ali/openskills)
*   **Skills Directory (Marketplace)**: [https://www.skillsdirectory.com/](https://www.skillsdirectory.com/)
*   **AgentSkills Open Standard**: [https://agentskills.io/home](https://agentskills.io/home)

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

## Integrasi Universal

Kerangka ini disokong sepenuhnya oleh fail [`AGENTS.md`](AGENTS.md) dan boleh disegerakkan menerusi alat `openskills` secara universal:

```bash
npx openskills sync
```
