'''微博共同关注'''
import redis

r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')


#user_one 关注的人(放到集合中)
r.sadd('user_one','qiaozhi','peiqi','danni')

#user_two 关注的人(放到集合中)

r.sadd('user_two','qiaozhi','peiqi','lingyang')

#user_one和user_two共同关注的人为??求集合的交集

result=r.sinter('user_one','user_two')
print(result)
#结果:{'peiqi','qiaozhi'}
focus_on_set=set()
for r in result:
    focus_on_set.add(r.decode())
print(focus_on_set)



















