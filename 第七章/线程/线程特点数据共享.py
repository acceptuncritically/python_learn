import threading
import time

my_list=[]
def write_data():
    for i in range(10):
        my_list.append(i)
        print(f"写入数据{i}")
    print(my_list)
def read_data():
    #加入休眠保证读一定在写入之后
    time.sleep(1)
    print(my_list)
if __name__ == '__main__':
    thread1 = threading.Thread(target=write_data)
    thread2 = threading.Thread(target=read_data)
    thread2.start()
    thread1.start()