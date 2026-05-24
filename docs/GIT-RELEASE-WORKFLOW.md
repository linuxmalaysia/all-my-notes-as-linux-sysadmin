# Aliran Kerja Git & Pengurusan Keluaran (Git Release Workflow)

Dokumen ini merekodkan cara ejen AI mengurus kawalan versi (version control) dan proses pengepakan perisian (release packaging) secara automatik dalam projek Sovereign Markdown Palace. Panduan ini amat penting agar ejen AI masa depan (atau skrip automasi) dapat meniru dan melaksana kembali aliran kerja ini dengan tepat.

## 1. Pembuatan Komit Git Berstruktur (Semantic Commits)

Sepanjang projek ini dibina, ejen AI menggunakan spesifikasi **Mesej Komit Semantik (Semantic Commit Messages)** (berasaskan Konvensyen Angular/DSOM) bagi mewujudkan sejarah log yang berstruktur, mudah dibaca, dan berorientasikan mesin.

Ejen diwajibkan menggunakan struktur berikut bagi setiap komit:
```
<jenis>[skop pilihan]: <penerangan ringkas>
```

**Contoh-contoh Komit:**
- `docs(skill-example): add boilerplate example skill template`
- `feat(mempalace-loci): initialize spatial memory directory structure`
- `fix(opsec-pii): implement opsec boundary filter to block untrusted docs and pii`
- `refactor(skill-yaml): improve executive profile template with best practices`

**Kenapa Penting:** Mesej komit semantik membolehkan ejen menganalisis log perubahan (`git log`) dan menjana nota keluaran (*release notes*) secara automatik pada masa hadapan.

## 2. Pengurusan Keluaran Secara Setempat (Local Release Packaging)

Bagi memastikan repositori ini dapat dijadikan "templat induk" (master template) yang bersih untuk disalin berulang kali, kita menggunakan kaedah `git archive` untuk membina fail zip berbanding arahan utiliti zip am.

### Arahan Pengepakan Keluaran (*Release Packaging Command*)

Berikut adalah jujukan arahan Git PowerShell/Bash yang ejen laksanakan untuk membina keluaran sedia untuk diedar:

```bash
# 1. Cipta penanda keluaran (tag) pada 'commit' terkini
git tag v1.0.1

# 2. Cipta direktori untuk menyimpan fail zip (jika belum ada)
mkdir -p releases

# 3. Jana fail zip keluaran menggunakan 'git archive'
git archive --format=zip --prefix=sovereign-markdown-palace-v1.0.1/ --output=releases/sovereign-markdown-palace-v1.0.1.zip v1.0.1
```

### Kelebihan `git archive`

Mana-mana ejen AI yang bekerja di dalam ruang lingkup projek Loci **MESTILAH** menggunakan `git archive` bagi tujuan pempakejan (*packaging*) atas sebab-sebab berikut:

1. **Pengecualian .git Automatik**: Tidak akan menyertakan folder `.git/` di dalam fail `.zip`, justeru menjadikan templat bersih dan sedia diguna pakai oleh klien tanpa sejarah Git terdahulu.
2. **Kepatuhan .gitignore**: Secara asli menghormati aturan di dalam fail `.gitignore`—menghalang sebarang kebarangkalian bocornya fail PII tersulit (cth: yang ada di dalam `assets/locks/`) dan rahsia OpSec.
3. **Penyusunan Awalan (Prefix)**: Argument `--prefix=.../` menjamin apabila templat ini di-*unzip*, semua fail akan terhimpun kemas di dalam sebuah root folder tunggal.

## 3. Garis Panduan Ejen AI

Jika anda (Ejen AI) diminta untuk **mengemas kini** atau **mencipta keluaran baharu**, sila ikuti SOP ini:
1. Selesaikan semua penambahan fail dan suntingan.
2. Daftar semua perubahan menggunakan perintah `git add`.
3. Laksanakan komit menggunakan amalan *Semantic Commit*.
4. Semak versi terkini, dan tambahkan nilai tag `git tag vX.Y.Z` dengan wajar (SemVer).
5. Laksanakan `git archive` ke dalam folder `releases/`.
