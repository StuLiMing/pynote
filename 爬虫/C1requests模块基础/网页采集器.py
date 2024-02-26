import pandas
import requests
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
url='https://www.sogou.com/'
kw=input('enter a word: ')
param={
    'query':kw
}
resp=requests.get(url=url,params=param,headers=headers)
page_text=resp.text
fileName='C2requests模块基础//'+kw+'.html'
with open(fileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(fileName,'保存成功')
