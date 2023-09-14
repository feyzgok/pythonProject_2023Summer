import numpy as np
myArr=np.arange(0,15)
print(myArr)
print(myArr[0])
print(myArr[3:8])
myArr[3:8]=-5#dizi içerisindeki elemanlar değştirildi
print(myArr)
arr2=np.arange(0,24)
print(arr2)
sliceArr=arr2[3:8]
print(sliceArr)
sliceArr[::]=19
print(sliceArr)
print(arr2)#[0 1 2 [3 4 5 6 7] 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23] -küme içinde küme
sliceArr2=sliceArr.copy()
sliceArr2[:]=10
print(sliceArr2)
print(arr2)