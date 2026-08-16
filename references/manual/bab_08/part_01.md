---
okf_version: 0.1
name: Bab 8 - Bahagian 1
topics: [linux, manual, references, chapter-8]
tags: [noss, dbp]
---
# Bab 8 - Bahagian 1

Mukadimah:
Dalam pelajaran ini, anda akan diperkenalkan kepada dua utiliti berguna dalam
menaiktarafkan pakej dalam Linux. Kedua-duanya amat berguna dalam memastikan anda
sentiasa bersedia dengan perubahan dan pertambahan dalam Linux.
Objektif:
1. Mengetahui kepentingan menaiktarafkan pakej dalam Linux
2. Mengetahui asas pilihan dalam rpm
3. Mengetahui  perkakasan GUI dalam RPM
4. Mengetahui kaedah mengompil kod sumber
5. Mengetahui kepenggunaan apt
6. Mengetahui perkakasan GUI dalam apt

17 MENGINSTALASI DAN MENAIKTARAF PERISIAN
17.1 Pengenalan
Kebanyakan pengedaran Linux (Linux Distribution) yang moden penuh dengan pelbagai pakej
perisian yang pelbagai, ada banyak yang boleh dipilih semasa menginstalasi sistem dan boleh
terus digunakan sebaik sahaja selesai proses instalasi. Ada kalanya, anda juga perlu
menginstalasi dan menggunakan perisian/perisian tambahan, atau menaik taraf perisian yang
sedia ada dan yang telah anda diinstalasikan ke dalam sistem tersebut sebelum ini. Bergantung
kepada distribusi Linux yang mana anda gunakan sekarang (dalam kes ini, ia sepatutnya adalah
Red Hat Linux), anda mempunyai pelbagai pilihan untuk beberapa format pakej yang
berlainan.
Selain daripada pilihan untuk format pakej, suatu perisian/aplikasi boleh diedarkan sama ada
dalam format binari atau kod sumber. Format Binari adalah perisian siap sedia untuk
digunakan; manakala format kod sumber pula mengandungi fail kod perisian yang asal, yang
perlu dikompilkan kepada bentuk binari sebelum seseorang itu boleh menggunakannya di
dalam Linux. Walaupun format kod sumber memerlukan anda  melakukan banyak perkara
untuk digunakan berbanding dengan format binari, tetapi ia adalah lebih mudah dibawa
berbanding dengan pakej binari. Contohnya, anda boleh mengunakan pakej kod sumber yang
sama pada kedua-dua komputer Intel x86 dan PowerPC.
Mengemaskinikan pakej yang sedia ada  adalah sama penting seperti menambah pakej yang
baru. Menaiktaraf mungkin boleh membaiki masalah pepijat (bug) dan ketidaksempurnaan
keselamatan sistem, atau pun hanya menambah ciri-ciri baru /sokongan baru yang diperlukan
oleh perisian baru yang akan dilarikan.

17.2 Pakej Binari
Prosedur untuk pemasangan perisian adalah berbeza untuk setiap Distribusi Linux.
Kebanyakan distribusi hari ini menggunakan samaada fail Red Hat Package Manager (RPM)
atau Debian package (deb), manakala yang lain mungkin menggunakan format hak milik
mereka sendiri. Di sini kita akan melihat kepada salah satu daripada format yang paling lazim
digunakan dalam pemasangan pakej binari - RPM.
17.2.1 Manfaat Daripada Pakej Rpm
Kebanyakan Distribusi Linux yang moden menggunakan format RPM. Ia adalah perkakas
(perkakas)yang sangat berguna kerana terdapatnya pengkalan data pada pakej yang telah
dipasang. Pengkalan ini  termasuk informasi pada pakej (nama dan versi), fail berkaitan dengan
pakej tersebut, menyemak jumlah untuk setiap fail dan fail serta pakej yang bergantung
kepadanya.
Pengkalan data ini membolehkan distribusi Linux berasaskan RPM untuk mengesan
ketidaksesuaian serta ciri-ciri yang hilang yang diperlukan oleh pakej baru tertentu. Ini akan
mengelakkan daripada merosakkan sistem jika ada cubaan untuk menginstalasi pakej yang
telah rosak atau percanggahan pakej pada sistem itu. Amaran akan diberikan bermula dari awal
lagi untuk mengelakkan penemuan masalah di kemudian hari yang berkaitan dengan
kehilangan pakej atau isu kebergantungan.
17.2.2 Menginstalasi Pakej Rpm
Instalasi RPM adalah proses yang sangat mudah. RPM boleh dilaksanakan dalam banyak
cara, menggunakan sama ada perkakas (tool) berdasarkan-teks atau perkakas (tool) antara
muka (interface) grafik pengguna (GUI). Kedua-dua perkakas akan dibincangkan secara
ringkas di sini.

