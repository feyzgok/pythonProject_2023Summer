class Matematik:
    def topla(self,sayi1, sayi2):
        return sayi2 + sayi1

    def cıkar(self,sayi1, sayi2):
        return sayi1 - sayi2

    def carp(self,sayi1, sayi2):
        return sayi1 * sayi2

    def bol(self,sayi1,sayi2):
        return sayi1/sayi2

    def us(self,sayi1,sayi2):
        return sayi1**sayi2

    def mod(self,sayi1,sayi2):
        return sayi1%sayi2

    def tamBol(self,sayi1,sayi2):
        return sayi1//sayi2

    def sayi1isayi2kezkendisiylecarp'(self,sayi1,sayi2):
        return sayi1**sayi2

matematik = Matematik()
print(matematik.bol(11,2))
