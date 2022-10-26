#!/usr/bin/env python
# 知识库-文档-添加文档

import requests,unittest,random,urllib3
from common.getConfig import Config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


test_par = int(Config().get('heads','par'))
test_url = Config().get('heads','url')
test_cookies = Config().get('heads','cookies')
test_Token = Config().get('heads','token')
# print(test_url,test_cookies)
test_groupId = [1, 2, 7, 20]



class test_Aashboardshijian_wd(unittest.TestCase):
    try:
        for i in range(1, test_par+1):
            par = '文档-自动构造%s' % i
            test_type = random.choice(test_groupId)
            url = test_url + '/ics/api/knowledge/documentLibrary/createDocument?T=1647502105135'

            hd = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Connection': 'keep-alive',
                'Csrf-Token': test_Token,
                'Cookie': test_cookies,
                # 'Host': '172.16.6.224',
                # 'Referer': 'https://172.16.6.224',
                'sec-ch-ua': 'Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'Windows',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'ame-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'

            }

            data = {
                "documentDescribe": "文档描述。。。",
                "documentName": par,
                "groupId": test_type,
                "ids": [],
                "treeId": 79
            }

            resp = requests.post(url=url, headers=hd, json=data, verify=False)

            if i == test_par:
                print(resp.text)
                if '200' in resp.text and '添加文档成功' in resp.text:
                    print('知识库-文档构造完成！')
                else:
                    print('err_message:','知识库-文档构造存在异常！')
                    print('err_message:','请检查Cookies与请求参数！')
    except Exception as e:
        print('err_message:{}'.format(e))


