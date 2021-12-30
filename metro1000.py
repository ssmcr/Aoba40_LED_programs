#!/usr/bin/env python3
# coding: UTF-8

import time
import sys
import csv
from PIL import Image, ImageDraw,ImageFont
from rgbmatrix import RGBMatrix, RGBMatrixOptions

# 使用するLEDのパラメーター(この辺はgithubのサンプルのコピペです)
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 4
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.gpio_slowdown = 2
matrix = RGBMatrix(options = options)

img1 = Image.open('metro1000/pics/metro1000_asakusa.ppm')
img2 = Image.open('metro1000/pics/metro1000_asakusa1.ppm')
 
images = []
i = 1
k = 4
j = 4
while True :  # スクロール画像を生成
    ims_base = Image.new("RGB",(128,32),(0,0,0))
    if i <=40 :
        ims_base.paste(img1)
    elif (40 < i and i <= 45):
        ims_base.paste(img1,(0,k))
        ims_base.paste(img2,(0,-32+k))
        k += 4
    elif (45 < i and i <= 48):
        ims_base.paste(img1,(0,k))
        ims_base.paste(img2,(0,-32+k))
        k += 2
    elif (48 < i and i <= 50):
        ims_base.paste(img1,(0,k))
        ims_base.paste(img2,(0,-32+k))
        k += 1
    elif (50 < i and i <= 90):
        ims_base.paste(img2)
    elif (90 < i and i <= 95):
        ims_base.paste(img2,(0,j))
        ims_base.paste(img1,(0,-32+j))
        j += 4
    elif (95 < i and i <= 98):
        ims_base.paste(img2,(0,j))
        ims_base.paste(img1,(0,-32+j))
        j += 2
    elif (98 < i and i <= 100):
        ims_base.paste(img2,(0,j))
        ims_base.paste(img1,(0,-32+j))
        j += 1
    images.append(ims_base)
    if i == 100:
        break
    else:
        i += 1

while True:
    for im_scroll in images:
        matrix.SetImage(im_scroll)
        time.sleep(0.1)
     
