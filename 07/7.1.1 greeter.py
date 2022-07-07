# 7.1.1 编写清晰的程序

# 当使用函数input()时，应该给出直白清晰的提示，告诉用户你希望得到什么信息
name = input("Please enter your name: ")
print("Hello, " + name + "!" )

# 有时提示不止一行，比如需要告诉用户为什么需要他输入那些信息
# 我们可以使用+=来拼接两部分字符串，它的意思是将后面的内容与原来的内容拼起来赋给变量
# 此时，我们可以将提示存储在一个变量中，再将变量放进函数input()

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

# 7.1.2 使用int()获取数值输入
# 使用input()时，python将用户输入的信息解读为字符串

# age = input("How old are you? ")
# print(age)

# 假如我输入18，输出就是18
# 但是，这个18的数据类型是字符串
# 如果我们仅仅是用print()打印age，这没什么问题
# 但是如果我们需要将age跟18比较，看看用户输入的年龄是否达到18
# 就会引发错误

# age = input("How old are you? ")
# if age >= 18:
#     print("You're an adult.")

# >>>>>>
# Traceback (most recent call last):
#   File "/Users/bob/Desktop/learning_python/07/greeter.py", line 29, in <module>
#     if age >= 18:
# TypeError: '>=' not supported between instances of 'str' and 'int'

# 发生了typeError，类型错误
# 因为18是int类型（数值类型），而用户输入的是字符串类型，它们不能直接拿来比较大小
# 我们需要先将用户输入的age转换成int类型

# age = input("How old are you? ")
# age = int(age)
# if age >= 18:
#     print("You're an adult.")

# int()方法将我们输入的数字转换成了数值类型
# 这样我们就可以拿来比大小了if age >= 18:

# 7.1.3 求模运算符
# 我们常见的%号就是求模运算符
# 它将两个数相除并返回余数

print(4%3)
print(5%4)
print(10%7)

# 显然，如果一个数可以被另一个数整除，求模运算将返回0
# 我们可以利用求模运算判断一个数是奇数还是偶数

number = input("Enter a number, and I'll tell you if ti's even or odd: ")
number = int(number)

if number%2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

