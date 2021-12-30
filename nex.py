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
options.brightness = 80
options.parallel = 1
options.brightness = 100
options.gpio_slowdown = 2
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.gpio_slowdown = 2
matrix = RGBMatrix(options = options)

images = []

for num in range (1,26,1):
    file_name = 'nex/pics/nex_' + str(num) + '.png'
    img = Image.open(file_name)
    images.append(img)

anime = []

for flame in range (0,49): 
   ims_base = Image.new("RGB",(128,32),(0,0,0))
   ims_base.paste(images[0])
   anime.append(ims_base)

for flame in range (50,79):
   ims_base = Image.new("RGB",(128,32),(0,0,0))
   ims_base.paste(images[1])
   anime.append(ims_base)

for flame in range (80,89):
   ims_base = Image.new("RGB",(128,32),(0,0,0))
   anime.append(ims_base)

for komasu in range (4,16):
   ims_base = Image.new("RGB",(128,32),(0,0,0))
   ims_base.paste(images[komasu])
   anime.append(ims_base)

for flame in range (93,95):
   ims_base = Image.new("RGB",(128,32),(0,0,0))
   ims_base.paste(images[17])
   anime.append(ims_base)

for komasu in range (18,25):
   ims_base = Image.new("RGB",(128,32),(0,0,0))
   ims_base.paste(images[komasu])
   anime.append(ims_base)

for flame in range(10):
    ims_base = Image.new("RGB",(128,32),(0,0,0))
    anime.append(ims_base)

while True:
    for im_scroll in anime:
        matrix.SetImage(im_scroll)
        time.sleep(0.1)
     
