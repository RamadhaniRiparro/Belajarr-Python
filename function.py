#cara loop
# memotong list (mengambil lebih dari 1 item d list) dengan range
number2 =[100, 200, 300, 400, 500, 600, 700,]
ambil_angka3 = number2[2:5] #yang diambil hanya 3 angka bukan 4 angka
print(ambil_angka3)
# jika angka range pertama tidak ada maka dimulai dari item pertama
number2 =[100, 200, 300, 400, 500, 600, 700,]
print(number2[:4])
# jika angka range terakhir tidak ada maka dimulai dr index yg disebutkan
print(number2[4:])