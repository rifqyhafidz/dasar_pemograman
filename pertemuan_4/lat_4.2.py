pembeli = input("Input nama pembeli : ")
no_hp = int(input("Input No. Handphone : "))
jurusan = input("Input jurusan [SBY/BL/LMP]: ")

if jurusan == "SBY":
    nama_jurusan = "Surabaya"
    harga = 30000
elif jurusan == "BL":
    nama_jurusan = "Bali"
    harga = 35000
else:
    nama_jurusan = "Lampung"
    harga = 50000

jumlah = int(input("Masukan jumlah beli : "))

if jumlah >= 3 :
    potongan = int((jumlah*harga) * 0.1)
else:
    potongan = 0

total = int((jumlah*harga)- potongan)

print("\n=================================================")
print("               PENJUALAN TIKET BUS")
print("                      XYZ")
print("=================================================")
print(f"Nama Pembeli : {pembeli}")
print(f"No. Handphone : {no_hp}")
print(f"Kode jurusan yang dipilih : {jurusan}")
print(f"Nama kode tujuan : {nama_jurusan}")
print(f"Harga : {harga}")
print(f"Jumlah beli : {jumlah}")
print("===================================================")
print(f"potongan yang didapat : {potongan}")
print(f"Total bayar : {total}")
ubay = int(input('Masukan uang bayar : '))
if ubay >= total:
    uang_kembali = ubay - total
    print(f"Uang kembali : {uang_kembali}")
else: 
    print("Uang anda tidak cukup untuk membayar tiket bus")