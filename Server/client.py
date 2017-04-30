#!/usr/bin/pyhon2.7.9

import socket
import sys


class MyClient:
    def __init__(self, address, port, data_size):
        self.data_size=data_size
        self._createTcpSocket()
        self._connectToServer(address, port)

    def sendMsg(self, msg):
        self.sock.send(msg)
        response = self.sock.recv(self.data_size)
        return response
#        print ('recive %s' % response)

    def _createTcpSocket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _connectToServer(self, address, port):
        server_address = (address, port)
        print ('connecting to %s port %s' % server_address)
        self.sock.connect(server_address)

if __name__ == "__main__":
    host = 'localhost'
    port = 50001
    data_size = 1024
    client = MyClient(host, port, data_size)
    client.sendMsg("Hello")
    client.sendMsg("echooooo")
    client.sendMsg("END")