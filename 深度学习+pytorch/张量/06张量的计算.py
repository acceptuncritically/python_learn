"""
张量的基本运算
    add() sub() mul() div() neg()取反
    add_() sub_() mul_() div_() neg_() 可以修改原数据
    + - * / 可以用符号替代加减乘除
    如果是张量和数值运算，则张量会和数据中的每个值依次进行运算
"""
import torch
def add_function():
    t1=torch.tensor([1,2,3])
    t2=t1.add(10)#相当于t1+=10
    # t3=t1.add_(10)
    print(f"t1:{t1},type(t1):{type(t1)}")
    print(f"t2:{t2},type(t2):{type(t2)}")
    # print(f"t3:{t3},type(t3):{type(t3)}")
def sub_function():
    t1=torch.tensor([1,2,3])
    t2=t1.sub(10)#相当于t1-=10
    # t3=t1.sub_(10)
    print(f"t1:{t1},type(t1):{type(t1)}")
    print(f"t2:{t2},type(t2):{type(t2)}")
    # print(f"t3:{t3},type(t3):{type(t3)}")
def neg_function():
    t1=torch.tensor([-1,-2,-3])
    t2=t1.neg()
    print(f"t1:{t1},type(t1):{type(t1)}")
    print(f"t2:{t2},type(t2):{type(t2)}")
if __name__ == "__main__":
    add_function()
    sub_function()
    neg_function()