import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top/"
response=requests.get(url)
print(response)
