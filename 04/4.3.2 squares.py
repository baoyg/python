# 4.3.2 使用range()创建数字列表
# 创建一个数列，包含前10个整数的平方

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(min(digits))
print(max(digits))
print(sum(digits))

# 4.3.4 列表解析
# 解析列表让你只需编写一行代码就能生成这样的列表
# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
squares = [value**2 for value in range(1,11)]
print(squares)

# 使用列表解析，首先指定一个描述性的列表名(squares)
# 指定一个左方括号，定义一个表达式(value**2)，用于生成存储到列表的值
# 编写for循环，用于给表达式赋值，再加上右方括号
# for循环是for value in range(1,11)，将值1～10赋给表达式value**2

# 练习
# 4.3 使用一个for循环打印数字1～20（含）
numbers_one_to_twenty = []
for value in range(1,21):
    numbers_one_to_twenty.append(value)
print(numbers_one_to_twenty)

# 4.4 创建一个列表，包含数字1～1000000，再使用一个for循环将数字打印出来
numbers_1_to_onemillion = []
for value in range(1,1000001):
    numbers_1_to_onemillion.append(value)
print(numbers_1_to_onemillion)

# 4.5 计算1～1000000的总和：创建一个列表，包含数字1～1000000，再使min()和max()核实从1开始，1000000结束。
# 对列表调用sum()，看计算需要多久
numbers_1_million = []
for value in range(1,1000001):
    numbers_1_million.append(value)

print("\nThe min number is " + str(min(numbers_1_million)))
print("\nThe max number is " + str(max(numbers_1_million)))
print("\nThe sum is " + str(sum(numbers_1_million)))

# 4.6 奇数：通过给函数range()设定参数创建列表，包含1～20的奇数，用for循环打印出来
odd_numbers = []
for value in range(1,21,2):
    odd_numbers.append(value)
print(odd_numbers)

# 4.7 3的倍数：创建一个列表，包含3～30以内能被3整除的数字，使用for循环打印出来
numbers_3 = []
for value in range(3,20,3):
    numbers_3.append(value)
print(numbers_3)

# 4.7 立方：创建一个列表，包含前10个整数的立方，用for循环打印出来
numbers = []
for value in range(1,11):
    numbers.append(value**3)
print(numbers)

# 4.8 立方解析：创建一个列表，包含前10个整数的立方，用for循环打印出来
numbers_cube = [value**3 for value in range(1,11)]
print(numbers_cube)