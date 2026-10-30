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
        n_features=3,  #一个特征点
        noise=10,       #噪声越大 样本点越散
        coef=True,      #是否返回系数 默认为False 返回值为None  coef 是真实权重
        bias=14,        #偏置
        random_state=3    #随机种子 随机种子相同 输出数据相同
    )
    #y = coef * x + 14 + 噪声
    #此时为ndarray
    # print(type(x))
    #将numpy数据封装为tensor对象 下面的训练需要转换为张量
    x=torch.tensor(x,dtype=torch.float)
    y=torch.tensor(y,dtype=torch.float)
    print(x,y)
    # 返回参数
    return x,y,coef
def train(x,y,coef):
    dataset=TensorDataset(x,y)
        #参1 数据集对象 参2 批次大小 参3 是否打乱数据 (训练集打乱 测试集不打乱)
    dataloader=DataLoader(dataset,batch_size=10,shuffle=True)
    #创建出事的线性回归模型
        #参1 表示输入的维度 参2 表示输出的维度  内部包含w b
        # 用模型来计算 y_pred = w * x + b
    model=nn.Linear(3,1)
    #创建损失函数对象
    critertion=nn.MSELoss()
    #创建优化器对象
        #告诉模型你要修改的对象 和学习率
        #参1 表示模型参数 参2 表示学习率
    optumizer=optim.SGD(model.parameters(),lr=0.01)
    #具体的训练过程
        #定义变量分别表示 训练轮数 每轮的(平均)损失值 训练总损失值 训练的样本数
    epochs,loss_list=100,[]
    #开始训练 按轮训练
    for epoch in range(epochs):
        total_loss, total_sample=0.0,0
        #每轮是分批次训练的 所以从加载器中 获取 批次数据
        #将原本的x，y换了个名 为train_x,train_y
        for train_x,train_y in dataloader:
            #模型的预测 用先前定义的nn.Linear对象 内部会自动执行前向传播
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
    y_pred = model(x).detach().squeeze()

    y_true=y

    plt.scatter(y_true.numpy(), y_pred.numpy(), alpha=0.6, color='dodgerblue', label="样本预测点")

    min_val = min(y_true.min().item(), y_pred.min().item())
    max_val = max(y_true.max().item(), y_pred.max().item())
    plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label="完美预测线 (y=x)")

    plt.title("多特征线性回归：真实值 vs 预测值")
    plt.xlabel("真实值 (True)")
    plt.ylabel("预测值 (Pred)")
    plt.legend()
    plt.grid(True)
    plt.show()
def test():
    # 模拟你的数据：2个样本，3个特征
    x = torch.tensor([[1.0, 2.0, 3.0],
                      [4.0, 5.0, 6.0]])  # 形状: [2, 3]

    # 模型：输入3，输出1
    model = nn.Linear(3, 1)

    print("--- 参数形状 ---")
    print("Weight形状:", model.weight.shape)  # [1, 3]
    print("Bias形状:", model.bias.shape)  # [1]

    print("\n--- 内部权重具体值 ---")
    print("Weight:", model.weight.data)
    print("Bias:", model.bias.data)

    print("\n--- 自己手动算一遍 ---")
    # 1. 矩阵乘法 (weight需要转置)
    # [2, 3] @ [3, 1] = [2, 1]
    manual_pred = torch.matmul(x, model.weight.T)
    print("乘法后结果 (还没加bias):\n", manual_pred)

    # 2. 加上偏置
    manual_pred = manual_pred + model.bias
    print("加上bias后结果:\n", manual_pred)

    print("\n--- 直接用 model 跑 ---")
    model_pred = model(x)
    print("模型预测结果:\n", model_pred)


if __name__ == '__main__':

    # 创建数据集
    # x,y,coef=create_dataset()
    # train(x,y,coef)
    test()
