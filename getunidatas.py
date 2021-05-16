# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
  
imgurl = [] 
uninames = [] 
uniTuru = []
uniSehir = []
uniSite = []
#*******************************************************************
r = requests.get("https://yokatlas.yok.gov.tr/universite.php")
soup = BeautifulSoup(r.content)
list = soup.find_all('body')
for ul in list:
  imgList = ul.find_all('img', attrs={'class':'col-md-2 logo'})
  nameList = ul.find_all('h3')
  turList = ul.find_all('span', attrs={'class':'tur'})
  sehirList = ul.find_all('span', attrs={'class':'sehir'})
  siteList = ul.find_all('a', attrs={'target':'_blank'})
  for site in siteList:
    uniSite.append(site.text)
  for sehir in sehirList:
    uniSehir.append(sehir.text)
  for tur in turList:
    uniTuru.append(tur.text)
  for name in nameList:
    uninames.append(name.text)
  for li in imgList:
    imgurl.append(li['src'])
    
#print(len(imgurl))
#print(len(uninames))
#print(len(uniTuru))
#print(len(uniSehir))
#print(len(uniSite))

with open('Universiteler.csv','w') as file:
    for line in range(0, len(imgurl)):
        file.write(imgurl[line])
        file.write(',')
        file.write(uninames[line])
        file.write(',')
        file.write(uniTuru[line])
        file.write(',')
        file.write(uniSehir[line])
        file.write(',')
        file.write(uniSite[line])
        file.write('\n')