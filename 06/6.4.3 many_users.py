# 6.4.3 在字典中存储字典

# 可以在字典中嵌套字典，虽然代码会变得很复杂
# 例如，对于每个用户，我们存储了其三个信息：名、姓、居住地
# 为了访问这些信息，我们遍历所有的信息，访问关联的信息字典

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

# >>>>
# Username: aeinstein
#         Full name: Albert Einstein
#         Location: Princeton

# Username: mcurie
#         Full name: Marie Curie
#         Location: Paris

# 练习 
# 6-7 人
# 在为完成练习6-1而编写的程序中，再创建两个表示人的字典，
# 然后将这三个字典都存储在一个名为people的列表中。
# 遍历这个列表，将其中每个人的信息都打印出来

jasmine = {'first_name':'jasmine','last_name':'wang','age':28,'city':'hangzhou'}
bob = {'first_name':'bob','last_name':'bao','age':30,'city':'wuhan'}
my_child = {'first_name':'siqi','last_name':'bao','age':'1','city':'hangzhou'}
people = [jasmine,bob,my_child]
for p in people:
    print(p)

# 6-8 宠物
# 创建多个字典，对于每个字典，都使用一个宠物的名称命名
# 每个字典中，包含宠物的类型和主人的名字
# 将这些字典存储在一个名为pets的列表中
# 遍历该列表，将宠物的所有信息打印出来

lele = {'pet':'萨摩耶','name':'bob'}
huahua = {'pet':'柴犬','name':'lily'}
tutu = {'pet':'柯基','name':'bob'}
tiaotiao = {'pet':'拉布拉多','name':'lili'}
pets = [lele,huahua,tutu,tiaotiao]
for p in pets:
    for key, value in p.items():
        print(key)
        print(value)

# 6-9 喜欢的地方
# 创建一个名为favorite_places的字典
# 在这个字典中，将三个人的名字用作键
# 对于其中每一个人都存储他喜欢的1-3个地方
# 为让这个练习更有趣，让一些朋友指出她们喜欢的几个地方
# 遍历这个字典，将其中每个人的名字及其喜欢的地方打印出来

favorite_places = {
    'bob':['nanjing','hangzhou','guangzhou'],
    'lily':['hainan','xiamen','qingdao'],
    'wangli':['chengdu','hangzhou','beijing']
    }
for key, value in favorite_places.items():
    print("\n" + key.title() + "'s favorite places are: ")
    for v in value:
        print("\t" + v.title())

# 6-10 喜欢的数字
# 修改6-2，让每个人都可以有多个喜欢的数字
# 然后将每个人的名字、数字打印出来

numbers = {
    'wangli':[167,88,66,123],
    'bob':[186,11,22,33,44]
    }
for name, num in numbers.items():
    print(name.title() + "'s number is")
    for n in num:
        print("\t" + str(n))

# 6-11 城市
# 创建一个名为cities的字典，将3个城市名用作键
# 对于每个城市创建一个字典，在其中包含该城市所属的国家、人口数以及有关该城市的事实
# 在表示每座城市的字典中，包含country、population、fact等键
# 将每座城市的名字及它们的信息打印出来。

cities = {
    'wuhan':{
        'country':'china',
        'population':'13.64 million',
        'fact':'There are 166 lakes in Wuhan.'
        },
    'tokyo':{
        'country':'japan',
        'population':'420 million',
        'fact':'There are 202 harbors in tokyo'
        },
    'cairo':{
        'country':'egypt',
        'population':'22.80 million',
        'fact':'there are 110 Pyramids in Egypt.'
        }
    }
for city, info in cities.items():
    print("Here is the city: " + city)
    for k, v in info.items():
        print("\tThe " + k + " is " + v)

# 6-12 扩展
# 本章的示例足够复杂，可以以很多方式进行扩展了。
# 请对本章的一个示例进行扩展：添加键和值，调整程序要解决的问题或改进输出的格式

# 略