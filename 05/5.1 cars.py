# 5 if语句
# 有时需要检查一些条件，据此决定采取什么措施

# 5.1 一个简单示例
# 假设有一个汽车列表，将每辆车的名称打印出来
# 对大多数汽车以首字母大写打印，对于bmw以全大写的方式打印

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())