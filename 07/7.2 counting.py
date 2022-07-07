# 7.2 while循环介绍

# 7.2.1 使用while循环
# 使用while循环数数，从1数到5

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 7.2.2 让用户选择何时退出
# while循环让程序愿意时不断运行，在想退出时停止运行

prompt = "\nTell me something, and I will repeat it to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# 7.2.3 使用标志
# 在上一个示例中，程序在满足指定条件时会执行特定任务
# 但是在更复杂的程序中，很多事件都会导致程序停止
# 例如游戏中，玩家的飞船坠毁了，要保护的目标被摧毁了
# 如果有很多事件，在一条while中逐一检查这些条件会非常困难

# 在要求很多条件都满足才继续运行的程序中
# 我们定义一个变量，用于判断程序是否处于活动状态
# 这个变量被称为 标志
# 当标志为True时，程序继续运行
# 在任何事件发生时，标志变为False，导致程序停止
# 那么while循环就只检查标志的状态即可
# 这样程序可以变得更整洁

prompt = "\nTell me something, and I will repeat it to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)