import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.books.com.tw/web/sys_saletopb/books')
soup = BeautifulSoup(res.text,'html.parser')
divs = soup.find_all('div', class_="type02_bd-a")

for index,each_div in enumerate(divs):
    h4 = each_div.find('h4')
    if not h4:
        continue
    a = h4.find('a')
    if not a:
        continue
    bookName = a.text
    print('排名'+str(index+1)+': ' +bookName)