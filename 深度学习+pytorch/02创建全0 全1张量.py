"""
创建全0全1指定值的张量
    torch.ones和torch.ones_like(tensor类型) 创建全1变量
    torch.zeros和torch.zeros_like 创建全0变量
    torch.full和  torch.full_like 创建指定值变量
zeros() full()
"""
import torch

#创建全1变量
t1=torch.ones(3,4)
print(f"t1:{t1},type(t1):{type(t1)}")
print("-"*20)
t2=torch.tensor([[1,2],[3,4],[5,6]])
print(f"t2:{t2},type(t2):{type(t2)}")
print("-"*20)
t3=torch.ones_like(t2)
print(f"t3:{t3},type(t3):{type(t3)}")
#创建了一个和t2一样模板的全一张量

#创建全0变量

#创建指定值变量

t1=torch.full(size=(3,4),fill_value=255)
print(f"t1:{t1},type(t1):{type(t1)}")
print("-"*20)
t2=torch.tensor([[1,2],[3,4],[5,6]])
print(f"t2:{t2},type(t2):{type(t2)}")
print("-"*20)
t3=torch.full_like(t2,255)
print(f"t3:{t3},type(t3):{type(t3)}")
#0~255 颜色 白到黑