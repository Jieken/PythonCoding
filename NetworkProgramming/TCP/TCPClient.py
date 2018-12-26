#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM

serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
print("客户端已连接…………")
while True:
    message = input("请输入需要发送的文字：")
    while message == "":
        message = input("请重新输入：")
    clientSocket.send(message.encode())
    if message == "bye":
        print("客户端退出……")
        break
    modifyMessage = clientSocket.recv(2048)
    print("收到来自服务端" + serverName + ":" + str(serverPort) + "的数据：" +
          modifyMessage.decode())

clientSocket.close()
