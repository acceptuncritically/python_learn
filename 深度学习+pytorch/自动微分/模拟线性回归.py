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
    # 返回参数
    return x,y,coef
if __name__ == '__main__':
    # 创建数据集
    x,y,coef=create_dataset()
    print(x, y, coef)
