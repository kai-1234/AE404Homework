# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 08:15:12 2021

@author: kbsung
"""

import requests
from bs4 import BeautifulSoup
import re

respond = requests.get("https://www.books.com.tw/web/sys_saletopb/books/") 
soup = BeautifulSoup(respond.text,"html.parser")

a_tags = soup.find_all('a')
print(a_tags)

'''
for url in a_tags:
    if re.fullmatch("https://www.books.com.tw/web/sys_saletopb/books/(\d+)/[?]loc=P_0002_(\d+)", url['href'])!= None:
        print(url.text+':'+url['href'])
'''
no= open("nooo.txt",'w')
no.write('eesrfes')
for url in soup.find_all('a',href = re.compile('[?]loc=P_0002_(\d+)')):
    print(url.text+':'+url['href'])
    no.write("EEEE")
    #no.write(url.text+' '+url['href']+"\n")
        