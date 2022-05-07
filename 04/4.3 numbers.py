# 4.3 创建数值列表
# 很多时候我们需要存储一组数字
# 列表非常适合存储数字集合，python有很多工具帮助你处理数字列表

# 4.3.1 使用函数range()
for value in range(1,5):
    print(value)

# range()让python从指定的第一个值开始数，在达到第二个值之后停止
# 输出不包含第二个值

print("\n")

for value in range(1,6):
    print(value)

print("\n")

# 4.3.2 使用range()创建数字列表
# 要创建数字列表，使用list()将range()的结果转换为列表
# 如果将range()作为list()的参数，输出将作为一个数字列表
numbers = list(range(1,6))
print(numbers)
