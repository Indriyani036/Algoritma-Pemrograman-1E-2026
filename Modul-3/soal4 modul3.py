jumlah_penuh = 0

for i in range(1, 11):
    if jumlah_penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi")
        break
    print("Mahasiswa ke-", i)
    nama = input("masukkan nama: ")
    ipk = float(input("masukkan IPK: "))

    if ipk < 3.00:
        print("Tidak memenuhi syarat beasiswa")
        continue
    penghasilan = int(input("Penghasilan orang tua per bulan (Rp): "))
    if penghasilan <= 3000000:
        status = "Beasiswa penuh"
        jumlah_penuh += 1
    elif penghasilan <= 5000000:
        status = "Beasiswa sebagian"
    else:
        status = "Tidak mendapat beasiswa"

    print("nama:", nama)
    print("IPK:", ipk)
    print("Penghasilan orang tua Rp:", penghasilan)
    print("Hasil seleksi:", status)
    print("jumlah penerima beasiswa penuh:", jumlah_penuh)