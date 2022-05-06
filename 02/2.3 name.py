# -*- coding: utf-8 -*-

# 2.3 字符串
# 对数据进行分类很有必要
# 首先介绍字符串，字符串就是一系列字符
# 在Python中用引号括起来的就是字符串

# "This is a string."
# 'This is also a string.'
# 'I told my friend, "Python is my favorite language."'
# "The language 'Python' is named after Monty Python, not the snake."
# "One of Python's strengths is its diverse and supportive community."

# 2.3.1 使用方法修改字符串大小写

from numpy import full


name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
# 将所有字母变为大写
print(name.upper())
# 将所有字母变为小写
print(name.lower())

# 2.3.2 拼接字符串
# 有时需要将数据分别储存（例如姓和名），等要显示的时候再合并

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

# 2.3.3 使用制表符或换行符添加空白
# 使用\t添加制表符
print("\tPython")

# 使用\n添加换行符
print("Languages:\nPython\nC\nJavaScript")

# 在一个字符串中同时包含制表符和换行符
# 让Python换到下一行，并在开头添加一个制表符
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 2.3.4 删除空白
# 'python'与'python '在人看来没什么两样，但是对程序是两个不同字符串
# 空白很重要，例如在用户登录网站时检查其用户名

# rstrip()去掉末尾空白(r可以记为right)
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language)

# 第二次输出显示去掉了空格
# 第三次输出显示空格还在，因为变量没有改变，需要将删除后的变量重新赋值
favorite_language = favorite_language.rstrip()
print(favorite_language)

# 此时的输出末尾将永久没有空格

# lstrip()去掉开头的空白（l可以记为left）
# strip()去掉两端的空白
favorite_language = ' python '
print(favorite_language)
print(favorite_language.lstrip())
print(favorite_language.strip())