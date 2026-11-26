playlist = {}

while True:
    print("\nMenu Playlist Musik")
    print("1. Buat Playlist")
    print("2. Tambah lagu")
    print("3. Tampilkan Semua Playlist")
    print("4. Cari Lagu")
    print("5. Hapus Lagu")
    print("6. Hapus Playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama Playlist: ")

        if nama in playlist:
            print("Playlist sudah ada!")
        else:
            playlist[nama] = {}
            print("Playlist berhasil dibuat")

    elif pilihan == "2":
        nama = input("Masukkan nama Playlist: ")

        if nama in playlist:
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            playlist[nama][judul] = penyanyi
            print("lagu berhasil ditambahkan")
        else:
            print("Playlist tidak ditemukan")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist")
        else:
            for nama, lagu in playlist.items():
                print("\nPlaylist:", nama)

                if len(lagu) == 0:
                    print("Belum ada lagu")
                else:
                    for judul, penyanyi in lagu.items():
                        print("-", judul, "Oleh", penyanyi)

    elif pilihan == "4":
        judul = input("Masukkan judul lagu: ")
        ditemukan = False

        for nama, lagu in playlist.items():
            if judul in lagu:
                print("Lagu ditemukan!")
                print("Playlist:", nama)
                print("Penyanyi:", lagu[judul])
                ditemukan = True

        if not ditemukan:
            print("Lagu tidak ditemukan")

    elif pilihan == "5":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            judul = input("Masukkan judul lagu: ")

            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu berhasil dihapus")
            else:
                print("Playlist tidak ditemukan")

    elif pilihan == "6":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            del playlist[nama]
            print("Playlits berhasil dihapus")
        else:
            print("Playlist tidak ditemukan")

    elif pilihan == "7":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid!")