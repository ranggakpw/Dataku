import sys

def Masuk(Nama, Tahun, Judul, Prodi):
    
    return 0

All = {
    'Nama':{},
    'Tahun':{},
    'Judul':{},
    'Prodi':{}
    }

absen = 0
loop = True
while loop == True:
    nama = input("Masukkan nama : ")
    tahun = input("Masukkan Tahun : ")
    Judul = input("Masukkan Judul : ")
    Prodi = input("Masukkan Prodi : ")
    lanjut = input("Apakah ingin memasukkan file lagi? ")
    absen += 1
    if lanjut == 'tidak':
        loop = False
        print(All)