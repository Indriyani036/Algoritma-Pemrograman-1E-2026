pin = int(input("masukkan 3 digit PIN = "))
jam = int(input("masukkan jam kedatangan (0-23) = "))

# Memecah 3 digit PIN secara matematis
digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

# Pengecekan aturan keamanan pintu garasi
if pin % 5 == 0:
    if jam < 12:
        pesan = "Garasi Pagi Terbuka"
    else:
        pesan = "Garasi Malam Terbuka"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        pesan = "Garasi VIP Terbuka Khusus Bos"
    else:
        pesan = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    pesan = "Akses Ditolak Sepenuhnya"

# Status kamera CCTV markas menggunakan tenary operator
status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"

print("Digit pertama :", digit1)
print("Digit Kedua :", digit2)
print("Digit Ketiga :", digit3)
print("Pesan Status :", pesan)
print("Status CCTV :", status_cctv)