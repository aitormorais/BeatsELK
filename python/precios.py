import urllib.request
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
url= "https://www.backmarket.es/es-es/l/imac-qwerty-espanol/c5019c61-18f4-46f9-a052-6b989400a434#model=999%20iMac&year_date_release=79%202020"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(req)
soup = BeautifulSoup(html)

nombres = soup.find_all("p",class_= "body-1-bold mb-1 text-black text-left flex-grow")
precios = soup.find_all("span",class_="body-2-bold text-black")
nlista = list()
plista = list()
for nombre in nombres:
    nlista.append(nombre.contents[0])
for precio in precios:
    plista.append(precio.contents[0])

dic = dict(zip(nlista,plista))
with open('./data/web.json','w') as file:
    json.dump(dic,file, indent=2)

