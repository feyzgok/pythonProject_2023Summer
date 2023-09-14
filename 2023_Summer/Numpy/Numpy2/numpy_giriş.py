import random

import numpy as np
#numpy array
#dizi dediğimiz kavram liste kavramıyla benzerdir. Listeler daha esnek koleksiyon yapılarıdır.
#Numpy bilmek pandas ve tensorflow için önemlidir.
myList=[20,30,40]
print(type(myList))
myList=np.array(myList)#listeyi arraye çevirdi
print(type(myList))

matrixList=[[10,20,30],[20,30,40],[30,40,50]]
print(matrixList[1][0])#1. elamanın 0. elemanını getirir
matrixList=np.array(matrixList)
print(matrixList)

#listeleri kolay yoldan oluşturmak için range metodu kullanılırdık
#numpy'ın liste oluşturme metodu arange'dir.

np_array=np.arange(0,10,2)
print(np_array)
print(type(np_array))

#zeros-ones-->float cinsinden oluşturur
print(np.zeros(5))
print(np.ones(5))
print(np.ones((2,3)))#parantezi iki kere açmayı unutma

#linspace metodu-eşit olarak boyutlandırılmış/aralık bırakılmış şkeilde dizi oluşturur
print(np.linspace(0,20,19))#1. eleman==1. sayı-2. eleman==2. sayı

print(np.arange(1,101))
print(np.linspace(1,100,100))

#eye-indentity matrix oluşturur

#numpy dizi metodları
myNumpyArray=np.arange(30)
myNumpyArray=myNumpyArray.reshape(5,6)
print(myNumpyArray)

myRandArray=np.random.randint(0,100,20)
print(myRandArray.max())