#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM
serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("localhost", serverPort))
print("服务端开始运行…………")
while True:
    message, clientInfo = serverSocket.recvfrom(2048)
    print("客户端" + str(clientInfo[0]) + ":" + str(clientInfo[1]) + "发过来信息：" +
          message.decode())
    if message.decode() == "bye":
        print("服务端退出…………")
        break
    modifyMessage = message.decode().upper()
    serverSocket.sendto(modifyMessage.encode(), clientInfo)

serverSocket.close()
