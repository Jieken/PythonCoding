from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
import struct
import time
serverName = "localhost"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(2)
clientSocket, clientInfo = serverSocket.accept()
sessionMessage = clientSocket.recv(struct.calcsize("ii"))
start = time.time()
num, length = struct.unpack("ii", sessionMessage)
total_mb = 1.0 * length * num / 1024 / 1024
print("receive buffer length = %d\n receive number of buffers = %d\n" %
      (length, num))
print("准备接受%.3f MB 的数据" % (total_mb))
formatstr = "i" + str(length) + "s"
for i in range(num):
    PayloadMessageLengthStr = clientSocket.recv(struct.calcsize(formatstr))
    PayloadMessageLengt, PayloadMessageStr = struct.unpack(formatstr, PayloadMessageLengthStr)
    if(PayloadMessageLengt != length):
        print("收到的数据包大小不是指定的%d大小" % (length))
        break
    clientSocket.send(struct.pack("i", PayloadMessageLengt))
end = time.time()

elapsed = end - start
print("%.3f seconds\n%.3f MB/s\n" % (elapsed, total_mb / elapsed))
