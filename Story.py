#Judul = "Hikayat Kancil"
import random
import time
import os,sys
import xlrd
from functools import partial
import functools 
import xlrd

def clear_screen(): 
    os.system('cls' if os.name=='nt' else 'clear')

def title():
     print ("===========================================================")
     print ("============= Kisah Si Kancil Pencuri Timun ===============")
     print ("===========================================================")

def north():
    print ("tekan n untuk pergi ke hutan")
def east():
    print ("tekan e untuk pergi ke sungai")
def south():
    print ("tekan s untuk pergi ke jalan raya")
def west():
    print ("tekan w untuk pergi ke gurun")


def setup():

    global name
    global HP
    global MP
   
    name = input("Siapa nama kancilnya? ")
    
    HP = random.randint(35,50)
    MP = random.randint(5,20)

weapons = []
weapons.append("Sword")
weapons.append("Knife")
weapons.append("Tongkat Baseball")
weapons.append("Tangan Kosong")
weapons.append("Kayu")
weapons.append("Batu")

def status():
    print ("Sedang Mengecek Status si Kancil, " + name)
    time.sleep(2)
    print ("si Kancil, "+name + " masih punya " + " " + str(HP) + " " + "Total Darah")
   
def lastenemy():
    global enemyHP
    global enemyMP
    global lastenm
    enemyHP = random.randint(5,10) 
    enemyMP = random.randint(5,10)
   
    lastenm = "Anjing"
    print ("Sedang Mengecek Status si "+lastenm)
    time.sleep(2)
    print (lastenm +"nya punya " + " " + str(enemyHP) + " " + "Total Darah")
    print (lastenm +"nya punya " + " " + str(enemyMP) + " " + "Total Stamina")

def lastboss():
    global enemyHP
    global enemyMP
    global lastb
    enemyHP = random.randint(5,10) 
    enemyMP = random.randint(5,10)
   
    lastb = "Cave Man"
    print ("Sedang Mengecek Status si "+lastb)
    time.sleep(2)
    print (lastb +"nya punya " + " " + str(enemyHP) + " " + "Total Darah")
    print (lastb +"nya punya " + " " + str(enemyMP) + " " + "Total Stamina")

def enemy():
    global enemyHP
    global enemyMP
    global enemyname
    enemyHP = random.randint(5,20)
    enemyMP = random.randint(5,20)
   
    enemyname = "Buaya"
    print ("\nDatang Seekor Hewan "+enemyname+" Datang Ingin Memakanmu....")
    time.sleep(2)
    print ("Sedang Mengecek Status si "+enemyname)
    time.sleep(2)
    print (enemyname +"nya punya " + " " + str(enemyHP) + " " + "Total Darah")
    print (enemyname +"nya punya " + " " + str(enemyMP) + " " + "Total Stamina")
    
def enemy2():
    global enemyHP
    global enemyMP
    global enemyname2
    enemyHP = random.randint(5,20)
    enemyMP = random.randint(5,20)
   
    enemyname2 = "Robot"
    print ("\nDatang Sebuah "+enemyname2+" Datang Ingin Menghancurkanmu....")
    time.sleep(2)
    print ("Sedang Mengecek Status si "+enemyname2)
    time.sleep(2)
    print (enemyname2 + "nya punya " + " " + str(enemyHP) + " " + "Total Darah")
    print (enemyname2 + "nya punya " + " " + str(enemyMP) + " " + "Total Stamina")

def enemy3():
    global enemyHP
    global enemyMP
    global enemyname3
    enemyHP = random.randint(5,20)
    enemyMP = random.randint(5,20)
   
    enemyname3 = "Kala njengking"
    print ("\nDatang Seekor "+enemyname3+" Datang Ingin Memakanmu....")
    time.sleep(2)
    print ("Sedang Mengecek Status si "+enemyname3)
    time.sleep(2)
    print (enemyname3 + "nya punya " + " " + str(enemyHP) + " " + "Total Darah")
    print (enemyname3 + "nya punya " + " " + str(enemyMP) + " " + "Total Stamina")

