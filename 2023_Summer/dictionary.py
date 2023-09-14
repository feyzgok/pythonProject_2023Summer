#listede sıralarının doğru olması önemli:
#sehirler=['kocaeli','istanbul']
#plakalar=[41,34]

#key-value
plakalar={'kocaeli':41, 'istanbul':34}
print(plakalar['kocaeli'])

users={
    'sadık turan':{
        'age':36, 'email':'sadıkturann@gmail.com'
    },
    'sadi turan':{
        'age':17, 'email':'sadituran@gmail.com'
    }
 }
print(users['sadi turan'])
print(users['sadi turan']['age'])
print(users['sadi turan']['email'])

ogrenciler={
    120:{
        'ad':'Ali',
        'soyad':'Yılmaz',
        'telefon':5320000001
    },
    125:{
        'ad':'Can',
        'soyad':'Korkmaz',
        'telefon': 5320000002
    },
    128:{
        'ad':'Volkan',
        'soyad':'Yükselen',
        'telefon':5320000003
    }
}

print(ogrenciler[128]['telefon'])
print(ogrenciler)

number=input('öğrenci no:')
name=input('öğrenci ad:')
surname=input('öğrenci soyad:')
phone=input('telefon no:')

ogrenciler[number]={
    'ad':name,
    'soyad':surname,
    'telefon':phone
}


number=input('öğrenci no:')
name=input('öğrenci ad:')
surname=input('öğrenci soyad:')
phone=input('telefon no:')

ogrenciler.update({
    number:{
        'ad':name,
        'soyad':surname,
        'telefon no':phone
    }
})
print(ogrenciler)


