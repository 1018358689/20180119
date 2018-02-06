#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
# import os
import win32gui, win32ui, win32con, win32api
from PIL import Image
import pytesseract

def binarizing(img,threshold): #二值化
    pix_data = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pix_data[x, y] < threshold:
                pix_data[x, y] = 0
            else:
                pix_data[x, y] = 255
    return img

def window_capture(filename1, filename2):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    # MoniterDev = win32api.EnumDisplayMonitors(None, None)
    # w = MoniterDev[0][2][2]
    # h = MoniterDev[0][2][3]
    w1 = 380
    h1 = 150
    w2 = 380
    h2 = 190
    height = 200
    saveBitMap.CreateCompatibleBitmap(mfcDC, w1, h1)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w1, h1), mfcDC, (20, height), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename1)
    saveBitMap.CreateCompatibleBitmap(mfcDC, w2, h2)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w2, h2), mfcDC, (20, h1 + height), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename2)


# 冲顶大会 170 上无篮框 200 上有篮框
# 花椒直播-百万赢家 166 上无框 170 上有框
def ocr():
    window_capture('Que_ocr.jpg', 'Ans_ocr.jpg')
    Que_img = Image.open('Que_ocr.jpg')
    Que_ocr = pytesseract.image_to_string(Que_img, lang='chi_sim').replace(' ', '').replace('\n',
                                                                                                              '')
    try:
        Que_ocr = re.findall('(?<=\d\.).*', Que_ocr)[0]
    except:
        Que_ocr = Que_ocr

    Ans_img = Image.open('Ans_ocr.jpg')
    # Ans_img = Ans_img.convert('L') #灰度化
    # Ans_img = binarizing(Ans_img, 206) #可调参数
    # Ans_img.save('Ans_ocr2.jpg')
    Ans_ocr = pytesseract.image_to_string(Ans_img, lang='chi_sim').replace(' ', '').split('\n')
    Ans_ocr = [x for x in Ans_ocr if x != '']
    return Que_ocr, Ans_ocr


def p_it(Que_ocr, Ans_ocr):
    print(Que_ocr)
    for i in range(len(Ans_ocr)):
        print('{}: {}'.format(i + 1, Ans_ocr[i]))
    print('')

if __name__ == '__main__':
    Que = '新装修的房子通常哪种化学物质含量会比较高?'
    Ans = ['甲醛', '苯', '甲醇']
    p_it(Que, Ans)