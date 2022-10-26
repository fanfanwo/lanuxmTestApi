#!/usr/bin/env python
import time
import logging.handlers

logger = logging.getLogger()
fh = logging.handlers.SysLogHandler(('172.16.15.106', 514), logging.handlers.SysLogHandler.LOG_AUTH)

n = 1
while True:
    try:
        # time.sleep(5)
        # # logger = logging.getLogger()
        # # fh = logging.handlers.SysLogHandler(('172.16.16.101', 514), logging.handlers.SysLogHandler.LOG_AUTH)
        formatter_1 = logging.Formatter('<1>Jul 12 14:59:18 D12;530000000119051342010751;ipv4;3; servconn_policy: time=2019-07-12 14:59:18;policy_name=out;server_addr=192.168.24.80;out_addr=192.168.24.255;proto=UDP;port=137;action=1')
        # print('111',formatter_1)
        fh.setFormatter(formatter_1)
        logger.addHandler(fh)
        logger.warning("msg")

        n = n+1
        print(n)
    except Exception as e:
        print('err_message',e)