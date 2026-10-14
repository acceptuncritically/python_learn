# 只有将__init__加入到目录中才能作为一个包，来操作
# __all__  指定from...import * 指的是什么功能
# 要提前在此文件中指定__all__ 指向什么，在from... import * 中才能运行
# *即指代所有的模块即所指定的all中
__all__=["my_ven","my_fun"]