# # 有参无返回
# def fun_outter(fn_name):
#     def fun_inner(x,y):
#         print("正在计算中")
#         fn_name(x,y)
#     return fun_inner
# @fun_outter
# def add(num1,num2):
#     print(f"{num1 + num2}")
# add(10,20)
# #无参有返回
# def fun_outter(fn_name):
#     def fun_inner():
#         print("正在计算中")
#         return fn_name()
#     return fun_inner
# @fun_outter
# def add():
#     a=10
#     b=20
#     return a+b
# sum=add()
# print(sum)
#有参有返回值
def fun_outter(fn_name):
    def fun_inner(x,y):
        print("正在计算中")
        return fn_name(x,y)
    return fun_inner
@fun_outter
def add(num1,num2):
    return num1 + num2
sum=add(10,20)
print(sum)