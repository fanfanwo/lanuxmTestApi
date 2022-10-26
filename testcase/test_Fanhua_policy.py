#!/usr/bin/env python
# 事件分析-范化-添加策略
import json

import requests, unittest, random, urllib3, time
from common.getConfig import Config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

test_par = int(Config().get('heads', 'par'))
test_url = Config().get('heads', 'url')
test_cookies = Config().get('heads', 'cookies')
test_Token = Config().get('heads', 'token')
# print(test_url,test_cookies)
test_status = [1, 0]


class test_Normalization_cl(unittest.TestCase):
    try:
        for i in range(1, test_par + 1):
            policy_name = 'upgradePre%s' % i
            url_dev_type = test_url + '/ics/api/select/tree/add?T=1665622550366'
            test_type = random.choice(test_status)
            regularExpression = "\\A([^\\|]*)\\|([^\\|]*)\\|([^\\|]*)\\|([^\\|]*)\\|"  # \A([^\|]*)\|([^\|]*)\|([^\|]*)\|([^\|]*)\|
            logSamples = "8|6|Mac|ip|"
            # regularExpression = '\{"action":"?([^"]*)"?,"action_id":([^,]*),"alert_severity":"?([^"]*)"?,"alert_severity_id":([^,]*),"datagram":"?([^"]*)"?,"device_id":([^,]*),"device_name":"?([^"]*)"?,"direction":"?([^"]*)"?,"dst_ip":"?([^"]*)"?,"dst_mac":"?([^"]*)"?,"dst_port":"?([^"]*)"?,"epoch":([^,]*),"instruct":"?([^"]*)"?,"instruct_id":"?([^"]*)"?,"layers":"(.*)","policy_id":([^,]*),"policy_name":"?([^"]*)"?,"protocol":"?([^"]*)"?,"rule_id":"?([^"]*)"?,"rule_name":"?([^"]*)"?,"source":"?(flow)"?,"src_ip":"?([^"]*)"?,"src_mac":"?([^"]*)"?,"src_port":"?([^"]*)"?,"tag":"?([^"]*)"?,"timestamp":([^,]*),"timestamp_local":([^,]*),"type":"?([^"]*)"?,"type_id":([^\}]*)\}'
            # logSamples = '{"action":"accept","action_id":1,"alert_severity":"low","alert_severity_id":1,"datagram":"0123","device_id":2,"device_name":"审计一体机-6.197","direction":"C_to_S","dst_ip":"226.1.0.1","dst_mac":"01:00:5e:01:00:01","dst_port":"7001","epoch":1.6557969706441E9,"instruct":"告警","instruct_id":"1","layers":"none","policy_id":0,"policy_name":"未授权的通讯数据","protocol":"test","rule_id":"1.00000004E8","rule_name":"未授权的通讯数据","source":"flow","src_ip":"172.101.1.18","src_mac":"00:18:7d:09:cf:84","src_port":"32772","tag":"审计一体机-6.197-2-100000004-172.101.1.18-226.1.0.1-test","timestamp":1655796970644,"timestamp_local":1655796970644,"type":"异常报文","type_id":1}'
            dev_type_name = "upgrade%s" % i
            dev_type_id = ""
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
            # 创建设备类型所需数据
            data_dev_type = {
                "nodeName": dev_type_name,
                "description": dev_type_name,
                "sharedFlag": 1,
                "treeType": 1,
                "id": "",
                "parentId": 22,
                "xpath": "全部",
                "xpathValue": dev_type_name
            }
            time.sleep(1)
            # 创建流量审计策略 所需数据
            data_flow_audit = {
                "fieldCount": 0,
                "logResourceTypeId": dev_type_id,  # 设备类型ID
                "logSamples": logSamples,
                "policeFields": [
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 1045,
                        "number": "1",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 1370,
                        "number": "2",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": 295,
                        "extractField": "",
                        "assignmentWay": "MAPPING",
                        "fieldId": 5,
                        "number": "3",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 1330,
                        "number": "4",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 1046,
                        "number": "5",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 1123,
                        "number": "6",
                        "supplementField": 0
                    },
                    {
                        "extractField": "",
                        "assignmentWay": "MAPPING",
                        "fieldId": 9,
                        "number": "7",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 1331,
                        "number": "8",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 24,
                        "number": "9",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 26,
                        "number": "10",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 25,
                        "number": "11",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 1326,
                        "number": "12",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 1333,
                        "number": "13",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 1337,
                        "number": "14",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 1000000,
                        "number": "15",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "  ",
                        "extractField": "",
                        "assignmentWay": "DIRECT",
                        "fieldId": 65,
                        "number": "16",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "17",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "18",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "19",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "20",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "21",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "22",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "23",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "24",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "25",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "26",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "27",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "28",
                        "supplementField": 0
                    },
                    {
                        "assignmentValue": "",
                        "extractField": "",
                        "assignmentWay": "",
                        "number": "29",
                        "supplementField": 0
                    }
                ],
                "policeId": 0,
                "policyDesc": "fcytestpolicy",
                "policyGroupId": "",
                "policyName": policy_name,
                "regularExpression": regularExpression,
                "status": 1
            }

            # 创建设备类型响应
            resp_dev = requests.post(url=url_dev_type, headers=hd, json=data_dev_type, verify=False)
            print(resp_dev.text)
            resp_dev_type = json.loads(resp_dev.text)
            print(resp_dev_type)
            if '200' in resp_dev.text and '添加成功' in resp_dev.text:
                dev_type_id = resp_dev_type["result"]
                print(f'设备类型创建成功 ！dev_type_id = {dev_type_id}')
                # 创建范化策略所需数据
                data_self_4value = {
                    "fieldCount": 0,
                    "logResourceTypeId": dev_type_id,
                    "logSamples": logSamples,
                    "policeFields": [
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 4,
                            "number": "1",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 5,
                            "number": "2",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 18,
                            "number": "3",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 16,
                            "number": "4",
                            "supplementField": 0
                        }
                    ],
                    "policeId": 0,
                    "policyDesc": "fcytestpolicy",
                    "policyGroupId": "",
                    "policyName": policy_name,
                    "regularExpression": regularExpression,
                    "status": 1
                }
                # 15111意涵的日志
                data_centos = {
                    "fieldCount": 0,
                    "logResourceTypeId": dev_type_id,
                    # "logSamples": "<4> 2022-10-12 14:24:05 FWsadsad FW 1 6 日志时间：2022-10-12 16:55:05，级别：信息，类型：用户管理，操作IP：172.16.24.80，用户：root，执行结果：成功，日志内容：用户登录",
                    "logSamples": "<4> 2022-10-12 14:24:05 FWsadsad FW 1 6 日志时间:2022-10-12 16:55:05，级别:信息，类型:用户管理，操作IP:172.16.24.80，用户:root，执行结果:成功，日志内容:用户登录",
                    "policeFields": [
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 1029,
                            "number": "1",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 42,
                            "number": "2",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 7,
                            "number": "3",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 4,
                            "number": "4",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 8,
                            "number": "5",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 2,
                            "number": "6",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 5,
                            "number": "7",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 33,
                            "number": "8",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 16,
                            "number": "9",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 1022,
                            "number": "10",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 32,
                            "number": "11",
                            "supplementField": 0
                        },
                        {
                            "assignmentValue": "  ",
                            "extractField": "",
                            "assignmentWay": "DIRECT",
                            "fieldId": 219,
                            "number": "12",
                            "supplementField": 0
                        }
                    ],
                    "policeId": 0,
                    "policyDesc": "",
                    "policyGroupId": "",
                    "policyName": policy_name,
                    # "regularExpression": "<(\\d+)>\\s([^\\r\\n]*)\\sFWsadsad\\s(\\S*)\\s(\\d)\\s(\\d).日志时间.(\\S[^\\，]*).级别.(\\S[^\\，]*).类型.(\\S[^\\，]*).操作IP.(\\S[^\\，]*).用户.(\\S[^\\，]*).执行结果.(\\S[^\\，]*).日志内容.(\\S*)",
                    "regularExpression": "<(\\d+)>\\s([^\r\n]*)\\sFWsadsad\\s(\\S*)\\s(\\d)\\s(\\d).....(\\S[^\\，]*)....(\\S[^\\，]*)....(\\S[^\\，]*)...IP.(\\S[^\\，]*)....(\\S[^\\，]*)......(\\S[^\\，]*)......(\\S*)",
                    "status": 1
                }
                time.sleep(2)
                # 创建范化策略响应
                url_policy = test_url + '/ics/genera-police/save?T=1665622769346'
                resp_policy = requests.post(url=url_policy, headers=hd, json=data_self_4value, verify=False)
                # print(resp_policy.text)
                if i == test_par:
                    print(resp_policy.text)
                    if '200' in resp_policy.text and '添加策略成功' in resp_policy.text:
                        print('事件分析-范化策略构造完成！')
                    else:
                        print('err_message:', '事件分析-范化策略构造存在异常！')
                        print('err_message:', '请检查Cookies与请求参数！')
    except Exception as e:
        print('err_message:{}'.format(e))
