import socket


# 客户端
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接目标IP和端口,connect takes a tuple as args
s.connect(('127.0.0.1',4013))
#接收消息
print('--->>'+s.recv(1024).decode('utf-8'))
#发送消息
s.send(b'Hello, I am a client.')
s.send(b'exit')
s.close()