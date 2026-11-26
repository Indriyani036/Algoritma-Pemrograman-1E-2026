daftar = []
daftarhari = []

nama_asisten = input("masukkan nama: ")
while nama_asisten != "cukup":
    daftar.append(nama_asisten)
    nama_asisten = input("masukkan nama: ")
asisten = tuple(daftar)

print("\n=== Satu Tambahan Orang ===")
tambahan = input("masukkan nama: ")
asisten_akhir = asisten + (tambahan, )

hari = input("masukkan hari: ")
while hari != "cukup":
    daftarhari.append(hari)
    hari = input("masukkan hari: ")
hari = tuple(daftarhari)

asistenA = input("masukkan nama asisten pengecualian: ")
hariA = input("masukkan hari pengecualian: ")

jadwal = []
for a in asisten_akhir:
    for h in hari:
        if a == asistenA and h == hariA:
            continue
        jadwal.append((a, h))

print("\nJadwal Shift: ")
for a, h in jadwal:
    print(f"{a} - {h}")