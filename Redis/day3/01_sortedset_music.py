import redis

r = redis.Redis(host='127.0.0.1',port=6379,password='123456',db=0)
#zadd ranking 1 song1 1 song2 1 song3
#注意参数为字典类型{'元素':'分值'}
r.zadd('ranking',{'song1':1,'song2':1,'song3':1,'song4':1})
r.zadd('ranking',{'song5':1,'song6':1,'song7':1})
r.zadd('ranking',{'song8':1,'song9':1})

#给任意三个元素添加任意分值
r.zincrby('ranking',100,'song1')
r.zincrby('ranking',200,'song3')
r.zincrby('ranking',300,'song4')

#获取排行榜前三名
result=r.zrevrange('ranking',0,2,withscores=True)
i=1
for r in result:
    print('第{}名:{}播放量:{}'.format(i,r[0].decode(),r[1]))
    i+=1

#第一名:
#第二名:海阔天空  播放量:6666
#第三名:


# [(b'song1', 1.0), (b'song2', 1.0), (b'song3', 1.0), (b'song4', 1.0), (b'song5', 1.0), (b'song6', 1.0), (b'song7', 1.0), (b'song8', 1.0), (b'song9', 1.0)]

# result=r.zrange('ranking',0,-1,withscores=True)
# print(result)















