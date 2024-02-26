import json
import requests
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
url='https://fanyi.baidu.com/sug'
word=input('Enter a word: ')
data={
    'kw':word
}
resp=requests.post(url=url,data=data,headers=headers)
dic_obj=resp.json()
fileName='C1requests模块基础//'+word+'.json'
fp=open(fileName,'w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)

