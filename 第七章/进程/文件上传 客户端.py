import socket
# 创建socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定IP地址和端口号
client_socket.connect(('127.0.0.1', 8080))
with open(r"C:\Users\fan\Desktop\屏幕截图 2026-09-01 183808.png",'rb')as f:
    while True:
        #具体的读取操作
        data=f.read(1024)
        # 把读取到的数据写给服务端
        client_socket.send(data)
        #如果读取到的数据为空说明读取完毕
        if not data:
            break
# 释放资源
client_socket.close()