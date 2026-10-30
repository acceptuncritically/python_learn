a="""
Sigmoid 函数表达式：
σ(x) = 1 / (1 ， e^(-x))
σ'(x) = e^(-x) / (1 ， e^(-x))^2
一般来说sigmoid网络在5层之内就会产生梯度消失现象，：导数范围为(0，0.25)5次后梯度接近零 网络参数更新缓慢
而且激活函数并不是以0为中心的 所以在实践中运用较少 sigmoid函数一般只用于二分类的输出层
数据在(-6，6)中变化明显 会将其中的值转化为[0，1]之间
Sigmoid (-6，6) (-3，3) (0，1) (0，0.25)

tanh(x) = sinh(x) / cosh(x)
        = (e^x - e^(-x)) / (e^x ， e^(-x))
d/dx tanh(x)= 4 * e^(2x) / (e^(2x) ， 1)^2
图像以0为中心 梯度相对于sigmoid大 收敛速度快 在大于3和小于-3 被映射为-1或1 导数映射为0
tanh (-3，3)(-1，1)(-1，1)(0，1)

ReLU=max(0，x)只考虑正样本 导数为0或1
当x>0时 不存在饱和问题 ReLU能够在x>0时保持梯度不衰减 从而缓解梯度消失问题 
随着训练的推进部分输入会落入小于0的区域内 导致权重无法更新 
可以使用Leakyrelu Prelu来考虑正负样本 

softmax用于多分类过程中 他是二分类函数sigmoid在多分类上的推广 目的是将多分类的结果以概率的形式展现出来
Softmax 函数数学公式：
S(z_i) = exp(z_i) / Σ(exp(z_j))   (其中 j 从 1 到 K)
就是将网络中输出的logits通过softmax函数映射成(0，1)的值 而这些值的累加和为1 选取概率最大的数 作为我们的预测目标类别 
参数说明：
z_i : 输入向量中的第 i 个元素 K   : 向量的总长度（元素个数） exp : 以自然常数 e 为底的指数函数
实际工程中的防溢出（数值稳定版）公式：
S(z_i) = exp(z_i - max_z) / Σ(exp(z_j - max_z))

# ==========================================
# 激活函数选择指南
# 对于隐藏层：
# 1. 优先选择 ReLU 激活函数。
# 2. 如果 ReLU 效果不好，那么尝试其他激活函数，如 Leaky ReLU 等。
# 3. 如果你使用了 ReLU，需要注意一下 Dead ReLU 问题，避免出现 0 梯度从而导致过多的神经元死亡。
# 4. 少使用 sigmoid 激活函数，可以尝试使用 tanh 激活函数。

# 对于输出层：
# 1. 二分类问题选择 sigmoid 激活函数。
# 2. 多分类问题选择 softmax 激活函数。
# 3. 回归问题选择 identity 激活函数（即不使用激活函数，直接输出原值）。
"""
import torch
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def sigmoid():
    # 创建画布和坐标轴 1行2列
    fig, axes = plt.subplots(1, 2)

    # 生成-20~20 之间的1000个数据点
    x = torch.linspace(-20, 20, 1000)

    # 计算上述的1000个点 Sigmoid激活函数处理过后的值
    y = torch.sigmoid(x)

    # 在第一个子图中绘制Sigmoid激活函数的图像
    axes[0].plot(x, y)
    axes[0].set_title('Sigmoid')
    axes[0].grid(True)

    # 在第二个图中绘制Sigmoid的导数图像
    # 重新生成1000个数据 并参数设置为可导
    x = torch.linspace(-20, 20, 1000, requires_grad=True)
    # 具体计算上述的1000点 Sigmoid激活函数导数后的值
    torch.sigmoid(x).sum().backward()

    axes[1].plot(x.detach(), x.grad)
    axes[1].set_title('Sigmoid的导数')
    axes[1].grid(True)
    plt.show()
def tanh():
    #创建画布和坐标轴 1行2列
    fig,axes=plt.subplots(1,2)
    
    #生成-20~20 之间的1000个数据点
    x=torch.linspace(-20,20,1000)
    
    #计算上述的1000个点 tanh激活函数处理过后的值
    y=torch.tanh(x)
    
    #在第一个子图中绘制tanh激活函数的图像
    axes[0].plot(x,y)
    axes[0].set_title('tanh')
    axes[0].grid(True)
    
    #在第二个图中绘制tanh的导数图像
    #重新生成1000个数据 并参数设置为可导
    x=torch.linspace(-20,20,1000,requires_grad=True)
    #具体计算上述的1000点 tanh激活函数导数后的值
    torch.tanh(x).sum().backward()
    
    axes[1].plot(x.detach(),x.grad)
    axes[1].set_title('tanh的导数')
    axes[1].grid(True)
    plt.show()
def relu():
    # 创建画布和坐标轴 1行2列
    fig, axes = plt.subplots(1, 2)
    x = torch.linspace(-20, 20, 1000)
    y = torch.relu(x)
    axes[0].plot(x, y)
    axes[0].set_title('relu')
    axes[0].grid(True)
    x = torch.linspace(-20, 20, 1000, requires_grad=True)
    torch.relu(x).sum().backward()

    axes[1].plot(x.detach(), x.grad)
    axes[1].set_title('relu的导数')
    axes[1].grid(True)
    plt.show()
def softmax():
    scores=torch.tensor([0.2,0.3,0.22,0.33,0.55])
    pro=torch.softmax(scores,dim=0)
    print(pro)#由于浮点数精度问题导致 概率和不为1
    print(pro.sum())
if __name__ == '__main__':
    # sigmoid()
    # tanh()
    # relu()
    softmax()