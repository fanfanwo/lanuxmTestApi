#!/usr/bin/env python
# 防护评估-添加防护评估

import requests,unittest,random,urllib3,datetime,time
from common.getConfig import Config

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


test_par = int(Config().get('heads','par'))
test_url = Config().get('heads','url')
test_cookies = Config().get('heads','cookies')
test_Token = Config().get('heads','token')
# print(test_url,test_cookies)
test_eventLevel = [1, 2]



class test_Outgoingdata(unittest.TestCase):
    try:
        for i in range(1, test_par+1):
            par = '评估任务-自动构造%s' % i
            test_type = random.choice(test_eventLevel)
            url = test_url + '/ics/api/assess/task/add_or_update?T=1647510273656'
            startTime = str(int(time.time())) + '000'
            today = datetime.date.today()
            acquire = today + datetime.timedelta(days=2)
            endTime = str(int(time.mktime(time.strptime(str(acquire), '%Y-%m-%d'))) - 1) + '000'

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
                "modifyTime": startTime,
                "createTime": startTime,
                "id": '',
                "name": par,
                "description": "评估任务描述。。。",
                "specification": "工业控制系统信息安全防护能力评估方法",
                "mode": 1,
                "object": "1",
                "startTime": startTime,
                "endTime": endTime,
                "agency": 2,
                "status": test_type
            }

            resp = requests.post(url=url, headers=hd, json=data, verify=False)
            # print(resp.text)
            if i == test_par:
                print(resp.text)
                if '200' in resp.text and '添加防护评估任务数据成功' in resp.text:
                    print('防护评估-添加防护评估任务数据成功！')
                else:
                    print('err_message:','防护评估-添加防护评估任务失败！')
                    print('err_message:','请检查Cookies与请求参数！')
    except Exception as e:
        print('err_message:{}'.format(e))


