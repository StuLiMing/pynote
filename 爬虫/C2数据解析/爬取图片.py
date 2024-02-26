import requests 
url='https://pic4.zhimg.com/80/v2-1477092e706c0772bb6cef683d0d91d8_720w.jpg?source=1940ef5c'
img_data=requests.get(url=url).content
with open('C2数据解析//img.jpg','wb') as fp:
    fp.write(img_data)