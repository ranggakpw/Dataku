data =  [{'mahasiswa': 'kiki', 'lulus': 2017, 'judul': 'Rancangan bangun sistem monitoring',  'prodi' : 'informatika'},
         {'mahasiswa': 'yogi', 'lulus': 2018, 'judul': 'Pengolahan data sensor suara',  'prodi' : 'informatika'}]

def cari(data, kriteria):
    return data['mahasiswa'] in kriteria ['mahasiswa'] \
    and data['lulus'] in kriteria['lulus'] \
    and data['judul'] in kriteria['judul'] \
    and data['prodi'] in kriteria['prodi']
  
def tampil(key,value):
    if value == True:
        print(key,value)

substring = {'mahasiswa': ['kiki','yogi'], 'lulus': list(range(2000, 3001)), 'judul': ['Rancangan bangun sistem monitoring'],  'prodi': ['informatika']}

x = list(map(cari, data, [substring]*len(data)))
list(map(tampil,data,x))