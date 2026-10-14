class Duck: # 2用法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self): # 启动 1个用法
        print(f'{self.age} 岁的 {self.name} 正在游泳...')

class Dog: # 1个用法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self): # 启动
        print(f'{self.age} 岁的 {self.name} 正在游泳...')


class Pig: # 1个用法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self): # 启动
        print(f'{self.age} 岁的 {self.name} 正在游泳...')
def go__swimming(duck):
    duck.swimming()
if __name__ == '__main__':
    go__swimming(Dog("wang",1))
    go__swimming(Duck("ga",2))
    go__swimming(Pig("hong",3))