# 1
hasil_akhir = [
{'nama':'Reza', 'nilai':70},
{'nama':'Ciut', 'nilai':63},
{'nama':'Dian', 'nilai':80},
{'nama':'Badu', 'nilai':40}
]

def predikatlulus(data):
    lulus = [mahasiswa['nama']
        for mahasiswa in data
        if mahasiswa ['nilai'] > 65]
    return lulus

hasil = predikatlulus(hasil_akhir)
print('siswa yang lulus :',hasil)

#2
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def list_buah(buah):
    list_terbalik = []
    for i in range(len(buah)-1, -1, -1):
        list_terbalik.append(buah[i])
    return list_terbalik

hasil = list_buah(buah)
print('urutan setelah dibalik :', hasil)

#3
buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

def duplikasi(list_buah):
    list_duplikasi = []
    for buah in list_buah:
        list_duplikasi.append(buah)
        list_duplikasi.append(buah)
    return list_duplikasi

hasil = duplikasi(buah)
print (hasil)

#4
kalimat = "Nurul Fikri"

def konsonan(kalimat):
    huruf = ""

    for i in kalimat:
        if i not in "aiueo":
            huruf += i
    return huruf

hasil = konsonan('Nurul Fikri')
print('huruf konsonan dari kata nurul fikri adalah', hasil)