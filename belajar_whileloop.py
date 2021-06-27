a = 1
while a < 10:
   print(a)
   a += 1
else:
  print("stop")


# while dengan continue

i = 0
while i < 30:
  i += 1
  if i == 24:
      print("ini angkanya", i)
      continue
  print(i)

# while dengan break
i = 1
while i < 42:
  print(i)
  if i == 10:
    break
  i += 1

# loop bercabang
a = input("masukkan angka ")
x = int(a)
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1 


n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1