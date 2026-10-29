suhu = float(input("masukkan suhu reaktor :"))
tekanan = float(input("masukkan tekanan gas :"))

# Pengecekan tingkat bahaya bersarang
if suhu > 1000:
    if tekanan > 50:
        status_bahaya = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status_bahaya = "Bahaya Suhu: Segera Turunkan Daya"
elif suhu > 500:
    if tekanan > 30:
        status_bahaya = "Tekanan Tidak Stabil"
    else:
        status_bahaya = "Operasi Reaktor Normal"
else:
    status_bahaya = "Reaktor Belum Cukup panas"

status_pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("Suhu Reaktor :", suhu)
print("Tekanan gas :", tekanan)
print("Status Bahaya reaktor :", status_bahaya)
print("Status Pompa :", status_pompa)