def multiply(x,y):
        return x * y

def mapper(n): 
    return n * n * n

def search():
    txt = "abcdefghijklmnopqrstuvwxyz"
    x = txt.find("n")
    print(x)

def decor():
    def gchat():
        print("Si Kancil Sudah Selesai Mendata")
        time.sleep(2)
        print("Hasilnya Adalah : ")
        time.sleep(2)
    print("Si Kancil Sedang Mendata Timun Di Kebun")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("...")
    time.sleep(2)
    gchat()

def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False
def create_adder(x): 
    def adder(y): 
        return x+y 
    return adder 

def add_5():
    five = 5
    def add(arg): 
        return arg * five
    return add

def reduceall():
    lis = [ 11 , 33, 59, 62, 24 ] 
    print ("Angka Paling Besar Adalah : ",end="") 
    print (functools.reduce(lambda a,b : a if a > b else b,lis)) 

def death():
    print ("\nYah, Si Kancil, "+name+" Mati" )
    time.sleep(2)
    print ("Game Over")
    time.sleep(2)
    sys.exit(0)

def countdown(angka):
    if angka > 0 :
        print (angka)
        angka = angka - 1
        countdown(angka)
    else :
        print(angka)

def farmer():
    global npcname
    global responses
    responses = ["Sedang apa kamu disini?", "Mau ngapain?", "Ada yang bisa saya bantu?", "Ada Apa ya?"]
    npcname = "Pak Tani"
    print ("\n["+npcname+":] Halo, Aku"+npcname+", Apakah kamu mau bicara dengan ku?(y/n)")
    
    random.shuffle(responses)
    if input() == "y":
        print ("["+npcname+":] " +responses[0])
        time.sleep(2)
        list_answer = ["Saya mau mencuri timun", "Bolehkan saya mencuri timun?" , "Saya numpang lewat saja" , "Apa urusan anda menanyakan hal itu?"]
        print("0. Saya mau mencuri timun")
        print("1. Bolehkan saya mencuri timun?")
        print("2. Saya numpang lewat saja")
        print("3. Apa urusan anda menanyakan hal itu?")
        answer = input("Respon?[(0,1,2,3)/n]")
        if answer == '0':
            print (list_answer[0])
            time.sleep(2)
            print ("["+npcname+":] Hmm, beraninya kamu")
            time.sleep(2)
            print ("DOORR")
            print ("========== - - - >")
            print ("| )")
            print ("--")
            death()
        elif answer == '1':
            print (list_answer[1])
            time.sleep(2)
            print ("["+npcname+":] Hmm.....")
            time.sleep(2)
            print ("["+npcname+":] Boleh,")
            time.sleep(2)
            print ("["+npcname+":] Hanya dengan satu syarat!!!")
            time.sleep(2)
            resp = input("Terima tantangan? (y/n) : ")
            if resp == 'y':
                laststory()
            else :
                print("["+npcname+":] Kalau Begitu Silahkan Pergi!!!")
                time.sleep(2)
                print ("Si Kancil Tidak Memilih Untuk Mencuri Timun, Karena Takut Sama Pak Tani.")
                time.sleep(2)
                print ("Game Over")
                time.sleep(2)
                sys.exit(0)
        elif answer == '2':
            print (list_answer[2])
            time.sleep(2)
            print ("["+npcname+":] Owh, Oke silahkan lewat")
            time.sleep(2)
            print (".")
            time.sleep(2)
            print (".")
            time.sleep(2)
            print (".")
            time.sleep(2)
            print ("Yasudah, si kancil cuma lewat kan :v")
            time.sleep(2)
            sys.exit(0)
        elif answer == '3':
            print (list_answer[3])
            time.sleep(2)
            print ("["+npcname+":] Hmm, beraninya kamu")
            time.sleep(2)
            print ("DOORR")
            print ("========== - - - >")
            print ("| )")
            print ("--")
            death()
        time.sleep(2)

