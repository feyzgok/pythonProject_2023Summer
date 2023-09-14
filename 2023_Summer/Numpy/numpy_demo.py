import numpy as np

result1=np.array([10,15,30,45,60])
print(result1)

result2=np.arange(5,15) #arrange'e başlangıç-bitiş değerleri+adım
print(result2)

result3=np.arange(50,200,5)
print(result3)

result4=np.zeros(11)
print(result4)

result5=np.ones(10)
print(result5)

result6=np.linspace(0,100,5)#0-100 arasında eşit aralıklı
print(result6)

result7=np.random.randint(10,30,5)#10-30 arasına 5 tane sayı üretimi
print(result7)

result8=np.random.randn(10)#[-1 ve 1 arasında 10 tane sayı üretir
print(result8)

result9=np.random.randint(10,50,15).reshape(3,5)#15 elemanlı liste 3x5lik şekilde üsretiliyor
print(result9)

rowTotal=result9.sum(axis=1)
colTotal=result9.sum(axis=0)
print(rowTotal)
print(colTotal)

result11=result9.max()
print(result11)
result11=result9.min()
print(result11)
result11=result9.mean()
print(result11)

result12=result9.argmax()
print(result12)
result12=result9.argmin()
print(result12)

arr=np.arange(10,20)
print(arr)

result=arr[::-1]
print(result)
print(arr[::-1])

matris=np.random.randint(10,50,15).reshape(3,5)#15 elemanlı liste 3x5lik şekilde üsretiliyor
result=