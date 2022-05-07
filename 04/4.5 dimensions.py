# 4.5 元组
# 列表适合用于存储程序运行时可能变化的数据集，即列表是可以修改的
# 但是有时你需要创建一系列不可修改的元素，元组满足这个需求

# 4.5.1 定义元组
# 元组用圆括号表示，可以使用索引访问元素，就像访问列表元素那样
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250


# 4.5.2 遍历元组中所有的值
for dimension in dimensions:
    print(dimension)

# 4.5.3 改变元组变量
# 虽然不能修改元组的元素，但是可以给存储元组的变量赋值
# 如果要修改矩形的尺寸，可以重新定义整个元组
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


# 4-13

foods = ("bun","dumpling","noodle","rice","potato")
for food in foods:
    print(food)

foods[0] = "tomato"

foods = ("bun","dumpling","pho","shumai","potato")
for food in foods:
    print(food)