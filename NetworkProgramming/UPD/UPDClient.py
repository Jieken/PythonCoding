#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM
serverName = "localhost"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
print("客户端端开始运行…………")
while True:
    message = input("请输入要发送的文字：")
    while message == "":
        message = input("请重新输入：")
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    if message == "bye":
        print("客户端退出…………")
        break
    modifyMessage, serverInfo = clientSocket.recvfrom(2048)
    print("客户端" + str(serverInfo[0]) + ":" + str(serverInfo[1]) + "发过来的信息为：" +
          modifyMessage.decode())

clientSocket.close()
