from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
import struct
import time

serverName = "localhost"
serverPort = 12000
ClientSocket = socket(AF_INET, SOCK_STREAM)
ClientSocket.connect((serverName, serverPort))

start = time.time()
length = 104857600
num = 10
SessionMessage = struct.pack("ii", *[num, length])


totallength = length + struct.calcsize("i")
data = ""
for i in range(length):
    strdit = "0123456789ABCDEF"
    data += strdit[i % 16]
formatstr = "i" + str(length) + "s"
PayloadMessage = struct.pack(
    formatstr, *[length, data.encode(encoding='utf-8')])
start = time.time()
ClientSocket.sendall(SessionMessage)
total_mb = 1.0 * length * num / 1024 / 1024
print("%.3f MB Start Send To Server\n" % (total_mb))
for i in range(num):
    print("准备发送%d字节数据" % (PayloadMessage.__len__()))
    ClientSocket.sendall(PayloadMessage)
    ack = ClientSocket.recv(struct.calcsize("i"))
    ack = struct.unpack("i", ack)[0]
    if ack != length:
        print("收到的ACK字节数不是%d" % (length))
        break
end = time.time()

elapsed = end - start
print("%.3f seconds\n%.3f MB/s\n" % (elapsed, total_mb / elapsed))