def caveman():
    global cavename
    global caveresponses
    caveresponses = ["Sedang apa kamu disini?", "Mau ngapain?", "Ada yang bisa saya bantu?", "Ada Apa ya?"]
    cavename = "Penghuni Goa"
    print ("\n["+cavename+":] Halo, Aku "+cavename+", Ada perlu apa kamu kemari?(y/n)")
    
    random.shuffle(responses)
    if input() == "y":
        print ("["+cavename+":] " +caveresponses[0])
        time.sleep(2)
        list_answer = ["Biarkan saya mengambil harta itu", "Saya ingin mencuri harta karun itu" , "Di situ ada harta karun, boleh saya ambil?" , "gpp, saya mau lewat saja buat ambil harta"]
        print("0. Biarkan saya mengambil harta itu")
        print("1. Saya ingin mencuri harta karun itu")
        print("2. Di situ ada harta karun, boleh saya ambil?")
        print("3. gpp, saya mau lewat saja buat ambil harta")
        answer = input("Respon?[(0,1,2,3)/n]")
        if answer == '0':
            print (list_answer[0])
        elif answer == '1':
            print (list_answer[1])
        elif answer == '2':
            print (list_answer[2])
        elif answer == '3':
            print (list_answer[3])
        time.sleep(2)
        print("["+cavename+":] "+"Wah, berani sekali anda!")
        time.sleep(2)
        print("["+cavename+":] "+"Hadapi saya dulu dong!")
        time.sleep(2)
        print("["+cavename+":] "+"Aku akan memberikan beberapa QUIZ")
        time.sleep(2)
        ansquiz = input("Terima tantangan Quiz? (y/else) : ")
        if ansquiz == 'y':
            print("["+cavename+":] "+"Baiklah kalau begitu, kita mulai saja!!")
        else:
            print("["+cavename+":] Kalau Begitu Silahkan Pergi!!!")
            time.sleep(2)
            print ("Si Kancil Tidak Memilih Untuk Mencuri Timun, Karena Takut gak lulus.")
            time.sleep(2)
            print ("Game Over")
            time.sleep(2)
            sys.exit(0)
    else:
        print("["+npcname+":] Kalau Begitu Silahkan Pergi!!!")
        time.sleep(2)
        print ("Si Kancil Tidak Memilih Untuk Mencuri Timun, Karena Takut Sama Pak Tani.")
        time.sleep(2)
        print ("Game Over")
        time.sleep(2)
        sys.exit(0)
    
       
def finalchapter():
    global farmer
    farmer = "Pak Tani"
    print("["+farmer+":] "+"Hebat, Hebat sekali")
    time.sleep(2)
    print("["+farmer+":] "+"Terima Kasih Banyak "+name+" Kancil ")
    time.sleep(2)
    print("["+farmer+":] "+"Sekarang kamu boleh mengambil timun itu")
    time.sleep(2)
    finalans = input("["+farmer+":] "+"tapi sebelum itu, maukah kamu membantuku? (y/else)")
    if finalans == 'y':
        print("["+farmer+":] "+"Terima kasih")
        time.sleep(2)
        print("["+farmer+":] "+"Bantulah aku untuk mendata semua hasil panen ku!")
        time.sleep(2)
    else:
        print ("Si Kancil"+ name + "Memilih untuk menolak menolong, dan langsung mencuri timun tersebut" )
        time.sleep(2)
        print ("Si Kancil pulang kerumah membawa timun")
        time.sleep(2)
        print ("Hanya saja si kancil sadar telah berbuat jahat sebelumnya")
        time.sleep(2)
        print ("si kancil merenungi di rumahnya")
        time.sleep(2)
        print ("BAD ENDING")
        time.sleep(2)
        sys.exit(0)

