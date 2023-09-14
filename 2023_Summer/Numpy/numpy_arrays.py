import numpy as np

#result=np.array([1,3,5,7,9])
#result=np.arrange(1,10)
#result=np.arrange(10,100,3)
#result=np.zeros(10)
#result=np.ones(10)#float
#result=np.linspace(0,100,5)
#result=np.linspace(0,5,5)
#result=np.random.randint(0,10)#en fazla üretilen sayı 9
#result=np.random.randint(20)
#result=np.random.randint(1,10,3)
#result=np.random.rand(5)
#result=np.random.randn(5)#negatif değerler de dahil edilir
#result=np.arange(50)
#np_array=np.arange(50)
#np_multi=np_array.reshape(5,10)
#print(np_multi.sum(axis=1))#satırların toplamı gelir
#print(np_multi.sum(axis=0))#sütunların toplamı gelir

rnd_numbers=np.random.randint(1,100,10)
print(rnd_numbers)
#result=rnd_numbers.max()
#result=rnd_numbers.min()
#result=rnd_numbers.mean()
#result=rnd_numbers.argmax()#max sayının indexi- 0dan başlıyor
result=rnd_numbers.argsort()#küçükten büyüğe doğru indexlerini verir
print(result)