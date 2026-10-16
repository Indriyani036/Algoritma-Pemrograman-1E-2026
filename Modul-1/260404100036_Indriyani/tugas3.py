jarak = 100
bahan_bakar = 40
sisa_bahan_bakar = 1.5
harga_bahan_bakar = 10000
total_jarak = jarak * 2
kebutuhan_bahan_bakar = total_jarak / bahan_bakar
bahan_bakar_dibeli = kebutuhan_bahan_bakar - sisa_bahan_bakar
total_biaya = harga_bahan_bakar * bahan_bakar_dibeli

print(" total jarak pulang pergi yang harus ditempuh :",total_jarak)
print(" total kebutuhan bahan bakar : ",kebutuhan_bahan_bakar)
print(" total bahan bakar yang harus di beli : ", bahan_bakar_dibeli)
print(" total biaya : ",total_biaya)