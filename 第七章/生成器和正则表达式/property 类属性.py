#类属性方式：
#类属性=property(获取值方法，设置值方法)
# 保护数据安全（封装
class Student:
    def __init__(self):
        self.age=None
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age
    # 封装上述的公共方式为类属性
    age=property(get_age,set_age)
if __name__ == '__main__':
    s=Student()
    print(s.age)