"""
torch.arange()和torch.linspace() 创建线性变量
torch.random.inital_seed()和torch.random.manual_seed()随机种子设置
torch.rand/randn()创建随机浮点类型张量
torch.randint(low,high,size=()) 创建随机整数类型张量

arange(),linspace(),manual_seed(),randint()
"""
import torch
#定义函数创建线性张量
def function1():
    """
    参数表示 开始 结束 步长 不包括结束
    """
    #创建指定范围的线性张量
    t1=torch.arange(0,10,2) #0 2 4 6 8
    print(f"t1:{t1},type(t1):{type(t1)}")
    print("-"*30)
    #创建等差数列的线性张量
    """
    参数表示 开始 结束 元素个数 包括结束
    """
    t2=torch.linspace(1,10,5)
    #将1到10分成5份，包含1和10
    print(f"t2:{t2},type(t2):{type(t2)}")
# 定义函数创建随机张量
def function2():
    #设置随机种子
    torch.initial_seed() #默认采用当前系统的时间作为随机种子
    # torch.manual_seed(0)  #随机种子相同返回的张量也相同
    #创建随机张量

    #创建均匀分布的随机张量
    t1=torch.rand(size=(3,4))
    print(f"t1:{t1},type(t1):{type(t1)}")
    print("-"*30)
    #符合正太分布的随机张量
    t2=torch.randn(size=(3,4))
    print(f"t2:{t2},type(t2):{type(t2)}")
    print("-"*30)
    #创建随机整数张量
    t3=torch.randint(low=1,high=10,size=(3,4))
    print(f"t3:{t3},type(t3):{type(t3)}")
if __name__=="__main__":
    function1()
    function2()