#!/usr/bin/env python
# 事件分析-关联分析-添加策略

import requests,unittest,random,urllib3,time
from common.getConfig import Config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


test_par = int(Config().get('heads','par'))
test_url = Config().get('heads','url')
test_cookies = Config().get('heads','cookies')
test_Token = Config().get('heads','token')
# print(test_url,test_cookies)
test_enable = [1,0]
# 关注点
test_observationPoint = ['SRC_IP','DST_IP']
# 攻击阶段
test_attackPhase = ['INVESTIGATION','TARGETED_ATTACK','TARGET_AIM','IMPLANT_TOOL']
# 置信度
test_confidence = ['HIGH_RISK','IN_DANGER','LOW_RISK']



class test_Associationanalysis(unittest.TestCase):
    try:
        for i in range(1, test_par+1):

            par = '关联分析策略-自动构造%s' % i
            url = test_url + '/ics/api/aasrules/rule?T=1649212771315'
            mock_enable = random.choice(test_enable)
            mock_observationPoint = random.choice(test_observationPoint)
            mock_attackPhase = random.choice(test_attackPhase)
            mock_confidence = random.choice(test_confidence)

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
                  "createtime": "",
                  "description": "策略描述。。。",
                  "diffField": "",
                  "enable": mock_enable,
                  "eventMatchBeanList": [
                    {
                      "createtime": 0,
                      "eventMatchName": "event_1",
                      "expression": "{\"bool\":{\"must\":[{\"term\":{\"ieventpri\":\"5\"}}]}}",
                      "orgExpression": "{\"condition\":\"AND\",\"rules\":[{\"id\":\"ieventpri\",\"field\":\"ieventpri\",\"type\":\"string\",\"input\":\"text\",\"operator\":\"equal\",\"value\":\"5\"}]}",
                      "id": "",
                      "isDelete": 0,
                      "matchFlag": 1,
                      "matchFields": "",
                      "modifytime": 1649813786135
                    }
                  ],
                  "exeCycle": 1,
                  "exeCycleUnit": 2,
                  "expression": "",
                  "hasAlertRecord": 1,
                  "hasCorrelateEvent": 1,
                  "hits": "1",
                  "id": "",
                  "isDelete": 0,
                  "jobTime": "",
                  "jobTimeUnit": "",
                  "modifytime": 1649813786135,
                  "repeatTriggerDeadzone": 3,
                  "repeatTriggerDeadzoneUnit": 2,
                  "ruleAlertRecordList": [
                    {
                      "alertContent": "告警描述",
                      "alertFieldName": "generic.rule_name",
                      "alertName": "generic.rule_name",
                      "createtime": "",
                      "id": 0,
                      "isDelete": 0,
                      "modifytime": 1649813786135,
                      "ruleId": "",
                      "alertType": 4
                    }
                  ],
                  "ruleName": par,
                  "sameField": "",
                  "treeId": 31
                }


            resp = requests.post(url=url, headers=hd, json=data, verify=False)
            # print(resp.text)
            if i == test_par:
                print(resp.text)
                if '200' in resp.text and '操作成功' in resp.text:
                    print('事件分析-关联分析策略构造完成！')
                else:
                    print('err_message:','事件分析-关联分析构造存在异常！')
                    print('err_message:','请检查Cookies与请求参数！')
    except Exception as e:
        print('err_message:{}'.format(e))


