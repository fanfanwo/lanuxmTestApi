#!/usr/bin/env python
import time
import logging.handlers

logger = logging.getLogger()
fh = logging.handlers.SysLogHandler(('172.16.15.202', 514), logging.handlers.SysLogHandler.LOG_AUTH)

n = 1
while True:
    try:
        # time.sleep(5)
        # # logger = logging.getLogge r()
        # # fh = logging.handlers.SysLogHandler(('172.16.16.101', 514), logging.handlers.SysLogHandler.LOG_AUTH)
        formatter_1 = logging.Formatter('refused connect from 161.77.172.20 (161.77.172.20)\nDid not receive identifsdasdsasdomnjsdddsdication string from 71.191.170.112')
        # print('111',formatter_1)
        fh.setFormatter(formatter_1)
        logger.addHandler(fh)
        logger.warning("msg")

        n = n+1
        print(n)
    except Exception as e:
        print('err_message',e)