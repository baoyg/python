# 5.3.6 测试多个条件
requested_toppings = ['mushroom', 'extra cheese']

if 'mushroom' in requested_toppings:
    print("Adding mushrooms.")
if 'prpperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza.")

# 练习
# 5.3 外星人颜色1:射杀一个外星人，
# 创建一个alien_color的变量，设置为'green'、'yellow'或'red'
# 编写一条if语句，检查外星人是否是绿色，如果是，打印一条消息，指出玩家获得了5分
# 编写第二个版本，在上述测试中没有通过（无输出）
print("\n==========练习5.3==========\n")

alien_color = 'green'
if alien_color == 'green':
    print("You've got 5 points.")
if alien_color == 'red':
    print("You've got 5 points.")

# 5.4 外星人颜色2:编写一个if-else结构
# 如果外星人是绿色的，打印一条消息，玩家得到5分
# 如果外星人不是绿色的，打印一条消息，玩家得到10分
# 编写另一个版本，将上述条件互换
print("\n==========练习5.4==========\n")

alien_color = 'red'
if alien_color == 'green':
    print("You've got 5 points.")
else:
    print("You've got 10 points.")

if alien_color == 'red':
    print("You've got 10 points.")
else:
    print("You've got 5 points.")

# 5.5 外星人颜色3:将上述if-else结构改为if-elif-else结构
# 如果外星人是绿色的，打印一条消息，获得5分
# 如果是黄色，得10分
# 如果红色，15分
print("\n==========练习5.5==========\n")

alien_color = 'green'
if alien_color == 'green':
    print("You've got 5 points.")
elif alien_color == 'yellow':
    print("You've got 10 points.")
else:
    print("You've got 15 points.")

# 5.6 人生的不同阶段：设置变量age的值，编写一个if-elif-else结构，根据age判断阶段
# 小于2岁，婴儿
# 2（含）-4岁，蹒跚学步
# 4（含）-13岁，儿童
# 13（含）-20岁，青少年
# 20（含）-65岁，成年人
# 大于65（含），老年人
print("\n==========练习5.6==========\n")

age = 31
if age < 2:
    print("他是婴儿。")
elif 2 <= age < 4:
    print("他正在蹒跚学步。")
elif 4 <= age < 13:
    print("他是儿童。")
elif 13 <= age < 20:
    print("他是青少年。")
elif 20 <= age < 65:
    print("他是成年人。")
else:
    print("他是老年人。")

# 5.7 喜欢的水果：创建一个列表，包含喜欢的水果
# 编写独立的if语句，检查列表中是否包含特定的水果
print("\n==========练习5.7==========\n")

favorite_fruits = ['apple', 'cherry', 'grape', 'kiwi']
if 'banana' in favorite_fruits:
    print("Wow, I like banana.")
else:
    print("Why don't you get some bananas?")
