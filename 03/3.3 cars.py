# -*- coding: utf-8 -*-
# 3.3 组织列表

# 3.3.1 使用sort()对列表进行永久性排序
 
from numpy import sort

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sort()将元素按照字母顺序排列，排序无法恢复

# 按照字母倒序排列，增加参数reverse=True
cars.sort(reverse=True)
print(cars)

# 3.3.2 使用sorted()进行临时排序
# 保留列表原来的顺序，同时以特定的顺序呈现它们

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars,reverse=True))

print("\nHere is the original list again:")
print(cars)

# 3.3.3 倒着打印列表
cars.reverse()
print(cars)

# reverse()不是倒序排列，而是反转列表的排列顺序。
# reverse()永久改变排序，但是随时可以恢复

# 3.3.4 确定列表长度
# len()，列表包含4个元素，长度就是4
length = len(cars)
print(length)

zero_list = []
length = len(zero_list)
print(length)

places = ['tibet','dunhuang','xinjiang','taiwan','koyoto']

print("2.按照原始顺序打印:")
print(places)

print("3.使用sort()按字母顺序打印列表:")
print(sorted(places))

print("4.再次打印列表,核实列表顺序没有改变:")
print(places)

print("5.使用sorted()按与字母顺序相反的顺序打印:")
print(sorted(places,reverse=True))

print("6.打印这个列表核实是否修改了顺序:")
print(places)

print("7.使用reverse()修改元素排列顺序,打印核实:")
places.reverse()
print(places)

print("8.使用reverse()修改元素的排列顺序,打印核实恢复了顺序:")
places.reverse()
print(places)

print("9.使用sort()修改列表,使其元素按字母顺序排列:")
places.sort()
print(places)

print("10.使用sort()修改列表,使其按照相反顺序排列:")
places.sort(reverse=True)
print(places)

guests_names = ['grace', 'jersey', 'einstein']

guests_names.insert(0, 'alex')
guests_names.insert(2, 'michael')
guests_names.append('tom')

print("I have invited " + str(len(guests_names)) + " guests to have dinner with me.")

cars_brand = ['audi','bentley','bmw','cadillac','ferrari','benz','toyota']
cars_brand.sort()
print(cars_brand)

cars_brand.sort(reverse=True)
print(cars_brand)

sorted_cars_brand = sorted(cars_brand)
print(sorted_cars_brand)
print(sorted(cars_brand,reverse=True))

cars_brand.reverse()
print(len(cars_brand))


