#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
while True:
    resptext = requests.get('http://htpmsg.jiecaojingxuan.com/msg/current').text
    resptext_dict = json.loads(resptext)
    print(resptext_dict)