import redis

r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

# 新建1条键名为 userinfo 的数据,包含属性  username值自定义
r.hset('userinfo','username','chenqianwu')

#2.更改username属性的值(新值自定义)
r.hset('userinfo','username','chen')

#3取出username的值,并打印输出查看类型
#b'chen'

print(r.hget('userinfo','username'))

#4.批量添加属性 password=123456,gender=f,height=178
user_dict={'password':'123456','gender':'f','height':178}
r.hmset('userinfo',user_dict)

#5.取出所有数据,打印查看
# all_data: {b'username': b'chen', b'password': b'123456', b'gender': b'f', b'height': b'178'}
all_data=r.hgetall('userinfo')
print('all_data:',all_data)
#6.删除height属性
r.hdel('userinfo','height')
#7.取出所有属性名,打印查看类型

r.hkeys('userinfo')
print(type(r.hgetall('userinfo')))
#8.取出所有的属性值,打印查看类型
# r.hgetall()
r.hvals('userinfo')



    # key          field    value
# 'chenqianwu'    gender     m
#                   age        33