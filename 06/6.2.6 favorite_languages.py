# 6.2.6 由类似对象组成的字典
favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    }
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

# >>>
# Sarah's favorite language is C.

# 练习
# 6-1 人
# 使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
# 该字典应包含键first_name 、last_name 、age 和city 。
# 将存储在该字典中的每项信息都打印出来
people = {'first_name':'jasmine','last_name':'wang','age':28,'city':'hangzhou'}
print("first_name: " + people['first_name'].title())
print("last_name: " + people['last_name'].title())
print("age: " + str(people['age']))
print("city: " +  people['city'].title())

# 6-2 喜欢的数字
# 使用一个字典来存储一些人喜欢的数字。
# 请想出5个人的名字，并将这些名字用作字典中的键;
# 想出每个人喜欢的一个数字，并将这些数字作为值存储在字典中。
# 打印每个人的名字和喜欢的数字。
# 为让这个程序更有趣，通过询问朋友确保数据是真实的。
numbers = {'wangli':167,'bob':186}
print("Wangli's favorite number is " + str(numbers['wangli']))
print("Bob's favorite number is " + str(numbers['bob']))

# 6-3 词汇表
# Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
# 想出你在前面学过的5个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
# 以整洁的方式打印每个词汇及其含义。
# 为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义;
# 也可在一行打印词汇，再使用换行符(\n )插入一个空行，然后在下一行以缩进的方式打印词汇的含义。

alphabet = {
    'print':'打印',
    'if':'条件判断',
    'for':'for循环',
    'list':'列表',
    'dictionary':'字典'
    }
print('print')
print('\t' + alphabet['print'])
print('\nif')
print('\t' + alphabet['if'])
print('\nfor')
print('\t' + alphabet['for'])
print('\nlist')
print('\t' + alphabet['list'])
print('\ndictionary')
print('\t' + alphabet['dictionary'])

# 6.3 遍历字典
# 6.3.1 遍历所有键值对

# 一个字典可能包含几个键值对，也可能包含数百万个键值对
# 字典可以遍历键值对、键或值

user_0 = {
    'username': 'feermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# 要编写用于遍历字典的for循环，可声明两个变量用于存储键值对的键和值
# 对于这两个变量，可以使用任何值
# items()方法返回一个键值对列表，for循环依次将每个键值对存储到对应的两个变量中

# >>>
# Key: username
# Value: feermi

# Key: first
# Value: enrico

# Key: last
# Value: fermi

# 对于favorite_languges，键都是人名，值都是语言，循环中变量使用name和language
for name, language in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language is " + language.title() + ".")

# >>>
# Jen's favorite language is Python.

# Sarah's favorite language is C.

# Edward's favorite language is Ruby.

# Phil's favorite language is Python.

# 6.3.2 遍历所有键
for name in favorite_languages.keys():
    print(name.title())

# >>>
# Jen
# Sarah
# Edward
# Phil

# 不需要使用值的时候，使用方法keys()
# 遍历字典时，会默认遍历所有的键
# for name in favorite_languages.keys(): 等效于：
# for name in favorite_languages:

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + 
        favorite_languages[name].title() + "!")

# >>>
# Jen
# Sarah
#  Hi Sarah, I see your favorite language is C!
# Edward
# Phil
#  Hi Phil, I see your favorite language is Python!

# 使用keys()确认某人是否接受了调查
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# >>>
# Erin, please take our poll!

# 方法keys()并非只能用于遍历，它返回一个列表，其中包含字典的所有键

# 6.3.3 按顺序遍历字典中所有的键

# 字典明确地记录了键和值的关联关系，但是获取字典的元素时，获取顺序是不可预测的
# 通常我们只关心键与值的对应关系
# 要想以特定的顺序返回元素，一种办法是对for循环中对返回的键排序
# 使用函数sorted()返回按特定顺序排列的键列表的副本
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# >>>
# Edward, thank you for taking the poll.
# Jen, thank you for taking the poll.
# Phil, thank you for taking the poll.
# Sarah, thank you for taking the poll.

# 6.3.4 遍历字典中的所有值
# 如果对字典包含的值感兴趣，使用方法values()
# values()返回一个值列表，不包含任何键
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 取出字典中所有的值，没有考虑元素的是否重复
# 为剔除重复项，可使用集合（set），集合类似于列表，每个元素必须是独一无二的
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("\nthe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# 通过对包含重复元素的列表调用set()，可让python找出列表中独一无二的元素
# 并使用这些元素创建一个集合

# 练习
# 6-4 词汇表
# 既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，
# 将其中的一系列print语句替换为一个遍历字典中的键和值的循环。
# 确定该循环正确无误后，再在词汇表中添加5个Python术语。
# 当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。

for word in alphabet:
    print(word + ': ' + alphabet[word] + '\n')

# 6-5 河流
# 创建一个字典，在其中存储三条大河流及其流经的国家。
# 其中一个键—值对可能是'nile': 'egypt'。
# 使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
# 使用循环将该字典中每条河流的名字都打印出来。
# 使用循环将该字典包含的每个国家的名字都打印出来。

rivers = {'Yangtze': 'china', 'amazon': 'Brasil', 'Tigris': 'Iraq'}
for river, country in rivers.items():
    print('The ' + river.title() + ' runs through ' + country.title() + '.')
for river in rivers.keys():
    print(river.title())
for country in rivers.values():
    print(country.title())

# 6-6 调查
# 在6.3.1节编写的程序favorite_languages.py中执行以下操作。
# 创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
# 遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。

favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    }

name_list = ['jen', 'phil']
for name in favorite_languages:
    if name in name_list:
        print('Thank you, ' + name.title() + '.')
    else:
        print(name.title() + ', please come to the party.')