# 装饰器的参数有且只能有一个 且装饰的函数的格式要保持一致
# 用带有参数的装饰器嵌套在装饰器外面
def fn_outer(flag):
    def my_decorator(fu_name):
        def fn_inner(*args,**kwargs):
            if flag=="+":
                print("正在进行加法运算")
            elif flag=="-":
                print("正在进行减法运算")
            return fu_name(*args,**kwargs)
        return fn_inner
    return my_decorator
@fn_outer("+")
def add(num1,num2):
    return num1+num2
@fn_outer("-")
def sub(num1,num2):
    return num1-num2
print(add(10,20))

#
# # 1. 定义装饰器
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         # 根据传入的函数名，执行不同的额外功能
#         if func.__name__ == "add":
#             print("【系统提示】准备执行加法运算...")
#         elif func.__name__ == "sub":
#             print("【系统提示】准备执行减法运算...")
#         else:
#             print("【系统提示】准备执行未知运算...")
#         # 执行原函数
#         result = func(*args, **kwargs)
#         print(f"【执行结果】{func.__name__} 的计算结果是: {result}")
#         return result
#     return wrapper
# # 2. 使用装饰器装饰多个函数
# @my_decorator
# def add(a, b):
#     return a + b
# @my_decorator
# def sub(a, b):
#     return a - b
# # 3. 调用
# add(5, 3)
# print("-" * 20)
# sub(5, 3)