# 读取项目绝对路径
import os

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFDIR = os.path.join(dir, 'config')
# print(dir)
# print(CONFDIR)
