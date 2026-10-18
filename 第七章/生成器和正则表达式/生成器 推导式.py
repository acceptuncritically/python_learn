# 根据程序员设定的规则，当条件不成立的时候生成数据结束，数据不是一次性全部输出,来解决内存问题
"""
创建生成器方式，
    生成器推导式，
    yield关键字
"""
# 生成器推导式 （）不是元组
import sys
my_generator=(i for i in range(10) )
#generator是一个对象
print(my_generator)
print(type(my_generator))
print("--------------------")

# 如何从生成器中获取元素
print(next(my_generator))
print(next(my_generator))
# 基于当前指针继续向下输出
print("--------------")
for i in my_generator:
    print(i)

#验证生成器的目的 就是可以减少内存空间
my_list=[i for i in range(1000000)]
my_get3=(i for i in range(1000000))
print(f"my_list: {sys.getsizeof(my_list)}")
print(f"my_get3: {sys.getsizeof(my_get3)}")
