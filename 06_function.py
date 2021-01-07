import pizza
from pizza import make_pizzas


# def定义函数
def greet_user():
    # 文档字符串的注释 用来生成有关程序中函数的文档
    """打印hello"""
    print("hello")


def greet_user(username):
    print("hello " + username)


greet_user("1")
greet_user("mouse")


# 实参和形参
# 向函数传递实参的方式：位置 关键字 列表 字典
# 给定默认值
def describe_pet(animal, pet='mouse'):
    print("my " + animal + " name is " + pet)


# 位置
describe_pet("dot", "mouse")
# 关键字
describe_pet(animal='cat', pet='chao')


# 返回值
def get_name(first_name, last_name):
    return first_name + last_name


print(get_name("hou", "wenchao"))


# Python将非空字符串解读为True
def get_formatted_name(first, last, middle=''):
    if middle:
        return first + middle + last
    else:
        return first + last


print(get_formatted_name("hou", "wen"))
print(get_formatted_name("hou", "wen", "chao"))


# 在函数中对列表所做的修改都是永久性的, 可以传递列表的副本从而使得不影响原件 list_name[:]

# 传递任意数量的实参 *让python创建了一个空元祖
# 结合位置实参时 任意数量实参必须放最后
def make_pizza(*toppings):
    print(toppings)


make_pizza("1", "2", "3")


# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {'first': first, 'last': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('first', 'last', second='second')
print(user_profile)

# import导入模块
pizza.make_pizzas(12, "1")
# from module_name import function_name,function_name2导入特定函数
make_pizzas(12, "1", "2")
# as 可以给模块或者函数指定别名
# mp(12,"1","2")
# *可以导入模块中所有函数

# 函数名称只使用 小写字母和下划线
# 所有的import都放在文件开头
