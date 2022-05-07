# 4.1 遍历整个列表
# 有时需要遍历列表，对每个元素执行相同的操作。
# 游戏中，对每个界面元素平移相同的距离
# 数据中，对每个元素执行相同的统计运算
# 网站中，显示文章列表中每个标题

# 有一个魔术师名单，我们需要打印每个人的名字，for循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# 4.1.1 深入研究循环
# python逐个读取列表中的元素，将其存储到变量magician中，并打印出来

# 4.1.2 for循环中执行更多操作
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# 4.1.3在for循环结束后执行一些操作

print("Thank you, everypne. That was a great show!")

pizzas = ["french bread","baked ziti","grandma slice","new york slice","chicago pizza","puck's smoked salmon pizza"]
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print("I like " + pizza.title() + ".")
print("I really like pizza!")

fruits = ["pineapples","apples","mongos"]
for fruit in fruits:
    print(fruit.title() + " are rich in vitamins.")
print("Any of these fruits is rich in vitamins")