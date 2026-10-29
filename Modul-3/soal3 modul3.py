jumlah_mahasiswa = 10
data_mahasiswa = []
jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total_nilai = 0

for i in range(1, jumlah_mahasiswa + 1):
    print("/nmahasiswa ke-", i)
    nama = input("masukkan nama: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    akhir = tugas * 0.30 + uts * 0.30 + uas * 0.40

    if akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    data = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir,
        "kategori": kategori,
    }
    data_mahasiswa += [data]
    total_nilai += akhir

for data in data_mahasiswa:
    print("/nNama:", data["nama"])
    print("Nilai tugas:", data["tugas"])
    print("Nilai UTS:", data["uts"])
    print("Nilai UAS:", data["uas"])
    print("Nilai akhir:", data["akhir"])
    print("kategori:", data["kategori"])

tertinggi = data_mahasiswa [0]
terendah = data_mahasiswa [0]

for data in data_mahasiswa:
    if data["akhir"] > tertinggi["akhir"]:
        tertinggi = data
    if data["akhir"] < terendah["akhir"]:
        terendah = data

rata_rata = total_nilai / jumlah_mahasiswa
print("jumlah kategori A:", jumlah_A)
print("jumlah kategori B:", jumlah_B)
print("jumlah kategori C:", jumlah_C)
print("jumlah kategori D:", jumlah_D)
print("jumlah kategori E:", jumlah_E)
print("/nNilai tertinggi:", round(tertinggi["akhir"], 2))
print("nama:", tertinggi["nama"])
print("/nNilai terendah:", round(terendah["akhir"], 2))
print("nama:", terendah["nama"])
print("/Rata-rata nilai akhir:", round(rata_rata, 2))