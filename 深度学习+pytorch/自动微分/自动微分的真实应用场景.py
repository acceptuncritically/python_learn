"""
结论：
    1.先正向传播计算出预测值(z)
    2.基于损失函数，结合预测值(z)和真实值(y) 来计算梯度
    3.结合权重更新公式 w新=w旧-学习率*梯度 来更新权重
"""
import torch
#定义x表示特征(输入数据) 假设2行5列 全1矩阵
x=torch.ones(2,5)

#定义y 表示 标签(真实值) 假设2行3列 全0矩阵
y=torch.ones(2,3)

#初始化(可自动微分的)权重 和 偏置
w=torch.randn(5,3,requires_grad=True)
#由于 w@x=Y  w的列和y的行相同-->第一个位置为5  w@x的结果为A行B列--> 第二个位置为3
b=torch.randn(3,requires_grad=True) #3是因为w的列数为3要对每一列w 都有一个b进行累加

#前向传播 计算出 预测值(z)
z=x@w+b
print(f"z:{z}")

#定义损失函数
criterion=torch.nn.MSELoss()#neural network:神经网络
loss=criterion(z,y)         #loss=损失

#反向传播 计算梯度
print(f"loss:{loss}")
#进行自动微分 求导 结合反向传播 更新权重
loss.sum().backward()
#打印更新后的 w b
print(f"w.grad:{w.grad}")
print(f"b.grad:{b.grad}")