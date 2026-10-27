"""
演示张量的点乘和矩阵乘法操作
点乘 ：
    要求 两个张量的维度保持一致，组成的元素直接做相应的操作
    API
        t1*t2
        t1.mul(t2)
矩阵乘法：
    要求两个张量第一张量的列数 等于第二个张量的行数 （）A行*B列
    结果是A行B列
    API
        t1@t2
        t1.matmul(t2)
        t1.dot(t2) #只针对于一维张量有效
"""
import torch

#定义函数
def function1():
    t1 = torch.tensor([[1,2, 3],[4,5,6]])
    t2 = torch.tensor([[7,8,9],[10,11,12]])
    print(f"t1:{t1}\nt2:{t2}")
    t3=t1*t2
    print(f"t3:{t3}")
def function2():
    t1 = torch.tensor([[1,2,3],[4,5,6]])
    t2 = torch.tensor([[7,8,9],[10,11,12],[5,6,7]])
    # t3=t1@t2
    t3=t1.matmul(t2)
    print(f"t3:{t3}")
if __name__ == "__main__":
    function1()
    function2()
