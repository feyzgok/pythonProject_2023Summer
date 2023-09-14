#global scope
x='global x '

def function():
    #local scope
    x='local x'
    print(x)

function()
print(x)#fonksiyonlar yeni bir tanım alanı kullanır


name='Çınar'
def changeName(new_name=name):
    name=new_name
    print(name)

changeName('Ada')
print(name)

name='global name'

def greeting():
    name='Çınarr'

    def hello():
        name='Ada'
        print('Hello '+name)

    hello()
    print('hello '+name)

greeting()
print('hi '+name)


x=50
def test(x):
    print(x)

    x=100
    print(x)

test(x)
print(x)#global olarak tanımlanan x bilgisini değiştirmemiştir

#global değişkenin gerçekten değişmesi için fonksiyonda global x şeklinde kullanılması şarttır
x=50
def test():
    global x
    print(x)

    x=100
    print(x)

test()
print(x)

#scope:global built-in local nonlocal
#built-in scope refers all variables are accessible
#global scope is essentially file-wide