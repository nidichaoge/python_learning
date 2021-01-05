# 键—值对的排列顺序与添加顺序不同
# Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系
alien_0 = {'color': "green", 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['color'] = 'red'
print(alien_0['color'])
print(alien_0['x_position'])

print(alien_0)
del alien_0['color']
print(alien_0)

for key, value in alien_0.items():
    print(key)
    print(value)

for key in alien_0.keys():
    print(key)

# 按顺序遍历字典中的所有键
for key in sorted(alien_0.keys()):
    print(key)

for value in alien_0.values():
    print(value)

# 使用set对value去重
for value in set(alien_0.values()):
    print(value)

# 字典列表
# 字典中存储列表
# 字典中存储字典
