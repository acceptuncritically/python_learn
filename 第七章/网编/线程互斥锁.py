"""
多线程共享全局变量，出现问题：累加次数不够
产生原因：线程1还没有来得及执行完一个完整的动作前，被线程2抢走了资源
解决方案：互斥锁
        保证同一时刻只能有一个线程去操作全局变量
        互斥锁的创建：mutex=threading.Lock()
        上锁：mutex.acquire()
        释放锁：mutex.release()
        一直等待 因互相等待对方持有的资源而永久阻塞 要在合适地方释放锁
"""
import threading
global_num = 0
#创建锁对象
mutex = threading.Lock()
def write_data():
    mutex.acquire()
    #全局变量在循环外进行定义
    global global_num
    for i in range(1000000):
        global_num += 1
    print(global_num)
    mutex.release()
    #由于两个线程都有可能第一次抢到资源，为了防止双方抢资源，两边都要上锁
def write2():
    mutex.acquire()
    global global_num
    for i in range(1000000):
        global_num += 1
    print(global_num)
    mutex.release()
if __name__ == '__main__':
    thread1 = threading.Thread(target=write_data)
    thread2 = threading.Thread(target=write2)
    thread1.start()
    thread2.start()