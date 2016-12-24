#!/usr/bin/env python
# coding=utf-8
import gen_key
import redis

def save_key_redis(keys):
    conn=redis.Redis()
    for key in keys:
        conn.lpush('list',key)
    list=conn.lrange('list',0,-1)
    print(list)

if '__name__==__main__':
    keys=gen_key.gene_activation_code(200,25)
    print(keys)
    save_key_redis(keys)