def goals():
    global farmer
    farmer = "Pak Tani"
    print("["+farmer+":] "+"Terima Kasih Banyak "+name+" Kancil ")
    time.sleep(2)
    print("["+farmer+":] "+"Sekarang kamu boleh mengambil timun itu")
    time.sleep(2)
    goalans = input("Apakah kamu ingin mengambil timun? (y/else)")
    if goalans == 'y':
        timuns = [['Busuk', 'Segar', 'Hijau','Panjang', 'Expo', 'Roman','Jubi', 'Monroe', 'Mawi']] 
        dat_timuns = [] 
        for sublist in timuns: 
            for timun in sublist:        
                if len(timun) < 5: 
                    dat_timuns.append(timun)
        print("Dari sekian timun yang ada yaitu", timuns)     
        time.sleep(2)   
        print("Si kancil hanya ingin mengambil timun jenis",dat_timuns) 
    else:
        print ("Si Kancil"+ name + "Berubah pikiran" )
        time.sleep(2)
        print ("Si Kancil pulang kerumah dengan tidak membawa timun")
        time.sleep(2)
        print ("Si kancil hanya ingin berpetualang saja")
        time.sleep(2)
        print ("si kancil merenungi di rumahnya")
        time.sleep(2)
        print ("BAD ENDING")
        time.sleep(2)
        sys.exit(0)

def gending():
    print ("Si Kancil "+name+" Berhasil Membawa Pulang Timun Pak Tani" )
    time.sleep(2)
    print ("Setelah Sekian Lama Perjuangannya")
    time.sleep(2)
    print ("Akhirnya Si Kancil Bisa Kembali Dengan Sangat Gembira")
    time.sleep(2)
    print ("Di Rumah Nya, Si Kancil Menikmati Timun Yang Berhasil Di Dapatnya")
    time.sleep(2)
    print ("YUMMMM ENAAK")
    time.sleep(2)
    print ("GOOD ENDING")
    time.sleep(2)

def credit():
    time.sleep(2)
    print("============================================================================")
    print("============================= CREDITS ======================================")
    print("============================================================================")
    time.sleep(2)
    print("Story By: ")
    print("1. Abi Maulana ")
    print("2. Afwun Shiddiq ")
    print("3. Farid Abimanyu ")
    time.sleep(2)
    print("Programmer Team By: ")
    print("1. Rangga Kurnia ")
    print("2. M Adityo Abiyoga ")
    time.sleep(2)
    print("=======================================================================================")
    print("============================= THANKS FOR PLAYING ======================================")
    print("=======================================================================================")


