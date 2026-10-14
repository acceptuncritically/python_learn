# def rectangle(l,m):
#     """
#         计算长方形的面积
#     :param l: 长度
#     :param m: 宽度
#     :return: 面积
#     """
#     return round(l*m,1)
# l=float(input(""))
# m=float(input(""))
# c=rectangle(l,m)
# print(c)
# def circle(r):
#     """
#
#     :param r:
#     :return:
#     """
#     return round(3.14*r*r,1),round(3.14*r*2,1)
# r=float(input(""))
# area,len=circle(r)
# print(area)
# print(len)

#lambda 参数1, 参数2... : 表达式
#用来快速写函数   匿名函数
# 请在 ___ 划线处，替换成你的代码 below

# 创建lambda函数，计算两个数字的平方根之和
compute = lambda x,y:x**0.5+y**0.5

# 输入两个整数
n1 = int(input())
n2 = int(input())

# 调用函数并打印结果
print(compute(n1,n2))

# def reg(name,age,gender,city):
#     print(f"注册成功 名字：{name},年龄：{age},性别：{gender},城市：{city}")
#     return{"name": name,"age":age,"gender":gender,"city":city}
# #关键字参数   global 相当于c中的const
# s=reg("张三",18,gender="男",city="上海")
# print(s)

# 请在 ___ 划线处，替换成你的代码

# 创建函数
def print_numbers(arg1,arg2):
    print(arg1)
    print(arg2)

# 输入两个整数
n1 = int(input())
n2 = int(input())

# 调用函数
print_numbers(arg2 = n2, arg1 = n1)

#默认参数
# 默认参数必须放在没有默认值的参数列表的垢面，一个函数在定义时是可以设置个多个默认参数的
#函数调用时，如果为默认参数传递了值，则会修改默认参数值，否则直接使用默认值

# def reg(name,age,gender,city="北京"):

#不定长参数：再调用函数参数时参数个数不确定
def calc(*args,**kwargs):
    """

    :param args:不定长位置参数 需要计算的数据
    :param kwargs: 不定长关键字参数 调整结果的表现形式
            round:保留地小数位数
            print：是否打印输出
    :return: 最小值 最大值 平均值
    """
    # 位置参数时  *args 会被封装到元组中
    #关键字传递的不定长：被封装成字典类型
    min_calc=min(args)
    max_calc=max(args)
    avg=sum(args)/len(args)
    if kwargs.get("round") is not None:
        avg=round(avg,kwargs.get("round"))
    if kwargs.get("print"):
        print(min_calc,max_calc,avg)

    return min_calc,max_calc,avg  #封装到元组中
print(calc(1,2,5))

#普通参数 数字 布尔 字符串，列表 元组， 集合 字典 //函数//
# 可以进行函数的嵌套