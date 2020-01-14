#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        uiRun.py
#
# Purpose:     This module is used to provide a TCP client and TCP server program.
#
# Author:      Yuancheng Liu
#
# Created:     2019/01/13
# Copyright:   
# License:     
#-----------------------------------------------------------------------------

import time
import socket
import threading

SererIP = ('127.0.0.1', 502)
BUFFER_SZ = 4096

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class tcpClient(object):
    """ 
    """
    def __init__(self, ipAddr):
        # create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ipAddr = ipAddr
        self.connected = False  # connection flag.
        # connect the client
        self.connect()

#-----------------------------------------------------------------------------
    def connect(self, ipAddr=None):
        """ Connect/Reconnect to the server.
        """
        if self.connected: self.client.close() # disonncected the existed connection.
        if not ipAddr is None:
            self.ipAddr = ipAddr
        try:
            self.client.connect(self.ipAddr)
            self.connected = True
        except: 
            print("Connect to %s failed" %str(self.ipAddr))
            self.connected = False
        return self.connected

#-----------------------------------------------------------------------------
    def sendMsg(self, msg=None, resp=False):
        """ convert the msg to bytes and send to the server.
        """
        if self.connected:
            if not isinstance(msg, bytes):
                msg = str(msg).encode('utf-8')
            self.client.send(msg)
            response = self.client.recv(BUFFER_SZ) if resp else True
            return response
        return False

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

class tcpServer(object):
    """ 
    """
    def __init__(self, parent, port, connctNum=1):
        self.bindAddr = ('0.0.0.0', port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.bindAddr)
        self.server.listen(connctNum)
        self.terminate = False

#-----------------------------------------------------------------------------
    def serverStart(self, handler=None):
        """ start the server to handle the incomming message
        """
        while not self.terminate:
            client_socket, address = self.server.accept()
            print("Accepted connection from %s" %str(address))
            while not self.terminate:
                request = client_socket.recv(BUFFER_SZ)
                msg = handler(request) if not handler is None else request
                if not msg is None:
                    if not isinstance(msg, bytes):
                        msg = str(msg).encode('utf-8')
                    client_socket.send(msg)
                     
#-----------------------------------------------------------------------------
    def serverStop(self):
        self.terminate = True


def testCase():
    print("Start TCP server-client communication test.")
    pCount, tPass = 0, True # test fail count.

    








#-----------------------------------------------------------------------------
if __name__ == '__main__':
    testCase()







        
