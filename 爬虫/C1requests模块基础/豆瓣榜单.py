import json
import requests

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

url='https://movie.douban.com/j/chart/top_list?'

param={
    'type': '20',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}

resp=requests.get(url=url,params=param,headers=headers)

list_data=resp.json()
fp=open('C1requests模块基础//douban_rank.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)
print("success")
