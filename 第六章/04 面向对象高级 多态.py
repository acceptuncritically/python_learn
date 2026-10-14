a="""多态指同一操作作用于不同对象时可以产生不同行为，
在 Python 中通常通过“鸭子类型”实现，即不关心对象属于哪个类，
只关心它是否具有所需的方法；也常通过继承和方法重写实现，
父类定义统一接口，子类重写具体行为，调用时用统一接口处理不同子类对象，
运行时根据对象实际类型决定调用哪个方法。使用时只需让不同类实现同名方法，
然后在函数中接收任意对象并调用该方法，例如定义 speak(obj) 函数并调用 obj.speak()
传入 Dog、Cat 等实例即可分别输出不同声音；也可用 abc 模块定义抽象基类来约束子类实现。
多态能提高代码的扩展性、复用性和可维护性，新增类型时通常无需修改调用逻辑
"""
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
class FuelCar(Car):
    def charge(self):
        Car.charge(self)
        #父类名.方法(self)
        print(f"{self.brand} {self.model} 正在加油")
class ElectricCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model} 正在充电...')
def handle_charge(car: Car):
    # car为形参
    car.charge()
if __name__ == '__main__':
    handle_charge(FuelCar("bmw","x5","black","lu"))
    handle_charge(ElectricCar("bmw","x5","black","lu"))