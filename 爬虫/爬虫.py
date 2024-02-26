import requests
import random
import time
import numpy as np
import pandas as pd

#一堆要输入的参数
ID = input('请输入你要爬取内容的id: ')
num_page = int(input('请输入你要爬的页数: '))

#对应ajax请求的url
url = 'https://m.weibo.cn/comments/hotflow?'

#使用代理(被封IP就用)
proxies={

}

#UA伪装
user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
]

#请求头
headers = {'User-Agent': random.choice(user_agent),
            #在这个粘贴你的Cookie
            'Cookie':'SCF=AkOF3RE0iGpbCzsCTVNUUFdnp09eh4AA-S721wBzE0Z9mUF3A2BC_BJo1DhWnRvhUJv2XvtqrolsLrzQ1eRm3i8.; WEIBOCN_FROM=1110006030; SUB=_2A25P9xm-DeRhGeFJ7lUQ8SjFwjyIHXVtG6f2rDV6PUJbkdCOLVatkW1Nf4Y14ZYEDSkc7X759C_bCOucQxctKcmC; MLOGIN=1; _T_WM=53439941936; XSRF-TOKEN=faa9bf; M_WEIBOCN_PARAMS=oid%3D4800917776631714%26luicode%3D10000011%26lfid%3D100103type%253D60%2526q%253D%2523%25E5%2590%258D%25E5%2588%259B%25E4%25BC%2598%25E5%2593%2581%25E5%259B%259E%25E5%25BA%2594%25E4%25B8%258D%25E8%25AE%25B8%25E6%2594%25BE%25E4%25B8%25AD%25E6%2596%2587%25E6%25AD%258C%2523%2526t%253D10%26uicode%3D20000061%26fid%3D4800917776631714',
            'Referer':'https://m.weibo.cn/detail/'+ID,
            'Sec-Fetch-Mode':'navigate'
            }

#评论的列表
list_text = []
df=pd.DataFrame(columns=['时间','点赞数','评论内容'])
#记录评论条数
comment_inedx=0

#发起请求并解析数据
def get_max_id(params):
    global comment_inedx
    # 发起get请求
    response = requests.get(url=url, headers=headers,params=params).json()
    max_id = response['data']['max_id']
    max_id_type = response['data']['max_id_type']
    data = response['data']['data']
    for i in range(0, len(data)):
        comment_inedx+=1
        text = data[i]['text']
        like_count=data[i]['like_count'] 
        comment_time=data[i]['created_at'] 
        df.loc[comment_inedx]=np.array([comment_time,like_count,text])
        list_text.append(text)
        print(f"成功爬取第{comment_inedx}条评论")
    return max_id, max_id_type

return_info = ('0', '0')
for i in range(0, num_page):
    print(f'正在爬取第{i + 1}页')
    #防止请求密度过大
    time.sleep(20)
    params = {
        'id': ID,
        'mid': ID,
        'max_id': return_info[0],
        'max_id_type': return_info[1]
    }
    return_info = get_max_id(params)

name=input("请输入要保存成的ecxcel名")
df.to_excel(f"{name}.xlsx")
print("over!!!")

