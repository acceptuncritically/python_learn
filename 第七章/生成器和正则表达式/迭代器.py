"""
迭代器是一个实现了__iter__()和__next__()方法的对象，使得可以逐步遍历他的元素
手动管理：需要显示地实现__iter__() 和__next__()方法
状态管理：迭代器需要自己管理迭代的状态，包括当前位置和结束条件
内存使用：内存使用取决于迭代器的实现，通常是惰性计算（即按需生成数据）
只要重写了__iter__() 和__next__()方法，就可以成为迭代器
    目的：隐藏底层的逻辑，让用户使用更方便
        惰性加载，用的时候才会获取
"""
class MyIterator:
    def __init__(self, start,end):
        self.current_value = start
        self.end=end
    #重写iter方法
    def __iter__(self):
        return self
    def __next__(self):
        #判断当前值是否合法
        if self.current_value >= self.end:
            raise StopIteration
        # value = self.current_value
        # self.current_value += 1
        # return value
        self.current_value = self.current_value + 1
        return self.current_value-1
for i in MyIterator(1,10):
    print(i)
