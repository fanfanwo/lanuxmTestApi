#!/usr/bin/env python
import time
import logging.handlers
from logging.handlers import SysLogHandler

logger = logging.getLogger("mylog")
# log_format = logging.Formatter("hhl-%(name)s-server[%(process)d]-%(levelname)s:%(message)s")
fh = logging.handlers.SysLogHandler(('172.16.16.135', 514), logging.handlers.SysLogHandler.LOG_AUTH) #   LOG_AUTH = 4       #  security/authorization messages
print("logger:",logger)
n = 1
num = 4
while num:
    try:
        # time.sleep(5)
        # # logger = logging.getLogger()
        # # fh = logging.handlers.SysLogHandler(('172.16.16.101', 514), logging.handlers.SysLogHandler.LOG_AUTH)
        # test_str = 'refused connect from 161.77.172.20 (161.77.172.20)\nDid not receive identifsdasdsasdomnjsdddsdication string from 71.191.170.112'
        formatter_1 = logging.Formatter("hhl-%(name)s-server[%(process)d]-%(levelname)s:%(message)s")
        fh.setFormatter(formatter_1)
        logger.addHandler(fh)
        logger.warning("msg")

        # n = n+1
        # if n == 10:
        #     time.sleep(10)
        #     n = 1
        # print(n)

    except Exception as e:
        print('err_message',e)
        num -= 1