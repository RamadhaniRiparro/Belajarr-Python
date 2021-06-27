#contohlist
fruit = ["apple", "cherry", "grape"] #list string
number = [1, 2, 3, 4] #list integer
print(number)
"""
list ditandai dengan simbol kurung yang []
sedangkan
tuple ditandai dengan simbl kurung yang ()
"""
# mengakses item di list
#positif
number =[1, 2, 3, 4, 5, 6, 7,]
ambil_angka = number[3]
print(ambil_angka)

#negatif
#kalau negatif maka nagmbil listnya dari belakang
number =[1, 2, 3, 4, 5, 6, 7,]
ambil_angka2 = number[-3]
print(ambil_angka2)

# memotong list (mengambil lebih dari 1 item d list) dengan range
number2 =[100, 200, 300, 400, 500, 600, 700,]
ambil_angka3 = number[2:5] #yang diambil hanya 3 angka bukan 4 angka
print(ambil_angka3)
# jika angka range pertama tidak ada maka dimulai dari item pertama
number2 =[100, 200, 300, 400, 500, 600, 700,]
print(number2[:4])
# jika angka range terakhir tidak ada maka dimulai dr index yg disebutkan
print(number2[4:])


# menambah list
print(number + number2)

# merubah data content dari list
number =[1, 2, 3, 4, 5, 6, 7,]
print(number)
number[0] = 11
print(number)

# mengcopy list ke variable baru
a = number[:]
a[5] = 99
print(number)

# merubah conten di list mengunakan slicing
number =[1, 2, 3, 4, 5, 6, 7,]
number [1:2] = [99,100] #hanya angka kedua dan ketiga yang dirubah
print(number)

# membuat list dalam list
x = [number,number2]
print(x)

# mengakses item di dalam muiltidimensional list (list dalam list)
y = x[1] [5]
print(y)

# menambahkan sebuah item ke list
number2.append(999)
print(number2)
# menambahkan sebuah item ke list di index tertentu(urutan tertentu)
number2 =[100, 200, 300, 400, 500, 600, 700,]
number2.insert(0, 666)
print(number2)

# menghapus isi list
number3 = [111, 222, 333, 444, 555]
print(number3)
number3.remove(111)
print(number3)
# menghapus list di bagian tertentu
number3 = [111, 222, 333, 444, 555]
del number3[3]
print(number3)

# mengetahui panjang list
number =[1, 2, 3, 4, 5, 6, 7,]
print(len(number))

# mengcopy list
number3 = [111, 222, 333, 444, 555]
print(number3)
ab = number3.copy()
print(ab)

# mengosongkan list
number3 = [111, 222, 333, 444, 555]
number3.clear()
print(number3)