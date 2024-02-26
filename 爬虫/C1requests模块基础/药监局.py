# 网页加密了做不了

import requests
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

id_list=[]

id_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?hKHnQfLv=51XAPW90iQ2yy6Dh4E.a7hWUdIrLFOiIqdOnj791pxUUN7pN5naMD.Wbn.Tb.UKrz265uUFB8xjfrfue7bfi8rRC53exKUBiP_bdLh2rziuzExybR0EVu9yJe4YAgS7CxxU4dWVtBqVEKfoGu3Rc8qfEDq.pmc6raczNcz7ylmLRuJESwByC79fmRh6oAX5NSbyo2fQhZJuFT4yj5nB5oeXQtlKwsc9B85jpZAUK9E4tnwJuTtoxPPprGcq_iBeHap7WLLnxD9MGfTxE3TgHqwWmDxPF0mRL6GOzEmm63ZjZ&8X7Yi61c=41hUfxYw7q55Cosw1aRHXAAuyG2HFRegS0B3wDHY6X7SmqEUH7cqU6Zg_cJKGttmay7ZfYxQ_QZl0gwzijL_LVitz18KDrdfw..HrhpdoFvlCvr6514Ej.qD3tauSHYuW'
data={
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'productName': '' ,
    'conditionType': '1',
    'applyname': '',
    'applysn': ''
}

id_json=requests.post(url=id_url,headers=headers,data=data).json()
for id in id_json['list']:
    id_list.append(id['ID'])
print(id_list,"over")
