gaji_pokok = 300000
lembur = 3500

print("\n========== PROGRAM HITUNG KARYAWAN GAJI ==========")
nama = input(" \nNama karyawan            : ")
golongan_jabatan = int(input("Golongan jabatan(1/2/3)  : "))
pendidikan = input("Pendidikan(SMA/D1/D3/S1) : ")
jumlah_jam_kerja = int(input("Jumlah jam kerja         : "))

if golongan_jabatan == 1:
    tunjangan_jabatan = int((5*gaji_pokok)/100)
elif golongan_jabatan == 2:
    tunjangan_jabatan = int((10*gaji_pokok)/100)
elif golongan_jabatan == 3:
    tunjangan_jabatan = int((15*gaji_pokok)/100)
else:
    tunjangan_jabatan = 0
    
if pendidikan == "SMA":
    tunjangan_pendidikan = int((2.5*gaji_pokok)/100)
elif pendidikan == "D1":
    tunjangan_pendidikan = int((5*gaji_pokok)/100)
elif pendidikan == "D3":
    tunjangan_pendidikan = int((20*gaji_pokok)/100)
elif pendidikan == "S1":
    tunjangan_pendidikan = int((30*gaji_pokok)/100)
else:
    tunjangan_pendidikan = 0
    
if jumlah_jam_kerja <= 8 :
    honor_lembur = 0
elif jumlah_jam_kerja == jumlah_jam_kerja:
    honor_lembur = (jumlah_jam_kerja-8)*lembur
else:
    honor_lembur = 0    
    
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur
print("====================================================")
print("Karyawan yang bernama : " +str(nama).capitalize())
print("Honor yang diterima")
print(f"     Gaji pokok           : Rp.{gaji_pokok}")
print(f"     Tunjangan jabatan    : Rp.{tunjangan_jabatan}")
print(f"     Tunjangan pendidikan : RP.{tunjangan_pendidikan}")
print(f"     Honor lembur         : Rp.{honor_lembur}")
print(f"Total Gaji : Rp.{total_gaji}\n")