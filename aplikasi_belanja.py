harga_makanan = 10000
uang = 30000

input_hitung = input("mau beli berapa makanan ?")
hitung = int(input_hitung)
total_harga = hitung * harga_makanan
sisa_uang = uang - total_harga

print("anda akan membeli " + str(hitung) + " makanan")
print("harga total adalah " + str(total_harga) + " rupiah")

if uang > total_harga:
    print("anda telah membeli " + str(hitung) + " makanan")
    print("sisa uang anda " + str(sisa_uang) + " rupiah")
elif uang == total_harga:
    print("gak ada kembalian")
else:
    print("Uang anda gak cukup")


r = 5
if r >= 2:
    print("bagus")