import socket
# 创建socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定IP地址和端口号
client_socket.connect(('192.0.0.0', 8080))
data=client_socket.recv(1024).decode("utf-8")
print(f"{data}")
#给客户端发消息
client_socket.send(b"well")
# 接受客户端消息并打印
# 释放资源
client_socket.close()