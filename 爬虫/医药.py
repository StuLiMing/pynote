import requests 
from lxml import etree

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

url="http://zzk.xywy.com/p/neike.html"

page=requests.get(url=url,headers=headers)
page.encoding="GBK"
page_text=page.text
tree=etree.HTML(page_text)

fp=open("keshi.txt",'w',encoding='utf-8')

li_list1=tree.xpath('//*[@class="jblist-nav fl"]/ul/li')
for li in li_list1:
    Title_1=li.xpath('./a/text()')
    fp.write(Title_1[0])
    fp.write(" : ")
    keshi_list=li.xpath('./ul/li')
    for keshi in keshi_list:
        title=keshi.xpath('./a/text()')
        href=keshi.xpath('./a/@href')
        if(len(title)!=0):
            fp.write(title[0])
        fp.write(href[0])
    fp.write("\n")
   
