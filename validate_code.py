#!/usr/bin/env python
# coding=utf-8
import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import string 

def gene_str(length):
    letters=list(string.ascii_uppercase)
    numbers=[str(num) for num in range(10)]
    letters+=numbers
    key=''
    for i in range(length):
        key+=random.choice(letters)
    return key

def draw_points(draw,size,chance):
    width,height=size
    for w in range(width):
        for h in range(height):
            tmp = random.randint(0,50)
            if tmp > 50 - chance:
                draw.point((w,h),fill=(0,0,0))

def draw_str(draw,size,font_type,font_size,fg_color,content):
    font=ImageFont.truetype(font_type,font_size)
    f_w,f_h=font.getsize(content)
    w,h=size
    draw.text(((w-f_w)/3,(h-f_h)/4),content,font=font,fill=fg_color)




def gen_code(content,bg_color=(255,255,255),fg_color=(255,0,0)):
    size=(120,30)
    img=Image.new('RGB',size,bg_color)
    draw=ImageDraw.Draw(img)
    draw_str(draw,size,'/home/haiqing/.local/share/fonts/msyh.ttc',18,fg_color,content)
    draw_points(draw,size,10)
    img=img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img
def gen_code_img(file):
    content = gene_str(10)
    print(content)
    img= gen_code(content)
    img.save(file)

gen_code_img('validate_code.png')





    
    
