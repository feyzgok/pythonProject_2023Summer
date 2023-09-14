def square(num): return num**2

numbers=[1,2,3,5,9]

reulsts=list(map(square,numbers))#fonksiyonu kullanmıyor sadece adını veriyoruz

print(reulsts)

for i in map(square,numbers):
    print(i)
#for döngüsü veya listeleme metoduyla içeriğin çıktısı alındı
result=square(2)
print(result)
print(square(2))

lambdaResult=list(map(lambda num:num**2,numbers)) #square metodu yerine lambda fonksiyonuyla aynı iş
print(lambdaResult)

lambdaSquare=lambda num:num**2
for item in map(lambdaSquare,numbers):
    print(item)

def check_even(num):return num%2==0

resultEven=list(filter(check_even,numbers))
print(resultEven)

for even in filter(lambda num: num%2==0, numbers):
    print(even)