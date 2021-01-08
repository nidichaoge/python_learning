# class创建类 类名首字母大写
# 类中的函数叫做方法
# __init__是一个特殊的方法 每当根据类创建新实例时，Python都会自动运行它
# 形参self必不可少，还必须位于其他形参的前面。
# 因为Python调用这个__init__()方法来创建实例时，将自动传入实参self。每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
class Dog:
    """a dog"""

    def __init__(self, name, age):
        """INIT name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """sit"""
        print(self.name.title() + " is now sitting.")

    def update_name(self, name):
        self.name = name

