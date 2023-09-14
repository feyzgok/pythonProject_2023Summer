import json
import os

import self

class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email


class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUser={}

    def loadUser(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file:
                users=json.load(file)
                for user in users:
                    user=json.loads(user)
                    newUser=User(username=user['username'],password=user['password'])
                    self.users.append(newUser)
                print()
    def register(self, user=None):
        self.users.append(user)
        self.savetoFile()
        print('kullanıcı oluşturuldu')

    def login(self):
        for user in self.users:
            if user.username==username and user.password==password:
                self.isLoggedIn=True
                self.currentUser=user
                print('login yapıldı')
                break

    def logout(self):
        self.isLoggedIn=False
        self.currentUser={}
        print('çıkış yapıldı')

    def identitry(self):
        if self.isLoggedIn:
            print(f'username:{self.currentUser.username}')
        else:
            print('giriş yapılmadı')

    def savetoFile(self):
        list=[]
        for user in self.users:
            list.append(json.dumps(user.__dict__))#user classını dictionary'e çeviriyor
        with open('users.json','w') as file:
            json.dump(self.users , file)#dumps-objeyi kayıt edilebilir json'a çevirir
#dump metodu belli obje türlerini kabul eder

repository=UserRepository()


while True:
    print('menü'.center(50,'*'))
    secim=input('1-Register\n2- Login\n3- Logout\n4- identity\n5- Exit\nseçiminiz:')
    if secim=='5':
        break
    else:
        if secim=='1':
            username=input('username:')
            password=input('password')
            email=input('email')
            user=User(username=username,password=password,email=email)
            repository.register(user)
            #print(repository.users)

        elif secim=='2':
            username=input('username:')
            password=input('password:')
            repository.login(username,password)

        elif secim=='3':
            repository.login()
        elif secim=='4':
            repository.logout()
        elif secim=='5':
            with open('users.json','w') as file:
                json.dump(self.users,file)