def quiz():
    print("Jawablah soal soal berikut ini!")
    time.sleep(1)
    countdown(5)
    print("Pertanyaan Pertama!")
    time.sleep(1)
    print("3 + 5 + 6 = ?")
    quizans = input("Jawaban = ?")
    if quizans == '14':
        print("Jawaban anda benar")
    else:
        print("Jawaban anda salah")
        time.sleep(2)
        print("hasilnya adalah = "+search())
        time.sleep(2)
        print ("Penghuni gua langsung membunuhmu")
        time.sleep(2)
        death()

    print("Pertanyaan Kedua!")
    time.sleep(1)
    print("Sebutkan huruf vocal dari kata INFORMATIKA = ?")
    quizans2 = input("Huruf Pertama? = ")
    if quizans2 == 'i':
        ans21 = input("Huruf Kedua? = ")
        if ans21 == 'o':
            ans22 = input("Huruf Ketiga? = ")
            if ans22 == 'a':
                print("Jawaban anda benar")
            else:
                print("Jawaban anda salah")
                time.sleep(2)
                print("hasilnya adalah = ")
                sequence = ['a','i','o'] 
                filtered = filter(fun, sequence) 
                for s in filtered: 
                    print(s) 
                time.sleep(2)
                print ("Penghuni gua langsung membunuhmu")
                time.sleep(2)
                death()
        else:
            print("Jawaban anda salah")
            time.sleep(2)
            print("hasilnya adalah = ")
            sequence = ['a','i','o'] 
            filtered = filter(fun, sequence) 
            for s in filtered: 
                print(s) 
            time.sleep(2)
            print ("Penghuni gua langsung membunuhmu")
            time.sleep(2)
            death()
    else:
        print("Jawaban anda salah")
        time.sleep(2)
        print("hasilnya adalah = ")
        sequence = ['a','i','o'] 
        filtered = filter(fun, sequence) 
        for s in filtered: 
            print(s) 
        time.sleep(2)
        print ("Penghuni gua langsung membunuhmu")
        time.sleep(2)
        death()
    
    print("Pertanyaan Ketiga!")
    time.sleep(1)
    print("Hasil dari : ")
    print("1. (2^2) x 4")
    print("2. 3^3 x 9")
    print("Adalah???")
    quizans3 = input("Jawaban Pertama? = ")
    if quizans3 == '16':
        ans31 = input("jawaban Kedua? = ")
        if ans31 == '81':
            print("Jawaban anda Benar")
            time.sleep(2)
        else:
            print("Jawaban anda salah")
            time.sleep(2)
            print("hasilnya adalah = ")
            numbers = (2,3) 
            result = map(mapper, numbers) 
            print(list(result)) 
            time.sleep(2)
            print ("Penghuni gua langsung membunuhmu")
            time.sleep(2)
            death()
    else:
        print("Jawaban anda salah")
        time.sleep(2)
        print("hasilnya adalah = ")
        numbers = (2,3) 
        result = map(mapper, numbers) 
        print(list(result)) 
        time.sleep(2)
        print ("Penghuni gua langsung membunuhmu")
        time.sleep(2)
        death()

    print("Pertanyaan Keempat!")
    time.sleep(1)
    print("11 , 33, 59, 62, 24")
    print("Angka mana yang paling besar nilainya?")
    quizans4 = input("Jawaban? =")
    if quizans4 == '62':
        print("Jawaban anda benar")
    else:
        print("Jawaban anda salah")
        time.sleep(2)
        reduceall()
        time.sleep(2)
        print ("Penghuni gua langsung membunuhmu")
        time.sleep(2)
        death()

    print("Pertanyaan Kelima!")
    time.sleep(1)
    print("Si beruang punya 15 ikan, di kali 10 ")
    print("Berapa ikan si beruang?")
    quizans5 = input("Jawaban =")
    if quizans5 == '25':
        print("Jawaban anda benar")
    else:
        print("Jawaban anda salah")
        time.sleep(2)
        add_15 = create_adder(15) 
        print (add_15(10)) 
        time.sleep(2)
        print ("Penghuni gua langsung membunuhmu")
        time.sleep(2)
        death()
    
    print("Pertanyaan Keenam!")
    time.sleep(1)
    print("lima di kali lima sama dengan? ")
    quizans6 = input("Jawaban =")
    if quizans6 == '25':
        print("Jawaban anda benar")
    else:
        print("Jawaban anda salah")
        time.sleep(2)
        print("Jawabannya adalah = ")
        if __name__ == '__main__':
            closure1 = add_5()
            print(closure1(5))  
        time.sleep(2)
        print ("Penghuni gua langsung membunuhmu")
        time.sleep(2)
        death()
    time.sleep(2)
    
def laststory():
    print("Setelah si kancil, "+name+ " memutuskan untuk menerima tantangan dari pak Tani, ")
    time.sleep(3)
    print("pak Tani menjelaskan, di luar sana terdapat sebuah GUA yang tersimpan harta karun") 
    time.sleep(3)
    print("si kancil di tugas kan untuk mendapatkan harta karun tersebut") 
    time.sleep(3)
    print("karena pak Tani baik hati, dia memberikan si Kacil berupa hadiah") 
    time.sleep(3)
    print("___  ___   ___   ___   ___")
    print("|#|  |#|   |#|   |#|   |#|")
    print(" 1    2     3     4     5 ")     
    print("[Pak Tani:] Silahkan Pilih!! (Hati Hati, ada yang Bad & Good)")
    time.sleep(3)
            

