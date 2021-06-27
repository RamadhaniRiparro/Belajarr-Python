#scope variabel: local
# berguna untuk merubah variabel dalam fungsi

data = "makanan"
def rubahData(dataBaru):
    data = dataBaru #local
    print("data di ubah menjadi",data)

rubahData('minuman')
print('data',data)#data tak berubah menjadi minuman

# hasil :
# data di ubah menjadi minuman


#scope variabel : global
data = "makanan"
def rubahData(dataBaru):
    global data # kita telah mengakses variable data di dalam fungsi dengan secara global
    data = dataBaru
    print("data di ubah menjadi",data)
 
rubahData('minuman')
print('data',data)#data berybah menjadi  minuman
 
# hasil :
# data di ubah menjadi minuman
# data minuman => nilai akan ditampilkan berdasarkan fungsi