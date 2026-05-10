daftar_nama = ['red', 'green', 'blue']
daftar_kode = ['#FF0000', '#008000', '#0000FF']

hasil = {}

for indeks in range(len(daftar_nama)):
    hasil[daftar_nama[indeks]] = daftar_kode[indeks]

print(hasil)