angka1 = 20
angka2 = 30
if angka1 is not angka2:
   print("ya")
else:
   print("salah")

a = 5
b = 10
if a == b:

  print("1")
elif a > b:
  print("2")
else:
  print("3")

  a = 20
  b = 25
  if a > b:
      print( "a lebih kecil b")
  elif a == b:
      print("sama")
  elif a >= b:
      print('makan')
  else:
      print('ini benar')

# boolean dalam if
puasa = True
maksiat = False

if puasa != maksiat:
     print("Netral")
else:
     print("salah")

"""
contoh aplikasi sederhana dengan if
"""
uang = input("woyy berapa uang yang lo pegang ? ")
utang = 20000

if int(uang) > utang:
    print("Yaudah cepetan bayarr !!! ")
else:
      print("Awas lo jangan lama-lama!! ")

"""
contoh aplikasi sedehana if
"""
# putri raja mencari jodoh 
jodoh = input("Apa jenis kelamin mu ? ")
baik = True
soleh = True

if baik & soleh & (jodoh == 'pria'):
     print("yok nikah ! ")
elif baik & soleh & (jodoh == 'cewek'):
     print("jadi saudaraku ")
else:
     print("gak mauu ")      

# if cabang
i = 2
if(i<7):
    print("nilai i kurang dai 7")
    if (i<3):
         print("nilai i kurang dari 7 dan kurang dari 3")
    else:
         print("nilai i kurang dari 7 tapi lebih dari 3")