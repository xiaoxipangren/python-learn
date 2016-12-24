#!/usr/bin/env python
# coding=utf-8
from  gen_key import gene_activation_code
import sqlite3
def save_sqllite(data,dbfile):
    conn=sqlite3.connect(dbfile)
    curs=conn.cursor()
    curs.execute('''
                 Create table keys(id INT PRIMARY KEY,key VARCHAR(25))
                 ''')
    ins='Insert into keys values(?,?)'

    for i in range(len(data)):
        curs.execute(ins,(i,data[i]))

    return 0

data=gene_activation_code(200,25)
print(data)
save_sqllite(data,'keys.db')

