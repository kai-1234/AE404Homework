from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
chrome = webdriver.Chrome()
poo = []
#res = requests.get("https://pic.sogou.com/napi/pc/searchList?mode=1&start=48&xml_len=48&query=puppy")
chrome.get("https://pic.sogou.com/")
time.sleep(0.5)
a = chrome.find_element_by_class_name("query.query-defalut")
a.send_keys('puppy')
time.sleep(0.5)
a.send_keys(Keys.ENTER)
time.sleep(0.5)
#soup = BeautifulSoup(res.text,'html.parser')
c = chrome.get('https://pic.sogou.com/pics?query=puppy')

divs = soup.find_all('div',class_='img-layout')
for index,each_div in enumerate(divs):
    a = each_div.find("a")
    if not a:
        continue
    i = index+1
    
    poo.append(str(i))
    img = a.find('img')
    src = img['src']
    url = requests.get(src)
    print(src)
    
    with open(str(i)+".png",'wb') as f:
        f.write(url.content)
    if index == 199:
        break
# chrome.find_element_by_partial_link_text("兒童青少年程式").click()
# time.sleep(0.5)
# chrome.maximize_window()
# time.sleep(0.5)
# chrome.save_screenshot("wk3afd.png")
# time.sleep(0.5)
chrome.close()





