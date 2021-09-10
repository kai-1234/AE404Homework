import requests
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome = webdriver.Chrome(options=chrome_options)
chrome.get("https://movies.yahoo.com.tw/movie_thisweek.html")
time.sleep(3)

#下拉選單選擇台北松山
#selectCounty = Select(chrome.find_element_by_id('ddl_county'))
#selectCounty.select_by_index(1) #找到第2個選項 > 台北市
time.sleep(1)
#selectSite = Select(chrome.find_element_by_id('ddl_site'))  #測站地點
#selectSite.select_by_index(4)
time.sleep(1)
soup = BeautifulSoup(chrome.page_source,"html.parser")
divs = soup.find_all('div', class_="release_movie_name")
for index,each_div in enumerate(divs):
#取得測站點、時間、PM2.5值

    #air_info = soup.find_all('div',class_ = 'info')[0]
    name = soup.find('a')
    #date = air_info.find('div',class_ = 'date').text.strip()[:16]
    
    movie_name = name.text
    #PM25 = int(air_info.find('span',id = 'PM25').text)
    air_quality = ''

    
    
webhook_key = "Iv6-ykk5ugcCZG5Y5yWNs"
trigger_name = "movie"
#url ='https://maker.ifttt.com/trigger/'+trigger_name+'/with/key/'+webhook_key+'?value1={}&value2={}&value3={}'.format(date,state,air_quality)
#requests.get(url)
#print(date,movie_name,air_quality)
print(movie_name)

