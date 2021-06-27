def kuadrat(angka):
    total_kuadrat = angka ** 2
    print('kuadrat dari ', angka,'adalah', total_kuadrat)
    return total_kuadrat

a = kuadrat(5)
print(a)

# return juga bisa jadi list
def tambah(angka1, angka2):
    penjumlahan = angka1 + angka2
    print(angka1, '+', angka2, '=', penjumlahan)
    return[penjumlahan, 12, 13, 14]
a = tambah(2,9)
print(a)

#return unik
def tambah(angka3, angka4):
    total = angka3 + angka4
    print(angka3, '+', angka4, '=', total)
    return total

def kali(angka5, angka6):
    total_kali = angka5 * angka6
    print(angka5, 'x', angka6, '=', total_kali)
    return total_kali

a = tambah(6,7)
b = kali(a,9)
c= tambah(6,(kali(b,9)))
print(c)

# contoh
def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))
z = max(8, 5)
print(z)

"""
ingat kode dibawah return tidak akan diprint
"""
#contoh kode dibawah return
def add_numbers(x, y):
    total = x + y
    return total
    print("Ini gak bakal dicetak")

print(add_numbers(4, 5))