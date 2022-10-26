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
def creat_group(hd):
    url = test_url + '/ics/api/select/tree/add?T=1663894183071'
    group_name = "upgradePre1"
    group_xpathValue = "/pgradePre1%s"

    group = {
        "createTime": "",
        "creatorId": "",
        "creatorName": "",
        "defaultFlag": 0,
        "description": "fcytest",
        "icon": "",
        "id": 0,
        "modifyTime": "",
        "nodeName": group_name,
        "nodeTypeFlag": 0,
        "nodeValue": group_name,
        "parentId": 22,
        "sharedFlag": 1,
        "statusFlag": 1,
        "treeType": 7,
        "xpath": "",
        "xpathValue": group_xpathValue
    }
    resg = requests.post(url=url, headers=hd, json=group, verify=False)
    rd = json.loads(resg.text)
    print(resg.text)
    if '200' in resg.text and '添加成功' in resg.text:
        itemGroupId = rd["result"]
        print(f'监视项组创建成功 ！itemGroupId = {itemGroupId}')
        return itemGroupId
    else:
        print('err_message:', '监视项组存在异常！')
        print('err_message:', '请检查Cookies与请求参数！')

def create_items(hd,itemGroupId):
    cpu_util = {
        "alarm": 0,
        "alarmDesc": "",
        "alarmLevel": 2,
        "alarmModel": "0",
        "restoreConditions": "",
        "triggerCondition": "",
        "timeDead": 30,
        "itemStatus": 0,
        "itemName": "system.cpu.util[,,]",
        "itemShowDesc": "CPU利用率",
        "gatherWay": "15",
        "formula": "100-last(\"system.cpu.util[,,free]\")",
        "teamName": "",
        "port": 161,
        "oid": "",
        "dateType": 0,
        "unit": "%",
        "gatherCycle": 10,
        "monitorObjectId": 1,
        "itemGroupId": itemGroupId,
        "creatorId": 0,
        "id": 0,
        "createdTime": "",
        "creatorName": "",
        "modifiedTime": "",
        "modifiedId": 0,
        "modifiedName": ""
    }
    cpu_free = {
        "alarm": 0,
        "alarmDesc": "",
        "alarmLevel": 2,
        "alarmModel": "0",
        "restoreConditions": "",
        "triggerCondition": "",
        "timeDead": 30,
        "itemStatus": 0,
        "itemName": "system.cpu.util[,,free]",
        "itemShowDesc": "CPU空闲率",
        "gatherWay": "4",
        "formula": "",
        "teamName": "public",
        "port": 161,
        "oid": ".1.3.6.1.4.1.2021.11.11.0",
        "dateType": 0,
        "unit": "%",
        "gatherCycle": 10,
        "monitorObjectId": 1,
        "itemGroupId": itemGroupId,
        "creatorId": 0,
        "id": 0,
        "createdTime": "",
        "creatorName": "",
        "modifiedTime": "",
        "modifiedId": 0,
        "modifiedName": ""
    }
    vfs_pused = {
        "alarm": 0,
        "alarmDesc": "",
        "alarmLevel": 2,
        "alarmModel": "0",
        "restoreConditions": "",
        "triggerCondition": "",
        "timeDead": 30,
        "itemStatus": 0,
        "itemName": "vfs.fs.size[/,pused]",
        "itemShowDesc": "磁盘利用率",
        "gatherWay": "15",
        "formula": "100*last(\"vfs.fs.size[/,occupy]\")/last(\"vfs.fs.size[/,total]\")",
        "teamName": "",
        "port": 161,
        "oid": "",
        "dateType": 0,
        "unit": "%",
        "gatherCycle": 10,
        "monitorObjectId": 3,
        "itemGroupId": itemGroupId,
        "creatorId": 0,
        "id": 0,
        "createdTime": "",
        "creatorName": "",
        "modifiedTime": "",
        "modifiedId": 0,
        "modifiedName": ""
    }
    vfs_total = {
        "alarm": 0,
        "alarmDesc": "",
        "alarmLevel": 2,
        "alarmModel": "0",
        "restoreConditions": "",
        "triggerCondition": "",
        "timeDead": 30,
        "itemStatus": 0,
        "itemName": "vfs.fs.size[/,total]",
        "itemShowDesc": "磁盘总大小",
        "gatherWay": "4",
        "formula": "",
        "teamName": "public",
        "port": 161,
        "oid": "1.3.6.1.4.1.2021.9.1.6.1",
        "dateType": 0,
        "unit": "KB",
        "gatherCycle": 10,
        "monitorObjectId": 3,
        "itemGroupId": itemGroupId,
        "creatorId": 0,
        "id": 0,
        "createdTime": "",
        "creatorName": "",
        "modifiedTime": "",
        "modifiedId": 0,
        "modifiedName": ""
    }
    vfs_occupy = {
        "alarm": 0,
        "alarmDesc": "",
        "alarmLevel": 2,
        "alarmModel": "0",
        "restoreConditions": "",
        "triggerCondition": "",
        "timeDead": 30,
        "itemStatus": 0,
        "itemName": "vfs.fs.size[/,occupy]",
        "itemShowDesc": "已使用磁盘大小",
        "gatherWay": "4",
        "formula": "",
        "teamName": "public",
        "port": 161,
        "oid": ".1.3.6.1.4.1.2021.9.1.8.1",
        "dateType": 0,
        "unit": "KB",
        "gatherCycle": 10,
        "monitorObjectId": 3,
        "itemGroupId": itemGroupId,
        "creatorId": 0,
        "id": 0,
        "createdTime": "",
        "creatorName": "",
        "modifiedTime": "",
        "modifiedId": 0,
        "modifiedName": ""
    }
    mem_cus = {
        "alarm": 0,
        "alarmDesc": "",
        "alarmLevel": 2,
        "alarmModel": "0",
        "restoreConditions": "",
        "triggerCondition": "",
        "timeDead": 30,
        "itemStatus": 0,
        "itemName": "customizedMEM",
        "itemShowDesc": "内存利用率",
        "gatherWay": "15",
        "formula": "(last(\"vm.memory.size[total]\")-last(\"vm.memory.size[available]\")-last(\"vm.memory.size[cached]\")-last(\"vm.memory.size[buffer]\"))/last(\"vm.memory.size[total]\")*100",
        "teamName": "",
        "port": 161,
        "oid": "",
        "dateType": 0,
        "unit": "%",
        "gatherCycle": 10,
        "monitorObjectId": 2,
        "itemGroupId": itemGroupId,
        "creatorId": 0,
        "id": 0,
        "createdTime": "",
        "creatorName": "",
        "modifiedTime": "",
        "modifiedId": 0,
        "modifiedName": ""
    }
    mem_total = {
        "alarm": 0,
        "alarmDesc": "",
        "alarmLevel": 2,
        "alarmModel": "0",
        "restoreConditions": "",
        "triggerCondition": "",
        "timeDead": 30,
        "itemStatus": 0,
        "itemName": "vm.memory.size[total]",
        "itemShowDesc": "总内存",
        "gatherWay": "4",
        "formula": "",
        "teamName": "public",
        "port": 161,
        "oid": ".1.3.6.1.4.1.2021.4.5.0",
        "dateType": 0,
        "unit": "KB",
        "gatherCycle": 10,
        "monitorObjectId": 2,
        "itemGroupId": itemGroupId,
        "creatorId": 0,
        "id": 0,
        "createdTime": "",
        "creatorName": "",
        "modifiedTime": "",
        "modifiedId": 0,
        "modifiedName": ""
    }
    mem_cached = {
        "alarm": 0,
        "alarmDesc": "",
        "alarmLevel": 2,
        "alarmModel": "0",
        "restoreConditions": "",
        "triggerCondition": "",
        "timeDead": 30,
        "itemStatus": 0,
        "itemName": "vm.memory.size[cached]",
        "itemShowDesc": "隐藏内存",
        "gatherWay": "4",
        "formula": "",
        "teamName": "public",
        "port": 161,
        "oid": ".1.3.6.1.4.1.2021.4.15.0",
        "dateType": 0,
        "unit": "KB",
        "gatherCycle": 10,
        "monitorObjectId": 2,
        "itemGroupId": itemGroupId,
        "creatorId": 0,
        "id": 0,
        "createdTime": "",
        "creatorName": "",
        "modifiedTime": "",
        "modifiedId": 0,
        "modifiedName": ""
    }
    mem_buffer = {
        "alarm": 0,
        "alarmDesc": "",
        "alarmLevel": 2,
        "alarmModel": "0",
        "restoreConditions": "",
        "triggerCondition": "",
        "timeDead": 30,
        "itemStatus": 0,
        "itemName": "vm.memory.size[buffer]",
        "itemShowDesc": "缓冲内存",
        "gatherWay": "4",
        "formula": "",
        "teamName": "pubblic",
        "port": 161,
        "oid": ".1.3.6.1.4.1.2021.4.14.0",
        "dateType": 0,
        "unit": "KB",
        "gatherCycle": 10,
        "monitorObjectId": 2,
        "itemGroupId": itemGroupId,
        "creatorId": 0,
        "id": 0,
        "createdTime": "",
        "creatorName": "",
        "modifiedTime": "",
        "modifiedId": 0,
        "modifiedName": ""
    }
    mem_avaliable = {
        "alarm": 0,
        "alarmDesc": "",
        "alarmLevel": 2,
        "alarmModel": "0",
        "restoreConditions": "",
        "triggerCondition": "",
        "timeDead": 30,
        "itemStatus": 0,
        "itemName": "vm.memory.size[available]",
        "itemShowDesc": "可用内存",
        "gatherWay": "4",
        "formula": "",
        "teamName": "public",
        "port": 161,
        "oid": ".1.3.6.1.4.1.2021.4.6.0",
        "dateType": 0,
        "unit": "KB",
        "gatherCycle": 10,
        "monitorObjectId": 2,
        "itemGroupId": itemGroupId,
        "creatorId": 0,
        "id": 0,
        "createdTime": "",
        "creatorName": "",
        "modifiedTime": "",
        "modifiedId": 0,
        "modifiedName": ""
    }
    items = [cpu_util, cpu_free, vfs_total, vfs_pused, vfs_occupy, mem_total, mem_cus, mem_cached, mem_buffer,
             mem_avaliable]
    url_table = test_url + '/ics/monitor-item/save?T=1663892543731'
    try:
        for index, i in enumerate(items):
            time.sleep(2)
            print(f"{index}:{i}")
            resm = requests.post(url=url_table, headers=hd, json=i, verify=False)
            print(resm.text)
            if "200" in resm.text and "添加监视项成功" in resm.text:
                print(f'监视项创建成功 !')
    except Exception as e:
        print('err_message:{}'.format(e))


