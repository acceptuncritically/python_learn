"""
张量的拼接操作
cat()   不改变维度数，拼接张量，除了拼接的哪个维度，其他维度数必须保持一致
stack()     会改变维度数，拼接张量，所有维度都必须保持一致
shape(2,2,3)里的数分别表示：
第 1 个数字 2（对应 0 维度/最外层）：数最外面的括号里，有几个“大块”。
第 2 个数字 2（对应 1 维度/中间层）：数第二层的括号里，有几个“小块”（比如几行）。
第 3 个数字 3（对应 2 维度/最内层）：数最里面的括号里，有几个“具体的数字”（比如几列）。
"""
import torch
t1=torch.randint(1,10,size=(2,3))
print(f"t1:{t1},shape:{t1.shape}")

t2=torch.randint(1,10,size=(2,3))
print(f"t2:{t2},shape:{t2.shape}")

#cat() 拼接张量
t3=torch.cat([t1,t2],dim=0) #(2，3)+(2，3)=(4，3)
print(f"t3:{t3},shape:{t3.shape}")

t3=torch.cat([t1,t2],dim=1) #(2，3)+(2，3)=(2，6)
print(f"t3:{t3},shape:{t3.shape}")

#会报错 超出了张量的维度
# t3=torch.cat([t1,t2],dim=2)
# print(f"t3:{t3},shape:{t3.shape}")

#stack() 拼接张量可以是新维度 ，但是无论新旧维度，所有维度都必须保持
t7=torch.stack([t1,t2],dim=0)   #(2,3)+(2,3)=(2,2,3)
print(f"t7:{t7},shape:{t7.shape}")      #在最前面加2

t8=torch.stack([t1,t2],dim=1)   #(2,3)+(2,3)=(2,2,3)
print(f"t8:{t8},shape:{t8.shape}")      #在中间加2

t9=torch.stack([t1,t2],dim=2)   #(
print(f"t9:{t9},shape:{t9.shape}")