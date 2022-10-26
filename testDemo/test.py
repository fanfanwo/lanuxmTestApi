import json, random, time
from datetime import datetime
from kafka import KafkaProducer


class Test_KafkaProducer():
    def __init__(self):
        try:
            ser_ip = '172.16.16.101:10020'
            self.topic = 'event'
            dn = datetime.now()
            self.producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                          bootstrap_servers=ser_ip)
            self.testdate = str(dn)[0:19]
            print("*"*20)
            print('服务器地址：%s' % ser_ip)
            print('主题：%s' % self.topic)
        except Exception as e:
            print('连接kafka失败！')
            print(e)

    def data_json(self):
        # str = "<390>Mar 30 13:47:32 USG CONFIG: SerialNum=0811020909210070 GenTime=\"%s\" SrcIP=12.1.1.1 DstIP=192.168.1.1 Protocol=tcp SrcPort=21 DstPort=21 InInterface=eth0 OutInterface=eth1 VOIPName=H323 FwPolicyID= Action=PASS Content=\"other content\"" % self.testdate
        # data = {
        #     "msg": str,
        #     "engine_id": 1,
        #     "engine_ip": "192.168.166.21",
        #     "task_id": 1,
        #     "src_ip": "172.16.24.100",
        #     "timestamp": "2022-05-11 21:21:34"
        # }
        data = {"msg":"²»ºāˣ¬ɕ־τ¼þoĦˇ¿յÜn","engine_id":1,"engine_ip":"172.16.15.99","task_id":1,"src_ip":"192.168.166.111","timestamp":"1652265177818"}
        print(data)
        return data

    def kafkaproducer(self,val):
        try:
            starttime = datetime.now()
            print('开始时间：', starttime)
            if val == 0:
                while True:
                    self.producer.send(self.topic, self.data_json())
                    print('写入内容：', self.data_json)
                    # time.sleep(1)
                    # self.producer.close()
            else:
                for i in range(val+1):
                    self.producer.send(self.topic, self.data_json())
                    # print(self.data_json())
                self.producer.close()
                endtime = datetime.now()
                print("写入数据条数：%s" % i)
                print("结束时间：",endtime)
                print('进程耗时：', endtime - starttime)
                print("*" * 20)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    print('发送日志到kafka；指定发送数量：1-100000；输入0时为持续发送，输入其他无效。')
    # val = int(input('输入数量值：'))
    # Test_KafkaProducer().kafkaproducer(val)
    while True:
        try:
            val = int(input('输入数量值:'))
            if val == 0:
                Test_KafkaProducer().kafkaproducer(val)
                break
            elif val not in range(1, 100001):
                print('超出范围，,重新输入')
            else:
                Test_KafkaProducer().kafkaproducer(val)
                break
        except ValueError:
            print('数据类型错误,重新输入')