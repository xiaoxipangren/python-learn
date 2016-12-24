#!/usr/bin/env python
# coding=utf-8
import random
import string

def gene_activation_code(num,length):
    result=[]
    source=list(string.ascii_uppercase)
    num_list=[str(num) for num in range(0,10)]
    source+=num_list
    while len(result)<num:
        key=''
        for i in range(length):
            key+=random.choice(source)
        if key in result:
            continue
        else:
            result.append(key)
    return result
if __name__=='__main__':
    number=200
    length=25
    keys=gene_activation_code(number,length)
    print(keys)

