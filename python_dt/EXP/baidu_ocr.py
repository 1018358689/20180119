#!/usr/bin/env python
# -*- coding:utf-8 -*-

from aip import AipOcr

def getFile(filePath):
  with open(filePath, 'rb') as file:
    content = file.read()
    file.close()
    return content

APP_ID = '10693105'
API_KEY = 'uL9tgRmnNy5cOvqwvO4vqdze'
SECRET_KEY = 'PI2nSH8vsFOutC2e0Qx2vzKfrTWAlWMm'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
print(client)

ocr_result = client.basicGeneral(getFile('Que_ocr.jpg'))['words_result']
result = [x['words'] for x in ocr_result]
result = ''.join(result)
print(result)