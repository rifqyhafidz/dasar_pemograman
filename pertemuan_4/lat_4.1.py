kode_baju = input("Masukan kode baju [SP/AD] : ")
ukuran = input("Masukan ukuran baju [S/M] : ")

if kode_baju == "SP" or kode_baju == "sp":
    merk = "SuperDry"
    if ukuran == "S" or ukuran == "s":
        harga = 45000
    elif ukuran == "M" or ukuran == "m":
        harga = 500000
    else:
        harga = 0
elif kode_baju == "AD" or kode_baju == "ad":
    merk = "Adidas"
    if ukuran == "S" or ukuran == "s":
        harga = 650000
    elif ukuran == "M" or ukuran == "m":
        harga = 700000
    else:
        harga = 0
else:
    merk = "Anda Salah input kode merk"
    harga = 0

print("===================================")
print(f"Merk baju : {merk}")
print(f"Harga baju : Rp. {harga}")
