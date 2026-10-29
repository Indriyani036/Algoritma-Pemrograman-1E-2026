total_gaji = 0

for i in range(1, 8):
    print(f"\nHari ke-{i}")

    jam_lembur = int(input("masukkan jam lembur: "))
    shift_malam = input("Apakah bekerja shift malam? (y/n): ")

    gaji = 100000
    if jam_lembur >= 1 and jam_lembur <= 3:
        lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        lembur = 100000
    elif jam_lembur == 6:
        lembur = 200000
    elif jam_lembur == 8:
        lembur = 300000
    elif jam_lembur >= 8:
        print("lembur melebihi batas yang ditentukan dan tidak dihitung")
        lembur = 0
    else:
        lembur = 0

    if shift_malam == "y":
        malam = 50000
    else:
        malam = 0

    gaji = gaji + lembur + malam
    total_gaji = total_gaji + gaji
print("\nTotal gaji selama 7 hari: Rp", total_gaji)
print("Gaji hari ini:", gaji)