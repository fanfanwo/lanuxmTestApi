#!/usr/bin/env python
# 安全设备中-设备列表-添加设备
# 华为环境添加设备时的入参为密文

import requests,unittest,random,urllib3,time
from common.getConfig import Config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


test_par = int(Config().get('heads','par'))
test_url = Config().get('heads','url')
test_cookies = Config().get('heads','cookies')
test_Token = Config().get('heads','token')
# print(test_url,test_cookies)

test_deviceModelId = [832,833,600]


class test_Equipmentlist_equipment(unittest.TestCase):
    try:
        for i in range(1, test_par+1):

            par = '安全设备-自动构造%s' % i
            url = test_url + '/ics/api/devices/add?T=1649236559499'
            test_assetIp = "172.172.151.1%s" % i
            mock_deviceModelId = random.choice(test_deviceModelId)


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
                  "deviceBean": {
                    "important": "",
                    "safety_head": "",
                    "device_group_id": 5,
                    "id": 0,
                    "description": "设备描述。。。",
                    "is_active": 1,
                    "deviceTypeList": [
                      {
                        "id": "",
                        "typeName": "FLOW",
                        "description": "流量采集引擎",
                        "createTime": "",
                        "updateTime": "",
                        "defaultFlag": 1,
                        "remarks": "",
                        "deviceTypeId": 1
                      }
                    ],
                    "host": test_assetIp,
                    "name": par,
                    "position": "",
                    "safe_area": "",
                    "is_insight_enabled": 0,
                    "monitorTemplateList": []
                  },
                  "deviceToExpandBean": {
                    "deviceId": 0,
                    "deviceModelId": mock_deviceModelId,
                    "devicePassword": "ndLY3ZUP+c4qqDRD4kUQdw==",
                    "deviceUserName": "",
                    "protocolIds": "",
                    "filterMode": "exclude",
                    "target": "",
                    "model": "",
                    "version": "",
                    "sn": "",
                    "aggAlert": "true",
                    "intervalAlert": 1800,
                    "aggAudit": "true",
                    "intervalAudit": 1800,
                    "port": "161",
                    "snmpVersion": "2",
                    "community": "public",
                    "contextName": "",
                    "securityName": "",
                    "securityLevel": "",
                    "verifyProtocol": "",
                    "verifyPassword": "",
                    "privacyAgreement": "",
                    "privateKey": ""
                  }
                }


            resp = requests.post(url=url, headers=hd, json=data, verify=False)
            # print(resp.text)
            if i == test_par:
                print(resp.text)
                if '200' in resp.text and '操作成功' in resp.text:
                    print('安全设备-设备列表中的设备构造完成！')
                else:
                    print('err_message:','安全设备-设备列表中的设备构造存在异常！')
                    print('err_message:','请检查Cookies与请求参数！')
    except Exception as e:
        print('err_message:{}'.format(e))


