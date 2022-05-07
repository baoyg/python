# 4.4 使用列表的一部分

# 4.4.1 切片
# 要使用切片，指定要使用的第一个元素和最后一个元素的索引
# python在到达第二个索引前的元素会停止
# 要输出前3个元素，需要指定索引0-3，输出分别为0，1，2的元素
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:3])

# 没有指定第一个索引，默认从头开始
print(players[:2])

# 没有指定第二个索引，默认到最后
print(players[2:])

# 输出名单最后三个人
# 负数索引返回离列表末尾相应距离的元素
print(players[-3:])

# 4.4.2 遍历切片
# 如果要遍历列表的部分元素，可在for循环中使用切片
# 遍历前3名队员，并打印出来
print("Here are the first three players on my team:")
for player in players[0:3]:
    print(player.title())