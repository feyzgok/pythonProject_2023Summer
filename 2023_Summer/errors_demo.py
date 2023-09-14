liste =['1','2','5a','10b','abc','10','50']

for x in liste:
    try:
        y=int(x)
        print('try')
    except ValueError:
        print('exception')
        continue

    else:
        print(y)#try denedi exception olmayınca else çalıştı

    finally:
        print('finally')#her türlü bu satırı okuyor

    print('a')#continue denildiği için döngüye devam etti ve bu satırı okumadı