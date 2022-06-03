# 6.4 嵌套
# 有时候，需要将一系列字典存储在列表中
# 或者将列表存储在字典中，这称为嵌套
# 你可以在列表中嵌套字典，在字典中嵌套列表甚至字典

# 6.4.1 字典列表

# 字典alien_0包含一个外星人的各种信息
# 但是无法存储第二个外星人的信息
# 如何管理成群结队的外星人呢？
# 可以创建一个外星人列表，每个外星人是一个字典

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# >>>
# {'color': 'green', 'points': 5}
# {'color': 'yellow', 'points': 10}
# {'color': 'red', 'points': 15}

# 事实上，外星人不止3个，每个外星人是代码自动生成的
# 我们使用range()生成30个外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print('...')
print("Total number of aliens: " + str(len(aliens)))

# 在python看来，这些外星人都是独立的，可以独立修改属性
# 有时需要一大群外星人，它们会变色，还会变速
# 使用for循环和if语句修改前三个外星人的属性
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens [:5]:
    print(alien)
print('...')

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens [:10]:
    print(alien)
print('...')