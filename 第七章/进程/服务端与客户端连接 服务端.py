"""
    1.导包 通过socket方法创建socket对象
    2.通过connect方法绑定IP地址和端口号
    3.设置最大监听数
    4.等待客户端发送信息
    5.send(b"")将信息转换为二进制
    6.socket对象设置recv接收字节数 decode编码为
    7.释放资源

"""
import socket
# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定IP地址和端口号
server_socket.bind(('192.0.0.0', 8080))
#设置最大监听数
server_socket.listen(5)
#等待客户端申请连接
accept_socket,client_info= server_socket.accept()
#给客户端发消息
accept_socket.send(b"hello")
# 接受客户端消息并打印
data=accept_socket.recv(1024).decode("utf-8")
print(f"{client_info}发送的信息{data}")
# 释放资源
accept_socket.close()