myList=[1,2,3]
myString='my string'

print(len(myList))
print(len(myString))

print(type(myList))
print(type(myString))
#python len ve type metotları daha önceden tanımlanmış metotlardır

class Movie():
    def __init__(self,title='123',director='austin',duration=10):
        self.title=title
        self.director=director
        self.duration=duration
        print('the movie object is created by constructor (or init method)')

    def __str__(self):
        return f'{self.title}-> str'

    def __len__(self):
        return 1000

    def __del__(self):
        print(f'obje silindi')#print yazılmalı

m=Movie()#init metotu çalıştırıldı
print(str(myList))#yani aslında str dediğimizde __str__ metodu çalıştırılıyor
print(str(m))#artık movie için özel str metodunu yazdık

print(len(m))#diğer örnek

del m

