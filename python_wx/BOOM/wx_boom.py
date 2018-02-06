#!/usr/bin/env python
# -*- coding:utf-8 -*-

from wxpy import Bot
import datetime
import time
from f_str import fuck_str
import random

random.seed(datetime.datetime.now())
f_str = fuck_str


def check_yn_input(str_input):
    while str_input != 'y' and str_input != 'n' and len(str_input) != 0:
        str_input = input('\n输入错误,请重新输入 y/n[y]: ')
    return str_input

def check_sz_input(str_input):
    while str_input != 's' and str_input != 'z':
        str_input = input('\n输入错误,请重新输入 s or z: ')
    return str_input

i = 0
_ = input('**等一下你要扫码登录 ok?**\n回车扫码 -->')
bot = Bot(cache_path=False, console_qr=False, qr_path='QR_code.png')

check = 'n'
while check == 'n':
    person0 = input('\n请输入你要轰炸的人的微信名字：')
    person = bot.friends().search(person0)
    if len(person) == 0:
        print('查无此人!')
        continue
    person = person[0]
    check = input('\n一切与我无关哦\n确定轰炸"{}"?  y/n[y]: '.format(person0))
    check = check_yn_input(check)
co = input('\n随机内容轰炸,还是指定内容轰炸?\ns-随机内容\nz-指定内容\n输入上述序号: ')
co = check_sz_input(co)
if co == 'z':
    check = 'n'
    while check == 'n':
        c_input = input('\n请输入你的轰炸文本: ')
        check = input('\n确定轰炸文本为"{}"?  y/n[y]: '.format(c_input))
        check = check_yn_input(check)
_ = input('\n轰炸准备开始,轰炸中按【Ctrl+C】即可停止轰炸！\n回车开始轰炸 -->')
while 1:
    i += 1
    if co == 's':
        content = f_str[random.randrange(len(f_str))]
    else:
        content = c_input
    time.sleep(random.uniform(0, 1) + 0.5)
    print('第{}次轰炸 BOOM! "{}"'.format(i, content))
    person.send(content)
