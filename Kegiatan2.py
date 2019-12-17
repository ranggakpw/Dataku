def Masuk(absen, nama, Tahun, Judul, Prodi):
    global All
    All = {0:{'Nama':'a','Tahun':0,'Judul':'asd','Prodi':'dsa'}}
    Temp = {absen:{'Nama':nama,'Tahun':Tahun,'Judul':Judul,'Prodi':Prodi}}
    All.update(Temp)


absen = 1
loop = True
while loop == True:
    nama = input("Masukkan nama : ")
    tahun = input("Masukkan Tahun : ")
    Judul = input("Masukkan Judul : ")
    Prodi = input("Masukkan Prodi : ")
    lanjut = input("Apakah ingin memasukkan file lagi? ")
    absen += 1
    Masuk(absen, nama, tahun, Judul, Prodi)
    if lanjut == 'tidak':
        loop = False

print(All)