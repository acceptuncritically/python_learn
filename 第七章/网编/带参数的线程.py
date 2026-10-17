"""
这些任务要不要共享内存里的数据？ 要 → 倾向线程；不要 → 倾向进程。
一个任务挂了，能不能接受拖垮其他任务？ 不能接受 → 进程；能接受 → 线程。
进程做隔离边界，进程内用线程共享
"""
import threading
import time
def coding(name,num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f"{name}正在敲第{i}行代码")
def music(name,num):
    for i in range(1,num+1):
        time.sleep(0.1)
        print(f"{name}正在听第{i}行音乐")
if __name__ == "__main__":
    # 创建两个线程对象，分别关联两个线程
    # 在start没有开始时 并不会和main函数抢资源
    for i in range(10):
        print("main")
    threading.Thread(target=coding,args=["桑多涅",100]).start()
    threading.Thread(target=music,kwargs={"num":10,"name":"哥伦比亚"}).start()