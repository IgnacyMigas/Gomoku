#!/usr/bin/pyhon2.7.9

import socket


class MyServer:
    def __init__(self, address, port, data_size):
        self.data_size=data_size
        self._createTcpSocket()
        self._binSocketToPort(address, port)
        self.connection = None

    def getConnection(self):
        self.sock.listen(1)
        self.connection, client_address = self.sock.accept()

    def getMsg(self):
        while True:
            data = self.connection.recv(self.data_size)
            if data:
                return data

    def _createTcpSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _binSocketToPort(self, address, port):
        server_address = (address, port)
        print ('bind to %s port %s' % server_address)
        self.sock.bind(server_address)

if __name__ == "__main__":
    host = 'localhost'
    port = 50001
    data_size = 1024
    server = MyServer(host, port, data_size)