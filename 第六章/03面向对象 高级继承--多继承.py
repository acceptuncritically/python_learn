#class 子类名（父类名1，父类名2，...）
class Car:
    def __init__(self, brand, model, color,owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner
    def start(self):  # 启动
        print(f'{self.brand} {self.model} 正在启动...')
    def run(self):  # 行驶
        print(f'{self.__owner}{self.brand} {self.model} 正在行驶...')
        self.__control_fuel()
    def stop(self):  # 停止
        print(f'{self.brand} {self.model} 停止行驶...')
    # 如果是公共的方法是可以直接访问
    def __control_fuel(self):
        print(f'{self.brand} {self.model} 正在控制...')
    def charge(self):
        print(f'{self.brand} {self.model} 正在添加燃料...')
    def __str__(self):
        return f"{self.brand} {self.model} {self.color} "

class HuaweiAiDriving:
    """华为AI智能驾驶"""
    def __init__(self, version="V1.0"):
        self.version = version
    def run(self):
        print(f'使用华为AI智能驾驶系统{self.version}正在行驶...')
class WenJieCar(Car, HuaweiAiDriving):
    #如果既想要Car 中的属性 又想HuaweiAiDriving中的属性
    def __init__(self,brand, model, color,owner, version="V1.0"):
        # super().__init__() 调用第一个类
        Car.__init__(self, brand, model, color,owner)
        HuaweiAiDriving.__init__(self, version)
    def run(self):
        HuaweiAiDriving.run(self)
        Car.run(self)
if __name__=='__main__':
    #当一个类继承了多个父类时 默认优先使用第一个父类中的同名属性或方法
    #可以用类名.__mro__ 属性 或者 类名.mro()
    c=WenJieCar("Bmw","X5","black","lu")
    print(c.__dict__)
    c.run()
