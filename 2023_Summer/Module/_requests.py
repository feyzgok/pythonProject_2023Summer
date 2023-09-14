import requests
import json

result=requests.get('https://jsonplaceholder.typicode.com/todos')#kaynaktan istediğimiz bilgiyi alabiliriz
result=json.loads(result.text)


for i in result:
    if i['userId']==1:
        print(i['title'])
print(result)
