with open("newfile.txt",'r+',encoding='utf-8')as file:
    content = file.read()
    print(content)

# with komutu kullanıldığında open ve close işlemlerine gerek kalmıyor
#ancak içeriği yazdırmak için file.read() kullandığımız için as file diye belirtmek gerekiyor

    print(file.tell())#tell fonksiyonu kaçıncı karakterde olduğunu gösterir-it is an integer already
    file.seek(0)#x. konuma gönderildi-??????
    file.write(content)
    file.seek(0)
    content2=file.read()
    print(content2)