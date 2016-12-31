#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup as soup

def parseHtml(html,elem,attr):
    page=soup(html)
    return [element.get(attr) for element in page.find_all(elem)]

fin=open('redis.html','rt')
html=fin.read()

print(parseHtml(html,'a','href'))


