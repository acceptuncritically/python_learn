# 用于内部函数访问与修改外部函数参数的值
def fun_outer():
    a=100
    def fun_inner():
        nonlocal a
        a=a+1
        print(a)
    return fun_inner
fun_outer()()
#表示第一次调用外部函数 得到了内部函数 再次调用