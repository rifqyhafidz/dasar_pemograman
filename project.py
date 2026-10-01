while True:
    print("\n\033[1m                 NASI GORENG       ")
    print("                    SIGMA            \033[0m")
    print("|==========================================|")
    print("|                DAFTAR MENU               |")
    print("|==========================================|")
    print("| Kode.        jenis                Harga  |")
    print("|------------------------------------------|")
    print("| 1.   Nasi Goreng ayam bakso    Rp.15.000 |")
    print("| 2.   Nasi Goreng pete          Rp.16.000 |")
    print("| 3.   Nasi Goreng ati ampela    Rp.17.000 |")
    print("| 4.   Nasi Goreng asin cumi     Rp.21.000 |")
    print("| 5.   Nasi Goreng spesial       Rp.23.000 |")
    print("| 6.   Mie Goreng biasa          Rp.15.000 |")
    print("| 7.   Mie Goreng seafood        Rp.20.000 |")
    print("| 8.   Mie Goreng spesial        Rp.23.000 |")
    print("| 9.   Kwetiau goreng biasa      Rp.15.000 |")
    print("| 10.  Kwetiau goreng sosis      Rp.17.000 |")
    print("|==========================================|")
    print("Note : Setiap transaksi akan dikenakan pajak sebesar 5%\n")

    banyak_jenis = int(input("Berapa jenis yang ingin dibeli : "))

    kode = []
    harga = []
    banyak_beli = []
    jenis_makanan = []
    sub_total = []
    jumlah_harga = []

    for i in range(banyak_jenis):
        jenis = print(f"\nJenis Ke-{i+1}") 
        kode = int(input("Kode menu : "))
        banyak_beli.append(int(input(f"Banyak beli: ")))

        if kode == 1:
            harga.append(15000)
            jenis_makanan.append("Nasi Goreng ayam bakso")
        elif kode == 2:
            harga.append(16000)
            jenis_makanan.append("Nasi Goreng pete")
        elif kode == 3:
            harga.append(17000)
            jenis_makanan.append("Nasi Goreng ati ampela")
        elif kode == 4:
            harga.append(21000)
            jenis_makanan.append("Nasi Goreng asin cumi")
        elif kode == 5:
            harga.append(23000)
            jenis_makanan.append("Nasi Goreng spesial")
        elif kode == 6:
            harga.append(15000)
            jenis_makanan.append("Mie Goreng biasa")
        elif kode == 7:
            harga.append(20000)
            jenis_makanan.append("Mie Goreng seafood")
        elif kode == 8:
            harga.append(23000)
            jenis_makanan.append("Mie Goreng spesial")
        elif kode == 9:
            harga.append(15000)
            jenis_makanan.append("Kwetiau goreng biasa")
        elif kode == 10:
            harga.append(17000)
            jenis_makanan.append("Kwetiau goreng sosis")
        else:
            print("Harap masukan kode yang tersedia di menu")
            exit()
        

    sub_total = 0
    for i in range(banyak_jenis):
        jumlah_harga.append(harga[i] * banyak_beli[i])    
        sub_total += harga[i] * banyak_beli[i] 
        
    pajak = int(sub_total * 0.05)
    total_bayar = int(sub_total + pajak)

    print(f"\nTotal bayar Rp.{total_bayar}")
    uang_pembeli = (input("Masukan uang anda : "))
    while uang_pembeli == "":
        print("_____________________________")
        print("harap masukan uang anda")
        uang_pembeli = (input("Masukan uang anda : ")) 
    while int(uang_pembeli) <= total_bayar:
        print("_____________________________")
        print("Uang anda tidak cukup")
        uang_pembeli = (input("Masukan uang anda : "))
        while uang_pembeli == "":
            print("_____________________________")
            print("harap masukan uang anda")
            uang_pembeli = (input("Masukan uang anda : "))     

    kembalian = int(uang_pembeli) - total_bayar   

    if int(uang_pembeli) >= total_bayar:
        print()
        print("                                STRUK PEMBELIAN                       ")
        print("=============================================================================")
        print(" No.\tJenis\t\t\tHarga Satuan\tBanyak beli\tJumlah harga")
        print("-----------------------------------------------------------------------------")
        for i in range(banyak_jenis):
            print(f" {i+1}.\t{jenis_makanan[i]}\tRp.{harga[i]}\t{banyak_beli[i]}\t\tRp.{jumlah_harga[i]}")
        print("-----------------------------------------------------------------------------")
        print(f"\t\t\t\t\t\t Sub Total    : Rp.{sub_total}")
        print(f"\t\t\t\t\t\t pajak 5%     : Rp.{pajak}")
        print(f"\t\t\t\t\t\t Total bayar  : Rp.{total_bayar}")
        print(f"\t\t\t\t\t\t Uang Anda    : Rp.{uang_pembeli}")
        print(f"\t\t\t\t\t\t Kembalian    : Rp.{kembalian}")
        print("=============================================================================")
    pilihan = input("Apakah anda ingin membeli lagi? (y/n): ")    
    if pilihan == "n":
        print("\nTerimakasih sudah membeli makanan kami")
        exit()

        


