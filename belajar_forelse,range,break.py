for r in range (0,10,2): #angka ketiga menyatakan kelipatan
#dari 0 sampai 9 (ingat dikurang satu jadinya 10 gak di print)
    print(r) #dia akan menyebut angka dari 0-9

# contoh lain
for t in range (0,40,7):
    print(t)

# if dan else
for i in range (0,30):
    print(i)

    if i is 23:
        print("ini angkanya ", i)
    
else : 
    print("ga ada angkanya ")
"""
disini if akan memprint jika ada angka di antara range nya
maka jika tidak ada akan masuk ke else
else ditulis dibawah for jadi terpisah

"""

# break 
# fungsinya adalah menghentikan loop jika item sudah ditemukan
number = 23
for i in range(0,40):
    print(i)

    if i is number:
        print("angka ditemukan ", i)
        break
else:
    print("angka gak ketemu ")
"""
jika number ada di range maka break akan berhenti ketika sampe ke number
misal number = 23 maka break akan menghentikan range ketika sampe angka 23
dan memprint if
namun
jika number tidak ada di range maka akan memprint else
misal number = 120 maka akan di print else yaitu angka ga ketemu

"""