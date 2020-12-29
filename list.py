color = ['RED', 'BLUE', 'YELLOW']
print(color)

print(color[0])
# 负数返回倒数第几个元素
print(color[-1])

color[0] = 'PICK'
print(color)

color.append('RED')
print(color)

color.insert(0, 'BLACK')
print(color)

# del删除无法使用 pop删除可以使用
del color[0]
print(color)

result = color.pop()
print(result)
print(color)

color.remove('BLUE')
print(color)

# sort()永久 sorted()临时
color.sort()
print(color)
color.sort(reverse=True)
print(color)

print(sorted(color))
print(color)

# 永久
color.reverse()
print(color)

print(len(color))
