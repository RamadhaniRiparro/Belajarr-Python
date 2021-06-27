makanan = ['tahu', 'bakwan', 'risol']
for m in makanan:
    print(m)
# kalo listnya cuma satu jadi dieja per kata
aqua = 'aqua'
for a in aqua:
    print(a)
# kalau ditambahim len maka dihitung setiap karakternya
baju = ["distro", "muslim", "punk"]
for b in baju:
    print(b)
    print(len(b))

# for didalam for
# 1. buat list di dalam list
sayuran = ["ubi", "brokoli", 'lodeh']
minuman = ["frutang", "mijon", "aer"]
buku = ["fisika", "mtk", "biologi"]

data =[sayuran,minuman,buku]
print(data)

for SubData in data:
    print(SubData)
    for komponen in SubData:
        print(komponen)
# nanti hasilnya akan terbagi - bagi

# contoh loop for
foods =['energen', 'nugget', 'keju']
for food in foods:
    print("Saya suka makan " + food)

# contoh - contoh
for i in range(5):
    print("hello!")

nums = list(range(5))
print(nums[2])
