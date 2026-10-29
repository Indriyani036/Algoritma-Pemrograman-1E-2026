jumlah_baris = int(input("masukkan jumlah baris lampu: "))
for i in range(1, jumlah_baris + 1):
    print(f"\nbaris ke-{i}") 
    
    jumlah_lampu = int(input("masukkan jumlah lampu: "))
    for j in range(1, jumlah_lampu + 1):
        if j % 3 == 0:
            print(f"Lampu {j}: mengalami gangguan")
        else:
            print(f"Lampu {j}: berfungsi normal")

print("\nSemua lampu selesai diperiksa")
print("periksa sumber listrik utama taman")