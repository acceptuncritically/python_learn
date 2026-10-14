# 元素可重复，有序，不可修改
# 组包：将多个值合并到一个容器
# 解包：将容器解开成独立的元素，分别赋值给多个变量
from operator import index


t1=(5,7,9,1)
t2=5,7,9,1
t1.index()
t1.count()
print(t1,t2)
a,b,c,d=t1
G=a,b,c,d#变量与数据一一对应
print(a,b,c,d)
print(G)
# *表示收集剩余的元素，允许我们处理不确定数量的元素
x,*y,z=t1
print(x,y,z)
s,*o=t1
print(s,o)
# *变量 类型变为列表中


# 用元组
a=10
b=20
a,b=b,a
a=100
b=200
c=300
c,a,b=a,b,c
print(a,b,c)