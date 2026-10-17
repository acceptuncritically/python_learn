# 进程编号的作用
# 进程编号唯一标识一个进程， 方便管理进程。
#  在一个操作系统中，一个进程拥有的进程号是唯一的，进程号可以反复使用。
# 获取进程编号的目的是验证主进程和子进程的关系， 可以得知子进程是由那个主进程创建出来的
"""
案例：演示获取进程的编号.
进程的编号解释：
    概述：
        在设备中，每个程序(进程)都有自己的唯一进程id，当程序释放的时候，该进程id也会释放. 即：进程id是可以重复使用的.
    目的：
        1. 查看子进程和父进程的关系，方便 管理.
        2. 例如：杀死指定进程，创建子进程...
    格式：
        查看当前进程的pid：
            os模块(operating，系统模块) 的 getpid()            get Process id
            multiprocessing#current_process()的pid属性

        查看当前进程的ppid：          parent process id(父进程id)
            os#getppid()
细节：
    main中创建的进程， 如果没有特殊指定，它的父进程都是main进程，
    而main进程的父进程是pycharm
"""
import os
# 导包
import multiprocessing
import time
# 需求：小明一边写代码 一边听音乐
def code(name,count):
    for i in range(1,count+1):
        time.sleep(0.1)
        print(f"{name},正在写第{count}行代码")
    print(f"{os.getpid()},{multiprocessing.current_process().pid},父进程{os.getppid()}")
def music(name,count):
    for i in range(1,count+1):
        time.sleep(0.1)
        print(f"{name},正在唱第{i}首歌")
    print(f"{os.getpid()},{multiprocessing.current_process().pid},父进程{os.getppid()}")
if __name__ == '__main__':
    p1=multiprocessing.Process(target=code,args=("lu",10))
    p2=multiprocessing.Process(target=music,kwargs={'name':"li",'count':10})
    p1.start()
    p2.start()