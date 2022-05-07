# 4.4.3 复制列表
# 要复制列表，可以创建包含整个列表的切片[:]

# 假设有一个列表，有你最喜欢的食品，你还想创建一个列表，里面包含你朋友喜欢的食品
# 你喜欢的食品，你朋友也喜欢，所以列表是一样的
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 为检验确实存在两个列表，每个列表中添加一个食品
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 不使用切片复制列表

my_foods = ['pizza', 'falafel', 'carrot cake']
# 行不通
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')

print(">>> My favorite foods are:")
print(my_foods)

print("\n>>> My friend's favorite foods are:")
print(friend_foods)

# python将新变量friend_foods关联到包含在my_foods中的列表
# 这两个变量都指向同一个列表

# 4-10

letters = ['A','B','C','D','E','F','G']

print("The first three items in the list are:")
print(letters[:3])

print("Three items from the middle of the lists are:")
print(letters[2:5])

print("The last three items in the list are:")
print(letters[-3:])

# 4-11

pizzas = ["Napoletana","Taglio","Sfincione","Calzone","Pizzolo"]
print("\nMy favorite pizzas are:")
print(pizzas)
pizzas.append("Padellino")
print("\nMy favorite pizzas are:")
print(pizzas)

friend_pizzas = pizzas[:]
friend_pizzas.append("Scaccia")
print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)
print("\nMy favorite pizzas are:")
print(pizzas)

print("\n")
for pizza in pizzas:
    print(pizza)
print("\n")
for pizza in friend_pizzas:
    print(pizza)

# 4-12

# 略