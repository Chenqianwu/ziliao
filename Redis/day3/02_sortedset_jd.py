import redis

r = redis.Redis(host='127.0.0.1',port=6379,password='123456',db=0)

# 第1天
day01_dict = {
    'huawei' : 5000,
    'oppo'   : 4000,
    'iphone' : 3000
}
# 第2天
day02_dict = {
    'huawei' : 5200,
    'oppo'   : 4300,
    'iphone' : 3230
}
# 第3天
day03_dict = {
    'huawei' : 5500,
    'oppo'   : 4660,
    'iphone' : 3580
}
r.zadd('mobile-day01',day01_dict)
r.zadd('mobile-day02',day02_dict)
r.zadd('mobile-day03',day03_dict)
#并集:(key,(z1,z2,z3),aggregate='max')
r.zunionstore('mobile-day01:03',('mobile-day01','mobile-day02','mobile-day03'),aggregate='max')
rlist = r.zrevrange('mobile-day01:03',0,-1,withscores=True)

i = 1
for r in rlist:
    print('第{}名：{}'.format(i,r[0].decode()) )
    i+=1