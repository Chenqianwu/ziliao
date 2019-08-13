import redis

r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

#1.set:设置{'mystring':python}
r.set('mystring','python')
#2.获取mystring的值,打印查看类型
print(type(r.get('mystring')))
#3.设置mystring ,当键不存在的时候在设置.存在则不操作
print(r.setnx('mystring','python'))
#4.一次性设置多个键时,{'mystring':mysql,'mystring3':'redis'}
#提示:参数为字典
r.mset({'mystring2':'mysql','mystring3':'redis'})
#5.一次性获取三个键的值,查看结果类型?
mget_list=r.mget('mystring','mystring2','mystring3')
for mget in mget_list:
    print(mget.decode())
print(r.mget('mystring','mystring2','mystring3'))
#6.打印mystring的长度
r=r.strlen('mystring')
print(r)
#数字类型操作'
#设置number为20
r.set('number','20')

#8 +10 操作
r1=r.incrby('number',10)
print(r1)
#9 -10 操作
r2=r.decrby('number',10)
print(r2)
#10  +8.88操作
r3=r.incrbyfloat('number',8.88)
print(r3)
#11  -8.88操作
r4=r.decrbyfloat('number',8.88)
print(r4)
#12.查看number的值






