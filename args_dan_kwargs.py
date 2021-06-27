# args digunakan untuk data yang tidak diketahui jumlahnya
#args juga digunakan untuk data yang jumalahnya banyak

def daftar_profil(*args):
    for name in args:
        print(name)

daftar_profil('dani', 'hammad', 'adi', 'haekal')

#kalau tidak pakai args maka akan error 

#kwargs
#kwargs biasanya digunakan untuk dictionary

def profil(**kwargs):
    for key, value in kwargs.items():
        print(key, '=', value)

profil(nama = 'dani', umur = '18', hobi = 'tidur ')
"""
 nama *args dan **kwargs bukanlah sesuatu yang baku. 
 Kita juga bisa membuatnya sesuka hati 
 seperti *nama, **nama, *buku, dsb.

"""
def rata_rata(*data):
    banyak_data = len(data)
    jumlah_data = sum(data)
    nilai_rata_rata = (jumlah_data) / (banyak_data)
    return nilai_rata_rata

print (rata_rata(2,4,1,2,4,1,2,3,4,5,1,8,2))

