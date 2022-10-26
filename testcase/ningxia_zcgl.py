#!/usr/bin/env python
# 资产-资产管理-添加资产

import requests,unittest,random,urllib3,time
from common.getConfig import Config
import random
import struct
import socket
RANDOM_IP_POOL=['192.168.10.222/0']
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


test_par = int(Config().get('heads','par'))
test_url = Config().get('heads','url')
test_cookies = Config().get('heads','cookies')
test_Token = Config().get('heads','token')
print(test_url,test_cookies)

test_xpathValue = ['网络设备/路由器','主机设备/Linux/RedHat','主机设备/Linux/CentOS','虚拟化/ESXi']
test_assetMac = ['A','B','B','C','D']


# def get_random_ip():
#     str_ip = RANDOM_IP_POOL[random.randint(0, len(RANDOM_IP_POOL) - 1)]
#     str_ip_addr = str_ip.split('/')[0]
#     str_ip_mask = str_ip.split('/')[1]
#     ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
#     mask = 0x0
#     for i in range(31, 31 - int(str_ip_mask), -1):
#         mask = mask | (1 << i)
#     ip_addr_min = ip_addr & (mask & 0xffffffff)
#     ip_addr_max = ip_addr | (~mask & 0xffffffff)
#     return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))

class test_Assets_zcgl(unittest.TestCase):

    try:
        for i in range(1, test_par+1):

            par = 'Afcy%s' % i
            url = test_url + '/ics/api/asset/add?T=1663551389424'
            test_assetIp = "172.16.151.10%s" % i
            mock_assetMac = 'F8-8%s-D2-%s2-8B-2%s' % (random.choice(test_assetMac),random.choice(test_assetMac),random.choice(test_assetMac))
            mock_xpathValue = random.choice(test_xpathValue)

            hd = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate,deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json;charset=UTF-8',
                'Csrf-Token': test_Token,
                'Cookie': test_cookies,
                'sec-ch-ua': 'Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': 'Windows',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
            }

            data = {
                      "monitorTemplateList": [0],
                      "runinfoMode": 0,
                      "id": 0,
                      "assetAttrContentMap": "",
                      "assetAttrContents": [],
                      "assetBrand": "",
                      "assetCode": "",
                      "assetConfig": "",
                      "assetContact": "",
                      "assetIpBeans": [
                        {
                          "assetIp": test_assetIp,
                          "assetMac":  mock_assetMac,
                          "isManageIp": 1
                        }
                      ],
                      "assetLeader": "",
                      "assetMobile": "",
                      "assetModel": "",
                      "assetName": par,
                      "assetPosition": "",
                      "assetPreFlag": 2,
                      "assetVendorSource": 3,
                      "gradeXpath": "",
                      "assetSecurityLevelId": "",
                      "assetSn": "",
                      "assetTags": [],
                      "assetVendor": "",
                      "orgIdList": [
                        3
                      ],
                      "storageTime": "",
                      "xpathValue": mock_xpathValue,
                      "propertyBeans": []
                    }

            resp = requests.post(url=url, headers=hd, json=data, verify=False)

            if i == test_par:
                print(resp.text)
                if '200' in resp.text and '操作成功' in resp.text:
                    print('资产-资产管理资产构造完成！')
                else:
                    print('err_message:','资产-资产管理资产构造存在异常！')
                    print('err_message:','请检查Cookies与请求参数！')
    except Exception as e:
        print('err_message:{}'.format(e))


