#!/usr/bin/env python
import time
import logging.handlers

logger = logging.getLogger()
fh = logging.handlers.SysLogHandler(('172.16.3.108', 514), logging.handlers.SysLogHandler.LOG_AUTH)

while True:
    try:
        time.sleep(5)
        # logger = logging.getLogger()
        # fh = logging.handlers.SysLogHandler(('172.16.16.101', 514), logging.handlers.SysLogHandler.LOG_AUTH)
        formatter_1 = logging.Formatter('<133>EFW: TCP_FLAG: rule=TCPECN action=strip_ECN recvif=ge1 srcip=60.28.240.120 destip=10.161.136.249 ipproto=TCP ipdatalen=20 srcport=80 destport=4890 rst=1 ack=1 cwr=1')
        # print('111',formatter_1)
        fh.setFormatter(formatter_1)
        logger.addHandler(fh)
        logger.warning("msg")
        formatter_2 = logging.Formatter('SESLOG: tcp inside/10.99.129.39(1529) -> outside/60.28.240.120(80) (session create) [bridge 0 id 6311709]; ip=10.99.128.121')
        # print('222',formatter_2)
        fh.setFormatter(formatter_2)
        logger.addHandler(fh)
        logger.warning("msg")

    except Exception as e:
        print('err_message',e)