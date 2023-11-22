#no 1
def profil():
    print(nama, alamat, gender, umur, hobby)

nama = "Rafly"
alamat = "Bogor"
gender = "Laki laki"
umur = "18"
hobby = "diam"
profil()

#no 2
def hasil(nilai):
    if nilai <= 60:
     return "gagal"
    elif nilai <= 70:
     return "baik"
    elif nilai <= 80:
     return "sangat baik"
    elif nilai >= 80:
     return "istimewa"

print(hasil (nilai=60))

#no 3
def ganjil(n):
    for i in range(1, n+1, 2):
        print(i)
ganjil(100)