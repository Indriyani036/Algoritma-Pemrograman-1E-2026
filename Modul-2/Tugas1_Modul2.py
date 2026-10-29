kode = int(input("Masukkan kode 3 digit: "))

# Pemisah digit secara matematis
digit1 = kode // 100
digit2 = (kode // 10) % 10
digit3 = kode % 10

# Nilai pelacak awal
pelacak_awal = digit1 * digit3

# Perubahan tahap pertama
if digit2 % 2 != 0:
   # Jika digit kedua ganjil
   pelacak_tahap1 = pelacak_awal + 25
else:
   # Jika digit kedua genap
   pelacak_tahap1 = pelacak_awal - digit2

# Perubahan tahap kedua (Nilai akhir)
if pelacak_tahap1 % 3 == 0:
   # Jika kelipatan 3
   nilai_akhir = pelacak_tahap1 // 3
else:
   # Jika bukan kelipatan 3
   nilai_akhir = pelacak_tahap1 * 2

# Status password
if nilai_akhir > 50:
    status_password = "Kategori A"
elif nilai_akhir > 20:
    status_password = "Kategori B"
else:
    status_password = "Password Ditolak"

print("Digit Pertama =", digit1)
print("Digit Kedua =", digit2)
print("Digit Ketiga =", digit3)
print("pelacak awal =", pelacak_awal)
print("nilai pelacak tahap pertama =", pelacak_tahap1)
print("nilai akhir =", nilai_akhir)
print("status password =", status_password)