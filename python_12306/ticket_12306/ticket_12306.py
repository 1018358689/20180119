#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
import sys
import requests
from trains_collection import TrainsCollection
from docopt import docopt
from colorama import init,Fore
from stations import stations_id

init(autoreset=True)

def cli():
    """command-line interface"""
    # arguments = docopt(__doc__)
    try:
        arguments = docopt(__doc__)
    except:
        print('输入不合规\n正确例子：-gd 上海 杭州 2018-1-24')
        sys.exit(1)

    options = ''.join([
        key for key, value in arguments.items() if value is True
    ])
    error_str = Fore.RED + '----------查无结果----------' + Fore.RESET

    from_station = stations_id[arguments['<from>']]
    to_station = stations_id[arguments['<to>']]
    date = arguments['<date>']
    new_url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date,from_station,to_station
    )
    headers = {
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
    }
    response = requests.get(url=new_url,headers=headers) #verify = False
    # print(response.status_code)
    response.encoding = 'utf-8-sig'
    # pprint(response)
    try:
        available_trains = response.json()['data']['result']
        if len(available_trains):
            TrainsCollection(available_trains, options).pretty_print()
        else:
            print(error_str)
    except:
        print(error_str)

if __name__ == '__main__':
    cli()
