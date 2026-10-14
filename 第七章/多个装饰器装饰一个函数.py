def check_login(fn_name):
    def fun_inner():
        print("登陆成功")
        fn_name()
    return fun_inner
def check_code(fn_name):
    def fun_inner():
        print("验证码登陆成功")
        fn_name()
    return fun_inner
#如果是语法糖的形式装饰 就直接按照输出顺序 填写
#如果是传统方式 就按照出栈理解 先进后输出
@check_login
@check_code
def comment():
    print("发表评论")
comment()