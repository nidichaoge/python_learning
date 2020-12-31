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

# 遍历
# Python根据缩进来判断代码行与前一个代码行的关系
for co in color:
    print(co)
print("end")

numbers = list(range(1,5))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
for value in range(1,5):
    print(value)

squares = [value**2 for value in range(1, 11)]
print(squares)

# 切片
print(squares[0:3])
print(squares[:3])
print(squares[3:])

# 复制列表而互不影响
# other_squares = squares会互相影响
other_squares = squares[:]

# 不能修改的值称为不可变的，而不可变的列表被称为元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
    print(dimension)
# 报错
dimensions[0] = 300
print(dimensions[0])


