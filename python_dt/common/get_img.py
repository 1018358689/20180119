#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from PIL import Image
import time
import subprocess
import win32gui, win32ui, win32con, win32api

def binarizing(img, threshold):  # 二值化
    pix_data = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pix_data[x, y] < threshold:
                pix_data[x, y] = 0
            else:
                pix_data[x, y] = 255
    return img


def window_capture(filename1='Que_ocr.png', filename2='Ans_ocr.png'):
    # hwnd = 0
    hwnd = win32gui.FindWindow(None, 'BlueStacks App Player')
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    # MoniterDev = win32api.EnumDisplayMonitors(None, None)
    # w = MoniterDev[0][2][2]
    # h = MoniterDev[0][2][3]
    w1 = 380
    h1 = 66  # 150
    w2 = 380
    h2 = 190
    height = 210
    saveBitMap.CreateCompatibleBitmap(mfcDC, w1, h1)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w1, h1), mfcDC, (20, height), win32con.SRCCOPY)  # 1：起始位置（截图内容）2：长宽 4：截图位置
    saveBitMap.SaveBitmapFile(saveDC, filename1)
    saveBitMap.CreateCompatibleBitmap(mfcDC, w2, h2)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w2, h2), mfcDC, (20, h1 + height), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename2)


# 模拟器 简单搜索h1=66 else h1=150
# 百万英雄 170
# 冲顶大会 170 上无篮框 200 上有篮框
# 花椒直播-百万赢家 166 上无框 170 上有框

adb_bin = os.path.join('adb', "adb.exe")


def adb_screen1(filename='scr_win.png'):
    os.system("{0} shell /system/bin/screencap -p /sdcard/{1}".format(adb_bin, 'scr_ad.png'))
    os.system("{0} pull /sdcard/{1} {2}".format(adb_bin, 'scr_ad.png', os.path.join(filename)))


def adb_screen2(filename='scr_win.png'):
    process = subprocess.Popen(
        "{0} shell /system/bin/screencap -p".format(adb_bin),
        shell=True, stdout=subprocess.PIPE)
    binary_screenshot = process.stdout.read().replace(b'\r\r\n', b'\n')
    with open(os.path.join(filename), "wb") as writer:
        writer.write(binary_screenshot)


def adb_capture(filename1='Que_ocr.png', filename2='Ans_ocr.png', game_num = '1'):
    adb_screen2('scr_win.png')
    # time_start = time.time()
    j_d = [290, 150, 330]
    h_j = [290, 250, 363]
    c_j = [220, 180, 330]
    x_g = [290, 240, 363]
    position = []
    if game_num == '1':
        position = j_d
    elif game_num == '2':
        position = h_j
    elif game_num == '3':
        position = c_j
    elif game_num == '4':
        position = x_g
    else:
        print('\n***输入错误****\n')
    x1 = 33
    y1 = position[0]
    x2 = 680 #700
    y2 = position[1] + y1
    # 简单搜索 y1:290 y2:150
    # 花椒 y1:290 y2:250     2&3&4
    # 冲顶大会 y1:220 y2:180  1&2
    # 西瓜 y1:290 y2:240      1&2
    Que_size = (x1, y1, x2, y2)  # （x1，y1）和（x2，y2）定位
    x3 = x1
    y3 = y2
    x4 = x2
    y4 = position[2] + y2
    # else 330
    # 花椒 西瓜 363
    Ans_size = (x3, y3, x4, y4)
    img = Image.open('scr_win.png')
    img = img.convert('L')
    # img = binarizing(img, 222)  # 可调参数
    Que_img = img.crop(Que_size)
    Ans_img = img.crop(Ans_size)
    Que_img.save(filename1)
    Ans_img.save(filename2)
    # time_end = time.time()
    # print(time_end - time_start)

