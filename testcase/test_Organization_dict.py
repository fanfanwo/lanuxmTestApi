#!/usr/bin/env python
# 资源-组织机构-添加组织机构目录

import requests,unittest,random,urllib3,time
from common.getConfig import Config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


test_par = int(Config().get('heads','par'))
test_url = Config().get('heads','url')
test_cookies = Config().get('heads','cookies')
test_Token = Config().get('heads','token')
# print(test_url,test_cookies)



class test_Organization_dict(unittest.TestCase):
    try:
        for i in range(1, test_par+1):
            par = '组织机构-自动构造%s' % i
            url = test_url + '/ics/organization/save-structure?T=1647846657950'

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
                  "organization_name": par,
                  "organization_type": 0,
                  "parentId": 1,
                  "additive_attr": "",
                  "assetPositionDTO": {
                    "coordinate": "",
                    "detailedAddress": "",
                    "district": '',
                    "orgTypeId": 1,
                    "province": '',
                    "town": ''
                  },
                  "descript": "描述-自建组织机构"

                }

            resp = requests.post(url=url, headers=hd, json=data, verify=False)
            # print(resp.text)
            time.sleep(2)   # 不加等待时间会报重复提交
            if i == test_par:
                print(resp.text)
                if '200' in resp.text and '新建成功' in resp.text:
                    print('资源-组织机构构造完成！')
                else:
                    print('err_message:','资源-组织机构构造存在异常！')
                    print('err_message:','请检查Cookies与请求参数！')
    except Exception as e:
        print('err_message:{}'.format(e))


