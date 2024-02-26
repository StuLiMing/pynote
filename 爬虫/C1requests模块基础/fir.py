import requests
from sympy import pager_print
url1='https://www.sogou.com/'
resp=requests.get(url=url1)
page_text=resp.text
print(page_text)
with open('C2requests模块基础//sogou.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
