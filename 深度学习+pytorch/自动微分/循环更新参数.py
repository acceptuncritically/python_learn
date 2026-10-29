"""
演示自动微分模块 循环计算梯度 更新参数
"""
import torch

w=torch.tensor(10,requires_grad=True,dtype=torch.float)

loss=w**2+20

print(f"开始权重初始值：{w},(0.01*w.grad):无，loss:{loss}")
for i in range(1,101):
    loss=w**2+20
    #梯度清零w.grad_zero()  默认梯度会增加
    if w.grad is not None:
        w.grad.zero_()
    #反向传播
    loss.sum().backward()
    #梯度更新
    # print(f"梯度值为：{w.grad}")
    w.data=w.data-0.01*w.grad

    #打印本次梯度更新后的权重参数结果   加不加item()都可以
    print(f"第{i}次，权重初始值：{w},(0.01*w.grad):{(0.01*w.grad).item():.4f} loss:{loss:.4f}")
print(f"最终结果权重：{w},梯度{w.grad},loss:{loss:.4f}")