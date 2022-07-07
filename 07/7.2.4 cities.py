# 7.2.4 使用break退出循环

# 要立即退出while循环，不再运行余下的代码，使用break语句

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# 程序会不断运行，直到遇到break