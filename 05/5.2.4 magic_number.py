# 5.2.4 比较数字
# 检查两个数字是否不等

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# 5.2.5 检查多个条件
answer_1 = 18
answer_2 = 12
if answer_1 >= answer and answer_2 <= answer:
    print("OK")

if answer_1 > answer or answer_2 > answer:
    print("Fine")

# 5.2.6 检查特定值是否包含在列表中

requested_toppings = ['mushroom', 'onions', 'pineapple']
if 'mushroom' in requested_toppings:
    print("We got mushrooms!")
if 'pepperoni' in requested_toppings:
    print('We got pepperoni!')
else:
    print("We gotta buy some pepperoni!")