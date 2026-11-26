tugas = {}

while True:
    print("\nMENU TO-DO LIST")
    print("1. Menambah tugas")
    print("2. Menampilkan semua tugas")
    print("3. Menandai tugas selesai")
    print("4. Menghapus tugas")
    print("5. Jumlah tugas yang sudah selesai")
    print("6. Jumlah tugas yang belum selesai")
    print("7. Keluar")

    pilihan = input("Pilih Menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            print("Tugas sudah ada!")
        else:
            tugas[nama] = "Belum Selesai"
            print("Tugas berhasil ditambahkan")

    elif pilihan == "2":
        if len(tugas) == 0:
            print("Belum ada tugas")
        else:
            for nama, status in tugas.items():
                print(nama, "-", status)

    elif pilihan == "3":
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas berhasil diselesaikan.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "4":
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            del tugas[nama]
            print("Tugas berhasil dihapus.")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "5":
        selesai = list(tugas.values()).count("Selesai")
        print("Jumlah tugas yang sudah selesai:", selesai)

    elif pilihan == "6":
        belum = list(tugas.values()).count("Belum Selesai")
        print("jumlah tugas yang belum selesai", belum)

    elif pilihan == "7":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid")