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