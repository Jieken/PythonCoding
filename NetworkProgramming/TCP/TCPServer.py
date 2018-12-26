#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
import threading


class ClientHandl(threading.Thread):
    def __init__(self, clientSocket, clientInfo):
        super(ClientHandl, self).__init__()  # 调用父类的构造函数
        self.clientSocket = clientSocket
        self.clientInfo = clientInfo

    def run(self):
        print("客户端" + str(self.clientInfo[0]) + ":" + str(self.clientInfo[1]) +
              "已连接")
        while True:
            message = self.clientSocket.recv(2048)
            print("收到来自客户端" + str(self.clientInfo[0]) + ":" +
                  str(self.clientInfo[1]) + "的消息：" + message.decode())
            if message.decode() == "bye":
                print("客户端" + str(self.clientInfo[0]) + ":" +
                      str(self.clientInfo[1]) + "已退出")
                break
            modifyMessage = message.decode().upper()
            self.clientSocket.send(modifyMessage.encode())
        self.clientSocket.close()


serverName = "localhost"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((serverName, serverPort))
serverSocket.listen(2)
print("服务端端开始监听…………")
while True:
    clientSocket, clientInfo = serverSocket.accept()
    clientHandler = ClientHandl(clientSocket, clientInfo)
    clientHandler.start()
