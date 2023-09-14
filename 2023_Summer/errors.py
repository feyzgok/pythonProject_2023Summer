while True:
 try:
    x=int(input('enter first integer'))
    y=int(input('enter second integer'))
    print(x/y)

 except(ZeroDivisionError,ValueError) as exe:
    print('error',exe)
    #hangi objeden gelen hata olduğunu gösteriyor -takma adı printlettiğimizde

 else:
    print('ok')
    break#hatırla!

 finally:
     print('finally')#kaynakların kapatılması-tanımlanmış içeriklerin sonlandırılması(mesela dosya okuma sonlandırma) yapılır
     