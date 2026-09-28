list_nim = []
list_uts = []
list_uas = []
list_total = []

ulang = int(input("Berapa banyak NIM yang ingin di input : "))
for i in range(ulang):
    print("\nData ke - " + str(i+1))
    list_nim.append(input("Masukan Nim anda : "))
    list_uts.append(int(input("Masukan Nilai UTS anda : ")))
    list_uas.append(int(input("Masukan Nilai UAS anda : ")))
for i in range(ulang):
    list_total.append(int(list_uas[i] + list_uts[i]) / 2)

print("==================================================================================")
print("NIM\t\tNilai UTS\t\tNilai UAS\t\tTotal")
print("==================================================================================")
for i in range(ulang):
    print(f"{list_nim[i]}\t{list_uas[i]}\t\t\t{list_uas[i]}\t\t\t{list_total[i]}")
print("==================================================================================")