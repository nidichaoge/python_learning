# input的输入解读为字符串
message = input("tell me something: ")
print(message)
# 字符串不能和数值进行比较, 使用int
print(message == 18)
age = int(message)
print(age == 18)

# while
current_number = 1
while current_number < 5:
    print(current_number)
    current_number += 1

# break
while True:
    if current_number > 10:
        break
    else:
        print(current_number)
        current_number += 1

# continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
