# -*- coding: utf-8 -*-
# 第2章 变量和简单数据类型

# 2.4.3 使用str()比免类型错误

# age = 23
# message = "Happy" + age + "rd Birthday!"
# print(message)

# >>> Traceback (most recent call last):
# >>>   File "birthday.py", line 2, in <module>
# >>>       message = "Happy " + age + "rd Birthday!"
# >>> TypeError: Can't convert 'int' object to str implicitly

# 变量age是一个整数（int）类型，Python不知道如何解读它
# 在字符串中使用整数，应当显性地告知Python将这个整数用作字符串

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# 动手试一试

# 2-8 数字8
# 编写4个表达式，它们分别使用加法、减法、乘法和除法运算，但结果都是数字8。
# 为使用print 语句来显示结果，务必将这些表达式用括号括起来，也 就是说，你应该编写4行类似于下面的代码:
# print(5+3)

print(2 * 4)
print(2 ** 3)
print(9 - 1)
print(6 + 2)

# 2-9 最喜欢的数字
# 将你最喜欢的数字存储在一个变量中，再使用这个变量创建一条消息，指出你最喜欢的数字，然后将这条消息打印出来。

favorite_number = 9
print("My favorite number is " + str(favorite_number) + ".")