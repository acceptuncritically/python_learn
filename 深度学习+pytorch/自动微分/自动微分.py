"""
Pytorch 不支持向量张量对向量张量的求导，只支持标量张量对向量张量的求导
loss.sum().backward(),算完导数后自动反向传播  正向传播forword()
loss.sum()将张量中的值全部加起来 一个数字 进行变成标量张量
获取x点的梯度值 x.grid()会累加上一次的梯度值
    权重更新公式
        w新=w旧-学习率*梯度
        梯度=损失函数的导数
"""
import torch

#1定义变量 记录初始的权重w旧
#参1 初始值 参2是否进行自动微分 参3 数据类型
w=torch.tensor(10,requires_grad=True,dtype=torch.float)

#2 定义loss变量表示损失函数
loss=2*w**2
#3 打印梯度函数类型
print(f"梯度函数类型{type(loss.grad_fn)}")    #class 'MulBackward0'
# print(loss)    #它是一个 0 维的标量张量 所以看起来像一个浮点数
print(loss.sum())

#求导计算梯度
loss.sum().backward()
#带入权重更新公式
w.data=w.data-0.01*w.grad
print(w.data)

