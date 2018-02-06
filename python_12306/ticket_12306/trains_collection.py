#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
from colorama import init, Fore
from prettytable import PrettyTable
import prettytable
from stations import stations_id
from pprint import pprint

init(autoreset=True)

class TrainsCollection:
    header = '车次 车站 时间 历时 商务特等座 一等座 二等座 高级软卧 软卧 动卧 硬卧 软座 硬座 无座 备注'.split(' ')

    def __init__(self, available_trains, options):
        self.available_trains = available_trains  # available_trains: 一个列表, 包含着所有车次的信息
        # self.station_id = station_id  # station_id: 一个字典，包含不同代号对应的站点
        self.options = options  # options: 查询的选项, 如高铁, 动车, etc...

    def get_duration(self, duration):
        duration = duration.replace(':', '小时') + '分'
        if duration.startswith('00'):
            return duration[4:]
        elif duration.startswith('0'):
            return duration[1:]
        else:
            return duration

    def trains_info(self):
        dic_station_1 = stations_id
        dic_station_2 = dict(zip(dic_station_1.values(), dic_station_1.keys()))
        for raw_train in self.available_trains:
            # pprint(raw_train)
            train_type = re.compile('(?<=\|)([A-Z])\d+(?=\|)').findall(raw_train)[0].lower() #排除非用户所选的 options
            if train_type in self.options and '停运' not in raw_train or not self.options:
                station = re.compile('(?<=\|)[A-Z]{3}(?=\|)').findall(raw_train)
                f_station = station[2]
                t_station = station[3]
                train = {
                    'train_id': re.compile('(?<=\|)([A-Z]\d+)(?=\|)').findall(raw_train)[0],
                    'f_station': dic_station_2[f_station],
                    't_station': dic_station_2[t_station],
                    'f_t_station' : Fore.CYAN+dic_station_2[f_station]+Fore.RESET+ '\n'+Fore.MAGENTA+dic_station_2[t_station]+Fore.RESET,
                    'f_time': re.compile('(?<=\|)(\d{2}:\d{2})(?=\|)').findall(raw_train)[0],
                    't_time': re.compile('(?<=\|)(\d{2}:\d{2})(?=\|)').findall(raw_train)[1],
                    'f_t_time' : Fore.CYAN+re.compile('(?<=\|)(\d{2}:\d{2})(?=\|)').findall(raw_train)[0]+Fore.RESET+'\n'+Fore.MAGENTA+re.compile('(?<=\|)(\d{2}:\d{2})(?=\|)').findall(raw_train)[1]+Fore.RESET,
                    'duration': self.get_duration(re.compile('(?<=\|)(\d{2}:\d{2})(?=\|)').findall(raw_train)[2]),
                    'SWZ': raw_train.split('|')[-5],
                    'YDZ': raw_train.split('|')[-6],
                    'EDZ': raw_train.split('|')[-7],
                    'GJRW': raw_train.split('|')[-16],
                    'RW': raw_train.split('|')[-14],
                    'DW': raw_train.split('|')[-4],
                    'YW': raw_train.split('|')[-9],
                    'RZ': raw_train.split('|')[-13],
                    'YZ': raw_train.split('|')[-8],
                    'WZ': raw_train.split('|')[-11],
                    'BZ': re.compile('(?<=\|)[\u4e00-\u9fa5]{1}.*?[\u4e00-\u9fa5]{1}(?=\|)').findall(raw_train)[0]
                    # 'QT': raw_train.split('|')[-],
                }
                for train_key in train:
                    if train[train_key] == '无':
                        train[train_key] = '售完'
                    elif train[train_key] == '有':
                        train[train_key] = Fore.LIGHTGREEN_EX+'充足'+Fore.RESET
                if '<br/>' in train['BZ']:
                    train['BZ'] = Fore.LIGHTRED_EX+train['BZ'].replace('<br/>', '')+ Fore.RESET
                for train_key in train:
                    if not train[train_key]:
                        train[train_key] = '--'
                yield train

    def pretty_print(self):
        pt = PrettyTable(self.header)
        pt.hrules = prettytable.ALL
        pt.vrules = prettytable.FRAME
        pt.padding_width = 1
        pt.align = 'c'
        pt.valign = 'm'
        for i in self.trains_info():
            pt.add_row([i['train_id'],i['f_t_station'],i['f_t_time'],i['duration'],i['SWZ'],i['YDZ'],i['EDZ'],i['GJRW'],i['RW'],i['DW'],i['YW'],i['RZ'],i['YZ'],i['WZ'],i['BZ']])
        print(pt)