dbl = partial(multiply,2)
print(dbl(random.randint(1,5)))

clear_screen()
title()
setup()
global name
global HP
global MP
global move
global enemyHP
print ("Selamat Datang Kancil Dengan Nama, " + name)

time.sleep(2)

print ("\nTotal Darah Mu" + " " + str(HP))
print ("Total Stamina Mu" + " " + str(MP))
print ("Apakah Kamu Ingin Memulai Perencanaan Untuk Mencuri Timun di Kebun Pak Tani? (y/n)")

if input() == "y":
    print("Pada suatu hari, seperti biasa si kancil sedang bersiap siap memanen timun pak tani")
    time.sleep(3)
    print("Karena kebun petani sangat jauh, maka kancil harus melewati berbagai rintangan") 
    time.sleep(3)
   
   
else:
    print ("Si Kancil Tidak Memilih Untuk Mencuri Timun, Karena Sudah Tobat.")
    time.sleep(2)
    print ("Game Over")
    time.sleep(2)
    sys.exit(0)
	
print ("Jauh di utara sana kamu dapat melihat Hutan, di timur terlihat sungai dan barat terdapat gurun.")
time.sleep(3)

print ("\n")
north()
east()
west()
south()
move = input("Kemana kamu mau pergi? ")
if move == 'n':
    print ("\nKamu telah sampai di Hutan.")
    time.sleep(2)
    print ("\nSi Kancil Mencoba Berjalan Memasuki Hutan.")
    time.sleep(3)
    print ("\nTiba Tiba.")
    time.sleep(2)
    print ("\nDUAAARRRR.")
    time.sleep(1)
    enemy()
elif move == 'e':
     print ("\nKamu telah sampai di Sungai.")
     time.sleep(2)
     print ("\nSi Kancil Mencoba Berjalan Memasuki Sungai.")
     time.sleep(3)
     print ("\nTiba Tiba.")
     time.sleep(2)
     print ("\nDUAAARRRR.")
     time.sleep(1)
     enemy()
elif move == 's':
     print ("\nKamu telah sampai di Jalan Raya.")
     time.sleep(2)
     print ("\nSi Kancil Mencoba Berjalan Memasuki Jalan Raya.")
     time.sleep(3)
     print ("\nTiba Tiba.")
     time.sleep(2)
     print ("\nDUAAARRRR.")
     time.sleep(1)
     enemy2()
elif move == 'w':
     print ("\nKamu telah sampai di Gurun.")
     time.sleep(2)
     print ("\nSi Kancil Mencoba Berjalan Memasuki Gurun.")
     time.sleep(3)
     print ("\nTiba Tiba.")
     time.sleep(2)
     print ("\nDUAAARRRR.")
     time.sleep(1)
     enemy3()
    
time.sleep(3)

fight = input("Apa kamu ingin bertarung?(y/n)" )
weapons = ['Pedang', 'Tongkat Baseball', 'Pisau', 'Tangan Kosong', 'Kayu', 'Batu']
if fight == "y":
    print(weapons)
    weap = input("Senjata apa yang ingin kamu gunakan?([0,1,2,3,4,5]/n)")
    if weap == '0':
        item = weapons[0]
    elif weap == '1':
        item = weapons[1]
    elif weap == '2':
        item = weapons[2]
    elif weap == '3':
        item = weapons[3]
    elif weap == '4':
        item = weapons[4]
    elif weap == '5':
        item = weapons[5]
    time.sleep(2)
    while enemyHP >= 0:
        enemyhit = random.randint(0,5)
        print ("Giliran Musuhnya Menyerang Mengakibatkan " + str(enemyhit) + " Kerusakan ")
        HP = HP - enemyhit
        print ("Sisa Nyawa Kancil = "+ str(HP))
        time.sleep(2)
        if HP <= 0:
             print ("\nYah, Si Kancil, "+name+" Mati" )
             time.sleep(2)
             print ("Game Over")
             time.sleep(2)
             sys.exit(0)
        else:
             hit = random.randint(0,5)
             print (name + " Si Kancil Menggunakan  "+ item +" Mengakibatkan " + str(hit) + " Kerusakan")
             enemyHP = enemyHP - hit
             print ("Sisa Nyawa Musuh = "+ str(enemyHP))
             time.sleep(2)
    
        
