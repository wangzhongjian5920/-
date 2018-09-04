# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-

import urllib
import json
while True:
    content = input("请输入需要翻译的内容：")  # 系统捕获输入，就是命令框会弹出提示，需要你进行手动输入
    if content == 'q':  # 输入q退出while循环
        break

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data = {}  # 构造data，里面构造参数传入
    data['type'] = 'AUTO'
    data['i']=content
    data['doctype'] = 'json' 
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_ENTER'
    data['typoResult'] = 'true'

    data = urllib.urlencode(data).encode('utf-8')  # 将构造的data编码
    req = urllib.Request(url)  # 向浏览器发出请求
    response = urllib.urlopen(req, data)   # 带参请求，返回执行结果
    html = response.read().decode('utf-8')
    # print(html)  # 可以取消print的注释，查看其中效果，这边获取的结果是进行解析

    target = json.loads(html)   # 以json形式载入获取到的html字符串

    print("翻译的内容是："+target['translateResult'][0][0]['tgt'].encode('utf-8'))


# 请输入需要翻译的内容：test
# 翻译的内容是：测试
# 请输入需要翻译的内容：测试
# 翻译的内容是：test
# 请输入需要翻译的内容：q