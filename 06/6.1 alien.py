# 6 字典

# 本章学习将相关信息关联起来的python字典
# 学习如何访问和修改字典中的信息
# 由于字典可存储的信息量几乎不受限制，将会学习如何遍历字典
# 还要学习存储字典的列表、存储列表的字典和存储字典的字典

# 6.1 一个简单的字典
# 一个游戏，包含一些外星人，颜色和点数不同
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# 6.2 使用字典
# 字典是一系列键值对，每个键与一个值关联，可以使用键访问值
# 与键相关的值可以是数字、字符串、列表、字典，任何值都可以
# 字典中想存多少个键值对都可以

# 6.2.1 访问字典中的值
print(alien_0['color'])

# 访问与键相关的值，依次指定字典名和放在括号内的键

new_ponits = alien_0['points']
print("You just earned " + str(new_ponits) + " points!")

# 6.2.2 添加键值对
# 字典是一种动态结构，可随时在其中添加键值对
# 依次指定字典名、键、值

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# python不关心键值对的添加顺序，只关心键值的关联关系

# 6.2.3 先创建一个空字典
alien_0 = {}
alien_0['color' ] = 'green'
alien_0['points'] = 5

print(alien_0)

# 6.2.4 修改字典中的值
# 要修改字典中的值，依次指定字典名、方括号括起的键以及与该键相关的新值
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# 对于一个以不同速度移动的外星人的位置进行跟踪
# 存储外星人当前速度，据此确定外星人向右移动多远
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 外星人很快
    x_increment = 3
# 新位置等于老位置加增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-positon: " + str(alien_0['x_position']))

# 6.2.5 删除键值对
# 使用del，需要指明字典名和要删除的键，将指定的键值对彻底删除
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)