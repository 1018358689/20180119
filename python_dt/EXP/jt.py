#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
# import os
from skimage.io import imsave
import win32gui, win32ui, win32con, win32api
from PIL import Image
import pytesseract

# 二值化算法
def binarizing(img,threshold):
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

def window_capture(filename1):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    # MoniterDev = win32api.EnumDisplayMonitors(None, None)
    # w = MoniterDev[0][2][2]
    # h = MoniterDev[0][2][3]
    # w = 380
    # h = 150
    w_h = (380, 190)
    saveBitMap.CreateCompatibleBitmap(mfcDC, w_h[0], w_h[1])
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), w_h, mfcDC, (20, 316), win32con.SRCCOPY)#第一个参数是输出图像的开始位置
    saveBitMap.SaveBitmapFile(saveDC, filename1)

window_capture('jt.jpg')
Qus_img = Image.open('jt.jpg')
# Qus_img = Qus_img.convert('L')
# Qus_img = binarizing(Qus_img, 106)
# imsave('jt2.jpg',Qus_img)
Ans_ocr = pytesseract.image_to_string(Qus_img, lang='chi_sim').replace(' ','').split('\n')
Ans_ocr = [x for x in Ans_ocr if x != '']
print(Ans_ocr)