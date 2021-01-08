import dog

my_dog = dog.Dog("willie", 6)
print(my_dog.name)
my_dog.sit()

# 直接修改属性值
my_dog.name = 'chao'
print(my_dog.name)
# 通过方法修改属性值
my_dog.update_name("mouse")
print(my_dog.name)


# 继承 一个类继承另一个类时，它将自动获得另一个类的所有属性和方法
# 创建子类的实例时，Python首先需要完成的任务是给父类的所有属性赋值
# 创建子类时，父类必须包含在当前文件中，且位于子类前面
# 定义子类时，必须在括号内指定父类的名称
class Car():
    """Car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return str(self.year) + " " + self.make + " " + self.model


class ElectricCar(Car):
    """ElectricCar"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = 70

    def get_descriptive_name(self):
        return str(self.year) + " " + self.make + " " + self.model + " "


my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())

# 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加上下划线。
