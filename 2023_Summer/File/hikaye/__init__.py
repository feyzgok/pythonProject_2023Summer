def toplamKarater():
    x=0
    with open("C:/Users/feyza/OneDrive/Masaüstü\python/hikaye", "r", encoding="utf-8") as file:
        content=file.read()
        for i in content:
            if i == " ":
                continue
            else:
                x = x + 1

    print(f'toplam karakter sayısı:{x}')

def toplamSatır():
    x=0
    with open("C:/Users/feyza/OneDrive/Masaüstü\python/hikaye", "r", encoding="utf-8") as file:
        content = file.read()
        satır = content.split("\n\n")
        for i in satır:
            x = x + 1
    print(f'toplam satır sayısı:{x}')

def toplamKelime():
    x=0
    with open("C:/Users/feyza/OneDrive/Masaüstü\python/hikaye", "r", encoding="utf-8") as file:
        content = file.read()
        satır = content.split("\n\n")
        for s in satır:
            kelime=s.split(" ")
            for k in kelime:
                x=x+1

    print(f'toplam kelime sayısı:{x} ')

def toplamCumle():
    x=0
    with open("C:/Users/feyza/OneDrive/Masaüstü\python/hikaye", "r", encoding="utf-8") as file:
        content = file.read()
        cumle=content.split(".")
        for i in cumle:
            x=x+1
    print(f'toplam cümle sayısı:{x-1}')

def soru1():
    toplamKarater()
    toplamKelime()
    toplamCumle()
    toplamSatır()

def soru2():
    x=0
    with open("C:/Users/feyza/OneDrive/Masaüstü/python/hikaye", "r", encoding="utf-8") as file:
        content=file.read()
        for i in content:
            x=x+1
            if i=='a':
                print(x)
                break


def soru3():
    x=0
    with open("C:/Users/feyza/OneDrive/Masaüstü/python/hikaye", "r", encoding="utf-8") as file:
        content=file.read()
        satır = content.split("\n\n")
        for i in satır[4]:
            if i=='e':
                x=x+1
    print(x)

def soru4():
    with open ("C:/Users/feyza/OneDrive/Masaüstü/python/hikaye", 'r', encoding='utf-8') as file:
        content=file.read()
        for i in content:
            match(i):
                case 'ğ': i=='g'