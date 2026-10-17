# 线程的使用步骤
# 1导包
# 2创建线程对象
# 3启动线程
# 进程是CPU分配资源的基本单位，线程是CPU调度资源的基本单位
# 每个进程至少有一个线程，线程是依附于进程的，
#线程间数据相互隔离，每一个进程的线程间数据可以共享
"""
不带参数的线程
"""
import threading
import time
def coding():
    for i in range(10):
        time.sleep(0.1)
        print(f"正在敲第{i}行代码")
def music():
    for i in range(10):
        time.sleep(0.1)
        print(f"正在听第{i}行音乐")
if __name__ == "__main__":
    # 创建两个线程对象，分别关联两个线程
    # 在start没有开始时 并不会和main函数抢资源
    for i in range(10):
        print("main")
    threading.Thread(target=coding).start()
    threading.Thread(target=music).start()

    # t1=threading.Thread(target=coding)
    # t2=threading.Thread(target=music)
    # t1.start()
    # t2.start()