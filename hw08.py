from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
chrome = webdriver.Chrome()
#res = requests.get("https://pic.sogou.com/napi/pc/searchList?mode=1&start=48&xml_len=48&query=puppy")
chrome.get("https://pic.sogou.com/")
time.sleep(0.5)
a = chrome.find_element_by_class_name("query.query-defalut")
a.send_keys('puppy')
time.sleep(0.5)
a.send_keys(Keys.ENTER)
time.sleep(0.5)
#soup = BeautifulSoup(res.text,'html.parser')
chrome_options = Options()

#瀏覽器頁面不可視 (背景執行)
chrome_options.add_argument('--headless')

chrome = webdriver.Chrome(options=chrome_options)

#開啟瀏覽器視窗(chrome)
#chrome = webdriver.Chrome()

#前往網頁
chrome.get("https://pic.sogou.com/pics?query=puppy")

#讓程式休息三秒 網頁會延遲一下 確保資料有載入
time.sleep(3)

#讓游標往下移
for i in range(20):
    chrome.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)
      
time.sleep(5)

#page_source 讀取網頁原始碼
soup = BeautifulSoup(chrome.page_source,"html.parser")

j=0
for div in soup.find_all('div',class_ ='row sc-hjRWVT gvezjq'):
    j=j+1
    Name = div.find('h4').text
    Price = div.find('span',class_='sc-eIHaNI bvDXCA').text
    print(j,Name,Price)
    
#關閉網頁    
#chrome.close()