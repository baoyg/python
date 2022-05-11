# 5.4 使用if语句处理列表

# 5.4.1 检查特殊元素

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza.")

# 如果green pepper用完了
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + '.')
print("Finished making your pizza.")

# 5.4.2 确定列表不是空的

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + '.')
    print("\nFinished making your pizza.")
else:
    print("Are you sure you want a plain pizza?")

# python将在列表至少包含一个元素时返回True，在列表为空时返回False

# 5.4.3 使用多个列表
# 如果顾客想在pizza里加薯条怎么办？使用if确定能否满足顾客需求
# 一个列表包含披萨店供应的配料，一个列表包含顾客点的配料
# 对于顾客的列表中的元素，检查它是否是披萨店的配料
available_toppings = ['mushrooms', 'olives', 'green peppers',
                    'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + '.')
    else:
        print("Sorry, we don't have " + requested_topping + '.')
print("\nFinished making your pizza.")

# 练习
# 5.8 特殊方式与管理员打招呼
# 创建一个列表，有5个人，其中有admin
# 当有人登录时，向他打招呼，如果是管理员，输出：Hello admin, would you like to see a status report?
# 如果是其他人，输出：Hello Eric, thank you for logging in again.
print("\n==========练习5.8==========\n")

name_list = ['bob', 'will', 'hank', 'mason', 'admin']
for name in name_list:
    if name == 'admin':
        print("Hello " + name.title() + ", would you like to see a status report?")
    else:
        print("Hello " + name.title() + ", thank you for logging in again.")

# 5.9 处理没有用户的情形：在5.8中添加一条if语句，检查用户名列表是否为空
# 如果为空，打印消息we need to find some users
# 删除列表中所有用户名，确定将打印正确信息

print("\n==========练习5.9==========\n")

name_list2 = []
if name_list2:
    print('')
else:
    print("We need to find some users.")

# 5.10 检查用户名：模拟网站确保每位用户的用户名都独一无二
# 创建一个至少包含5个用户名的列表，命名为current_users
# 再创建一个包含5个用户名的列表，命名为new_users

print("\n==========练习5.10==========\n")

current_users = ['bob', 'will', 'hank', 'mason', 'admin']
new_users = ['BOB', 'will', 'tom', 'jack', 'sam']

for name in new_users:
    if name.lower() in current_users:
        print(name.title() + " has been taken, please change a new one.")
    else:
        print(name.title() + " is available.")

# 5.11 序数：序数表示位置，大多数序数都以th结尾，只有1、2、3除外
# 在列表中存储数字1-9
# 遍历这个列表，在循环中使用一个if-elif-else结构，打印每个数字对应的序数
# 输出：1st 、2nd 、3rd 、4th 、5th 、6th 、7th 、8th、9th

print("\n==========练习5.11==========\n")

'''
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number == 1:
        print(str(number) + "st\n")
    elif number == 2:
        print(str(number) + "nd\n")
    elif number == 3:
        print(str(number) + "rd\n")
    else:
        print(str(number) + "th\n")
'''

for number in range(1, 6):
    if number == 1:
        print(str(number) + "st\n")
    elif number == 2:
        print(str(number) + "nd\n")
    elif number == 3:
        print(str(number) + "rd\n")
    else:
        print(str(number) + "th\n")