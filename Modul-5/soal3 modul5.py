def nilai_mahasiswa(nama, tugas, uts, uas):
    akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if akhir >= 85:
        kategori = "A"
    elif akhir >= 70:
        kategori = "B"
    elif akhir >= 55:
        kategori = "C"
    else:
        kategori = "D"

    if kategori == "D":
        status = "Tidak Lulus"
    else:
        status = "Lulus"

    print("\nNama Mahasiswa:", nama)
    print("Nilai Tugas:", tugas)
    print("Nilai UTS:", uts)
    print("Nilai UAS:", uas)
    print("Nilai Akhir:", akhir)
    print("Kategori:", kategori)
    print("Status:", status)

nama = input("masukkan nama mahasiswa: ")
tugas = float(input("masukkan nilai tugas: "))
uts = float(input("masukkan nilai uts: "))
uas = float(input("masukkan nilai uas: "))

nilai_mahasiswa(nama, tugas, uts, uas)