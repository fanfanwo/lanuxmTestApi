#!/usr/bin/env python
# 事件分析-范化-添加字段值映射表

import requests,unittest,random,urllib3,time
from common.getConfig import Config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


test_par = int(Config().get('heads','par'))
test_url = Config().get('heads','url')
test_cookies = Config().get('heads','cookies')
test_Token = Config().get('heads','token')
# print(test_url,test_cookies)
test_fieldId = [1,2,3,4]



class test_Normalization_ysb(unittest.TestCase):
    try:
        for i in range(1, test_par+1):

            par = '范化映射表-自动构造%s' % i
            url = test_url + '/ics/mappingsummary/manager/add?T=1649226934695'
            test_type = random.choice(test_fieldId)

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
                  "id": "",
                  "mappingTableName": par,
                  "fieldId": test_type,
                  "description": "映射表描述。。。",
                  "systemFlag": 0,
                  "xpath": "/22/"
                }


            resp = requests.post(url=url, headers=hd, json=data, verify=False)
            # print(resp.text)
            if i == test_par:
                print(resp.text)
                if '200' in resp.text and '映射表新增成功' in resp.text:
                    print('事件分析-范化映射表构造完成！')
                else:
                    print('err_message:','事件分析-范化映射表构造存在异常！')
                    print('err_message:','请检查Cookies与请求参数！')
    except Exception as e:
        print('err_message:{}'.format(e))


