import redis

#创建连接对象
r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

#查看所有key[b'mylist3', b'mylist1', b'mylist', b'2', b'mylist2']
print(r.keys('*'))

#type
print(r.type('mylist'))
#判断键是否存在返回0   1

print(r.exists('spider::urls'))
#删除key
r.delete('mylist3')





























