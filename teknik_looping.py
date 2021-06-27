daftar_hobby = ['Main Bola',
        'Main tenis',
        'Main bulutangkis',
        'Programming',
        'Makan']

nama_orang = ['dhani', 'adi', 'ari', 'aji', 'madi']
# enumerate = penomoran
for i, hobby in enumerate(daftar_hobby):
    print(i,'=', hobby)

# zip = penyatuan
for nama, daftar in zip(nama_orang, daftar_hobby):
    print(nama, 'menyukai', daftar)

# sorted = mengurutkan sesuai alfabet
nama_hewan = ['elang', 'burung', 'anjing', 'ayam', 'ikan']
for i in sorted(nama_hewan):
    print(i)

# dictionary
profil = {'Nama':'Dhani', 
          'Umur':'25',
          'Hoby':'Makan',
          'Job':'Programmer'}
# mengakses key saja
for i in profil.keys():
    print(i)
# mengakses value saja
for i in profil.values():
    print(i)
# mengakses key dan value
for key, value in profil.items():
    print(key, '===', value)

# reverse = dibalik
for i in reversed(range(1,10,1)):
    print(i)