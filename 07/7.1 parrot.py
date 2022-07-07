# 7 用户输入和while循环

# 大多数程序解决最终用户的问题，需要从用户那里获取一些信息
# 本章学习如何接受用户输入，让程序对其进行处理
# 还要学习让程序不断地运行，直到指定的条件不满足为止

# 7.1 函数input()的工作原理

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# 函数input()接受一个参数，这个参数就是向用户显示的提示信息
# 用户输入信息，按回车后程序继续运行
# 用户输入的信息存储在message中