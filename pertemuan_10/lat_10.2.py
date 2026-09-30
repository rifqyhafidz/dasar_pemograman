# input
print("\n===========================================================")
print("|                    SEWA KAMAR HOTEL                     |")
print("===========================================================")
print("| Kode     Tipe kamar      Harga          lama penginapan |")
print("===========================================================")
print("| A        Standard        Rp. 300.000    1 hari          |")
print("| B        Deluxe          Rp. 500.000    1 hari          |")
print("| C        Suite           RP. 800.000    1 hari          |")
print("===========================================================")
print("Note : untuk setiap transaksi dikenakan pajak sebesar 2%")



banyak_tipe = int(input("\nBanyak tipe: "))

tipe_kamar = []
harga_kamar = []
lama_penginapan = []


for i in range(banyak_tipe):
    jenis = print(f"\nTipe Ke-{i+1}") 
    kode_kamar = input("Kode kamar: ")
    lama_penginapan.append(int(input("Lama penginapan(hari) : ")))

    if kode_kamar == "A" or kode_kamar == "a":
        harga_kamar.append(300000)
        tipe_kamar.append("Standard ")
    elif kode_kamar == "B" or kode_kamar == "b":
        harga_kamar.append(500000)
        tipe_kamar.append("Deluxe   ")
    elif kode_kamar == "C" or kode_kamar == "c":
        harga_kamar.append(800000)
        tipe_kamar.append("Suite    ")
    else:
        print("kode kamar tidak valid")
        break

jumlah_bayar = 0
for i in range(banyak_tipe):
    jumlah_bayar += harga_kamar[i] * lama_penginapan[i]

pajak = int(jumlah_bayar * 0.02)
total_bayar = int(jumlah_bayar + pajak)

print("\n=============================================================")
print("|\033[1m                      BILL PEMBAYARAN                 \033[0m     |")
print("=============================================================")
print("| No.   Tipe         Harga         Lama          Total      |")
print("|       Kamar        Satuan        Penginapan    Harga      |")
print("=============================================================")
for i in range(banyak_tipe):
    print(f"| {i+1}.    {tipe_kamar[i]}    Rp.{harga_kamar[i]}     {lama_penginapan[i]} hari        Rp.{harga_kamar[i] * lama_penginapan[i]}  |")
print("=============================================================")

print(f"|                                 jumlah bayar : Rp.{jumlah_bayar}  |")
print(f"|                                 Pajak 2 %    : Rp.{pajak}   |")
print(f"|\033[1m                                 Total bayar  : Rp.{total_bayar}\033[0m  |")
print("=============================================================\n")



