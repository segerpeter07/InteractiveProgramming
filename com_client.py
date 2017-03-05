#!/usr/bin python3
""" TCP Client """

import socket
import select
import sys


class client(object):
    def __init__(self, HOST='10.7.8.33', PORT=1337):
        self.HOST = HOST
        self.PORT = PORT

        self.MASTER_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.MASTER_SOCK.settimeout(200)

        self.SOCKET_LIST = [sys.stdin, self.MASTER_SOCK]
        # Get the list sockets which are readable
        self.READ_SOCKETS, WRITE_SOCKETS, ERROR_SOCKETS = select.select(self.SOCKET_LIST, [], [])

        try:
            self.MASTER_SOCK.connect((self.HOST, self.PORT))
        except Exception as msg:
            print(type(msg).__name__)
            print("Unable to connect")
            sys.exit()

    def send_message(self, message):
        print(message)
        self.MASTER_SOCK.sendall(message.encode())

    def check_messages(self):
        for sock in self.READ_SOCKETS:  # incoming message from remote server
            if sock == self.MASTER_SOCK:
                data = sock.recv(4096)
                if not data:
                    print('\nDisconnected from chat server')
                    sys.exit()
                else:  # print data
                    # print()  # erase last line
                    # print(data.decode(), end="")
                    return data.decode()

    def messages(self, msg):
        for sock in self.READ_SOCKETS:  # incoming message from remote server
            if sock == self.MASTER_SOCK:
                data = sock.recv(4096)
                if not data:
                    print('\nDisconnected from chat server')
                    sys.exit()
                else:  # print data
                    print(data.decode(), end="")
            else:  # user entered a message
                self.MASTER_SOCK.sendall(msg)
