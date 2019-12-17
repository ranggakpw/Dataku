angka = [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

hasil1 = filter(lambda x: x % 2, angka) 
print(list(hasil1)) 

hasil2 = filter(lambda x: x % 2 == 0, angka) 
print(list(hasil2)) 

