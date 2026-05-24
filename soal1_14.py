jumlah_kategori = int(input('Masukkan jumlah kategori: '))

kategori_aplikasi = {}

for index in range(jumlah_kategori):
    nama_grup = input(f'\nMasukkan nama kategori ke-{index+1}: ')
    print(f"Masukkan 5 nama aplikasi di kategori '{nama_grup}'")

    list_app = []

    for nomor in range(5):
        input_app = input(f'  Nama aplikasi ke-{nomor+1}: ').strip().lower()
        list_app.append(input_app)

    kategori_aplikasi[nama_grup] = list_app

print("\nDaftar aplikasi per kategori:")

for grup, daftar in kategori_aplikasi.items():
    print(f"- {grup}: {daftar}")

gabungan_set = []

for daftar in kategori_aplikasi.values():
    gabungan_set.append(set(daftar))

irisan = gabungan_set[0]

for index in range(1, len(gabungan_set)):
    irisan = irisan.intersection(gabungan_set[index])

print("\nAplikasi yang muncul di SEMUA kategori:")

if irisan:
    print(irisan)
else:
    print("Tidak ada aplikasi yang muncul di semua kategori.")

semua_data = []

for daftar in kategori_aplikasi.values():
    semua_data += daftar

jumlah_muncul = {}

for aplikasi in semua_data:
    if aplikasi in jumlah_muncul:
        jumlah_muncul[aplikasi] += 1
    else:
        jumlah_muncul[aplikasi] = 1

muncul_satu_kali = []

for aplikasi in jumlah_muncul:
    if jumlah_muncul[aplikasi] == 1:
        muncul_satu_kali.append(aplikasi)

print("\nAplikasi yang hanya muncul di SATU kategori:")

if muncul_satu_kali:
    print(set(muncul_satu_kali))
else:
    print("Tidak ada.")

if jumlah_kategori > 2:
    muncul_dua_kali = []

    for aplikasi in jumlah_muncul:
        if jumlah_muncul[aplikasi] == 2:
            muncul_dua_kali.append(aplikasi)

    print("\nAplikasi yang muncul TEPAT di DUA kategori:")

    if muncul_dua_kali:
        print(set(muncul_dua_kali))
    else:
        print("Tidak ada.")

