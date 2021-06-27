# lambda function
"""
dengan fungsi lambda 
kita dapat membuat 
fungsi tanpa nama
perhatikan perbedaannya dengan fungsi biasa
"""
#fungsi biasa
def kuadrat(x):
    return x**2

kuadrat(3)

def kali(x,y):
    return x*y
     
kali(4,3)

#fungsi lambda
# Program menggunakan lambda 1 argumen 
kuadrat = lambda x: x*x 

# Output: 9 
print(kuadrat(3))

# Lambda dengan 2 argumen 
kali = lambda x, y: x*y 

# Output: 12 
print(kali(4,3))