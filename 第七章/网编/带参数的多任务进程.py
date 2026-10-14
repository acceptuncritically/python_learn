# 进程传参有两种方式
# 方式一 args传位置参数
# 方式二 kwargs传关键字参数

# 导包
import multiprocessing
import time
# 需求：小明一边写代码 一边听音乐
def code(name,count):
    for i in range(1,count+1):
        time.sleep(0.1)
        print(f"{name},正在写第{count}行代码")
def music(name,count):
    for i in range(1,count+1):
        time.sleep(0.1)
        print(f"{name},正在唱第{i}首歌")
if __name__ == '__main__':
    p1=multiprocessing.Process(target=code,args=("lu",10))
    p2=multiprocessing.Process(target=music,kwargs={'name':"li",'count':10})
    p1.start()
    p2.start()
