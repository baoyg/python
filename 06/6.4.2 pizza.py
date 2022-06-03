# 6.4.2 在字典中存储列表
# 回顾：列表是有序集合，通过索引访问元素
# 如何描述顾客点披萨？如果使用列表，只能存储要添加的披萨配料
# 如果使用字典，不仅在其中包含配料，还可以包含其他描述

# 下面存储了两方面信息，其中有toppings相关的值
# 要访问该列表，使用字典名和键toppings

# 存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# 概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza" + 
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languags = {
    'jen': ['python', 'nuby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languags.items():
    print("\n" + name.title() + "'s favorite language are:")
    for language in languages:
        print("\t" + language.title())

# 每个与名字相关的值都是一个列表
# 遍历字典时，用变量languages依次存储字典的每个值，这些值都是列表
# 注：方法items()返回字典中的键值对列表
# 再使用一个for循环遍历语言列表

# >>>>
# Jen's favorite language are:
#         Python
#         Nuby

# Sarah's favorite language are:
#         C

# Edward's favorite language are:
#         Ruby
#         Go

# Phil's favorite language are:
#         Python