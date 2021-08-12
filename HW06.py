from bs4 import BeautifulSoup
import requests
ride = input("要哪一天搭乘?")
start = input("起點車站是甚麼?")
end = input("終點車站是甚麼?")
starttime = input('開始的時間是甚麼?')
endtime = input('停止的時間是甚麼?')
def theDay(ride,start,end):
    post = {"startStation": end,
            "endStation": start,
            "transfer": "ONE",
            "rideDate": ride,
            "startOrEndTime": "true",
            "startTime": starttime,
            "endTime": endtime,
            "trainTypeList": "ALL"}
    res = requests.post("https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime",data=post)
    soup = BeautifulSoup(res.text,"html.parser")
    uls = soup.find_all('ul',class_="train-number")
    for index,each_ul in enumerate(uls[:11]):
        li = each_ul.find('li')
        if not li:
            continue
        a = li.find('a')
        if not a:
            continue
    
        print(a.text)
        
theDay(ride,start,end)
