#!/usr/bin/env python
# -*- coding:utf-8 -*-

from wxpy import *
bot = Bot(cache_path=True, console_qr=True, qr_path='QR_code.png')
print(bot.self)
# bot.enable_puid(path='wxpy_puid.pkl')
# fh = bot.file_helper
# print(fh.puid)

# bot.self.add()
# bot.self.accept()
# bot.self.send_image('1.png')
# m_id = bot.upload_file('1.png')
ys = bot.friends(update=True).search(keywords='颜色')[0]
# ys.send('@img@1.png',m_id)
ys.get_avatar('ys.jpg')