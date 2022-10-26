#!/usr/bin/env python
# 事件分析-范化-添加数据字典

import requests, unittest, random, urllib3, time
from common.getConfig import Config
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

test_par = int(Config().get('heads', 'par'))
test_url = Config().get('heads', 'url')
test_cookies = Config().get('heads', 'cookies')
test_Token = Config().get('heads', 'token')
# print(test_url,test_cookies)
# test_fieldId = [1,2,3,4]

count = 0

class test_StateTemplate_monitorItem(unittest.TestCase):

    try:
        for i in range(1, test_par + 1):
            url = test_url + '/ics/safe-template/templates-create?T=1663917026684'
            tem_name = "t%s" % i
            pol_name = "p%s" % i
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
                "deviceSn": "",
                "id": 0,
                "safeDevice": 1,
                "safeDeviceModelId": 608,
                "templateName": tem_name,
                "templateDesc": "",
                "deviceTypeId": "9"
            }

            rest = requests.post(url=url, headers=hd, json=data, verify=False)
            re = json.loads(rest.text)

            if '200' in rest.text and '操作成功' in rest.text:
                temid = re["result"]
                print(f"创建模板:{rest.text},template_id : {temid}")
                url = test_url + "/ics/safe-template/templates-policy?T=1663917545039"
                time.sleep(1)
                data1 = {
                    "policyContent": "{\"policy_name\":\"po1\",\"src_interface\":\"ANY\",\"src_ip\":[\"172.16.5.120\"],\"dst_interface\":\"ANY\",\"dst_ip\":[\"172.16.16.208\"],\"function_time\":{\"type\":-1,\"data\":{\"name\":\"always\"}},\"service\":[{\"id\":-1,\"name\":\"ANY\",\"type\":-1}],\"ipv_type\":\"IPV4\",\"action\":\"PERMIT\",\"src_mac\":\"11:11:33:33:33:22\",\"remarks\":\"\",\"log_switch\":0,\"switch\":1,\"application_id\":0,\"industrial_id\":0,\"ddos_id\":0,\"virus_id\":0,\"learn_industrial_id\":0,\"readBack\":[-1],\"dst_mac\":\"11:33:33:23:23:23\",\"src_interface_type\":0,\"dst_interface_type\":0}",
                    "policyName": pol_name,
                    "safeDeviceType": "9",
                    "securityTemplateId": temid,
                    "id": 0
                }
                url = test_url + "/ics/safe-content/save?T=1663917050547"
                resp = requests.post(url=url, headers=hd, json=data1, verify=False)

                if '200' in resp.text and '操作成功' in resp.text:
                    print(f"创建策略:{resp.text}")
                else:
                    print('err_message:', '新建策略存在异常！')
            else:
                print('err_message:', '新建策略模板存在异常！')
                print('err_message:', '请检查Cookies与请求参数！')

    except Exception as e:
        print('err_message:{}'.format(e))
