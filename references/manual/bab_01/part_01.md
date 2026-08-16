---
okf_version: 0.1
name: Bab 1 - Bahagian 1
topics: [linux, manual, references, chapter-1]
tags: [noss, dbp]
---
# Bab 1 - Bahagian 1

Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
PANDUAN PENGAJAR
Infrastruktur Sistem & Linux
Red Hat 9
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
PANDUAN PENGAJAR
Seksyen B
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
PANDUAN PENGAJAR
Pelajaran 12 : Pengenalan Kepada Linux
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Mukadimah:
Dalam pelajaran ini anda akan diperkenalkan kepada sistem operasi Linux, tenaga kerja
di sebalik tabir Linux. Di sini juga anda akan diperlihatkan beberapa contoh pecahan
Linux yang popular. Isu-isu yang berkaitan Linux juga ada diutarakan di sini seperti isu
Hak cipta dan sebagainya. Kedudukan Linux dalam bidang pendidikan juga ditekan di
sini. Selain itu anda akan diberikan beberapa jadual yang mengandungi URL yang
penting untuk anda memahami Linux. Anda juga akan dipertontonkan dengan jadual
perbandingan aplikasi Linux dan Microsoft Windows.
Objektif:
1. Memahami sistem operasi Linux dan mengenali beberapa orang yang menjadi
tunjang di sebalik kejayaannya
2. Mengenali pecahan sebahagian daripada pecahan Linux yang boleh diperolehi dan
digunakan
3. Mengetahui hak cipta Linux, GPL dan segala macam permasalahan yang mungkin
timbul berkenaan undang-undang terutamanya di Malaysia
4. Mengetahui sebahagian persoalan lazim yang dikaitkan dengan Linux dan sistem
pengkomputeran
5. Mengetahui kedudukan Linux dalam bidang pendidikan
6. Memperjelaskan sifat-sifat asas pecahan Linux
7. Membandingkan perisian aplikasi Linux dan Microsoft Windows, URL informasi
Linux dan URL pecahan dan aplikasi Linux
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
12 SISTEM OPERASI LINUX
Bahagian ini membimbing anda untuk membiasakan diri dengan Red Hat Linux versi 9
sebagai satu sistem pengendalian yang asas dengan menggunakan persekitaran bergrafik
GNOME. Tugas seperti meninjau apa yang terdapat dalam cakera anda, memulakan
program, memformatkan cakera dan bekerja dengan lipatan dan fail dibincangkan dalam
bahagian berikutnya.
12.1 Sistem Operasi Linux
Jika direnungkan asal-usul Linux saya percaya anda akan tersenyum kecil sambil
menyatakan kekaguman anda. Ini adalah kerana Linux sebenarnya hanya merupakan hobi
kepada seorang pelajar aliran komputer sains di Universiti Helsinki dan kemudian telah
dibangunkan oleh ratusan ribu jurukod (programmer) di seluruh dunia hingga menjadi
salah satu sistem operasi terunggul di dunia ketika ini.
Pelajar yang dimaksudkan ini ialah Linus Benedict Torvalds. Ketika Linus mula
memperkenalkan Linux pada Ogos 1992, hanya Intel sahaja yang menguasai pasaran
pemproses mikro dengan cip 386 mereka. Microsoft pula hanyalah sebuah syarikat kecil
yang baru memperkenalkan DOS.
Pada peringkat awal, Linux hanyalah merupakan satu terbitan dari sistem operasi yang
dibina oleh Prof. Andrew Tannenbaum yang dikenali sebagai Minix. Akhirnya, Linus
berjaya membina Linux sebagai sebuah sistem operasi yang tersendiri dan pecahan Red
Hat dianggap sebagai telah menemui rentak yang betul setelah pengeluaran versi Red Hat
5.2.
Seperti sistem operasi Unix lain, Linux dibina dengan bahasa pengaturcaraan C dan
mematuhi kaedah serta peraturan pengaturcaraan Posix. Satu perkara penting yang perlu
dijelaskan di sini ialah Linux dibangunkan oleh ratusan ribu jurukod di seluruh dunia oleh
itu hak cipta Linux terletak di tangan Linus, namun program lain terletak kepada pengatur
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
cara yang membuatnya. Oleh itu penghormatan pengeluaran isirung (kernel) secara
rasminya akan hanya dilakukan oleh Linus sendiri.
Linux boleh di peroleh secara percuma dari Internet. Kebanyakan syarikat yang
menerbitkan pecahan Linux seperti MandrakeSoft Inc. ada menjual perisian Linux pada
harga yang amat rendah berserta dengan sokongan pembelian yang hebat. Terpulang
kepada anda sama ada untuk menurun muatkan dari Internet atau membeli dari pengeluar.
12.1.1 Linus Torvalds
Setiap satu ada permulaannya, begitulah juga dengan Linux yang dimulakan oleh Linus
Benedict Torvalds sewaktu beliau masih lagi menjadi seorang pelajar jurusan komputer
sains di sebuah universiti di Helsinki, Finland. Idea untuk memulakan projek hobinya ini
telah berputik daripada kelas sistem operasinya. Ketika itu pelajar-pelajar yang
mengambil mata pelajaran tersebut menggunakan buku teks yang ditulis oleh Prof.
Andrew Tanenbaum.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Gambar Rajah 130 : Linus Benedict Torvalds
Prof Tanenbaum telah memperkenalkan sistem operasi Minix melalui bukunya, oleh itu
tidak hairanlah apabila saudara Linus telah bermula dengan Minix untuk membangunkan
Linux pada awal tahun 1991. Hasrat awalnya hanyalah ingin mencipta satu sistem operasi
yang lebih teratur dan berkesan dari Minix. Namun enam bulan setelah itu, Linus telah
berjaya menjadikan Linux sebagai satu sistem operasi yang stabil dan tersendiri tanpa
perlu bergantung kepada Minix lagi.
Sebenarnya pada peringkat awal, Linux hanyalah mengekodkan program pengaturan
ingatan yang merupakan sebahagian daripada isirung (kernel) Linux. Setelah itu beliau
mula menggabungkan dengan pelbagai kod yang boleh di peroleh secara bebas di Internet
dengan isirung (kernel) Linux.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Pada waktu ini, Linus bekerja di bawah naungan syarikat Transmeta Corporation di
Silicon Valley. Terdapat khabar angin yang mengatakan beliau akan bekerja untuk Red
Hat, tetapi beliau tetap kekal dengan pendirian untuk tidak menunjukkan minat dan
kecenderungan ke atas mana-mana pecahan Linux. Namun Linux tidak menafikan beliau
menggunakan Red Hat Linux di rumahnya dan pernah dilihat memakai kemeja-t Red Hat
di persidangan Linux Sedunia.
Beliau pernah menegaskan yang beliau bukanlah seorang ketua pengarah syarikat, tetapi
beliau hanyalah seorang ketua teknikal yang menumpukan ke arah landasan yang fokus
dan jelas di mana setiap keputusan yang beliau ambil akan dipastikan supaya sentiasa
dihormati dan diterima pakai oleh semua orang.
Apabila diajukan apa yang akan Linux tempuhi dalam tempoh 10 tahun akan datang
beliau menegaskan 10 tahun lepas beliau tidak tahu hala tuju Linux apatah lagi untuk 10
tahun akan datang beliau masih tiada idea ke mana arah Linux. Oleh itu anda mungkin
salah seorang yang mencorakkan masa depan Linux.
12.1.2 Alan Cox
Janggut yang panjang dan tebal merupakan identiti Alan Cox yang harus dikenali oleh
pengguna Linux. Sebagai seorang yang bertanggungjawab dalam pembangunan isirung
(kernel) Linux terutamanya untuk rangkaian dan sistem pemprosesan selari beliau
sentiasa menjadi rujukan dan pelakon utama dalam pengeluaran isirung (kernel) rasmi
selain Linus Torvalds. Jika anda lebih peka, anda akan mendapati kebanyakan ikon-ikon
berkenaan isirung (kernel) akan dilambangkan sebagai seorang yang berjanggut dan
bertopi sempena menghargai hasil usaha Alan Cox.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
Gambar Rajah 131 : Alan Cox
Beliau telah mula bekerja dengan isirung (kernel) Linux sejak pengeluaran isirung
(kernel) 1.0 (isirung (kernel) terkini ialah 2.6.x), oleh itu hampir setiap hari beliau
melakukan perubahan terhadap isirung (kernel). Untuk memudahkan pembangun isirung
(kernel) Linux yang lain, beliau telah menyediakan diari hariannya yang boleh dicapai di
http://www.linux.org.uk. Kini Cox banyak menulis diarinya dalam bahasa Welsh, oleh itu
lebih baik jika anda membaca diari isterinya.
Jika anda melihat diari beliau pasti anda akan terkejut dengan cara kehidupannya, ia
menunjukkan seolah-olah beliau hanya makan Linux, minum Linux dan tidur Linux. Tapi
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
harus diingat itu semua tidak menjadi penghalang untuknya mengekalkan
perkahwinannya dengan isterinya, Telsa dan hidup bahagia di samping keluarga.
Sebagai keluarga penggodam yang berjaya, Telsa juga banyak menyumbang kepada
pembangunan Linux terutamanya dalam pembangunan aplikasi X Windows GNOME.
12.1.3 Bob Young
Nama Bob Young sentiasa sinonim dengan Red Hat Software Inc.. Sebagai pengerusinya
Bob Young telah berjaya membawa Red Hat Software Inc. untuk mencapai titik pulangan
modal dalam masa 5 tahun pertama operasi syarikat. Dengan hanya mempunyai 23 orang
pekerja pada tahun awal penubuhannya, mereka telah berjaya menyaingi produk yang
dikeluarkan oleh Microsft Inc sehingga memenangi pelbagai pengiktirafan dunia. Ini
merupakan satu kejayaan besar apatah lagi untuk syarikat yang perisian yang
memberikan perisian secara bebas. Oleh itu tanggapan tiada keuntungan boleh diperolehi
dari Linux harus dikikis jauh-jauh.
Kejayaan Bob Young memujuk Marc Ewing untuk membangunkan sebuah perisian
pengurusan yang dikenali sebagai RPM dengan menggunakan sumber kewangan Caldera,
telah menjadi titik tolak kepada kepopularan Red Hat. Selain itu falsafah dan
kesungguhan Bob Young dalam mengendalikan Red Hat amat dihormati dan disegani.
12.1.4 Richard Stallman
Beliau merupakan seorang Profesor berbangsa Yahudi di MIT yang kemudiannya
menjadi pengasas Free Software Foundation Inc, beliau tidaklah terlibat dengan Linux
secara langsung, namun usaha yang dimulakannya telah berjaya membuka mata orang
ramai akan keberkesanan perisian bebas ini. Melalui organisasi tersebut, Stallman telah
menghasilkan pelbagai projek perisian, oleh itu beliau mendapati beliau memerlukan
lesen hak cipta untuk melindungi perisian mereka tanpa melanggar prinsip-prinsip
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
mereka, hasilnya lesen GNU GPL telah diterbitkan. Kita akan membincangkan lesen
GNU GPL ini dengan lebih lanjut selepas ini.
Sebenarnya sebahagian ideologi yang cuba dibawa oleh Free Software Foundation ini
telah lama dianjurkan oleh Islam, iaitu ilmu haruslah dikongsi dan disebarkan cuma yang
menyedihkan ialah tiadanya sokongan yang kukuh terhadap pendekatan sebegini.
Sesungguhnya ilmu yang kita miliki itu hanyalah umpama setitik air di lautan yang luas,
saya tidaklah bermaksud ingin mendabik dada tetapi sekadar mengingati sesama insan
termasuk diri sendiri. Sebagai manusia yang tidak maksum kita selalu melewati batas-
batas yang telah digariskan.
12.1.5 Robert Scheifler dan James Gettys
Mereka berdua merupakan pengasas awal kepada sistem grafik Linux yang dikenali
sebagai X Windows. Bahkan nama James Gettys telah disemadikan untuk terminal
konsol Linux.
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
12.2Pecahan Linux
Salah satu keunikan Linux ialah tersedianya banyak pilihan untuk pengguna memilih
pelbagai pecahan Linux. Pecahan yang dimaksudkan di sini ialah pecahan Linux yang
mempunyai pelbagai ideologi dan falsafah yang tersendiri. Namun semua pecahan ini
sentiasa menggunakan isirung (kernel) dan beberapa perisian asas yang sama. Inilah
kunci sebenar yang menyebabkan kejayaan Linux.
Adalah mustahil untuk saya menyenaraikan semua pecahan Linux di sini, oleh itu saya
hanya akan membincangkan pecahan yang terbaik, popular dan dikenali ramai sahaja.
12.2.1 Debian
Debian atau nama timangannya "DEB" yang dijalankan oleh beberapa sukarelawan
merupakan antara versi Linux yang mengandungi paling banyak pakej perisian yang
sedia-atur untuk dilarikan. Proses pemuatannya amat mudah dan menarik.
Logo
Tapak web  http://www.debian.org
Versi terkini  Debian v3.0r2 (Isirung 2.4.20)
Seni bina  Intel/IBM
Pilihan penulis  *****
Ministry of Education : Computerisation (IT Lab)
Infrastruktur Sistem & Linux
Strictly Confidential
12.2.2 Red Hat
Satu ketika dahulu di antara semua pecahan Linu
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
