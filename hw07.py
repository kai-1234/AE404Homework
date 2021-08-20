import requests 

#count 可以得知 一頁有20筆資料
count = 0

pageNumber=1
while pageNumber <2:
#while pageNumber <: #要100筆資料，條件？
    
                        #https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page=1&sort=sale/dc format(要插入字串{}裡的值)
    res = requests.get("https://tw.eztable.com/search?country=tw&date=2021-08-21&people=2&searchTab=condition&source=mobile.eztable.com".format(pageNumber))
    pageNumber+=1
    
    #json資料轉換成python格式
    res = res.json()['prods']
    
    for eachProduct in res:
        productName = eachProduct['name']
        productPrice = eachProduct['price']
        print(productName,productPrice)
        count+=1
        
