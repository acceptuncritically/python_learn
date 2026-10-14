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
if __name__ == '__main__':
    car=Car("aodi","A6","黑色","lu")
    print(car.brand)
    print(car.model)
    print(car.color)
    # 封装在私有里 不能在这里查询 与应用
    car.start()
    car.run()
    car.stop()
    # python里没有真正的私有属性 可以在方法或属性前加上_Car
    print(car._Car__owner)
