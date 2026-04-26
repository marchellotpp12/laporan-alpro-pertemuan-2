def kuis_file(nama_file):
    print(f"Nama file: {nama_file}")
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            for line in file:
                if '||' in line:
                    soal, jawaban_benar = line.strip().split('||')
                    soal = soal.strip()
                    jawaban_benar = jawaban_benar.strip()

                    print(soal)
                    jawaban_user = input("Jawab: ").strip()

                    if jawaban_user.lower() == jawaban_benar.lower():
                        print("Jawaban benar!")
                    else:
                        print("Jawaban salah!")
    except:
        print(f"File '{nama_file}' tidak ditemukan.")