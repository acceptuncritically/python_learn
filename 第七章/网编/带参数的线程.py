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