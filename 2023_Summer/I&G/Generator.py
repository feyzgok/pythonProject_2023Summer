#bellekte yer işgal etmeyen iterator üretiyor
def cube():
    result=[]

    for i in range(5):#range büyüdükçe bellek üzerinde yer kaplanacak
        result.append(i**3)
    return result
print(cube())

def cube():
    for i in range(5):
        yield i**3#yield is a special key word which will make your generator as generator
        #yield is a generator which will give you an iterator
generator=cube()
iterator=iter(generator)
print(next(iterator))

for i in cube():
    print(i)

generator=(i**3 for i in range(5))
print(generator)

def topten():
    yield 1
    yield 2
    yield 3
    yield 4

values=topten()

print(values.__next__())#nextini almadığın sürece next'in çıktısını vermez kaç kere yield yazarsan yaz
#sürekli print yazmak yerine for loop kullnabilirsin

for i in values:
    print(i)

def topten2():
    n=1
    while(n<=10):
        s1=n*n
        yield s1
        n+=1

values=topten2()

for i in values:
    print(i)