else:
    print ("Si Kancil"+ name + "Memilih untuk melarikan diri, karena merasa lemah dan memilih untuk kembali pulang" )
    time.sleep(2)
    print ("Game Over")
    time.sleep(2)
    sys.exit(0)

print ("HOREE, si Kancil " + name + " Berhasil selamat dari ancaman yang berbahaya")
time.sleep(2)
status()
time.sleep(2)

phase = input("Ingin Melanjutkan Petualangan Ke Rumah Pak Tani?(y/n): ")

if phase == 'y':
    print ("\nSetelah Menelusuri Berbagai Area.")
    time.sleep(2)
    print ("\nTerlihat di Depan Ada Rumah Pak Tani.")
    time.sleep(2)
    print ("\nDirumahnya terdapat banyak sekali Mentimun.")
    time.sleep(2)
    print ("\nSi Kancil, "+name+" tanpa keraguan langsung mendatangi kebun tersebut")
    time.sleep(2)
    print ("\nTetapi")
    time.sleep(2)
    print ("\nKebunnya di jaga Anjing nya pak tani :(")
    time.sleep(2)
    
    sight = input("\nIngin Melawan?(y/n)")
    if sight == 'y':
        lastenemy()
        time.sleep(2)
        while enemyHP > 0:
            enemyhit = random.randint(0,5)
            print ("Giliran Si Anjing Menyerang Mengakibatkan " + str(enemyhit) + " Kerusakan ")
            HP = HP - enemyhit
            print ("Sisa Nyawa Kancil = "+ str(HP))
            time.sleep(2)
            if HP <= 0:
                print ("\nYah, Si Kancil, "+name+" Mati" )
                time.sleep(2)
                print ("Game Over")
                time.sleep(2)
                sys.exit(0)
            else:
               hit = random.randint(0,5)
               print (name + " Si Kancil Menggunakan  "+ item +" Mengakibatkan " + str(hit) + " Kerusakan")
               enemyHP = enemyHP - hit
               print ("Sisa Nyawa Musuh = "+ str(enemyHP))
               time.sleep(2)    
    else:
        print ("Si Kancil"+ name + "Memilih untuk melarikan diri, karena merasa lemah dan memilih untuk kembali pulang" )
        time.sleep(2)
        print ("Game Over")
        time.sleep(2)
        sys.exit(0)
        
else:
    print ("Si Kancil"+ name + " mager dan memilih untuk kembali pulang" )
    time.sleep(2)
    print ("Game Over")
    time.sleep(2)
    sys.exit(0)

print ("HOREE, si Kancil " + name + " Berhasil selamat dari anjing yang berbahaya")
time.sleep(2)
status()
time.sleep(2)

print("\n")
print ("Setelah si "+name+" melawan anjing penjaga kebun pak tani, si kancil pun mencoba mendekati kebunnya")
time.sleep(2)
print ("Dan tiba tiba pak tani pun keluar")
farmer()


