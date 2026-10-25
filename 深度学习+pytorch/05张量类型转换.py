"""
张量与numpy之间的转换
涉及到API
    张量-->numpy nd 数组
        张量对象.numpy()        共享内容
        张量对象.numpy().copy() 不共享内容
    numpy nd数组-->张量
        from_numpy()        共享内容
        torch.tnesor(nd数组)  不共享内容
    从标量张量中提取内容  标量张量：里面只装了一个数字的零维张量
        标量张量.item()
"""
import torch
import numpy as np

def function1():
    t1=torch.tensor([1,2,3])
    #张量转numpy
    # n1=t1.numpy()
    n1=t1.numpy().copy()
    print(f"t1:{t1},type(t1):{type(t1)}")
    print(f"n1:{n1},type(n1):{type(n1)}")
    #演示上述方式共享内存
    n1[0]=100
    print(f"n1:{n1},type(n1):{type(n1)}")
    print(f"t1:{t1},type(t1):{type(t1)}")
def function2():
    n1=np.array([1,2,3])
    print(f"n1:{n1},type(n1):{type(n1)}")
    print("-"*30)
    #把numpy数组转换为张量
    t1=torch.from_numpy(n1) #不共享内存
    t2=torch.tensor(n1)     #共享内存
    n1[0]=100
    print(f"n1:{n1},type(n1):{type(n1)}")
    print(f"t1:{t1},type(t1):{type(t1)}")
    print(f"t2:{t2},type(t2):{type(t2)}")
def function3():
    #在一个值的条件下才能提取出来
    t1=torch.tensor([100])
    print(f"t1:{t1},type(t1):{type(t1)}")
    value=t1.item()
    print(f"value:{value},type:{type(value)}")
if __name__ == "__main__":
    function1()
    print("-"*30)
    function2()
    print("-" * 30)
    function3()