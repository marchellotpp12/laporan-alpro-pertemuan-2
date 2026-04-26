def bandingkan_file(file1, file2):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            baris1 = f1.readlines()
            baris2 = f2.readlines()

        max_baris = max(len(baris1), len(baris2))

        ada_perbedaan = False

        for i in range(max_baris):
            b1 = baris1[i].strip() if i < len(baris1) else None
            b2 = baris2[i].strip() if i < len(baris2) else None

            if b1 != b2:
                ada_perbedaan = True
                print(f"\n>>> Perbedaan di Baris ke-{i + 1}:")
                print(f"    File 1 : {b1 if b1 is not None else '[Tidak ada baris]'}")
                print(f"    File 2 : {b2 if b2 is not None else '[Tidak ada baris]'}")

        if ada_perbedaan:
            print("\nKesimpulan: Kedua file BERBEDA!")
        else:
            print("\nKesimpulan: Kedua file IDENTIK!")

    except:
        print(f"Error: File tidak ditemukan!")

bandingkan_file("file1.txt", "file2.txt")

