import numpy as np

numbers1=np.random.randint(10,100,6)
numbers2=np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

result=numbers1+numbers2
print(result)

result1=numbers1+10
print(result1)

result2=np.sin(numbers1)
result3=np.sqrt(numbers1)
result4=np.log(numbers1)
print(result2)
print(result3)
print(result4)

print("---------------------")
#vertical stack
result=np.vstack((numbers1,numbers2))#(numbers1,numbers2)denseydi farklı parametereler olarak görürdü o yüzden paranteze alındı
print(result)#hepsini tek bir matris yaptı

print("---------------------")
#horizontal stack
result=np.hstack((numbers1,numbers2))
print(result)

result=numbers1<=numbers2
print(result)

result=numbers1%2==0
print(result)