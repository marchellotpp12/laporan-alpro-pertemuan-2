nama_file = input('Masukkan nama file: ').strip()

try:
    buka = open(nama_file, 'r')
except FileNotFoundError:
    print('file tidak ditemukan', nama_file)
    quit()

hasil = {}

for i in buka:
    if not i.startswith('From '):
        continue
    email = i.split()[1]
    domain = email.split('@')[-1]
    hasil[domain] = hasil.get(domain, 0) + 1

buka.close()

print(hasil)