'''生产者负责生产url地址'''

import redis
import random
import time

r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')


#生成很多个url地址,放到redis的列表中
for i in range(1,20):
    url='http://app.mi.com/#page=' + str(i)
    #放到redis列表
    r.lpush('xiaomi:urls',url)
    #随机休眠3-5s
    time.sleep(random.randint(3,5))



















