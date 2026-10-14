"""
class 类名：
    pass
对象名=类名（）
对象名.属性名=属性值
对象名.属性名=属性值
对象名.属性名=属性值

"""
# -------------------------------------------------
# class Car:
#     def __init__(self,c_name,c_price,c_brand):
#         self.name=c_name
#         self.price=c_price
#         self.brand=c_brand
#         print("实例对象添加完毕")
"""
     将特定参数应用到实例中确定调用时需要加入的值
     方便下面调用
"""
#     def running(self):
#         print(f"{self.brand}{self.name}已被买下")
#     def total(self,rate):
#          total=self.price+self.price*rate
#          return total
"""
    在其他方法中要调用实例对象里的值时要用 self.参数
"""
# c1=Car("苹果",8848,"iPhone18")
# print(c1.__dict__)
"""
会以字典的形式输出结果
"""
# print(f"总价为{c1.total(0.1)}")
# c1.running()
# ---------------------------------------
class Car:
    wheel=4
    def __init__(self,c_name,c_price,c_brand):
        self.name=c_name
        self.price=c_price
        self.brand=c_brand
        print("实例对象添加完毕")
    def running(self):
        print(f"{self.brand}{self.name}已被买下")
    def total(self,rate):
         total=self.price+self.price*rate
         return total
    def __str__(self):
        return f"{self.name} {self.price} {self.brand}"
    def __lt__(self,other):
        return self.price<other.price
    """
    相当于if else 的缩写
    系统会自己判断谁是self
    """
    def __eq__(self,other):
        return self.price==other.price and self.brand==other.brand and self.name==other.name
c1=Car("苹果",8848,"iPhone18")
"""
当加上__str__时直接输出c1并不会得到地址，而是得到自己所定义的字符串
"""
c2=Car("苹果",8848,"iPhone18")
print(c1)
print(c2==c1)
print(c2<c1)
print(Car.wheel)
print(c1.wheel)
# ------------------------------------------------------------
"""
类属性：通过类名.属性的方式操作
直接像平常定义，定义在class类的下面
实例属性：通过实例对象.属性的方式操作
通过实例查找属性时，会先查找实例属性，然后再查找类属性
"""