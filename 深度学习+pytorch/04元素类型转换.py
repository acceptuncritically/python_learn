"""
    创建指定类型的张量
涉及到的函数：
    type(Torch 支持的数据类型)
    half()/double()/float()/int()/long()
"""
import torch

t1=torch.tensor([1,2,3,4,5,6])
print(f"t1:{t1},元素类型：{t1.dtype}，张量类型:{type(t1)}")
# 通过dtype将张量里的元素类型转换
t2=torch.tensor([1,2,3,4,5,6],dtype=torch.float64)
print(f"t2:{t2},元素类型：{t2.dtype}，张量类型:{type(t2)}")

#创建好张量后进行转换
    #通过type函数
t3=t1.type(torch.float64)
    # half()/double()/float()/int()/long()
print(t2.half())        #float16
print(t2.double())      #float64
print(t2.float())       #float32
print(t2.int())         #int32
print(t2.long())        #int64
print(t2.short())       #int16
