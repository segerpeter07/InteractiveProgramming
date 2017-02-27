# Save as server.py
# Message Receiver
import os
from socket import *
host = ""
port_recieving = 13051
port_sending = 13050
addr = (host, port_recieving)
addr2 = (host, port_sending)
buf = 1024
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    mode = input('Select mode (1 = recieving, 0 = sending): ')
    if mode == '1':
        print("Waiting to receive messages...")
        UDPSock.bind(addr)
        (data, addr) = UDPSock.recvfrom(buf)
        print("Received message: " + str(data))

        if data == "exit":
            break
    elif mode == '0':
        UDPSock.bind(addr2)
        data2 = input("Enter message to send or type 'exit': ")
        (data2, addr2) = UDPSock.sendto(data2.encode('utf-8'), addr2)

        if data == "exit":
            break
UDPSock.close()
os._exit(0)
