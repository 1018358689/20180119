#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import re
from pprint import pprint
station_id_url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9039'
response = requests.get(station_id_url).text
content = re.compile('([\u4e00-\u9fa5]+)\|([A-Z]+)').findall(response)

pprint(content)

# dict_result = {}
# for i in content:
#     dict_result[i[0]] = i[1]

dict_result = dict(content)

pprint(dict_result) #parse_station_id.py > stations.py