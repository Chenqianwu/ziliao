# 用户想要查询个人信息
# 1、到redis缓存中查询个人信息
# 2、redis中查询不到，到mysql查询，并缓存到redis
# 3、再次查询个人信息
import redis
import pymysql
# 用户从终端输入要查询的用户:chenqianwu
username = input('请输入用户名:')
age=input('请输入新的年龄:')

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
#改mysql数据库
db = pymysql.connect('localhost', 'root', '123456', 'userdb', charset='utf8')
cursor = db.cursor()
upd = 'update user set age=%s where username=%s'
cursor.execute(upd, [age,username])
db.commit()
#同步到redis数据库
r.hset(username,'age',age)
r.expire(username,20)
print(r.hget(username,'age'))