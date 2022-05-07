# -*- coding: utf-8 -*-
# 第3章 列表简介

# 3.1 列表是什么
# 列表由一系列按特定顺序排列的元素组成
# Python中用方括号（[]）表示列表，用逗号分隔元素

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# >>> ['teck', 'cannondale', 'redline', 'specialized']

# 3.1.1 访问列表元素
# 列表是有序集合，访问列表元素，只需将该元素的位置或索引告诉python
# 访问列表元素，指出列表的名称，再指出元素的索引，放在方括号里

print(bicycles[0])
# >>> teck
# 请求获取列表元素时，仅获得元素，不包括方括号和引号

print(bicycles[1].title())
# >>> Cannondale

# 3.1.2 索引从0而不是1开始
# Python中第一个元素的索引是0，不是1
# 大多数编程语言都是如此

print(bicycles[2])
print(bicycles[3])

# 最后一个元素的索引指定为-1
print(bicycles[-1])
# >>> specialized

# 3.1.3 使用列表中的各个值
# 像使用其他变量一样使用列表中各个值
# 例如可以使用拼接元素创建消息

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
# >>> My first bicycle was a Trek.

# 动手试一试

# 3-1 姓名
# 将一些朋友的姓名存储在一个列表中，并将其命名为names 。
# 依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。

names = ['Wang X.G', 'Zhang X', 'Zhang D.X', 'Wu X.B']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 3-2 问候语
# 继续使用3-1中的列表，不打印每个朋友的名字，而是为每个人打印一条消息
# 每条消息包含同样的问候语，但抬头为相应朋友的名字

print("Hello " + names[0] + ", how you doing?")
print("Hello " + names[1] + ", how you doing?")
print("Hello " + names[2] + ", how you doing?")
print("Hello " + names[3] + ", how you doing?")

# 3-3 自己的列表
# 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。
# 根据该列表打印一系列有关这些通勤方式的宣言，如“I would like to own a Honda motorcycle”。

vehicles = ['tesla', 'xiaopeng', 'benz', 'audi']
print("I would like to own a(an) " + vehicles[0].title() + " electric car.")
print("I would like to own a(an) " + vehicles[1].title() + " electric car.")
print("I would like to own a(an) " + vehicles[2].title() + " electric car.")
print("I would like to own a(an) " + vehicles[3].title() + " electric car.")