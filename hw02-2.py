import requests
from bs4 import BeautifulSoup
res = requests.get('https://www.books.com.tw/web/sys_saletopb/books')
soup = BeautifulSoup(res.text,'html.parser')
divs = soup.find_all('div', class_="type02_bd-a")
#for each_div in divs:
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
    li = each_div.find('li',class_="price_a")
    if not li:
        continue
        #for each_li in li:
    strong = each_div.find_all('strong')
    # if not strong:
    #     continue
    if len(strong) == 2:
        price2= strong[1].text
    else:
        price2 =strong[0].text
    #price = strong[0].text
    i = index+1
    print("排名"+str(i) +": "+bookName+" 價錢: "+price2+'\n')
    if index == 29:
        break
            
            
    

    
# for each_div in divs:
#     ul = each_div.find('ul',class_="msg")
#     if not ul:
#         continue
#     li = each_div.find('li',class_="price_a")00

#     if not li:
#         continue
#     strong = each_div.find('strong')
#     if not strong:
#         continue
#     b=each_div.find("b")
#     strong2 = each_div.find('strong')
#     b2 = each_div.find("b")
#     price = b2.text
#     print(price)


# for index,each_div in enumerate(divs):
#     h4 = each_div.find('h4')
#     if not h4:
#         continue
#     a = h4.find('a')
#     if not a:
#         continue
#    bookName = a.text
