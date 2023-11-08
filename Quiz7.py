#1
a = input("masukan nama kendaraan?")
b =input("masukan jenis bensin?")
c =input("masukan kota?")


if b == 'pertalite':
 harga = 10000
 jartem = 12
elif b == 'pertamax':
 harga = 14000
 jartem = 13
elif b == 'pertamax turbo':
 harga = 17000
 jartem = 13.5
else :   
 print("tidak diketahui")

if c == 'jakarta':
 jarak = 20
elif c == 'bekasi':
 jarak = 35.7
elif c == 'depok':
 jarak = 5
elif c == 'tanggerang':
 jarak = 99
elif c == 'bogor':
 jarak = 120.6
else:
 print("tidak diketahui")

d = jarak/jartem
e = d*harga

print("\nNama kendaraan:", a,"\nJenis Bensin:", b,"\nKota tujuan:", c,"\nPemakaian bensin:", d,"\nTotal harga dari bensin:", e)

#2
a = input("masukan nama pembeli?")
b =input("masukan no hp pembeli?")
c =input("pesan menu apa?")