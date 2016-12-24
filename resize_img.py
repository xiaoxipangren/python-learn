#!/usr/bin/env python
# coding=utf-8
import os
from PIL import Image

def resize_img(dir,w,h):
    files=list(os.listdir(dir))
    print(files)
    for image in files:
        img=Image.open(dir+image)
        iw,ih=img.size
        f1=iw/w
        f2=ih/h
        f=max([f1,f2])
        img=img.resize((int(f1*w),int(f1*h)),Image.ANTIALIAS)
        f=os.path.basename(image)
        name,ext=os.path.splitext(f)
        newName=dir+name+'_resize'+ext
        img.save(newName)

resize_img('/home/haiqing/Pictures/',640,1136)
