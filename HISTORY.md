# Project History (Sovereign Markdown Palace)

## Pengenalan

Projek **Sovereign Markdown Palace** bermula sebagai satu anjakan paradigma (paradigm shift) dalam cara kita menguruskan pengetahuan peribadi, terutamanya modal kerjaya (career capital), daripada dokumen konvensional kepada struktur yang dapat diproses dan dimanfaatkan secara terus oleh kecerdasan buatan (AI).

## Evolusi Konsep

### 1. Cabaran Awal (Monolith Problem)
Pada asalnya, pengurusan maklumat peribadi selalunya disatukan dalam satu atau dua buah dokumen besar yang statik. Apabila Ejen AI (LLM) cuba memproses fail sedemikian, ia menyebabkan dua isu utama:
- **LLM Amnesia**: Kegagalan mengekalkan memori antara perbualan.
- **Kekangan Konteks**: Mengisi terlalu banyak maklumat yang tidak relevan yang memakan kuota token.

### 2. Metodologi Loci (Spatial Memory)
Bagi mengatasi masalah di atas, kerangka ini diinspirasikan daripada teknik pengekalan memori kuno iaitu "Method of Loci" (Istana Minda).
Kami mengubah maklumat tersebut kepada direktori berstruktur:
- **Wings, Halls, Rooms** - Mewakili pengkategorian besar.
- **Drawers, Closets** - Menyimpan komponen maklumat terperinci yang hanya akan dibuka jika perlu.

### 3. Progressive Disclosure & Agent Skills
Kunci utama keberkesanan Istana Markdown ini ialah penggunaan standard **Agent Skills**. Daripada menyuruh Ejen membaca semuanya sekaligus, kami menyusun arahan dalam format `SKILL.md`. Fail-fail ini mematuhi prinsip *Progressive Disclosure*, di mana AI hanya memuat turun maklumat dan arahan (rujukan tambahan di dalam `/references`) yang diperlukan untuk menyelesaikan tugasan semasa.

### 4. Pematuhan OpSec (Security)
Sebaik sahaja struktur dipersetujui, kami mula melaksanakan langkah-langkah keselamatan ketat. Semua Maklumat Pengenalan Peribadi (PII) diasingkan daripada konteks AI dan dikunci ke dalam direktori `/assets/locks/` berpandukan dasar `PROMPTS.md` dan saringan `.gitignore`.

### 5. Penubuhan Templat Pengedaran (Distribution)
Kerangka ini akhirnya disatukan untuk menyokong format universal melalui *OpenSkills*, lantas menjadi satu sistem (exocortex) yang boleh disalin dan disebarkan dengan cara `git release` yang bersih (seperti tag `v1.0.0` dan ke atas).

### 6. Era DSOM & Fokus Kepada Linux NOSS (v2.0.0)
Selepas kejayaan fasa pengedaran, fokus repositori ini telah ditransformasikan secara menyeluruh daripada sebuah "Templat CV" kepada sebuah **Pangkalan Pengetahuan Pendidikan (Educational Knowledge Base)**. Berpandukan standard **Deep State of Mind (DSOM) v0.1**, kami menyusun semula kandungan repositori ini untuk memuatkan silibus teknikal Sistem Operasi Linux berasaskan **National Occupational Skills Standard (NOSS)** Malaysia. Transformasi ini membuktikan kemampuan kerangka Loci dan DSOM untuk memetakan kepakaran industri berat ke dalam minda Ejen AI tanpa membebankan token konteks.

Hari ini, ia berdiri sebagai platform gred pengeluaran (*production-grade*) yang mengintegrasikan kecerdasan AI dengan spesifikasi kemahiran teknikal negara (secara tidak rasmi).
