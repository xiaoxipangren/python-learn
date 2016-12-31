#!/usr/bin/env python
# coding=utf-8
import word_count as wc
import os
def word_count_article(dir):
    result={}
    for article in os.listdir(dir):
        dic=wc.word_count(dir+article)
        print(dic)
        key,count=max(list(dic.items()),key=lambda d:d[1] )
        result[str(article)]=key
    
    return result

result = word_count_article('/home/haiqing/Documents/Vim/code/insert_mode/')
print(result)
