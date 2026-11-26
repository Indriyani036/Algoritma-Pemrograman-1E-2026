anggota = []

while True:
    nama = input("Masukkan nama anggota: ")

    if nama.lower() == "selesai":
        break
    anggota.append(nama)
print("\n=== Evaluasi Anggota ===")

for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

penyusup = input("\nMasukkan nama yang ingin dihapus: ")

if penyusup in anggota:
    anggota.remove(penyusup)
    print("Nama", penyusup, "berhasil dihapus.")
else:
    print("Nama tidak ditemukan dalam pendaftaran. ")

print("\n=== Daftar Anggota Akhir ===")
print(anggota)