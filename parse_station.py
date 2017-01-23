# /usr/bin/python3.
# -*- coding: utf-8 -*-

"""取得城市的英文缩写，保存在 stations.py 里面"""

from pprint import pprint
import re
import requests


urls = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
response = requests.get(urls, verify=False)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
pprint(dict(stations), indent=4)
