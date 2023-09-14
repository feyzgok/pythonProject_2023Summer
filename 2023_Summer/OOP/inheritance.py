class Person():
    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age
        print("Person created")

    def eat(self):
        print('eat method')


class Student(Person):
    def __init__(self,name='name',lastname='last',age=11):
        Person.__init__(self,name,lastname,age)
        print("Student Created")

class Teacher(Person):
    pass

p1=Person(name='feyza', lastname='gök', age=20)
s1=Student()

print(f'{p1.name}')
print(f'{s1.name}')

"""inhheritance yaparken 'extends' yerine direk class Cat(Animal) şeklinde yazılır
self=this"""

class Animal():
    name='boncuk'

    def __init__(self):
        print('animal created')

    def callName(self):
        print(self.name)#return statement'i bulunmayan metod +None çıktısını verir

class Cat(Animal):
    def __init__(self,name):
        self.name=name
        Animal()

    def callName(self):
        return (self.name)


a1=Animal()
a2=Cat('kedi')
print(a2.callName())
print(a1.callName())