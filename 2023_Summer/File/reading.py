try:
    file=open("newfile.txt")
    print('dosya açıldı')
except FileNotFoundError:
    print("dosya okuma hatası")
finally:
    print('dosya kapandı')

file=open('newfile.txt','r',encoding='utf-8')

for i in file:
    print(i,end="")#dosyadakilerin çıktısını verir
#eğer tekrardan oku denirse imleç kalan yerden yani dosyanın sonundan devam edecektir
#ÇÖZÜM:dosyayı kapatmak ve tekrar açmak
file.close()

file=open('newfile.txt','r',encoding='utf-8')
content=file.read()
print(content)#diğer yöntem:okunulan içeriği yazdırmak
file.close()

file=open('newfile.txt','r',encoding='utf-8')
integer=file.readline()
#print(int(integer)) normal
print(int(integer))
#print integer dersek content çıktısını almadan önce bir satır boş-bu yüzden content.read fonksiyonunda int(integer) şeklinde kullanıldı
print(integer)
content=file.read(int(integer))#kaç karakter okunacağını seçebilirsin
print(content)
file.close()

#??? integer neden satır+boş line çünkü o satır aslında sadece 3'ten oluşmuyor
#her satırın orijinal halinde /n eklentisi var