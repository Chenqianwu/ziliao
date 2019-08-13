# 用户想要查询个人信息
# 1、到redis缓存中查询个人信息
# 2、redis中查询不到，到mysql查询，并缓存到redis
# 3、再次查询个人信息
import redis
import pymysql
# 用户从终端输入要查询的用户:chenqianwu
username = input('请输入用户名:')
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
# 从redis里面查询(gender age)  (r.getall(username))
# 如果查到,直接打印输出
result=r.hgetall(username)
# print(result)
if result:
    print('redis数据:',result)
else:
    # 如果没有查到:
    # 1.从mysql中查询(gender age)
    db = pymysql.connect('localhost', 'root', '123456', 'userdb', charset='utf8')
    cursor = db.cursor()
    sel = 'select gender,age from user where username=%s'
    cursor.execute(sel, [username])
    # (('m',21),)
    res = cursor.fetchall()
    if not res:
        print('MySQL中无此用户')
    else:
        print('MySQL中用户信息查询结果:',res)
    # 2.加入redis缓存,设置过期时间5分钟
        r.hmset(username,{'gender':res[0][0],'age':res[0][1]})
        r.expire(username,20)
#
#   key        field    value
# username      gender  m
#               age     21