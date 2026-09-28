baris_pertama = [1, 2, 3]
baris_kedua = [4, 5, 6]
baris_ketiga = [7, 8, 9]
baris_keempat = [0]

print("|   1   |   2   |   3   |")
print("|   4   |   5   |   6   |")
print("|   7   |   8   |   9   |")
print("|   0   |       |       |\n")

baris = int(input("Baris ke : "))
kolom = int(input("Kolom ke : "))

if baris == 1 and kolom == 1 :
    print(f"Baris pertama, kolom pertama adalah {baris_pertama[0]}")
elif baris == 1 and kolom == 2 :
    print(f"Baris pertama, kolom kedua adalah {baris_pertama[1]}")
elif baris == 1 and kolom == 3 :
    print(f"Baris pertama, kolom ketiga adalah {baris_pertama[2]}")
elif baris == 2 and kolom == 1 :
    print(f"Baris kedua, kolom pertama adalah {baris_kedua[0]}")
elif baris == 2 and kolom == 2 :
    print(f"Baris kedua, kolom kedua adalah {baris_kedua[1]}")
elif baris == 2 and kolom == 3 :
    print(f"Baris kedua, kolom ketiga adalah {baris_kedua[2]}")
elif baris == 3 and kolom == 1 :
    print(f"Baris ketiga, kolom pertama adalah {baris_ketiga[0]}")
elif baris == 3 and kolom == 2:
    print(f"Baris ketiga, kolom kedua adalah {baris_ketiga[1]}")
elif baris == 3 and kolom == 3:
    print(f"Baris ketiga, kolom ketiga adalah {baris_ketiga[2]}")
elif baris == 4 and kolom == 1:
    print(f"Baris keempat, kolom pertama adalah {baris_keempat[0]}")
elif baris == 4 and kolom == 2:
    print(f"Baris keempat, kolom kedua adalah ")
elif baris == 4 and kolom == 3:
    print(f"Baris keempat, kolom ketiga adalah ")
else:
    print("\nbarisnya cuma sampe 4, dan kolomnya cuma sampe 3, kenapa lu isi lebih")
    
