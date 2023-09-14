
#class
class Person():
    adress='no info'

#constructor
    def __init__(self,name,year):
        self.name=name
        self.year=year
        print('init method')

    def calculateAge(self):
        return 2023-self.year

p1=Person(name='ali',year=1996)

print(f'adım {p1.name}, yaşım {p1.calculateAge()}')

class Circle:
    pi=3.14

    def __init__(self,yaricap=1):#yarıcap (default) 1 olarak alır
        self.yaricap=yaricap
        print("circle created")


    def cevre(self):
        return 2*self.pi*self.yaricap

    def alan(self):
        return self.pi*(self.yaricap)

c1=Circle(2)
print(c1.alan())