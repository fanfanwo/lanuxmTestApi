#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
从excel的province sheet页读取省市区
'''
import json,time
import xlrd
from faker import Faker
from datetime import datetime
from kafka import KafkaProducer


class Test_KafkaProducer():
    def __init__(self):
        self.fa = Faker(locale='zh_CN')
        self.producer = KafkaProducer(value_serializer=lambda m: json.dumps(m,ensure_ascii=False).encode(),
                                      bootstrap_servers=['172.16.16.207:10020'])

    def data_json(self):
        dataexcel = xlrd.open_workbook('assetData.xls')  #exceL
        protable = dataexcel.sheet_by_name('province')  #存放省市区的sheet页
        ipmactable = dataexcel.sheet_by_name('ip_mac')  #存放IP/MAC的sheet页
        datalis = []
        num = 100  #获取
        i = 484
        while num:
            if num % 10 == 0: #取编号为10的余数 对应的省市区 作为资产数据的省市区--可修改
                prodata = protable.row_values(i)
            else:
                prodata = protable.row_values(i + 1)
            ipdata = ipmactable.col_values(0)
            macdata = ipmactable.col_values(1)
            t = str(int(round((time.time() * 1000)))) #时间戳
            deviceName = prodata[1] + prodata[2] + prodata[3] + "-功率控制系统"
            vendorChn = prodata[1] + "代理"
            data = {
                "deviceTypeOneName": "设备",
                "businessSoftware": [],
                "internal": "1",
                "isHaveDB": "0",
                "outageTime": "0",
                "deviceScore": "5",
                "licenseExpiredTime": "0",
                "storageTime": t,
                "vendorChn": vendorChn,
                "physicalRegion": "2",
                "deviceTypeTwo": "网络设备",
                "inputTime": t,
                "deviceName": deviceName,
                "deviceTypeTwoName": "操作员站",
                "isVirtualMachine": "0",
                "safeDefendSoftware": [],
                "safetyOfTime": "0",
                "commissioningTime": "0",
                "security": "5",
                "database": [],
                "usability": "5",
                "orgCode": "00001000370000500007",
                "isFreeAsset": "0",
                "manageState": "0",
                "sourceCity": prodata[2],
                "ipList": [{
                    "type": "业务",
                    "ipAddr": ipdata[num],
                    "macAddr": macdata[num]
                }],
                "businessSector": "3",
                "sourceFactory": "local",
                "os": [],
                "isDelete": "0",
                "integrality": "5",
                "updateTime": "0",
                "deviceTypeOne": "5",
                "maintenanceTime": "0",
                "createTime": t,
                "sourceProvince": prodata[1],
                "isStandby": "0",
                "isImportantAsset": "0",
                "deviceModel": "SU-GAP2",
                "insertDataBaseFunction": "1",
                "sourcePrefecture": prodata[3],
                "otherSoftware": []

            }

            datalis.append(data)
            # json.dumps(data, ensure_ascii=False)
            num -= 1
            i += 1
            # datajson = json.dumps(datalis, ensure_ascii=False)

        return datalis


    def kafkaproducer(self):
        starttime = datetime.now()
        print('开始时间',starttime)
        # dataFanhua = {"factoryTwoCode":"3","ceventName":"","cprotocolDtail":"","lOccurTime":1666683155000,"cAttack":"","cSrcRegion":"","ccollectorType":"FLOW","deviceSrcMac":"db:2c:76:61:80:74","cDstIp":"116.130.229.123","cDstName":"","cDstRegion":"","deviceName":"","sid":1020831,"cDstMac":"12:23:32:12:12:12","cSrcMac":"21:32:23:23:23:23","ceventSType":"","cUserName":"","cActions":"","imergeCount":1,"signaturemsg":"6cb311115cb6~~eth2~~3~~6cb311115cb4~~16~~3~~10~~col_1661913565052~~_05806_20220902174249.pcap","StationIP":"10.156.147.200","cCollectorTime":"","cMsgType":1,"sourceCity":"山西省","app":"","sourceFactory":"fcyshanxi","cDevIp":"","cRule":"/access","ceventDigest":"","ceventLevel":"","deviceCode":"","cCollectorIp":"","cEventMsg":" POLICY Empty User-Agent Header","cDevSn":"","cDevType":"/security","iDstPort":80,"sourceProvince":"太原市","cSrcName":"","ceventType":"","cprotocol":"TCP","incidentId":"1020831","cSrcIp":"10.156.147.149","iSrcPort":4687,"sourcePrefecture":"古交市"}
        # for i in range(1, 5):
        while True:
            self.producer.send('asset1', self.data_json()) #资产数据
            # self.producer.send('fanhua', dataFanhua)  # 范化数据
            print(self.data_json())
            # i += 1
        endtime = datetime.now()
        print('进程耗时：', endtime - starttime)

if __name__ == '__main__':
    """
    说明：
        1.修改本地hosts-在hosts中添加数据资产平台的节点信息
            内容如下：
                172.16.8.180	manager.datafort
                172.16.8.181	node1.datafort
                172.16.8.182	node2.datafort
        2.控制数据量-修改kafkaproducer中循环的次数
        3.更换topic-修改kafkaproducer中producer.send的值
        Topic：一组消息数据的标记符
        Producer：生产者，用于生产数据，可将生产后的消息送入指定的Topic
        Consumer：消费者，获取数据，可消费指定的Topic
        Partition：分区，为了保证kafka的吞吐量，一个Topic可以设置多个分区。同一分区只能被一个消费者订阅
        Group：消费者组，同一个group可以有多个消费者，一条消息再一个group 中，只会被一个消费者获取
    """
    Test_KafkaProducer().kafkaproducer()

    # Test_KafkaProducer().data_json()
