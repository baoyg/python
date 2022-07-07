# 7.2.5 在循环中使用continue

# 要返回到循环开头，并根据条件测试结果决定是否继续执行循环，使用continue
# 现在从1数到10，但是只打印偶数
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 1:
#         continue
#     print(current_number)

# 7.2.6 避免无限循环
# 每个while必须有停下的途径
# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# 7-4 披萨配料：编写一个循环，提示用户输入一系列的配料
# 在用户输入'quit'时结束循环
# 每当输入一个配料，就打印一条消息，说我们会在披萨中加入这种配料

# while True:
#     topping = input("Tell me what do you want on your pizza?")
#     if topping == 'quit':
#         break
#     else:
#         print("\nI'd like to add " + topping + " on my pizza.\n")

# 7-5 电影票：有家电影院根据观众的年龄收取不同的票价，
# 不到3岁的免费，3-12岁10元，超过12的15元
# 编写一个循环，在其中询问用户的年龄，指出其票价

# while True:
#     age = input("Tell me the audience's age, I'll tell you the ticket price: ")
#     if int(age) < 3:
#         print("The ticket is free.")
#     elif int(age) <= 12:
#         print("The ticket is 10 dollar.")
#     else:
#         print("The ticket is 15 dollar.")

# 7-6 三个出口：以另一种方式完成7-4或7-5，采用如下所有做法：
# 在while循环中使用条件测试来结束循环
# 使用变量active来控制循环结束的时机
# 使用break语句在用户输入quit时退出循环

# 使用条件测试结束循环
# prompt = "Tell me what do you want on your pizza?"
# topping = ""
# while topping != 'quit':
#     topping = input(prompt)
#     if topping != 'quit':
#         print("\nI'd like to add " + topping + " on my pizza.\n")

# 使用变量active控制循环结束
# prompt = "Tell me what do you want on your pizza?"
# active = True
# while active:
#     topping = input(prompt)
#     if topping == 'quit':
#         active = False
#     else:
#         print("\nI'd like to add " + topping + " on my pizza.\n")

# 使用break在用户输入quit时退出
prompt = "Tell me the age: "
age = ""
while True:
    age = input(prompt)
    if age != ' ':
        if age == 'quit':
            break
        elif int(age) < 3:
            print("The ticket is free.")
        elif int(age) <= 12:
            print("The ticket is 10 dollar.")
        else:
            print("The ticket is 15 dollar.")
    else:
        print("The input is not correct, please try again.") 