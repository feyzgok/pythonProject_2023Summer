liste=[1,2,3,4,5]

for i in liste:#iterable objede dolaşmak için iterator oluşturulmalı
    print(i)
    #for döngüsü bu iterator oluşturma işlemini bizim için yapıyor

iterator=iter(liste)

print(next(iterator))#elemanlar teker teker gezilecek
print(next(iterator))
print(next(iterator))
print(next(iterator))

iterator=iter(liste)

while True:
    try:
        element=next(iterator)
        print(element)
    except StopIteration:
        break

#list gibi bir objeyi kendimiz oluşturmak ve iterator kullanmak isteyebiliriz
class MyNumbers:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start<=self.stop:#stop dahil-stop'da dur
            x=self.start
            self.start+=1
            return x
        else:
            raise StopIteration


list=MyNumbers(30,50)
myiter=iter(list)#iterator oluşturma

while True:
    try:
        element=next(myiter)
        print(element)

    except StopIteration:
        break

#ireation->bir nesnenin elemanlarını adımlamak
sayilar=[1,2,3]
i_sayilar=sayilar.__iter__()
print(type(i_sayilar))
#ya da
i_sayilar=iter(sayilar)

print(i_sayilar.__next__())
print(next(i_sayilar))

while True:
    try:
        sayi=next(i_sayilar)
        print(sayi)

    except StopIteration:
        break

class New_Range:
    def __init__(self,start,end):
        self.yazilacak=start
        self.end=end

#iter metot:
    def __iter__(self):
        return self #kendini geri döndürecek ama kendisinde next metotu olmalı

    def __next__(self):
        if self.yazilacak>=self.end:
            raise StopIteration
        deger=self.yazilacak#eğer deger döndürülmese ilk elemanın çıktısı alınamaz
        self.yazilacak+=1
        return deger

sayilar=New_Range(10,20)
for i in sayilar:
    print(i)