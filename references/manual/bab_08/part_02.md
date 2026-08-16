---
okf_version: 0.1
name: Bab 8 - Bahagian 2
topics: [linux, manual, references, chapter-8]
tags: [noss, dbp]
---
# Bab 8 - Bahagian 2

si. Pakej individu juga boleh dipilih
daripada pakej kumpulan yang telah diinstalasikan dengan menekan butang Details dan
menanda di mana-mana pada pakej tambahan yang belum lagi diinstalasi.

Gambar Rajah 153 : Skrin pemilihan pakej untuk diinstalasikan
Selepas memilih pakej kumpulan dan pakej individual untuk instalasi , klik pada butang
Update pada tetingkap utama.  Aplikasi ini akan kemudiannya mengira jumlah ruang
cakera yang diperlukan untuk instalasi pakej seperti mana apa saja pakej kebergantungan
dan pameran tetingkap ringkasan. Jika terdapat pakej kebergantungan , ia akan ditambah
secara automatik kepada senarai pakej untuk instalasi.

Klik pada butang Show Details  untuk melihat senarai pakej yang akan diinstalasikan
secara lengkap.
Gambar Rajah 154 : Paparan kekotak dialog penyediaan pemasangan pakej
Klik Continue untuk mulakan proses instalasi. Apabila ia selesai , mesej Update
Complete akan muncul.

Gambar Rajah 155 : Paparan kekotak dialog bagi memberitahu progress meningkat taraf sistem
17.3.3 Membuang Pakej
Untuk membuang kesemua pakej yang diinstalasikan dalam kumpulan pakej , hilangkan
tanda pada kotak semakan di sebelahnya. Untuk mengalihkan pakej individual , klik
butang Details di sebelah pakej kumpulan dan hilangkan tanda pakej individual.
Apabila telah selesai memilih pakej untuk dialihkan , klik butang Update di tetingkap
utama. Aplikasi akan mengira jumlah ruang cakera yang akan dibebaskan seperti mana
pakej perisian kebergantungan. Jika pakej lain bergantung kepada pakej yang telah dipilih
, ia akan ditambah secara automatik kepada senarai pakej yang akan dialihkan. Klik
butang Show Details untuk melihat senarai pakej yang akan dialihkan.
Klik Continue untuk mulakan proses membuang pakej. Apabila ia telah selesai , mesej
Update Complete akan muncul.

17.4 Mengompil Kod Sumber
Kadangkala adalah perlu untuk mengompil perisian daripada kod sumber agar dapat
diinstalasi  ke dalam sistem. Mengompil kod sumber mungkin perlu dalam keadaan
seperti berikut:
• Tiada pakej binari untuk perisian yang hendak diinstalasi.
• Pakej binari bergantung pada sokongan perpustakaan yang baru atau pun lama
daripada apa yang telah diinstalasikan dalam sistem. Selalunya , anda hanya perlu
mengompil sekali lagi kod sumber perisian terhadap perpustakaan yang telah
diinstalasikan agar ia dapat menguruskan masalah.
• Untuk membolehkan pilihan compile-time yang tidak digunakan dalam pakej binari
yang telah ada. Pilihan ini mungkin mengoptimumkan pakej untuk komputer atau pun
menambah fungsi-fungsinya.
• Mahu memodifikasikan kod sumber. Jika terdapat pepijat (bugs) daripada pakej
binari yang terakhir atau jika ciri-ciri ingin ditambah atau melakukan modifikasi
perisian, anda perlu mengompil perisian daripada kod sumber yang sesuai dengan
keperluan yang tertentu.
Ia adalah mudah untuk mengompil daripada kod sumber : hanya perlu muat turun kod
sumber (yang mana selalunya datang sebagai tarball) , melakukan modifikasi , kompilkan
dan instalasikan secara langsung daripada kod yang telah dikompilkan. Sumber juga
boleh dikompilkan dalam format RPM , iaitu fail RPM yang mengandungi kod sumber.

17.4.1 Mengompil daripada Pakej ( fail sumber RPM)
Fail sumber RPM boleh dikenali oleh sambungan .src.rpm dalam nama fail. Sebagai
contohnya , openssh ± 3.4pl ± 2.src.rpm adalah sumber RPM manakala openssh ± 3.4pl ±
2.i386.rpm pula adalah binari yang telah dikompilkan pada pakej yang sama.
Untuk mengompil suatu sumber RPM , perlu guna pilihan ± rebuild dengan arahan rpm
pada paparan terminal (terminal skrin) atau “shell prompt”. Untuk mengompil suatu
sumber RPM , taipkan :
# rpm – rebild openssh – 3.4 pl – 2.src.rpm
Jika tiada masalah yang timbul , siri arahan kompilasi akan dilihat pada skrin. Ia mungkin
mengambil sedikit masa untuk dilaksanakan (walau pun memakan masa berjam-jam) ,
bergantung kepada pakej dan kelajuan PC.
Membina pakej memerlukan sokongan perpustakaan yang penting telah diinstalasikan ,
bukan sahaja perpustakaan yang diperlukan oleh pakej binari terakhir , malah sepadan
dengan pembangunan perpustakaan. Pembangunan perpustakaan ini tidak selalunya
termasuk dalam sumber informasi kebergantungan RPM yang diperlukan, maka ia
bukanlah sesuatu yang menghairankan untuk melihat kompilasi operasi menjadi gagal
kerana beberapa perpustakaan yang hilang. Sepatutnya mesej ralat diperiksa apabila ini
berlaku dan semak senarai keperluan yang selalunya boleh ditemui pada halaman
perisian. Jika tahu yang mana satu perkembangan perpustakaan diperlukan (yang mana
selalunya mempunyai sambungan .devel.rpm) , pakej binari boleh diinstalasi dan perisian
boleh dikompil semula.

---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
