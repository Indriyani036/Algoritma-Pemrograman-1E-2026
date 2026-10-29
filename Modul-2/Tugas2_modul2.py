total_belanja = int(input("masukkan total belanja awal: "))

# Pengecekan diskon (promo terbesar hingga terkecil)
if total_belanja % 100000 == 0 and total_belanja > 0:
    diskon = 1.00
elif total_belanja % 50000 == 0 and total_belanja > 0:
    diskon = 0.50
elif total_belanja % 10000 == 0 and total_belanja > 0:
    diskon = 0.20
elif total_belanja >= 200000:
    diskon = 0.10
else:
    diskon = 0.00

# Total harga akhir
total_bayar = total_belanja * (1 - diskon)

# Status poin
status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"

print("total belanja :", total_belanja)
print("total harga akhir :", int(total_bayar))
print("status poin :", status_poin)