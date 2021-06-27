"""
Cara menggunakan module cukup sederhana. 
Module sendiri berisi fungsi-fungsi. Cara orang melakukan akses kedalam fungsi juga berbeda. 
Coba lihat dan implementasikan kode di bawah ini
"""
import math
print("Nilai pi adalah:", math.pi)
# math.pi merupakan sintak untuk memanggil fungsi

#Import dengan Module Rename atau Alias
"""
Kita bisa mengimpor modul dengan menamainya. 
Hal ini biasanya kita lakukan 
untuk menyingkat nama modul yang panjang.
"""
import math as m  #menggunakan m sebagai module rename atau alias
print("Nilai pi adalah:", m.pi) 
#m.pi merupakan sintak untuk memanggil fungsi​

#Import Sebagian Fungsi
"""
Pada suatu module tidak bisa dipungkiri terdiri 
dari puluhan bahkan ribuan fungsi. 
Namun, yang kita butuhkan hanya 1 atau 2 fungsi saja. 
Untuk meminimalisir ketidakefisienan suatu program dalam load suatu module 
bisa dilakukan import module 
namun hanya beberapa fungsi saja yang kita import kedalam code. 
Format (from module_name import function_name)
"""
from math import pi

print("Nilai pi adalah:", pi)

#Import Semua isi Moduls
"""
Namun, jika memang yang dibutuhkan banyak, 
semisal lebih dari 10 atau bahkan ratusan fungsi, 
bisa dilakukan import semuanya dengan menggunakan 
format from module_name import *. 
Tanda * disini menunjukan semua fungsi diimport kedalam code.
"""
from math import *

print("Nilai e adalah:", e)

"""
Kita Juga bisa Mengimport 
file-file Python lain asalkan 
masih Satu Folder
"""
import contoh
print(contoh.a)
