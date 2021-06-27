
a = 100
b = 50
print (a % b)



data = [("beji", 77), ("rudi", 58), ("maya", 99)]
nilai = []
for x in data:
	nilai.append(x[1])
print(sorted(nilai))

a = 23
b = 78
if ( a == b):
	print("makan")
else:
	b = a
	m = b

print(m)

l = ("sa", "ma", "la", "ka", "ha")
print(l.index("la"))

angkaku = [1, 2, 3, 5]
def kalitiga(x):
	return x * 3
hasil = map(kalitiga,angkaku)
print(list(hasil))

for bg in range(1,5):
	for s in range(1,bg):
		print("*", end = " ")
	print("")

	


c = 10
d = 5
x = c
c = d
print(c)

myset = {"apple", "banana", "cherry"}
print(pop(myset))