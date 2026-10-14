def log_fun1():
    print("-"*30)
def log_fun2():
    print("#"*30)
def log_fun3():
    print("+"*30)
if __name__ == '__main__':
    #当在当前文件执行时，会输出main
    #在别的文件调用时__name__则会输出为文件名
    # 所以用这来检查，调试
    log_fun1()