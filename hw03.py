import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.books.com.tw/web/sys_saletopb/books')
soup = BeautifulSoup(res.text,'html.parser')
divs = soup.find_all('div', class_="type02_bd-a")
#for each_div in divs:
poo = []
for index,each_div in enumerate(divs):
    h4 = each_div.find('h4')
    
    if not h4:
        continue
    a = h4.find('a')
    if not a:
        continue
    bookName = a.text
    #print(bookName)
    ul = each_div.find('ul',class_="msg")
    if not ul:
        continue
    #for each_ul in ul:
    li = each_div.find('li')
    if not li:
        continue
    b = li.find("a")
    author = b.text
    i = index+1
    
    poo.append(str(i)+" "+bookName+"- "+author)
    
    print("No."+str(i)+": "+bookName+"- "+author)
    if index == 49:
        break
lis = soup.find_all("li",class_="item")

for ind,each_li in enumerate(lis):
    img = each_li.find("img")
    src = img['src']#書的圖片連結
    alt = img['alt']#書名
    #print(alt+" link: "+src)
    url = requests.get(src)
    
    
    #poo = str(i)+": "+bookName+"- "+author
    with open(poo[ind]+".png",'wb') as f:
        f.write(url.content)
    if ind == 49:
        break