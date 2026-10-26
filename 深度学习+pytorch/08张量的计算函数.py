"""
sum() max() min() mean()  都有dim参数 0表示列 1表示行
pow() sqrt() exp() log() log2() log10()  没有dim参数
"""
import torch
t1=torch.tensor([
    [1,2,3],
    [4,5,6],
    [7,8,9]
],dtype=torch.float32)
print(t1.sum(dim=0))#表示按列求和
print(t1.sum(dim=1))#表示按行求和
print(t1.sum())#表示整体求和

print(t1.max(dim=0))#表示按列求最大值
print(t1.max(dim=1))#表示按行求最大值
print(t1.max())#表示整体最大值
#indices表示维度

#mean()计算平均值,必须是浮点型才能进行计算
print(t1.mean(dim=0))
print(t1.mean(dim=1))
print(t1.mean())
# -------------------------------------------------
#没有dim参数
print(t1.pow(2))#每个数的平方
print(t1**2)
# sqrt()平方根
print(t1.sqrt())
