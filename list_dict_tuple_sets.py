#list
# data dalam list bisa diubah dan diganti

buku = ["fisika", "biologi", "kimia"]
print(buku)

#tuple
# data di tuple tidak bisa diubah

makanan = ("apel", "jeruk", "mangga")
print(makanan)

#dictionary
# terdiri dari key dan value
data = {'name':'dhani', 'buku':'kimia', 'makanan':'mie'}
print(data)

# mengubah list ke tuple dan sebaliknya
buku = ["fisika", "biologi", "kimia"] 
print(tuple(buku)) #list ke tuple

makanan = ("apel", "jeruk", "mangga")
print(list(makanan)) #tuple ke list

#looping dictionary
data = {'name':'dhani', 'buku':'kimia', 'makanan':'mie'}
for key, value in data.items():
    print(key, '=', value)

items = {'apel':'2','pisang':'4','jeruk':'6'}
# Buat loop for yang mengambil kunci dari items
for key, value in items.items():
    print('--------------------------------------------------')

    # Cetak '--------------------------------------------------'
    print('Harga setiap', key, 'adalah', value, 'dolar')

"""
nested dictionary(bercabang)
"""
profil ={1:{'nama':'dhani', 'umur':'17', 'hobi':'makan'},
         2:{'Nama':'Arik', 'Umur':'25', 'Hobi':'Tidur'}}

#angka 1 dan 2 bisa diubah boleh string
print(profil)

#cara mengakses 
print(profil[1]['nama'])

#cara loop
for key, value in profil.items():
    print('keynya =', key)

    for key2 in value:
        print(key2, '=', value[key2])


# sets
# tidak bisa diakses secara spesifik tapi bisa diubah
a = {1,2,3,4,5}
print(a)

# contoh aplikasi sets
a = {1,2,3,4,5}
b = {4,5,6,7,8}

#irisan
print(a&b)

# gabungan
print(a|b)

# mengambil angka yang tidak sama
print(a-b)
print(b-a)

#menggabungkan angka yang tidak sama
print(a^b)

total_kalori = int(input("Kalori yang dikonsumsi andi "))
waktu_olahraga = (total_kalori / 20) * 2
if total_kalori > 750:
        print("Jenis Olahraga : Lari")
elif 500 < total_kalori < 750:
        print("Jenis olahraga : Badminton")
else:
        print("Jenis olahraga : Renang") 

print("Waktu Olahraga : ", waktu_olahraga, "menit")