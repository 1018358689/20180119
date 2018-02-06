#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
from wxpy import *

bot = Bot(cache_path=False, console_qr=False, qr_path='QR_code.png')
print(bot.self)
# ys = bot.friends().search('11')[0]
tuling = Tuling(api_key='66e65491744d4b569587ef649c1121b7')
xiaoi = XiaoI(key='SlIwok1GCxXz',secret='udcoWc0C98CPXzahIZol')

@bot.register()
def print_messages(msg):
    print(msg)


@bot.register(chats=bot.chats(), msg_types=TEXT)
def get_msg(msg):
    xiaoi.do_reply(msg)
    i = datetime.datetime.now()
    # now_time = '{}:{}:{}'.format(i.hour, i.minute, i.second)
    print('{}  {}  {}'.format(msg.create_time, msg.sender.name, msg.text)) #msg.create_time



bot.join()
# embed()
