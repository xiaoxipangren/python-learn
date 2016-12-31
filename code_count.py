#!/usr/bin/env python
# coding=utf-8
import re,sys,os

def judge(line,pattern):
    return re.match(pattern,line)

def isSpaceLine(line):
    return judge(line,r'^\s*$')

def isCommentLine(line):
    return judge(line,'^#')

def code_count(file):
    fin=open(file,'rt')
    print(file)
    space=0
    comment=0
    code=0
    for line in fin:
        if(isSpaceLine(line)):
            space+=1
        elif(isCommentLine(line)):
            comment+=1
        else:
            code+=1
    print('space:',space,',comment:',comment,',code:',code)



code_count(os.path.abspath(sys.argv[0]))

