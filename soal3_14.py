def ambil_kata_dari_file(nama_file):
    try:
        with open(nama_file, 'r') as data:
            isi_teks = data.read().lower()
            kumpulan_kata = set(isi_teks.split())
            return kumpulan_kata

    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
        return None

    except IOError:
        print(f"Error: Tidak bisa membaca file '{nama_file}'.")
        return None


nama_file1 = input("Masukkan nama file pertama: ")
nama_file2 = input("Masukkan nama file kedua: ")

kata1 = ambil_kata_dari_file(nama_file1)
kata2 = ambil_kata_dari_file(nama_file2)

if kata1 is not None and kata2 is not None:

    kata_sama = kata1 & kata2

    print("\nKata-kata yang muncul di KEDUA file:")

    if kata_sama:
        for kata in sorted(kata_sama):
            print("-", kata)
    else:
        print("Tidak ada kata yang sama di kedua file.")
        
        
        
        