# Latihan Exceptions
| No. | DAFTAR ISI          | FILE       | GOTO                                               |
|-----|---------------------|------------|----------------------------------------------------|
| 1.  | Pengertian          | Latihan.py | [Menuju Kesini](#pengertian)                       |
| 2.  | Assertion Statement | ~~~~~~~~~~ | [Menuju Kesini](#assertion-statement)              |
| 3.  | Exception Handling  | ~~~~~~~~~~ | [Menuju Kesini](#menangani-sebuah-pengecualian)    |
| 4.  | Except Clause       | ~~~~~~~~~~ | [Menuju Kesini](#pengecualian-tanpa-exceptions)    |
| 5.  | Try-Finally         | ~~~~~~~~~~ | [Menuju Kesini](#try-finally)                      |
| 6.  | Exception Argument  | ~~~~~~~~~~ | [Menuju Kesini](#argumen-dari-sebuah-pengecualian) |
| 7.  | Raising Exceptions  | ~~~~~~~~~~ | [Menuju Kesini](#memunculkan-sebuah-pengecualian)  |
| 8.  | User Exceptions     | ~~~~~~~~~~ | [Menuju Kesini](#pengecualian-buatan-user)         |
| 9.  | Penutup             |            | [Menuju Kesini](#penutup)                          |

Pada pertemuan kali ini, tidak seperti kemarin yang mengerjakan praktikum. Pada repository ini, sekarang saya akan menuangkan hasil latihan Saya. Pada repository ini, saya akan menerangkan tentang exceptions handling / penanganan eksepsi.
Langsung saja, tanpa basa basi lagi, ini lah hasil dari latihan saya.

## Pengertian
Pada python, ada dua fitur yang sangat penting untuk menangani kesalahan tidak terduga di dalam program dan juga menambah kemampuan debugging di dalamnya.
### Exception Handling
Exception Handling adalah suatu mekanisme pada python yang bertujuan untuk menangani sebuah error pada program. Error ini nantinya akan menghentikan program yang dijalankan dengan cara yang tidak normal.
### Assertion
Assertion adalah pemeriksaan kewajaran yang dapat di aktifkan atau nonaktifkan setelah kita menyelesaikan uji pada program. 

## Assertion Statement
Saat menemukan pernyataan, Python mengevaluasi ekspresi yang menyertainya, yang mana
diharapkan semoga benar. Jika ekspresi salah, Python memunculkan pengecualian AssertionError.<br/>
**Syntax** untuk assert itu adalah :<br/>
```assert Expression[, Arguments]```<br/>
Jika pernyataan gagal, Python menggunakan ArgumentExpression sebagai argumen untuk AssertionError.
AssertionError exceptions dapat ditangkap dan ditangani seperti pengecualian lainnya menggunakan try-except statement, tetapi jika dibiarkan, mereka akan menghentikan program dan menghasilkan backtrace.<br/>
**Contohnya**<br/>
Berikut adalah fungsi yang mengubah suhu dari derajat Kelvin menjadi derajat Fahrenheit. Karena nol derajat Kelvin sedingin itu, fungsinya akan keluar jika melihat sebuah suhu negatif.<br/>
![img.ss](Screenshots/ss1.png)<br/>

## Menangani sebuah pengecualian
Jika kita memiliki beberapa kode *mencurigakan* yang bisa memunculkan sebuah pengecualian, kita bisa mempertahankan programnya. Caranya adalah dengan menempatkan kode *mencurigakan* itu didalam sebuah **try:block**. Setelah try:block, masukkan sebuah **except:statement**, dibarengi dengan sebuah block kode yang menangani masalah itu dengan se-sempurna mungkin.<br/><br/>
**Syntax**
Ini adalah sebuah syntax sederhana dari *try...except...else* blocks
```
try:
   Opetasi dilakukan disini;
   ......................
except ExceptionI:
   Jika disini adalah pengecualian1, maka blok ini akan dieksekusi.
except ExceptionII:
   Jika disini adalah pengecualian2, maka blok ini akan dieksekusi.
   ......................
else:
   Jika sama sekali tidak ada pengecualian blok ini yang akan dieksekusi. 
```
**Contoh pertama**<br/>
Dicontoh ini akan membuka file, lalu menulis ini file, dan akan keluar dengan normal karena tidak ada masalah didalamnya.<br>
![img.ss](Screenshots/ss2.png)<br/><br/>
**Contoh kedua**<br/>
Dicontoh ini akan mencoba membuka sebuah file dimana kita tidak mempunyai izin untuk menulis, jadi nantinya akan memunculkan sebuah pengecualian.<br/>
![img.ss](Screenshots/ss3.png)<br/>

## Pengecualian tanpa Exceptions
Kita bisa menggunakan except statement dengan no exceptions yang didefinisikan seperti ini :<br/>
``` 
try:
   Lakukan sebuah operasi disini;
   ......................
except:
   Jika ada sebuah pengecualian disini, maka eksekusi blok ini.
   ......................
else:
   Jika tidak ada pengecualian disini, maka eksekusi blok ini. 
```
Pernyataan **try-except** jenis ini menangkap semua pengecualian yang terjadi. Menggunakan jenis pernyataan try-exception ini tidak dianggap sebagai operasi yang baik, karena semua pengecualian ditangkap, tetapi tidak memungkinkan program untuk mengidentifikasi kemungkinan penyebab masalah.

## Pengecualian dengan beberapa Exceptions
kita bisa juga menggunakan except statement untuk mengatasi beberapa exceptions seperti ini :<br/>
``` 
try:
   Lakukan sebuah operasi disini;
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   Jika ada pengecualian dari list yang diberikan, 
   maka eksekusi blok ini.
   ......................
else:
   Jika tidak ada, maka eksekusi blok ini.
```
## Try-finally
kita bisa menggunakan sebuah **finally:block** bersamaan dengan sebuah **try:block**. Finally Block adalah sebuah tempat untuk menempatkan kode yang harus di eksekusi, apakah try-block akan memunculkan pengecualian atau tidak.<br/> 
Syntax dari try-finally statement adalah seperti ini :<br/>
``` 
try:
   Lakukan sebuah operasi disini;
   ......................
   Jika ada pengecualian, ini akan dilewati.
finally:
   Ini akan selalu di eksekusi.
   ......................
```
Kita tidak bisa menggunakan *else* berbarengan dengan sebuah *finally*.<br/>
**Contohnya**<br/>
![img.ss](Screenshots/ss4.png)<br/>
Contoh yang sama bisa ditulis lebih sempurna<br/>
![img.ss](Screenshots/ss5.png)<br/>
Ketika pengecualian dilemparkan ke *try-block*, eksekusi segera diteruskan ke *finally block*. Setelah semua pernyataan di blok *finally* dieksekusi, pengecualian dimunculkan lagi dan ditangani di dalam pernyataan *except* jika ada di lapisan di atas pernyataan *try-except* berikutnya.

## Argumen dari sebuah pengecualian
Jika kita menulis sebuah kode untuk mengatasi sebuah pengecualian, kita bisa mendapatkan sebuah variabel mengikuti nama dari pengecualian tersebut. Jika kita terjebak di beberapa pengecualian, kita bisa mendapatkan sebuah variabel mengikuti tuple dari pengecualiannya.<br/>
Variabel ini menerima value dari pengecualian yang sebagian besar berisi penyebab dari pengecualian. Variabelnya bisa menerima sebuah value atau beberapa value dalam bentuk sebuah tuple. Tuple ini biasanya berisi string yang error, nomor yang error, dan lokasi errornya.<br/>
**Contohnya**<br/>
![img.ss](Screenshots/ss6.png)<br/>

## Memunculkan sebuah Pengecualian
Kita bisa memunculkan sebuah pengecualian dengan berbagai cara menggunakan raise statement. Syntax untuk raise statement adalah sebagai berikut.<br/>
```raise [Exception [, args [, traceback]]]```<br/>
**Contohnya**<br/>
Sebuah pengecualian bisa berupa sebuah string, sebuah class atau sebuah objek. Umumnya pengecualian yang muncul pada python adalah sebuah class, dengan sebuah argumen yang mana itu adalah turunan dari class. Mendefinisikan pengecualian yang baru sangatlah mudah dan bisa diselesaikan dengan cara seperti ini:<br/>
```
def functionName( level ):
   if level < 1:
      raise ("Level salah!", level)
      # kode yang dibawah ini tidak akan di eksekusi
      # jika kita memunculkan sebuah pengecualian.
```
**Catatan:** Untuk menangkap sebuah pengecualian, sebuah "except" harus merujuk ke pengecualian yang sama, baik itu class object atau simple string. Untuk contoh menangkap pengecualian diatas, kita harus menulis "except" seperti ini:<br/>
``` 
try:
   Logika ditempatkan disini...
except "Invalid level!":
   Exception handling disini...
else:
   Semua kode disini...
```

## Pengecualian buatan User
Python juga membebaskan kita untuk membuat pengecualian sendiri, dengan menurunkan kelas-kelas dari standar built-in pengecualian.<br/>
Berikut adalah sebuah contoh yang berkaitan ke *RuntimeError*. Disini, class yang dibuat merupakan subclass dari *RuntimeError*. Ini berguna ketika kita butuh untuk menampilkan informasi yang lebih spesifik, ketika sebuah pengecualian tertangkap.<br/>
Dalam try block, Pengecualian yang dibuat User memunculkan dan menangkap didalam except block. Variabelnya digunakan untuk membuat sebuah turunan dari class *NetworkError*.<br/>
```
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
```
Jadi ketika kita mendefinisikan class diatas, kita bisa memunculkan pengecualian dengan cara seperti ini :<br/>
``` 
try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args
```

# Penutup
Akhirnya, sudah sampailah kita dipenghujung repository ini. Itulah hasil dari latihan Exception yang telah saya kerjakan. Seperti biasa, jika ada kesalahan kata dalam pengetikan, Saya memohon maaf yang sebesar besarnya. Sekian dari repository ini saya buat. Saya ucapkan, Terimakasih...<br/>
``` 
Nama    : Rhendy Diki Nugraha
NIM     : 312210150
Kelas   : TI.22.A1
Dosen   : Agung Nugroho, S.kom, M.kom
```