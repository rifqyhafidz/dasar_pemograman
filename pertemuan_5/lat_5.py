print("\nGEROBAK FRIED CHICKEN")
print("---------------------------------------")
print("Kode   Jenis Potong        Harga")
print("---------------------------------------")
print("D      Dada                Rp.2500")
print("P      Paha                Rp.2000")
print("S      Sayap               Rp.1500")
print("---------------------------------------")

banyak_jenis = int(input("Berapa jenis yang ingin dibeli : "))

kode = []
harga = []
banyak_potong = []
jenis_potong = []
total_harga = []
jumlah_harga = []

for i in range(banyak_jenis):
    jenis = print(f"\nJenis Ke-{i+1}") 
    kode = input("Kode Potong [D/P/S] : ")
    banyak_potong.append(int(input(f"Banyak Potong untuk {kode} : ")))

    if kode == "D" or kode == "d":
        harga.append(2500)
        jenis_potong.append("Dada ")
    elif kode == "P" or kode == "p":
        harga.append(2000)
        jenis_potong.append("Paha ")
    elif kode == "S" or kode == "s":
        harga.append(1500)
        jenis_potong.append("Sayap")
    else:
        print("Jenis Potong tidak valid. Harap masukkan D, P, atau S")

total_harga = 0
for i in range(banyak_jenis):
    jumlah_harga.append(harga[i] * banyak_potong[i])    
    total_harga += harga[i] * banyak_potong[i] 
    
pajak = int(total_harga * 0.10)
total_bayar = int(total_harga + pajak)

#output
print("\nGEROBAK FRIED CHICKEN")
print("----------------------------------------------")

print("No. Jenis      Harga      Banyak    Jumlah")
print("    Potong     Satuan     Beli      Harga")
print("----------------------------------------------")
for i in range(banyak_jenis):
    print(f"{i+1}.  {jenis_potong[i]}      Rp.{harga[i]}    {banyak_potong[i]}         Rp.{jumlah_harga[i]}")
print("----------------------------------------------")
print(f"                     Jumlah Bayar : Rp.{total_harga}")
print(f"                     Pajak 10%    : Rp.{pajak}")
print(f"\033[1m                     Total Bayar  : Rp.{total_bayar}\n\033[0m")