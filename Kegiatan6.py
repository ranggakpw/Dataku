#membuat dictionary
biodata1 = {'Nama': 'Rangga',   'Matkul': 'Web',        'Nim': 230, 'Semester': 1, 'IPK': 3.5}
biodata2 = {'Nama': 'Abi',      'Matkul': 'Fungsional', 'Nim': 233, 'Semester': 2, 'IPK': 3.7}
biodata3 = {'Nama': 'Farid',    'Matkul': 'PBO',        'Nim': 227, 'Semester': 3, 'IPK': 3.8}
biodata4 = {'Nama': 'Rifal',    'Matkul': 'Mobile',     'Nim': 219, 'Semester': 1, 'IPK': 3.9}
biodata5 = {}
temp = ('Nama','Matkul','Nim','Semester', 'IPK');
biodataBaru = {'JenisKelamin' : 'pria' }
 
#menghapus semua item dictionary biodata1
biodata1.clear()
print("Jumlah setelah dihapus : %d" % len(biodata1))
print("---------------------------------------------")
#meng-copy dictionary biodata4 ke biodata1
biodata1 = biodata4.copy()
print ("biodata1 : %s" % str(biodata1))
print("---------------------------------------------")
#mengembalikan nilai dari key
print ("Value : %s" % biodata2.get('Semester'))
print("---------------------------------------------")
#merubah item menjadi list
print ("Value : %s" % biodata2.items())
print("---------------------------------------------")
#menampilkan semua key
print ("Key : %s" % biodata3.keys())
print("---------------------------------------------")
#menambah item dengan default value
print ("Item baru : %s" % biodata4.setdefault('Nilai', 40))
print("---------------------------------------------")
#mengupdate dictionary
biodata4.update(biodataBaru)
print ("Update biodata4 : %s" % biodata4)
print("---------------------------------------------")
#menampilkan semua value dari dictionary
print ("Semua value : %s" % biodata4.values())
print("---------------------------------------------")
#membuat dictionary baru dari temp
biodata5 = biodata5.fromkeys(temp)
print ("New Dictionary biodata5 : %s" % str(biodata5))

biodata5.update(biodataBaru)
print ("Update biodata5 : %s" % biodata5)

biodataup = {'Nama': 'Rangga'}
biodata5.update(biodataup)
print ("Item baru : %s" % biodata5.setdefault('Nilai', 40))
print ("Item baru : %s" % biodata5.setdefault('JenisKelamin', 'Wanita'))
print("---------------------------------------------")
print(biodata5)