choose = input("Enaknya ambil yang mana ya? [(1,2,3,4,5)/n] : ")
if (choose == '1' or choose == '2' or choose == '3' or choose == '4' or choose == '5'):
    box = random.randint(1,5)
    if box == 1:
        HP = HP + 10
        print("Mendapatkan Herbal")
        time.sleep(2)
        print("Nyawa si kancil bertambah 10")
    elif box == 2:
        HP = HP + 20
        print("Mendapatkan Herbal Super")
        time.sleep(2)
        print("Nyawa si kancil bertambah 20")
    elif box == 3:
        HP = HP -5
        print("Mendapatkan Racun")
        time.sleep(2)
        print("Nyawa si kancil Berkurang 5")
    elif box == 4:
        print("Tidak dapet apa apa")
    elif box == 5:
        print("Mendapatkan Ranjau")
        time.sleep(2)
        print("DUUARRR")
        time.sleep(2)
        print("Si Kancil Langsung meledak terkena ranjau")
        time.sleep(2)
        print("Game Over")
        time.sleep(2)
        sys.exit(0)

status()

print("Setelah mendapatkan hadiah dari pak tani, si kancil pun menuju ke gua")
time.sleep(2)
print("Kancil bertemu seorang penjaga gua")
time.sleep(2)
print("Si kancil langsung menemui penjaga gua itu")
time.sleep(2)

caveman()
quiz()

global cavename
cavename = "Penghuni Goa"
print("["+cavename+":] "+"Wah, kamu telah menjawab semuanya dengan benar")
time.sleep(2)
print("["+cavename+":] "+"Aku tetap tidak terima itu")
time.sleep(2)
print("["+cavename+":] "+"Ayo kita bertarung")
time.sleep(2)
print("["+cavename+":] "+"Kalau kamu bisa membunuhku, silahkan ambil hartanya!")
time.sleep(2)
chall = input("Terima tantangan? (y/else) : ")
if chall == 'y':
    lastboss()
    time.sleep(2)
    while enemyHP > 0:
        enemyhit = random.randint(0,5)
        print ("Giliran Si Cave Man Menyerang Mengakibatkan " + str(enemyhit) + " Kerusakan ")
        HP = HP - enemyhit
        print ("Sisa Nyawa Kancil = "+ str(HP))
        time.sleep(2)
        if HP <= 0:
            print ("\nYah, Si Kancil, "+name+" Mati" )
            time.sleep(2)
            print ("Game Over")
            time.sleep(2)
            sys.exit(0)
        else:
            hit = random.randint(0,5)
            print (name + " Si Kancil Menggunakan  "+ item +" Mengakibatkan " + str(hit) + " Kerusakan")
            enemyHP = enemyHP - hit
            print ("Sisa Nyawa Musuh = "+ str(enemyHP))
            time.sleep(2)    
else:
    print ("Si Kancil"+ name + "Memilih untuk melarikan diri, karena merasa lemah dan memilih untuk kembali pulang" )
    time.sleep(2)
    print ("Game Over")
    time.sleep(2)
    sys.exit(0)

time.sleep(2)
print ("HOREE, si Kancil " + name + " Berhasil selamat dari pertarungan melawan Cave Man")
time.sleep(2)
print ("Si kancil langsung mengambil harta karun tersebut")
time.sleep(2)
print ("Dan setelah mendapatkan harta karus itu, si kancil langsung kembali menuju ke kebun pak tani")
time.sleep(2)
print ("Sesampai disana, si kancil memberikan harta tersebut ke pak tani")
time.sleep(2)
print ("Pak tani pun sangat senang menerimanya")

finalchapter()

data = {}

dat_file = xlrd.open_workbook('timun.xlsx')
dat_sheet = dat_file.sheet_by_index(0)
jum_baris = dat_sheet.nrows

for i in range(3, jum_baris) :
    data[dat_sheet.cell_value(rowx=i, colx=1)] = \
            dat_sheet.cell_value(rowx=i, colx=2)

decor()

print(data)

goals()

gending()

credit()



























print ("Ini Adalah Akhir Dari Kisah Si Kancil, TERIMA KASIH TELAH BERMAIN")

