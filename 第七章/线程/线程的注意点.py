"""
线程之间是无序的，具有随机性
    CPU调用哪个线程哪个线程就运行
默认主线程会等待所有的子线程执行结束后再结束
    可以设置守护主线程 提前结束
同一个进程的线程之间共享数据
多线程操作共享数据，可能会出现安全问题，可以用互斥锁解决

CPU调度资源的策略
    1均分时间片
    2抢占式调度(大多数)
"""
import threading
import time
def info():
    for i in range(10):
        time.sleep(0.1)
        print("g..")
if __name__ == '__main__':
    #创建十个线程，观察其运行效果
    # 守护线程 daemon 属性 主进程结束后就直接停止
    t=threading.Thread(target=info,daemon=True)
    t.start()
    time.sleep(0.5)
    print("主线程结束了")