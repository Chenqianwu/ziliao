import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# user1:一年之中第一天和第五天登录
r.setbit('user1', 0, 1)
r.setbit('user1', 4, 1)

# user2:一年之中第一百天和第二百天登录
r.setbit('user2', 99, 1)
r.setbit('user2', 199, 1)

# user3:一年之中有100天以上登录了,时间自己订
for i in range(0, 365, 3):
    #print(i)
    r.setbit('user5', i, 1)

# user4:一年之中有100天以上登录了,时间自己订
for i in range(0, 365, 3):
    r.setbit('user4', i, 1)

# 先找到所有用户
user_list = r.keys('user*')
active_users = []
noactive_users = []
for user in user_list:
    # 统计位图中有多少个 1
    login_count = r.bitcount(user)
    # print(login_count)
    if login_count >= 100:
        # 活跃用户
        active_users.append((user, login_count))

    else:
        # 非活跃用户
        noactive_users.append((user, login_count))
# 统计活跃用户和非活跃用户
# print('活跃用户:',active_users)
#
# print('非活跃用户:',noactive_users)
print(active_users)
for user in active_users:
    print('活跃用户:%s 活跃次数:%s' % (user[0].decode(), user[1]))
# 打印活跃用户
