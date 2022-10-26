# 安全分析-例外-新建例外
import requests

test_cookies = 'JSESSIONID=470cbbb5-fed1-4776-a10e-e8f950363f26'
url = 'https://172.16.6.224/ics/api/policies/exclude/add?T=1648024999112'

for i in range(20,80):
    par = '172.16.15.%s' % i

    hd = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Connection': 'keep-alive',
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
  "addrType": "ip",
  "id": "",
  "dst": "any",
  "policiesDevices": [],
  "ruleId": "any",
  "src": par,
  "srcPort": "any",
  "dstPort": "any",
  "proto": "any"
}


    resp = requests.post(url=url,headers=hd,json=data,verify=False)
    print(resp.text)

