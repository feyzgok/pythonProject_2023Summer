names= ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years=[1998,2000,1998,1987]

names.append('Cenk')#sona ekleme
names.insert(0,'Sena')#insert konumuna göre ekliyor
names.insert(len(names), "Ceren")
result='Ali'in names
result1=names.index('Ali')#saymaya 1'den başlıyor yani gerçek sırasını söylüyor
print(result)
print(result1)