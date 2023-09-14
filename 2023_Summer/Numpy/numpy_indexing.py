import numpy as np

numbers=np.array([0,5,10,15,20,25,50,75])

result=numbers[-1]
result1=numbers[0:4]
result2=numbers[:4]
result3=numbers[2:]
result4=numbers[::]
result5=numbers[::-1]#hepsini sıralar ve ters çevirir
result6=numbers[::2]# ikişerli ilerler
result7=numbers[::-2]#tersten ikişerli sıralar


print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)

array = np.array([1, 2, 3], ndmin=1)
print(array.shape)

numbers=np.array([[0,5,10],[15,20,25],[50,75,85]])
print(numbers)

result=numbers[0:,2]#tüm satırlardan 2. elemanı çıktı verir
print(result)

result=numbers[:,2]
print(result)

result=numbers[-1,:]
print(result)

result=numbers[0][1]
print(result)