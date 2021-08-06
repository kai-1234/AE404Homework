import requests,json
#res = requests.get('https://www.dcard.tw/service/api/v2/forums/pet/posts?popular=true&limit=30&before=236601503')
res = requests.get('https://www.dcard.tw/service/api/v2/forums/pet/posts?popular=true&limit=40')
jsonData = json.loads(res.text)
for i in jsonData:
    data = {'Title':i['title'],
            'ID':i['id'],
            'topics':i['topics']
        }
    
    with open('dcardpet.json','a',encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False)
        