Perhatian !!
Menaiktarafkan pakej RPM kadangkala menghilangkan fail konfigurasi asal pakej ,
oleh itu buatlah ‘BACK UP’ untuk fail konfigurasi yang penting (selalunya pada
salah sebuah tempat di dalam /etc/ tetapi mungkin ditempatkan di tempat lain di
dalam cakera keras sebelum menaik taraf perisian yang sedang diolah !
17.2.3 Perkakas Rpm Berdasarkan-Teks
Satu daripada cara mudah untuk melaksanakan rpm adalah melalui ‘SHELL PROMPT’.
Untuk menggunakan arahan rpm memerlukan sekurang-kurangnya satu parameter
operasi ( -U, -F, -i , etc ) dengan satu atau lebih pilihan (-V, -h, -a  etc). Kemungkinan
anda perlu untuk membekalkan nama pakej atau nama fail pakej (nama fail pakej yang
lengkap selalunya akan berakhir dengan .rpm) bersama-sama dengan operasi dan pilihan
parameter.
Pakej RPM boleh diinstalasikan satu demi satu, atau melalui senarai pelbagai pakej
(diasingkan oleh ruangan), dengan menggunakan arahan rpm.
17.2.4 Asas Pilihan rpm
Untuk menginstalasi dan menaiktaraf pakej melalui ‘SHELL PROMPT’, gunakan sintaks
berikut :
Rpm [ operation ] [ option ]  [ package – files \ package – names ]
Jadual di bawah meringkaskan operasi rpm yang lazim digunakan, dan beberapa pilihan
yang penting.
Operasi rpm Deskripsi
- I Instalasi pakej ; sistem itu mestilah tidak mengandungi

pakej yang mempunyai nama yang sama atau ia akan
memberikan error.
- U Instalasi pakej baru atau menaiktaraf perisian yang
telah sedia ada (wujud)
- F atau - freshen Menaiktaraf pakej jika versi yang sebelumnya telah
sedia ada (wujud).
- q Menyoal pakej ; memeriksa jika pakej itu telah pun
diinstalasi, apakah kandungan fail , dan lain-lain.
- V atau – y atau -verify Membuktikan kesahihan pakej ; memeriksa kehadiran
fail pakej dan tidak berubah sejak instalasi.
- e Nyah-instalasi / mengalihkan pakej daripada sistem.
- b Membina pakej binari , diberi kod sumber dan fail
konfigurasi.
- rebuild Membina pakej binari , diberi sumber fail RPM.
- rebuilddb Membina pengkalan RPM , untuk membaiki error.
Jadual 34 : Operasi rpm yang lazim digunakan

Pilihan rpm
Digunakan dengan
operasi Deskripsi
- root dir Apa saja Modifikasi sistem Linux mempunyai direktori akar
di lokasikan pada dir. Pilihan ini boleh digunakan
untuk mengekalkan satu instalasi Linux diskrit
daripada yang lain , sebegai contohnya , semasa
instalasi OS (sistem operasi) atau kecemasan.
- force - i , - U , - F Memaksa pakej diinstalasikan walau pun ia
bermakna terpaksa ‘overwrite’ pakej yang telah
sedia ada.
- h atau –
hash
- i , - U , - F Menggunakan siri signal pound (#) untuk
menunjukkan kemajuan operasi.
- V - i , - U , - F Selalunya digunakan dalam konjuksi dengan “- h”
untuk menghasilkan nombor seragam bertanda
hash (#) untuk setiap pakej.
- nodeps - i , - U , - F , - e Menyelenggarakan semak tanpa kebergantungan.
Instalasi atau mengalihkan pakej walau pun ia
terpaksa bersandar pada pakej lain yang tidak ada ,
atau ia diperlukan oleh pakej yang tidak dinyah-
instalasi.
- test - i , - U , - F Semak untuk kebergantungan , konflik dan masalah
lain tanpa sebenarnya menginstalasi pakej itu.
- prefix path - i , - U , - F Set direcktori instalasi kepada path (tidak sesuai
untuk semua pakej).
- a atau – all - q , - V Menyoal atau mengesahkan semua pakej.

- f file atau –
file file
- q , - V Menyoal atau mengesahkan pakej yang memiliki
fail tersebut.
- p package –
file
- q Menyoal fail-pakej RPM yang belum diinstalasi
lagi.
- i - q Mempamerkan informasi pakej.
- R atau –
requires
- q Mempamerkan pakej dan fail pada yang mana ia
bergantung.
- l atau - list - q M empamerkan fail yang terkandung dalam pakej.
Jadual 35 : Jadual 7.2 : Pilihan RPM yang terpenting
17.2.5 Menginstalasi atau Menaiktaraf
Apabila menginstalasi atau menaiktaraf suatu pakej , operasi “- U” adalah paling berguna
kerana ia membolehkan instalasi pakej tanpa menyah-instalasikan perisian yang lama.
Operasi satu demi satu ini asalah sangat berguna terutamanya apabila ada pakej dengan
kebergantungan yang banyak, kerana rpm mengesan semua ini dan boleh
menyelenggarakan operasi jika pakej baru memenuhi kebergantungan yang disediakan
oleh perisian yang lama.
Untuk menggunakan rpm untuk instalasi atau menaiktaraf suatu pakej , gunakan contoh
rpm berikut :
#  rpm  - Uvh  nmap  - 2 . 4 – 10 . i386 . rpm
Preparing . . .      #########################################  [ 100 % ]
1 . nmap             #########################################   [ 100 % ]

Gantikan “nmap  - 2 . 4 – 10 . i386 . rpm” dengan nama fail pakej ( atau senarai nama fail
yang mahu diinstalasi atau dinaiktaraf).
Cara lain untuk menginstalasi pakej baru ialah dengan menggunakan “rpm – ivh” sebagai
ganti kepada “rpm – Uvh”.
17.2.6 Menyoal dan Mengesahkan
Suatu pakej RPM boleh disahkan dengan arahan “rpm – i” , yang mana mempamerkan
informasi pada pakej yang disoal. Berikut adalah sampel tanyaan :
17.3 Perkakas Rpm Gui
Banyak distribusi Linux datang dengan beberapa perkakas GUI yang boleh membantu
untuk instalasi , mengalihkan , mengemaskini dan menyoal pakej RPM.
17.3.1 Perkakas Pengurusan  Pakej (Package Management Tool)
RED HAT Linux juga didatangi dengan perkakas lain yakni RPM antara muka (interface)
berasaskan grafik(GUI) yang berkuasa. Walaupun telah menggunakannya semasa
instalasi , ia masih boleh digunakan sekali lagi di dalam sistem bila-bila saja diperlukan
seperti iinstalasi , kemaskini , soal (query) atau membuang apa saja pakej-pakej RPM.
Perkakas GUI baru ini dipanggil Perkakas Pengurusan Pakej (Package Management
Tool). Untuk memulakan aplikasi , pergi butang menu utama (pada panel) > System
System > Packages , atau taip arahan redhat ± config ± packages pada shell prompt.

Gambar Rajah 152 : Langkah-langkah untuk mendapatkan srin Penambahan dan Pembunagan
Pakej
Antara muka (interface) untuk aplikasi ini adalah sama seperti yang digunakan semasa
instalasi. Pakej terbahagi kepada kumpulan pakej , yang mengandungi senarai pakej
standard dan pakej tambahan yang berkongsi fungsi-fungsi umum.
Sebagai contoh , kumpulan Internet grafik mengandungi pelihat jaringan , klien email ,
dan perisian grafik yang lain digunakan untuk menghubungkan pada internet. Pakej
standard tidak boleh dipilih untuk dialihkan kecuali keseluruhan kumpulan pakej juga
dialihkan. Pakej tambahan pula adalah pakej berpilihan yang boleh dipilih untuk instalasi
atau dialihkan , selagi kumpulan pakej dipilih.
Tetingkap utama menunjukkan senarai kumpulan pakej. Jika kumpulan pakej mempunyai
tanda semakan dalam kotak semakan di sebelahnya, maka pakej daripada kumpulan itu

sudah diinstalasikan dan sedang digunakan. Untuk melihat senarai pakej individual untuk
kumpulan , klik butang Details di sebelahnya. Pakej individual dengan tanda semakan di
sebelahnya adalah sedang digunakan.
17.3.2 Instalasi Pakej-pakej
Untuk menginstalasi pakej standard dalam kumpulan pakej yang tidak digunakan pada
masa itu , pilih kotak semakan di sebelahnya. Untuk menyesuaikan pakej yang akan
diinstalasikan dalam kumpulan , klik butang Details di sebelahnya. Senarai pakej
standard dan tambahan dipamerkan , seperti yang ditunjukkan pada rajah di bawah.
Menekan pada nama pakej yang dipamerkan pada ruang cakera yang diperlukan untuk
menginstalasi pakej pada bahagian bawah tetingkap. Tandakan pada kotak semakan di
sebelah nama pakej yang ditandakan untuk instala
---
*Linux for NOSS Malaysia (Sovereign Markdown Palace) | Harisfazillah Jamel (LinuxMalaysia) | 2026-08-16*
*Standard: UK English | DBP-standard Bahasa Melayu Malaysia (Piawai) | Dwi-Lesen: CC BY-SA 4.0 (Kandungan) / MIT (Skrip) | [Notis Perundangan, Privasi & Penafian](/docs/legal-notice.md)*
