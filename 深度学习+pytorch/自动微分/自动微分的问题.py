"""
一个张量一旦设置了自动微分，这个张量旧不能直接转成numpy的ndarry对象了，需要通过detach()函数
"""
import torch

#定义张量
t1=torch.tensor([10,20],requires_grad=True,dtype=torch.float)
t2=t1.detach()
print(f"t1:{t1},type(t1):{type(t1)}")
print(f"t2:{t2},type(t2):{type(t2)}")
print("-"*30)
#判断t1和t2是否可以自动微分
print(t1.requires_grad) #True
print(t2.requires_grad) #False

#将t2转换成numpy对象
n1=t2.numpy()
print(f"n1:{n1},type(n1):{type(n1)}")

#链式效果
# n2=n1.detach().numpy()
# print(f"n2:{n2},type(n2):{type(n2)}")