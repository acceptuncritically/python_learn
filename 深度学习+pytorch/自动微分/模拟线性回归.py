"""
numpy对象-->张量tensor-->数据库对象tensordataset-->数据加载器dataloader
现在是自己创造的数据可以看到标准w值 而在真实数据中 并不知道其中的w值 所以会减小loss值 相当于逼近真实w
"""
import torch
from torch.utils.data import TensorDataset  # 构造数据集对象
from torch.utils.data import DataLoader     # 数据加载器
from torch import nn                        # nn模块中有平方损失函数和假设函数
from torch import optim                     # optim模块中有优化器函数
from sklearn.datasets import make_regression # 创建线性回归模型数据集
#要下载pip install scikit-learn -i https://pypi.tuna.tsinghua.edu.cn/simple
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号

#定义函数创建线性回归样本数据
def create_dataset():
    x,y,coef=make_regression(
        n_samples=100,  #100条样本点
        n_features=1,  #一个特征点
        noise=10,       #噪声越大 样本点越散
        coef=True,      #是否返回系数 默认为False 返回值为None
        bias=14,        #偏置
        random_state=3    #随机种子 随机种子相同 输出数据相同
    )
    #此时为ndarray
    # print(type(x))
    #将numpy数据封装为tensor对象
    x=torch.tensor(x,dtype=torch.float)
    y=torch.tensor(y,dtype=torch.float)
    # 返回参数
    return x,y,coef
def train(x,y,coef):
    # numpy对象 -->张量tensor -->数据库对象tensordataset -->数据加载器dataloader
    dataset=TensorDataset(x,y)
    #参1 数据集对象 参2 批次大小 参3 是否打乱数据 (训练集打乱 测试集不打乱)
    dataloader=DataLoader(dataset,batch_size=10,shuffle=True)
    #创建出事的线性回归模型
    #参1 表示输入的维度 参2 表示输出的维度
    model=nn.Linear(1,1)
    #创建损失函数对象
    critertion=nn.MSELoss()
    #创建优化器对象
    #参1 表示模型参数 参2 表示学习率
    optumizer=optim.SGD(model.parameters(),lr=0.01)
    #具体的训练过程
    #定义变量分别表示 训练轮数 每轮的(平均)损失值 训练总损失值 训练的样本数
    epochs,loss_list,total_loss,total_sample=100,[],0.0,0
    #开始训练 按轮训练
    for epoch in range(epochs):
        #每轮是分批次训练的 所以从加载器中 获取 批次数据
        for train_x,train_y in dataloader:
            #模型的预测
            y_pred=model(train_x)
            #计算每批损失值
            loss=critertion(y_pred,train_y.reshape(-1,1))#将train_y转成 n行1列
            #计算总损失 和样本批次
            total_loss+=loss.item()
            total_sample+=1
            #梯度清零+反向传播+梯度更新
            optumizer.zero_grad()   #梯度清零
            loss.sum().backward()   #反向传播 计算梯度
            optumizer.step()        #梯度更新
        #把本轮的平均损失添加到列表中
        loss_list.append(total_loss/total_sample)
        print(f"轮数：{epoch+1},平均损失值：{total_loss/total_sample}")
    #打印最终训练结果
    print(f"{epochs}轮的平均损失分别为{total_loss/total_sample}")
    print(f"模型参数，权重：{model.weight.item()},偏置：{model.bias.item()}")

    #绘制损失曲线
    plt.plot(range(epochs),loss_list)
    plt.title("损失值曲线变化图")
    plt.grid(True)
    plt.show()
    #绘制真实值和样本值之间的关系
    #绘制样本点分布情况
    plt.scatter(x,y)#画样本点的位置
    y_pred=torch.tensor(data=[v*model.weight+model.bias for v in x])
    #计算真实值
    y_true=torch.tensor(data=[v*coef+14 for v in x])
    #绘制真实值和预测值的折线图
    plt.plot(x,y_pred,color="red",label="预测值")
    plt.plot(x,y_true,color="darkblue",label="真实值")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # 创建数据集
    x,y,coef=create_dataset()
    # print(x, y, coef)
    train(x,y,coef)
