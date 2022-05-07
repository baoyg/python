# -*- coding: utf-8 -*-
# 第3章 列表简介

# 3.2 修改、添加和删除元素
# 列表大多数时候是动态的，会随着程序运行增删元素

# 3.2.1 修改列表元素
# 修改列表元素的语法与访问列表元素的语法类似
# 指定列表名和要修改的元素索引，指定该元素的新值

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati' # 将第一个元素修改为'ducati'
print(motorcycles)

# 3.2.2 在列表中添加元素

# 1.在列表末尾添加元素
# 最简单的办法，使用append()将元素添加到列表末尾
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# 先创建一个空列表，再用一系列append()添加元素
motorcycles = []
motorcycles.append('bmw')
motorcycles.append('aima')
motorcycles.append('9bot')
print(motorcycles)

# 这种方法非常常见，经常要等程序运行后，才知道要添加哪些元素

# 2.在列表中插入元素，可在任意位置添加新元素
# 我们需要知道元素的索引和值
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
# 在索引0处添加空间，将'ducati'存储在此，既有的元素右移一个位置
print(motorcycles)

# 3.2.3 从列表中删除元素

# 使用del语句删除元素
# 可以根据位置或值来删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
# 1.使用del删除了第一个元素
print(motorcycles)

# 使用del可以删除任意位置的列表元素，条件是知道其索引

# 2.使用pop()删除元素
# 有时需要将元素从列表删除，并接着使用它的值
# 将敌人击杀后获取其坐标值，在相应位置显示爆炸效果
# 将成员从一个组移除，放到另一个组中

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# 3.弹出列表中任意位置处的元素
# 使用pop()删除任意位置的元素，只需在括号中指定索引即可

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

# 4.根据值删除元素
# 不知道元素所处的位置，只知道元素的值，使用方法remove()
motorcycles = ['ducati', 'honda', 'yamaha', 'suzuki']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove('ducati')
print(motorcycles)
print("\nA " + too_expensive.title() + "is too expensive for me.")

# remove()只能删除第一个值，如果有多个值需要循环处理

guests_name = ['grace', 'jersey', 'einstein']
print("I want to invite " + guests_name[0].title() + " to have dinner with me.")
print("I want to invite " + guests_name[1].title() + " to have dinner with me.")
print("I want to invite " + guests_name[2].title() + " to have dinner with me.")

print(guests_name[0].title() + " will not come for dinner.")
guests_name[0] = 'lily'
print("I want to invite " + guests_name[0].title() + " to have dinner with me.")
print("I want to invite " + guests_name[1].title() + " to have dinner with me.")
print("I want to invite " + guests_name[2].title() + " to have dinner with me.")

print("\nI have found a bigger table.")

guests_name.insert(0, 'alex')
guests_name.insert(2, 'michael')
guests_name.append('tom')
print("I want to invite " + guests_name[0].title() + " to have dinner with me.")
print("I want to invite " + guests_name[1].title() + " to have dinner with me.")
print("I want to invite " + guests_name[2].title() + " to have dinner with me.")
print("I want to invite " + guests_name[3].title() + " to have dinner with me.")
print("I want to invite " + guests_name[4].title() + " to have dinner with me.")
print("I want to invite " + guests_name[5].title() + " to have dinner with me.")

print("I'm sorry to tell you that the new table I bought hasn't been delivered yet, \
    I'm afraid I can't invite you to dinner tonight.")

print(guests_name)

guest_deleted = guests_name.pop()
print("To " + guest_deleted.title() + ": I'm so sorry to tell you that I can't invite you to dinner tonight.")
guest_deleted = guests_name.pop()
print("To " + guest_deleted.title() + ": I'm so sorry to tell you that I can't invite you to dinner tonight.")
guest_deleted = guests_name.pop()
print("To " + guest_deleted.title() + ": I'm so sorry to tell you that I can't invite you to dinner tonight.")
guest_deleted = guests_name.pop()
print("To " + guest_deleted.title() + ": I'm so sorry to tell you that I can't invite you to dinner tonight.")

print("To " + guests_name[0].title() + ": I'd like to invite you to dinner tonight.")
print(guests_name)
print("To " + guests_name[1].title() + ": I'd like to invite you to dinner tonight.")
print(guests_name)

del guests_name[0]
del guests_name[0]
print(guests_name)