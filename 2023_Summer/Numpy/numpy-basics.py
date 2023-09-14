import numpy as np
#numpy kütüphanesi veri analizinde kullanılan bir kütüphane

#python list
py_list = [1,2,3,4,5,6,7,8,9]

#büyük verileri numpy objeleri içerisine alıp kullanmak daha mantıklı çünkü numpy klasik bir python listesine göre daha az yer kaplıyor ve daha hızlı çalışıyor
#pythonda dizi kavramı yok
#pythondaki list==numpy arrays

#numpy array
np_array=np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))

py_multi=[[1,2,3],[4,5,6],[7,8,9]]
np_multi=np_array.reshape(3,3)#yani 2 boyutlu

print(py_multi)
print(np_multi)