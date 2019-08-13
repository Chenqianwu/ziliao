import redis

r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

#lpush  rpush
#[pythonweb,socket,spiderman]
r.lpush('tedu:python','socket','pythonweb')
r.rpush('tedu:python','spiderman')
print(r.lrange('tedu:python',0,-1))
#列表尾部弹出一个元素
r.rpop('tedu:python')
print(r.lrange('tedu:python',0,-1))
#列表头部弹出一个元素
r.lpop('tedu:python')
print(r.lrange('tedu:python',0,-1))
#列表尾部插入三个元素
r.rpush('tedu:python','web','java','javascript')
print(r.lrange('tedu:python',0,-1))
#删除索引为2的元素
index2=r.lindex('tedu:python',2)
# print(index2.decode())
r.lrem('tede:python',1,index2.decode())
print(r.lrange('tedu:python',0,-1))
#保留列表中的前两个元素
r.ltrim('tedu:python',0,1)
# print(r.lrange('tedu:python',0,-1))
#吧下标索引为0的元素设置为:redis
# r.lset('tedu:python',0,redis)
# print(r.lrange('tedu:python',0,-1))
#在redis元素的后面插入一个元素:AI
# r.linsert('tede:python','after','redis','AI')
# print(r.lrange('tedu:python',0,-1))
print(r.llen('tedu:python'))
print(r.lrange('tedu:python',0,-1))

# r.delete('tedu:python')