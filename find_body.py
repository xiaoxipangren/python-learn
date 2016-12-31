#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup as soup

def parseHtml(html,elem):
    page=soup(html)
    tag=page.find(elem)
    return tag

fin=open('redis.html','rt')
html=fin.read()
fin.close()
print(parseHtml(html,'body'))

