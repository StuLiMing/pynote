import re
import requests
import os

if not os.path.exists('C2数据解析//imgLibs'):
    os.mkdir('C2数据解析//imgLibs')

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

page_index=1
img_index=0
while page_index<=20:
    urls=f"https://konachan.net/post?page={page_index}&tags="
    page_index+=1
    res=requests.get(url=urls,headers=headers).text
    ex='<li style.*?<img src="(.*?)" style=.*?</li>'
    img_src_list=re.findall(ex,res,re.S)
    for src in img_src_list:
        img_index+=1
        with open(f'C2数据解析//imgLibs//{img_index}.jpg','wb') as fp:
            fp.write(requests.get(url=src,headers=headers).content)
        print(f"第{img_index}张图片爬取成功")
print("over!!!")
        


