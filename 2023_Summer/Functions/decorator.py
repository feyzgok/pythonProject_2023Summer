#decorator fonksiyonlar oluşturup birçok fonksiyonla ilişkilendirebiliriz

def my_decorator(func):
    def wraper():
        print('fonksiyondan önce işlemler')
        func()
        print('fonksiyondan sonraki işlemler')
    return wraper()

def sayHello(name):
    print('hello '+name)

@my_decorator
def sayGreeting():
    print('greeting')
#determine the common behaviour such as logging and input validation

sayHello=my_decorator(sayHello)
sayHello


import  math
def usalma(a,b):
    print()