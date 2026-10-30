a="""
在构建网络后 网络中的参数是需要初始化的，主要的初始化参数有权重和偏置 偏置一般初始化为0
作用：防止梯度消失或操作 初始权重值过大或过小会导致梯度在反向传播中指数级增大或缩小
    提高收敛速度  合理的初始化使得网络的激活值分布适中 有助于梯度高效更新
    保持对称性破除
方法：
    均分分布初始化(nn.init.uniform_()会改变原数据)： 权重参数初始化从区间均匀取值，默认区间为(0,1)其中神经元的输出数量
    正态分布初始化(nn.init.normal_()会改变原数据)：随机初始化从均值为0，标准差是1的高斯分布中取样，使用一些很小的值对参数w进行初始化

        优点：能有效打破对称性
        缺点：随机选择范围不当导致梯度问题
        使用场景：浅层网络或低复杂度模型，隐藏层1-3层 总层数不超过5层
    全0初始化(nn.init.zeros_())：将神经网络所有参数初始化为0
    全1初始化(ones_())：将神经网络所有参数初始化为1
    固定值初始化(constant_())：将神经网络中的所有权重参数初始化为某个固定值
高级初始化方法：
    kaiming初始化也叫HE初始化：
        正态分布的he初始化nn.init.kaiming_normal_() 从[0,std]中抽取样本的，std=sqrt(2/fan_in)
        均匀分布的he初始化nn.init.kaiming_uniform_() [-limit,limit]中的均匀分布中抽取样本 limit是sqrt(6/fan_in))
    xavier初始化，也叫做Glorot初始化 
        正态分布的xavier初始化nn.init.xavier_normal_() 从[0,std]中抽取样本，std=sqrt(2/fan_in+fan_out)
        均匀分布的xavier初始化nn.init.xavier_uniform_() [-limit,limit]中的均匀分布中抽取样本 limit是sqrt(6/fan_in+fan_out))
    fan_in是输入层神经元的个数 fan_out是输出层神经元个数
"""
