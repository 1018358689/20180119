#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PIL import Image
import pytesseract
from time import time
import imageio
from aip import AipOcr

# APP_ID = '10693105'
# API_KEY = 'uL9tgRmnNy5cOvqwvO4vqdze'
# SECRET_KEY = 'PI2nSH8vsFOutC2e0Qx2vzKfrTWAlWMm'
APP_ID = '10708120'
API_KEY = 'YWTDaVMGz0bYB7SGeWZdgnSu'
SECRET_KEY = 'Pr5wbojMVAgLObQzoSOqST6F4ZTF25AB'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def getFile(filePath):
  with open(filePath, 'rb') as file:
    content = file.read()
    file.close()
    return content

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

img = Image.open('jt.jpg')
# img = img.convert('L')
# new_img = binarizing(img, 206)
# imageio.imsave('img2.jpg', new_img)
# new_img.save('img2.jpg')
s_time = time()
# ocr_result = pytesseract.image_to_string(Image.open('Que_ocr.jpg'), lang='chi_sim') # lang='chi_sim'
ocr_result2 = client.basicGeneral(getFile('jt.jpg'))
e_time = time()
print(ocr_result2)
print(e_time - s_time)
