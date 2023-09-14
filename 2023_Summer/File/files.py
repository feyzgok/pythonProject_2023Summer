"""dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
Kullanımı:open(dosya_adi, dosya_erişme_modu)

dosya erişme modu:dosyayı hangi amaçla açtığını belirtir:
 w (Write) yazma modu->dosyayı konumda oluşturur-eski verileri silinir
 a (Append) ekleme modu-> dosya yoksa oluşturur-eski verileri kalır
 x (Create) oluşturma modu-> dosya zaten varsa hata verir sadece başlangıçta kullanılabilinir
 r (Read) okuma modu-> dosya yoksa okuyamaz ve hata verir (default)"""

file=open("newfile.txt","a") #w dersek eski yazılanlar silinir, a dersek eski yazılanlar orada kalır
file1=open("C:/Users/feyza/OneDrive/Masaüstü/newfile.txt","a")
file.write('feyzgok')
file1.write('gok')
file.close()
file1.close()

with open("newfile.txt","r+",encoding="utf-8") as file: #güncelleme
    file.seek(20)
    file.write("\n miraabaa")#alttakini siliyor kendini yazıyor
#alttaki içeriği koruyarak başa içerik yazmak için seek yapıp dosyayı okuyup sonra kalan tarafı content içerisine kaydedip
#yine seek'le yazı yazılmak istenilen konuma gelip oraya yazdırıp content'i de ekstra yazdırmak gerekiyor (zaten alttakini silip üstüne yazddığı için bir daha dosyanın devamını silip dosyanın sonundan itibaren contenti yazdırmak anlamsız olacaktır

with open("newfile.txt","r+",encoding='utf-8') as file:
    file.seek(22)
    content=file.read()
    file.seek(22)
    file.write(f'mirhaba{content}')#content='mirabaa'+content de denilebilinir

#liste yöntemiyle dosya güncelleme
with open("newfile.txt",'r+',encoding='utf-8') as file:
    list=file.readlines()
    list.insert(1,'c')
    file.seek(0)
    file.writelines(list)