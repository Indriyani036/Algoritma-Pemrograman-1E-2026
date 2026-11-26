def palindrom(kata):
    if kata == kata[::-1]:
        return True
    else:
        return False

kata = input("masukkan sebuah kata: ")
hasil = palindrom(kata)

if hasil == True:
    print(kata, "adalah kata palindrom")
else:
    print(kata, "bukan kata palindrom")