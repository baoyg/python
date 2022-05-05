# -*- coding: utf-8 -*-
# 第2章 变量和简单数据类型

# 2.1 运行hello_world.py发生的情况

print("Hello Python world!")

# 2.2 变量

message = "Hello Python world!"
print(message)

message = "Heelo Python Crash Course world!"
print(message)

# message = "Hello Python world!"
# print(mesage)

# 若运行上面的程序，会出现报错：
# Traceback (most recent call last):
#   File "hello_world.py", line 2, in <module>
#       print(mesage)
# NameError: name 'mesage' is not defined