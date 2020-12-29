# 字符串""和''都可以
message = "hello world"
print(message)
message = 'hello mouse'
print(message)
print(message.title())
print(message.upper())
print(message.lower())

first = 'hello'
second = 'world'
result = first + second
print(result)

print(" hello world ".rstrip())
print(" hello world ".lstrip())
print(" hello world ".strip())

print(4 + 2)
print(4 - 2)
print(4 * 2)
print(4 / 2)
print(4 ** 2)

# 直接使用23报错，必须使用str()函数
age = 23
message = "happy " + str(age) + " birthday"
print(message)
