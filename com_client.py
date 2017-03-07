"""
    Client Object for Super Tic Tac tic_tac_toe
    @Author Alex Chapman
    3/6/17
"""
import socket
import select
import sys


class client(object):
    """
        Client class encapsulating TCP client-side code

        Attributes:
            HOST            - IP address of server
            PORT            - Port number of hosted server
            MASTER_SOCK     - Master connection to server
            READ_SOCKETS    - list of sockets to read messages from
    """
    def __init__(self, HOST='10.7.64.108', PORT=1337):
        """Returns Client Object"""
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
        """Sends message to the server"""
        if message is not 'hb':
            print(message)
        self.MASTER_SOCK.sendall(message.encode())

    def check_messages(self):
        """Checks read sockets for any messages and returns them"""
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
        """ Idea for lightweighting implementation. Unimplemented."""
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
