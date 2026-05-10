berkas = input('Masukkan nama file: ').strip()

try:
    buka_berkas = open(berkas, 'r')
except FileNotFoundError:
    print('file tidak ditemukan', berkas)
    quit()

historgram = {}

for baris in buka_berkas:
    baris = baris.rstrip()

    daftar_kata = baris.split()
    if len(daftar_kata) < 2:
        continue

    alamat_email = daftar_kata[1]
    historgram[alamat_email] = historgram.get(alamat_email, 0) + 1

buka_berkas.close()

print(historgram)