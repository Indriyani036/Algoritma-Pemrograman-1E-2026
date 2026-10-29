jumlah_penumpang = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    jarak = int(input("masukkan jarak penumpang: "))
    if jarak == 0:
        break
    if jarak < 0:
        print("jarak tidak valid dan silahkan diulangi!")
        continue

    jumlah_penumpang += 1
    total_jarak += jarak

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + 1000
    else:
        tarif = 13000 + 500

    if jumlah_penumpang % 5 == 0 or jumlah_penumpang % 10 == 0:
        tarif = tarif * 0.5
        print("selamat mendapatkan diskon 50%")

    total_pendapatan += tarif
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak
        print("Tarif penumpang:", tarif)

    print("Jumlah penumpang:", jumlah_penumpang)
    print("Total pendapatan: Rp", total_pendapatan)
    print("Jarak terjauh: ", jarak_terjauh)

    if jumlah_penumpang > 0:
        rata_rata = total_jarak / jumlah_penumpang
        print("Rata rata jarak: ", rata_rata)