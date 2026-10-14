import socket
# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定IP地址和端口号
server_socket.bind(('127.0.0.1', 8080))
#设置最大监听数
server_socket.listen(5)

#等待客户端申请连接
accept_socket,client_info= server_socket.accept()
#读取客户端上传的数据
with open('../my_data/my.png', 'wb') as f:
    print("正在监听")
    while True:
        # 接受客户端消息并打印
        data=accept_socket.recv(1024)
        if len(data)==0:
            break
        f.write(data)

# 释放资源
accept_socket.close()