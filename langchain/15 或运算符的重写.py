"""
在python 中运算符(+|)的行为是由 类的魔法方法决定的
a+b 本质调用的是 a.__add__(b)
a|b 本质调用的是 a.__or__(b)
只要自行实现类的__or__方法，即可对|符号的功能进行重写
"""

"""self 
保存和读取实例属性(绑定数据) 将数据保存到类中
调用同一个类中的其他方法 调用同一个类的其他方法
返回 self 实现链式操作
区分局部变量和实例变量 没有self的在方法结束后就消失了
self一直都是当前实例对象，我在__init__里使用self 是在self里添加属性 ，在运用时，改变他的属性
"""
class Test(object):
    def __init__(self,name):
        self.name =name
    def __or__(self,other):
        return MySequence(self,other)
    def __str__(self):
        return self.name

class MySequence(object):
    def __init__(self,*args):
        self.sequence=[]
        for arg in args:
            self.sequence.append(arg)
    def __or__(self,other):
        self.sequence.append(other)
        return self
    def run(self):
        for i in self.sequence:
            print(i)
        #由于i是实例对象 他就会去调用Test里的方法 如果没有__str__等的方法时就会直接打印出地址

if __name__=="__main__":
    a=Test("a")
    b=Test("b")
    c=Test("c")
    d=a|b|c
    print(d.run())
    print(type(d))