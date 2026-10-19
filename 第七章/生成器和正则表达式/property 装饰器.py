"""
案例: 演示property属性的用法.

property属性介绍:
    概述/目的/作用:
        把 函数 当做 变量(属性)来使用.
    实现方式:
        方式1: 装饰器.
        方式2: 类属性.
property的装饰器用法:
    @property                   修饰 获取值的函数
    @获取值的函数名.setter      修饰 设置值的函数

    之后, 就可以直接 .上述的函数名 来当做变量直接用.
"""
# 需求: 定义学生类, 私有属性 age, 通过property实现简化调用.
class Student:
    def __init__(self):
        self.age =18
        # 提供公共的访问方式
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        # 可以在这里进行判断
        self.__age=age
if __name__ == '__main__':
    student=Student()
    student.age=18
    print(student.age)
