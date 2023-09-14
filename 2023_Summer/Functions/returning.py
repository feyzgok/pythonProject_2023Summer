def usalma(number):
    def inner(power):
        return number**power
    return inner

two=usalma(2)
print(two(3))


#üs alma fonksiyonuna bir değer gönderildi
#inner fonksiyonunu usalma fonksiyonunda direk çalıştırılmıyor onun yerine
#geriye fonksiyon döndürüp değişkene atadık
#referansına bir sayı gönderip çıktı olarak alıyoruz
#böylece içindeki fonksiyon çalıştırıldı

def yetki_sorgula(page):
    def inner(role):
        if role== ('Admin'):
            return '{0} rolü {1} sayfasına ulaşabilir.'.format(role,page)
        else:
            return '{0} rolü {1} sayfasına ulaşamaz.'.format(role,page)
    return inner

user0=yetki_sorgula('product edit')
print(user0('Admin'))
print(user0('User'))

def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam+=i
        return toplam

    def carpma (*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim

    if islem_adi=='toplama':
        return toplam
    else:
        return carpma

toplama=islem('toplama')
print(toplama(8,9))