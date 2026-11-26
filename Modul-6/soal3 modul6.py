def evaluasi_pc(status, ram):
    if status == "Normal" and int(ram) >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

jumlah = int(input("Masukkan jumlah pc: "))
data_pc = []
for i in range(jumlah):
    print("\nData pc ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status PC (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")
    data_pc.append([nama, status, ram])

print("\n=== Hasil Evaluasi PC ===")
for data in data_pc:
    nama = data[0]
    status = data[1]
    ram = data[2]

    try:
        kelayakan = evaluasi_pc(status, ram)
    except ValueError:
        kelayakan = "Format RAM Kacau"
    hasil = '{ "PC": "' + nama + '", "status": "' + kelayakan + '" }'
    print(hasil)