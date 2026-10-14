# 只继承非私有的
# 2.方法重写 在子类精确描述重写方法 在调用时 会执行子类中
#如果子类在重写时需要调用父类的方法 可以通过 父类名.方法名(self)/super().方法名()
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
        super.charge()
        #父类名.方法(self)
        print(f"{self.brand} {self.model} 正在加油")
class ElectricCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model} 正在充电...')
if __name__ == '__main__':
    fuelcar=FuelCar("aodi","A6","黑色","lu")
    print(fuelcar.brand)
