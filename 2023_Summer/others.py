#Identity Operator is
x=y=[1,2,3,4]
z=[1,2,3,4]

print(x is z)#aynı adreste tutulmuyor bu yüzden aynı referansı işaret etmiyor ve FALSE sonucunu veriyor
print(x==z)

a=[2,3,4]
b=[2,3]
a=b #adres(referans) eşitlemesi
a.insert(0,2)
print(a)
print(b)
print(a is b)

#Membershsip Operator:in