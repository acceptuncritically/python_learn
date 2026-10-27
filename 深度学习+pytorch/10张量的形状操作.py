"""
演示张量的形状操作
reshape()           在不改变张量内容的情况下 对其形状进行改变
unsqueeze()         在指定位置轴上添加一个(1)维
squeeze()           删除所有为1的维度 相当于降维
transpose()         一次只能交换两个维度
permute()           一次性可以交换多个维度
view()
contiguous()
is_contiguous()
"""
import torch
torch.manual_seed(24)
def function1():
    t1 = torch.randint(1,10,size=(2,3))
    print(f"t1:{t1},shape:{t1.shape},row:{t1.shape[0]},col:{t1.shape[1]},{t1.shape[-1]}")
    #通过reshape函数 将t1变成 1行5列 4行2列
    t2=t1.reshape(1,6)
    # t2=t1.reshape(3,2)  要保证张量数量一致 否则无法改变报错
    print(f"t2:{t2},shape:{t2.shape}")
def function2():
    t1 = torch.randint(1,10,size=(2,3))     #(2,3)
    print(f"t1:{t1}")
    #在0维上添加一个维度
    t2=t1.unsqueeze(0)                      #(1,2,3)
    print(f"t2:{t2},shape:{t2.shape}")
    t3=t1.unsqueeze(1)                      #(2,1,3)
    print(f"t3:{t3},shape:{t3.shape}")
    #在二维上添加一个维度
    t4=t1.unsqueeze(2)                      #(2,3,1)
    print(f"t4:{t4},shape:{t4.shape}")
    #无法跳一个维度添加维度
    t5=t1.unsqueeze(3)                      #(2,3,*,1)
    print(f"t5:{t5},shape:{t5.shape}")
    #删除所有为1的维度
    t6=torch.randint(1,10,size=(2,1,3,1,1))
    print(f"t6:{t6},shape:{t6.shape}")
    t7=t6.squeeze()                          #(2,3)
    print(f"t7:{t7},shape:{t7.shape}")
def function3():
    #定义张量
    t1 = torch.randint(1,10,size=(2,3,4))
    print(f"t1:{t1},shape:{t1.shape}")
    print("-"*30)
    t2=t1.transpose(0,1) #交换第1和2列 也可以用负数表示
    print(f"t2:{t2},shape:{t2.shape}")
    print("-"*30)
    #改变维度从(2,3,4)-->(4,2,3)
    t3=t1.permute(2,0,1)
    print(f"t3:{t3},shape:{t3.shape}")
def function4():
    t1 = torch.randint(1,10,size=(2,3))
    print(f"t1:{t1},shape:{t1.shape}")
    #判断张量是否连续 ：张量中的顺序是否和内存中的数据顺序一致
    # print(t1.is_contiguous())
    t2=t1.view(3,2)
    print(f"t2:{t2},shape:{t2.shape}")
    print(t2.is_contiguous())

    #通过transpose()交换维度后 导致维度不连续了
    t3=t1.transpose(0,1)
    print(f"t3:{t3},shape:{t3.shape}")
    print(t3.is_contiguous())

    #尝试把t3张量从(3,2) 通过view()转成(2,3)
    t4=t1.view(2,3)
    print(f"t4:{t4},shape:{t4.shape}")
if __name__ == '__main__':
    function1()
    function2()
    function3()