class test_StateTemplate_monitorItem(unittest.TestCase):

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
    itemGroupId = creat_group(hd)
    create_items(hd,itemGroupId)
    '''
    try:
        for i in range(1, test_par + 1):
            # par = 'fcy_Auto%s' % i
            url = test_url + '/ics/api/select/tree/add?T=1663894183071'
            group_name = "again%s" % i
            group_xpathValue = "/eqwe%s" % i

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

            group = {
                "createTime": "",
                "creatorId": "",
                "creatorName": "",
                "defaultFlag": 0,
                "description": "fcytest",
                "icon": "",
                "id": 0,
                "modifyTime": "",
                "nodeName": group_name,
                "nodeTypeFlag": 0,
                "nodeValue": group_name,
                "parentId": 22,
                "sharedFlag": 1,
                "statusFlag": 1,
                "treeType": 7,
                "xpath": "",
                "xpathValue": group_xpathValue
            }

            resg = requests.post(url=url, headers=hd, json=group, verify=False)
            rd = json.loads(resg.text)
            print(resg.text)
            # {"responseCode": 200, "result": 100000006, "values": {}, "message": "添加成功"}
            if '200' in resg.text and '添加成功' in resg.text:
                itemGroupId = rd["result"]
                print(f'监视项组创建成功 ！itemGroupId = {itemGroupId}')
                cpu_util = {
                    "alarm": 0,
                    "alarmDesc": "",
                    "alarmLevel": 2,
                    "alarmModel": "0",
                    "restoreConditions": "",
                    "triggerCondition": "",
                    "timeDead": 30,
                    "itemStatus": 0,
                    "itemName": "system.cpu.util[,,]",
                    "itemShowDesc": "CPU利用率",
                    "gatherWay": "15",
                    "formula": "100-last(\"system.cpu.util[,,free]\")",
                    "teamName": "",
                    "port": 161,
                    "oid": "",
                    "dateType": 0,
                    "unit": "%",
                    "gatherCycle": 10,
                    "monitorObjectId": 1,
                    "itemGroupId": itemGroupId,
                    "creatorId": 0,
                    "id": 0,
                    "createdTime": "",
                    "creatorName": "",
                    "modifiedTime": "",
                    "modifiedId": 0,
                    "modifiedName": ""
                }
                cpu_free = {
                    "alarm": 0,
                    "alarmDesc": "",
                    "alarmLevel": 2,
                    "alarmModel": "0",
                    "restoreConditions": "",
                    "triggerCondition": "",
                    "timeDead": 30,
                    "itemStatus": 0,
                    "itemName": "system.cpu.util[,,free]",
                    "itemShowDesc": "CPU空闲率",
                    "gatherWay": "4",
                    "formula": "",
                    "teamName": "public",
                    "port": 161,
                    "oid": ".1.3.6.1.4.1.2021.11.11.0",
                    "dateType": 0,
                    "unit": "%",
                    "gatherCycle": 10,
                    "monitorObjectId": 1,
                    "itemGroupId": itemGroupId,
                    "creatorId": 0,
                    "id": 0,
                    "createdTime": "",
                    "creatorName": "",
                    "modifiedTime": "",
                    "modifiedId": 0,
                    "modifiedName": ""
                }
                vfs_pused = {
                    "alarm": 0,
                    "alarmDesc": "",
                    "alarmLevel": 2,
                    "alarmModel": "0",
                    "restoreConditions": "",
                    "triggerCondition": "",
                    "timeDead": 30,
                    "itemStatus": 0,
                    "itemName": "vfs.fs.size[/,pused]",
                    "itemShowDesc": "磁盘利用率",
                    "gatherWay": "15",
                    "formula": "100*last(\"vfs.fs.size[/,occupy]\")/last(\"vfs.fs.size[/,total]\")",
                    "teamName": "",
                    "port": 161,
                    "oid": "",
                    "dateType": 0,
                    "unit": "%",
                    "gatherCycle": 10,
                    "monitorObjectId": 3,
                    "itemGroupId": itemGroupId,
                    "creatorId": 0,
                    "id": 0,
                    "createdTime": "",
                    "creatorName": "",
                    "modifiedTime": "",
                    "modifiedId": 0,
                    "modifiedName": ""
                }
                vfs_total = {
                    "alarm": 0,
                    "alarmDesc": "",
                    "alarmLevel": 2,
                    "alarmModel": "0",
                    "restoreConditions": "",
                    "triggerCondition": "",
                    "timeDead": 30,
                    "itemStatus": 0,
                    "itemName": "vfs.fs.size[/,total]",
                    "itemShowDesc": "磁盘总大小",
                    "gatherWay": "4",
                    "formula": "",
                    "teamName": "public",
                    "port": 161,
                    "oid": "1.3.6.1.4.1.2021.9.1.6.1",
                    "dateType": 0,
                    "unit": "KB",
                    "gatherCycle": 10,
                    "monitorObjectId": 3,
                    "itemGroupId": itemGroupId,
                    "creatorId": 0,
                    "id": 0,
                    "createdTime": "",
                    "creatorName": "",
                    "modifiedTime": "",
                    "modifiedId": 0,
                    "modifiedName": ""
                }
                vfs_occupy = {
                    "alarm": 0,
                    "alarmDesc": "",
                    "alarmLevel": 2,
                    "alarmModel": "0",
                    "restoreConditions": "",
                    "triggerCondition": "",
                    "timeDead": 30,
                    "itemStatus": 0,
                    "itemName": "vfs.fs.size[/,occupy]",
                    "itemShowDesc": "已使用磁盘大小",
                    "gatherWay": "4",
                    "formula": "",
                    "teamName": "public",
                    "port": 161,
                    "oid": ".1.3.6.1.4.1.2021.9.1.8.1",
                    "dateType": 0,
                    "unit": "KB",
                    "gatherCycle": 10,
                    "monitorObjectId": 3,
                    "itemGroupId": itemGroupId,
                    "creatorId": 0,
                    "id": 0,
                    "createdTime": "",
                    "creatorName": "",
                    "modifiedTime": "",
                    "modifiedId": 0,
                    "modifiedName": ""
                }
                mem_cus = {
                    "alarm": 0,
                    "alarmDesc": "",
                    "alarmLevel": 2,
                    "alarmModel": "0",
                    "restoreConditions": "",
                    "triggerCondition": "",
                    "timeDead": 30,
                    "itemStatus": 0,
                    "itemName": "customizedMEM",
                    "itemShowDesc": "内存利用率",
                    "gatherWay": "15",
                    "formula": "(last(\"vm.memory.size[total]\")-last(\"vm.memory.size[available]\")-last(\"vm.memory.size[cached]\")-last(\"vm.memory.size[buffer]\"))/last(\"vm.memory.size[total]\")*100",
                    "teamName": "",
                    "port": 161,
                    "oid": "",
                    "dateType": 0,
                    "unit": "%",
                    "gatherCycle": 10,
                    "monitorObjectId": 2,
                    "itemGroupId": itemGroupId,
                    "creatorId": 0,
                    "id": 0,
                    "createdTime": "",
                    "creatorName": "",
                    "modifiedTime": "",
                    "modifiedId": 0,
                    "modifiedName": ""
                }
                mem_total = {
                    "alarm": 0,
                    "alarmDesc": "",
                    "alarmLevel": 2,
                    "alarmModel": "0",
                    "restoreConditions": "",
                    "triggerCondition": "",
                    "timeDead": 30,
                    "itemStatus": 0,
                    "itemName": "vm.memory.size[total]",
                    "itemShowDesc": "总内存",
                    "gatherWay": "4",
                    "formula": "",
                    "teamName": "public",
                    "port": 161,
                    "oid": ".1.3.6.1.4.1.2021.4.5.0",
                    "dateType": 0,
                    "unit": "KB",
                    "gatherCycle": 10,
                    "monitorObjectId": 2,
                    "itemGroupId": itemGroupId,
                    "creatorId": 0,
                    "id": 0,
                    "createdTime": "",
                    "creatorName": "",
                    "modifiedTime": "",
                    "modifiedId": 0,
                    "modifiedName": ""
                }
                mem_cached = {
                    "alarm": 0,
                    "alarmDesc": "",
                    "alarmLevel": 2,
                    "alarmModel": "0",
                    "restoreConditions": "",
                    "triggerCondition": "",
                    "timeDead": 30,
                    "itemStatus": 0,
                    "itemName": "vm.memory.size[cached]",
                    "itemShowDesc": "隐藏内存",
                    "gatherWay": "4",
                    "formula": "",
                    "teamName": "public",
                    "port": 161,
                    "oid": ".1.3.6.1.4.1.2021.4.15.0",
                    "dateType": 0,
                    "unit": "KB",
                    "gatherCycle": 10,
                    "monitorObjectId": 2,
                    "itemGroupId": itemGroupId,
                    "creatorId": 0,
                    "id": 0,
                    "createdTime": "",
                    "creatorName": "",
                    "modifiedTime": "",
                    "modifiedId": 0,
                    "modifiedName": ""
                }
                mem_buffer = {
                    "alarm": 0,
                    "alarmDesc": "",
                    "alarmLevel": 2,
                    "alarmModel": "0",
                    "restoreConditions": "",
                    "triggerCondition": "",
                    "timeDead": 30,
                    "itemStatus": 0,
                    "itemName": "vm.memory.size[buffer]",
                    "itemShowDesc": "缓冲内存",
                    "gatherWay": "4",
                    "formula": "",
                    "teamName": "pubblic",
                    "port": 161,
                    "oid": ".1.3.6.1.4.1.2021.4.14.0",
                    "dateType": 0,
                    "unit": "KB",
                    "gatherCycle": 10,
                    "monitorObjectId": 2,
                    "itemGroupId": itemGroupId,
                    "creatorId": 0,
                    "id": 0,
                    "createdTime": "",
                    "creatorName": "",
                    "modifiedTime": "",
                    "modifiedId": 0,
                    "modifiedName": ""
                }
                mem_avaliable = {
                    "alarm": 0,
                    "alarmDesc": "",
                    "alarmLevel": 2,
                    "alarmModel": "0",
                    "restoreConditions": "",
                    "triggerCondition": "",
                    "timeDead": 30,
                    "itemStatus": 0,
                    "itemName": "vm.memory.size[available]",
                    "itemShowDesc": "可用内存",
                    "gatherWay": "4",
                    "formula": "",
                    "teamName": "public",
                    "port": 161,
                    "oid": ".1.3.6.1.4.1.2021.4.6.0",
                    "dateType": 0,
                    "unit": "KB",
                    "gatherCycle": 10,
                    "monitorObjectId": 2,
                    "itemGroupId": itemGroupId,
                    "creatorId": 0,
                    "id": 0,
                    "createdTime": "",
                    "creatorName": "",
                    "modifiedTime": "",
                    "modifiedId": 0,
                    "modifiedName": ""
                }
                items = [cpu_util,cpu_free,vfs_total,vfs_pused,vfs_occupy,mem_total,mem_cus,mem_cached,mem_buffer,mem_avaliable]
                url_table = test_url + '/ics/monitor-item/save?T=1663892543731'
                for index,i in enumerate(items):
                    time.sleep(2)
                    try:
                        print(f"i:{i}")
                        resm = requests.post(url=url_table, headers=hd, json=i, verify=False)
                        print(resm.text)
                        if "200" in resm.text and "添加监视项成功" in resm.text:
                            print(f'监视项创建成功 !')
                    except Exception as e:
                        print('err_message:{}'.format(e))

            else:
                print('err_message:', '监视项组存在异常！')
                print('err_message:', '请检查Cookies与请求参数！')

    except Exception as e:
        print('err_message:{}'.format(e))
    '''