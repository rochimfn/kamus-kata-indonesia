# Kamus Kata Bahasa Indonesia

* Tentang: Kamus kata dalam bahasa Indonesia.
* Sumber: Didapatkan dengan melakukan `reverse engineering` aplikasi android KBBI
* Step-by-step: 
  * Download berkas apk aplikasi KBBI
  * Extract dengan `apktool`
  * Ambil berkas `assets/acu_nilai.txt`
  * Bersihkan non-printable characters dengan `strings`
  * Ganti `tab` menjadi `newline` dengna `clean.py`
* Status: Belum bersih
