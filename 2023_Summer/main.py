# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

mesaj="Merhaba dünya"
print(mesaj.replace("ü","u"))

sayi1=10
sayi2=10

if sayi1==sayi2:
    print("bir şey")
    print("bir şey daha")

sehirler=["izmir","istanbul","ankara"]

i=1;
for sehir in sehirler:
    print("sehir",i," =",sehir)
    i=i+1

sayi=10
for x in range(2,sayi):
    print(x)
""" range yapısı x'ten y'ye kadar (y dahil değil)"""

def selamVer(isim="ziyaretçi",soyisim="belirsiz"):
    print(isim+" "+soyisim)