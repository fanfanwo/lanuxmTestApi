'''
通过爬虫获取省市区县，并将数据存放到excel(province.xls)文件的sheet页中(province)

'''
import xlwt
import requests
from bs4 import BeautifulSoup
class SavePro():
    def get_response(self, url, attr):
        headers = {
            'Connection': 'close'
        }
        response = requests.get(url, headers=headers)  # 发送请求并获得返回

        response.encoding = 'UTF-8'  # 编码转换
        soup = BeautifulSoup(response.text, 'html.parser')  # 分析数据

        table = soup.find_all('tbody')[1].tbody.tbody.table
        if attr:
            trs = table.find_all('tr', attrs={'class': attr})
        else:
            trs = table.find_all('tr')
        # print(trs)
        return trs

    def deal_data(self):
        base_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2021/'  # 地址数据url
        trs = self.get_response(base_url, 'provincetr')  # 获取返回值
        print(trs)
        num = 1
        provs = []
        for tr in trs:  # 循环每一行
            for tp in tr:  # 循环每个省
                province_name = tp.a.get_text()
                province_url = base_url + tp.a.attrs['href']
                print("province_name:" + province_name)
                print("province_url:" + province_url)
                trs = self.get_response(province_url, None)
                print(trs)
                for tci in trs[1:]:  # 循环每个市
                    print("city")
                    print(tci)
                    city_name = tci.find_all('td')[1].string
                    if city_name == '市辖区':
                        city_name = province_name
                    print("city_name")
                    print(city_name)

                    city_url = base_url + tci.a.attrs['href']
                    print('city_url')
                    print(city_url)
                    trs = self.get_response(city_url, None)
                    for tco in trs[1:]:
                        country_name = tco.find_all('td')[1].string
                        print("country_name")
                        print(country_name)
                        if country_name == '市辖区':
                            continue
                        prov = [num, province_name, city_name, country_name]  # 每一行省市区
                        print(prov)
                        provs.append(prov)
                        num += 1
        print(len(provs))
        return provs

    def write_pro(self,provs):
        # 新建工作蒲
        workbook = xlwt.Workbook()
        # 新建工作表并重命名
        worksheet = workbook.add_sheet("province")
        title = ['编号', '省', '市', '区']  # 把表头名称放入list里面
        # 循环把表头写入
        col = 0
        for t in title:
            worksheet.write(0, col, t)
            col += 1
        row = 1
        for p in provs:
            col = 0
            for v in p:
                worksheet.write(row,col,v)
                col += 1
            row += 1
        # 保存
        workbook.save('assetData.xls')

lp = SavePro().deal_data() #爬虫获取省市区到 并存放到列表中
SavePro().write_pro(lp) #将列表的省市区写入到excel中