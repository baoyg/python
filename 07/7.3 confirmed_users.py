# 7.3 使用while循环处理列表和字典

# 目前，每次都只处理了一项用户信息，获取用户的输入，再将输入打印出来
# 循环运行时，获取另一个输入并响应
# 需要大量记录用户和信息，就需要在while循环中使用列表和字典

# for循环时遍历列表的有效方式，但是在for循环中不应该修改列表
# 要想一边遍历一边修改，可使用while循环
# 将while循环同列表和字典结合起来使用
# 可收集、存储并组织大量输入，供以后查看和显示

# 7.3.1 在列表之间移动元素

# 假设有一个列表，包含新注册但是还未验证的用户
# 验证这些用户后，如何将他们移到另一个已验证用户列表中呢？
# 我们可以使用while循环，在验证用户的同时将其从未验证用户列表中提取出来
# 再将其加入到已验证用户列表中

# 首先创建待验证用户列表：
unconfirmed_users = ['alice', 'brian', 'candace']
# 创建用于存储已验证用户的空列表：
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止
while unconfirmed_users:
    # 将用户从未验证的列表中删除，并获取这个用户的值
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    # 将每个经过验证的列表都移到已验证用户列表中
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
# 遍历已验证用户列表，逐个打印之：
for confirmed_user in confirmed_users:
    print(confirmed_user.title())