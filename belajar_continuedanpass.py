# continue
# fungsinya adalah melanjutkan loop walaupun item telah ditemukan

# dengan continue
for i in range(1,5):
    if i is 2:
        print("nilai",i,"ditemukan")
        continue
        print("nilai setelah continue") # nilai tidak akan dicetak jika proses terpenuhi
    print("nilai saat ini adalah",i)

# tanpa continue
for i in range(1,5):
    if i is 2:
        print("nilai",i,"ditemukan")
        print("nilai setelah continue") # nilai tidak akan dicetak jika proses terpenuhi
    print("nilai saat ini adalah",i)

"""
ada 2 perbedaan 
1. print yg sejajar dibawah continue
   tidak akan dicetak
2. kalau pake continue maka dia gak akan 
   cetak ulang angka yang dimaksud
   continue : -nilai 2 ditemukan
              -nilai saat ini adalah 3
   tanpa continue : -nilai 2 ditemukan
                    -nilai saat ini adalah 2 (angka 2 nya diulang)
                    -nilai saat ini adalah 3
"""

# pass


for i in range(1,5):
    if i is 2:
        print("nilai",i,"ditemukan")
        pass
        print("nilai setelah pass")
    print("nilai saat ini adalah",i)

"""
Pada script diatas bisa kita lihat bahwa 
nilai setelah pass masih dapat ditampilkan, 
dan pass tersebut tidak melakukan fungsi apapun hanya, 
fungsi pass untuk mengkonstruksi sebuah loop.
"""