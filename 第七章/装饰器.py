"""
装饰器解释:
    概述:
        在遵循闭包的前提下，给原有函数增加额外功能，且不改变原有函数的代码和调用方式，这种写法就称之为装饰器.
    格式:
        def 外部函数名(形参列表):  # 外部函数的形参通常是：被装饰的函数对象
            def 内部函数名(形参列表):
                # 额外功能 (前)
                被装饰的函数对象(形参)
                # 额外功能 (后)

            return 内部函数名
        语法糖写法
        @外部函数名
        def 被装饰的函数名(形参列表):
            pass
    前提条件:
        1. 有嵌套.          外部函数嵌套内部函数
        2. 有引用.          内部函数使用外部函数的变量(包括外部函数的参数)
        3. 有返回.          外部函数中，返回 内部函数(对象)
        4. 有额外功能.      给需要装饰的原有函数增加额外功能
传统写法
被装饰的函数名 = 外部函数名(被装饰的函数名).
被装饰的函数名()
"""
#传统写法
# def check_login(fn_name):
#     def fun_inner():
#         print("登陆中...")
#         print("登陆成功...")
#         fn_name()
#     return fun_inner
# def comment():
#     print("发表评论")
# Comment=check_login(comment)
# Comment()
#语法糖写法
def check_login(fn_name):
    def fun_inner():
        print("登陆中...")
        print("登陆成功...")
        fn_name()
    return fun_inner
@check_login
def comment():
    print("发表评论")

def Comment():
    print("发表评论")
Comment()
