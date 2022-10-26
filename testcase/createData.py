'''
随机生成1000个 IP和MAC各存放到列表中，
然后将列表的IP和MAC写入到excel 中(assetData.xls的sheet页ip_mac)
'''
import xlrd
from xlutils.copy import copy as xl_copy
import struct
import socket
import random
RANDOM_IP_POOL=['192.168.10.222/0']

class Creat_data():

    def get_random_ip(self):
        ips = [] #多个IP
        str_ip = RANDOM_IP_POOL[random.randint(0, len(RANDOM_IP_POOL) - 1)]
        str_ip_addr = str_ip.split('/')[0]
        str_ip_mask = str_ip.split('/')[1]
        ip_addr = struct.unpack('>I', socket.inet_aton(str_ip_addr))[0]
        mask = 0x0
        num = 1000 #生成IP个数
        while num:
            for i in range(31, 31 - int(str_ip_mask), -1):
                mask = mask | (1 << i)
            ip_addr_min = ip_addr & (mask & 0xffffffff)
            ip_addr_max = ip_addr | (~mask & 0xffffffff)
            ip = socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))  #单个随机IP
            ips.append(ip)
            num -= 1
        # print(ips)
        return ips

    def get_random_mac(self):
        macsingle = [] #1个mac地址
        macs = []  #多个mac地址
        num = 1000 #随机生产1000个mac地址
        while num:
            for i in range(1, 7):
                mac_char = ''.join(random.sample('0123456789abcdef', 2))
                macsingle.append(mac_char)
                mac = ':'.join(macsingle)
                if i == 6:
                    macsingle=[]
            macs.append(mac)
            num -= 1
        # print(macs)
        return macs

    def write_pro(self,ipdata, macdata):
        #打开已经存在的工作表
        rb = xlrd.open_workbook('assetData.xls',formatting_info=True)
        wb = xl_copy(rb)
        sheet = wb.add_sheet('ip_mac')
        title = ['ip','mac']
        col = 0
        for t in title:
            sheet.write(0, col, t)
            col += 1
        row = 1
        for ip in ipdata:
            sheet.write(row,0,ip)
            row += 1
        row = 1
        for mac in macdata:
            sheet.write(row,1,mac)
            row += 1
        wb.save('assetData.xls')



ipdata = Creat_data().get_random_ip() #生成1000个IP地址 存放到ipdata列表中
macdata = Creat_data().get_random_mac() #生成1000个IP地址 存放到macdata列表中
Creat_data().write_pro(ipdata,macdata) #将ip和mac写入到excel中
