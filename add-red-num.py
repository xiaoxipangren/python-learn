#!/usr/bin/env pythonmZ# coding=utf-8
from PIL import Image,ImageDraw,ImageFont

def add_num(img):
    draw=ImageDraw.Draw(img) 
    fillcolor='#ff0000'
    width,height=img.size
    draw.text((width-40,0),'99',fill=fillcolor)
    img.save('/home/haiqing/Pictures/result.png')
    return 0

image=Image.open('/home/haiqing/Pictures/pic.png')
add_num(image)
