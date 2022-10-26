# 读取配置文件

import os
from configparser import ConfigParser
from common.getfiledir import dir


class Config(ConfigParser):

    def __init__(self):
        self.conf_name = os.path.join(dir, 'config.ini')
        super().__init__()
        super().read(self.conf_name, encoding='utf-8')

    def save_data(self, section, option, value):
        super().set(section=section, option=option, value=value)
        super().write(fp=open(self.conf_name, 'w'))

if __name__ == '__main__':
    con = Config()
    type = con.get('heads', 'cookies')
    print(type)


