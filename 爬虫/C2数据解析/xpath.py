from configparser import InterpolationMissingOptionError
from genericpath import exists
import requests 
from lxml import etree
import time

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

url="https://hy.58.com/ershouche/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0039-2591-5daa-e5f64a188a07&ClickID=4"

page_text=requests.get(url=url,headers=headers).text

tree=etree.HTML(page_text)

fp=open("C2数据解析//cars.txt",'w',encoding='utf-8')
li_list=tree.xpath('//*[@id="list"]/ul/li')
for car_li in li_list:
    car=car_li.xpath('./div/a/div[2]/h2/span/text()')
    if len(car)!=0:
        fp.write(car[0])        
