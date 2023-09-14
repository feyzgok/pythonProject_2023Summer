isim=input("isminiz:")
soyisim=input("soyisminiz:")
yas=int(input("yaşınız:"))
ogr=input("öğrenim durumunuz (ortaöğretim, üniversite vb.):")
if yas>=18 and (ogr=="üniversite" or ogr=="lise"):
    print(f'{isim} {soyisim} ehliyet alabilir')
else:
    print(f'{isim} {soyisim} ehliyet alamaz')