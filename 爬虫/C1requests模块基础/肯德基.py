from paddle import tolist
import requests 

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

kw=input("请输入地址: ")

param={
    'cname':'', 
    'pid': '',
    'keyword': kw,
    'pageIndex': '1',
    'pageSize': '10'
}

resp=requests.post(url=url,headers=headers,params=param)
msg=resp.text
for i in msg:
    print(i)
