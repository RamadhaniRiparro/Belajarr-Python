#stacks
kumpulan_angka = [1, 2, 3, 4, 5, 6, 7, 8]

# memasukkan data baru
kumpulan_angka.append(9)
print("Data masuk: ", 9)
print("Data sekarang: ", kumpulan_angka)
kumpulan_angka.append(10)
print("Data masuk: ", 10)
print("Data sekarang: ", kumpulan_angka)

# stacks :mengeluarkan data terakhir
out = kumpulan_angka.pop()
print("Data keluar: ", out)
print("Data sekarang: ", kumpulan_angka)

#queues
from collections import deque
antrian = deque([100, 200, 300, 400, 500])
print("Data sekarang: ", antrian)

# menambahkan data
antrian.append(600)
print("Data masuk: ", 600)
print("Data sekarang: ", antrian)

# queues : mengeluarkan data di depan
out = antrian.popleft()
print("Data keluar: ", out)
print("Data sekarang: ", antrian)

out = antrian.popleft()
print("Data keluar: ", out)
print("Data sekarang: ", antrian)