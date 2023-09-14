import requests
import json

api_url=('https://api.exchangeratesapi.io/latest?base=')

d1=input('bozulan dövizin cinsi nedir?')
d2=input('hangi tür dövüze çevrilecek?')
a=input('miktar:')

result=requests.get(api_url+d1)
result=json.loads(result.text)#result json bilgiye çeviriliyor
print(result)