import json

# 文件
# 读取文件 with在不再需要访问文件后自动将其关闭, 也可以使用close关闭文件但会有风险
with open("README.md") as file_object:
    contents = file_object.read()
    print(contents)

# 可以使用相对路径，也可以使用绝对路径
with open("/Users/mouse/testInput.txt") as file_object_2:
    contents = file_object_2.read()
    print(contents)

# 空白行问题 每行的末尾都有一个看不见的换行符，而print语句也会加上一个换行符，因此每行末尾都有两个换行符
# 使用rstrip()函数解决
with open("/Users/mouse/testInput.txt") as file_object_3:
    for line in file_object_3:
        print(line.rstrip())

# Python不限制文本的数据量
# 写入文件
# 读取模式（'r'）、写入模式（'w'）、附加模式（'a'）、能够读取和写入文件的模式（'r+'）Python默认只读模式打开文件
# 写入多行 使用\n换行符
with open("/Users/mouse/Desktop/test.txt", "w") as file_object_4:
    file_object_4.write("hello")

# 异常
# Python使用被称为异常的特殊对象来管理程序执行期间发生的错误
# ZeroDivisionError
# print(5/0)
try:
    print(5 / 0)
except ZeroDivisionError:
    print("can not divide by zero")

# try-except-else
print("give me two numbers,and i will divide them.")
print("enter 'q' to quit")
while True:
    first_number = input("first:")
    if first_number == 'q':
        break
    second_number = input("second:")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("can not divide by 0")
    else:
        print(answer)

# FileNotFoundError
# pass 什么都不要做
try:
    print(5 / 0)
except ZeroDivisionError:
    pass

# json
numbers = [1, 2, 3, 4, 5, 6]
# 写入到文件
with open("/Users/mouse/Desktop/number.json", "w") as filename:
    json.dump(numbers, filename)

# 读取文件
with open("/Users/mouse/Desktop/number.json") as filename2:
    number_result = json.load(filename2)
print(number_result)
