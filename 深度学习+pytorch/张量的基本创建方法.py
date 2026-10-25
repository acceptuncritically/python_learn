"""
什么是张量
PyTorch中的张量就是元素为同一种数据类型的多维矩阵。在PyTorch中，张量以“类”的形式封装起来，对张量的一些运算、处理的方法被封装在类中。

PyTorch张量与NumPy数组类似，但PyTorch的张量具有GPU加速的能力（通过CUDA），这使得深度学习模型能够高效地在GPU上运行。

PyTorch提供了对张量的强大支持，可以进行高效的数值计算、矩阵操作、自动求导等。

张量是 PyTorch 中的核心数据抽象，PyTorch 支持各种张量子类型。通常地，一维张量称为向量/矢量（vector），
"""
"""
张量：

    PyTorch框架属于 最常用的深度学习框架，无论是后续要学的ANN(人工神经网络)，还是CNN(卷积神经网络)，RNN(循环神经网络)
    底层在处理数据时，都是使用 张量 来处理的.

    张量 -> 存储同一类型元素的容器，且元素值必须是 数值才可以.

张量的基本创建方式：

    torch.tensor 根据指定数据创建张量 可以通过dtype来确定张量类型
    torch.Tensor 根据形状创建张量，其也可用来创建指定数据的张量
    Tensor创造张量时不能指定类型，基本用法和tensor一致
    torch.IntTensor、torch.FloatTensor、torch.DoubleTensor 创建指定类型的张量
"""
import torch
import numpy as np
def founction1():
    #可以通过dtype里来决定创建的张量是什么类型
    t1=torch.tensor(10)
    print(f"t1: {t1},type(t1): {type(t1)}")
    #列表-->张量
    data=[[1,2],[2,3]]
    t2=torch.tensor(data)
    print(f"t2: {t2},type(t2): {type(t2)}")
    #
    data=np.random.randint(0,10,size=(2,3))#size代表生成两行三列的矩阵
    t3=torch.tensor(data)
    print(f"t3: {t3},type(t3): {type(t3)}")
def founction2():
    t4=torch.Tensor(2,3)
    print(f"t4: {t4},type(t4): {type(t4)}")
def founction3():
    #如果类型不匹配，会尝试自动转变类型，转换不了就报错
    data=10
    t5=torch.FloatTensor(10) #默认float32
    print(f"t5: {t5},type(t5): {type(t5)}")
if __name__=="__main__":
    founction1()
    founction2()
    founction3()

