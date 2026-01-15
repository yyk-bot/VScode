#注释：类、编译器、解释器
#类：是一种软件设计模式，它是面向对象编程中的一种抽象数据类型，用于组织数据（属性）和操作（方法），用于创建具有相似特性的对象实例。类定义了对象的状态和行为，是构建复杂程序结构的基础。
#编译器：是一种计算机程序，它将源代码（如高级语言如Java、C++等）转换成机器语言（例如汇编语言或二进制代码）。这个过程称为编译，编译器会检查语法错误，并生成可以直接由计算机硬件执行的目标代码，通常在一个单独的步骤完成。
#解释器：是在运行时逐行解析并执行代码的程序。它并不像编译器那样预先把整个程序转换成机器码，而是一行一行地读取源代码，理解其含义后直接执行。解释器常用于脚本语言（如Python、JavaScript），它们的优点在于交互性强、动态类型检查，但执行效率相对较低。
# 注释：封装、继承和多态
# 封装：
# 它是一种数据隐藏的技术，通过将数据和操作这些数据的方法捆绑在一起形成一个独立的对象。
# 继承：
# 子类可以从父类继承属性和方法。
# ```
# class ChildClass(ParentClass):
#     pass  # 可以添加自定义的方法或覆盖父类的行为
# ```
# 多态：
# 同一接口的不同实例可以响应相同的调用，表现为多种形态。Python中的动态绑定允许我们在运行时确定实际调用哪个方法。
# def parent_method(self):  # 父类方法
#     print("Parent method")
#
# class ChildClass:
#     def parent_method(self):  # 子类重写
#         print("Child method")
#         
# obj = ChildClass()  # 创建子类实例
# obj.parent_method()  # 输出 "Child method"，体现了多态
# ```
class Animal:
    def __init__(self,name):
        self.name = name  # 封装：将属性设为私有
    
    def eat(self):  # 多态：子类需实现此方法
        print('食物')
    
    def sound(self):  # 多态：子类需实现此方法
        pass    

class Dog(Animal):  # 继承：Dog类继承自Animal类
    
    def __init__(self):
        super().__init__('小狗')
    
    def sound(self):
        print('汪')

class Cat(Animal):  # 继承：Cat类继承自Animal类
    
    def __init__(self):
        super().__init__('小猫')
    
    def sound(self):
        print('喵')

def makesound(animal):
    animal.sound()  # 多态：根据传入对象的实际类型调用相应的方法

dog=Dog()  #定义dog
cat=Cat()  #定义cat

print(dog.name)  # 输出
dog.eat()  # 输出
makesound(dog)  # 输出
print(cat.name)  # 输出
cat.eat()  # 输出
makesound(cat)  # 输出