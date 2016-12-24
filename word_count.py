#!/usr/bin/env python
# coding=utf-8
import re
def word_count(file):
    fin=open(file,'rt')
    dic={}
    for line in fin:
        for word in re.split('\s',line):
            if word in dic:
                dic[word]=dic[word]+1
            else:
                dic[word]=1
    return dic
dic=word_count('redis.html')
for key in dic:
    print(key,dic[key])
