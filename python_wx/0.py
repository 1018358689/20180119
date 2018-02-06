#!/usr/bin/env python
# -*- coding:utf-8 -*-
from wxpy import *

import time

import picamera

# 初始化微信机器人，扫码登录

bot = Bot(console_qr=True, cache_path=True, qr_path='/qrco.png')

# bot = Bot(console_qr=False)

my_friend = bot.friends().search('11')[0]

# 初始化图灵机器人

tuling = Tuling(api_key='66e65491744d4b569587ef649c1121b7')


# 自动回复所有文字消息

@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    # 当接受到文字为pp时，拍摄照片

    if msg.text == 'pp':

        # 初始化照相机

        with picamera.PiCamera() as camera:
            camera.resolution = (1024, 768)

            # 摄像头预热2秒

            camera.start_preview()
            time.sleep(2)

            # 捕获图像

            camera.capture('wx_image.jpg')

            # 发送给请求者

            my_friend.send_image('wx_image.jpg')

            # 关闭摄像头，释放资源

            camera.close()

    # 当接受到文字为vv时，录制视频

    elif msg.text == 'vv':

        with picamera.PiCamera() as camera:

            camera.resolution = (640, 480)

            # 摄像头预热2秒

            camera.start_preview()
            time.sleep(2)

            # 录制视频，视频格式为h264

            camera.start_recording('wx_video.h264', format='h264', quality=23)

            camera.wait_recording(11)

            camera.stop_recording()

            # MP4Box -add wx_video.h264 wx_video.mp4

            my_friend.send_video('wx_video.h264')

            camera.close()

    else:

        tuling.do_reply(msg)


# 开始运行

bot.join()
