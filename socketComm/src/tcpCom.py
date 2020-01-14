#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        uiRun.py
#
# Purpose:     This module will provide a TCP client + server API and a multi-thread
#              test case which may be used for other project.
#
# Author:      Yuancheng Liu
#
# Created:     2019/01/13
# Copyright:   
# License:     
#-----------------------------------------------------------------------------

import time
import socket
import threading    # create multi-thread test case.

BUFFER_SZ = 4096    # TCP buffer size.

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class tcpClient(object):
    """ TCP client module."""
    def __init__(self, ipAddr):
        """ Create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
            init example: client = tcpClient(('127.0.0.1', 502))
        """
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ipAddr = ipAddr
        self.connected = False  # connection flag.
        # connect the client
        self.connect()

#--tcpClient-------------------------------------------------------------------
    def connect(self, ipAddr=None):
        """ Connect/Reconnect to the server. return connected state."""
        if self.connected:
            self.client.close() # disonncected the existed connection.
            self.client = None  # re-init the socket for the new connection.
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not ipAddr is None: self.ipAddr = ipAddr
        try:
            self.client.connect(self.ipAddr)
            self.connected = True
        except:
            print("Connect to server %s failed" % str(self.ipAddr))
            self.connected = False
        return self.connected

#--tcpClient-------------------------------------------------------------------
    def sendMsg(self, msg=None, resp=False):
        """ Convert the msg to bytes and send to the server. resp: server response
            flag, will wait server's response if set to true.
        """
        if self.connected:
            if not isinstance(msg, bytes): msg = str(msg).encode('utf-8')
            self.client.send(msg)
            response = self.client.recv(BUFFER_SZ) if resp else True
            return response
        return False

#--tcpClient-------------------------------------------------------------------
    def disconnect(self):
        """ Send a empty message and close the socket.
        """
        self.sendMsg(msg='')
        self.client.close()

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class tcpServer(object):
    """ TCP client module."""
    def __init__(self, parent, port, connctNum=1):
        """ Create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
            init example: server = tcpServer(None, 5005, connctNum=1)
        """
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', port))
        self.server.listen(connctNum)
        self.terminate = False  # Server terminate flag.

#--tcpClient-------------------------------------------------------------------
    def serverStart(self, handler=None):
        """ Start the server to handle the incomming message."""
        while not self.terminate:
            client_socket, address = self.server.accept()
            print("Accepted connection from %s" % str(address))
            while not self.terminate:
                request = client_socket.recv(BUFFER_SZ)
                msg = handler(request) if not handler is None else request
                if not msg is None: # don't response client if the handler feed back is None
                    if not isinstance(msg, bytes): msg = str(msg).encode('utf-8')
                    if msg == b'': break  # client disconnected
                    client_socket.send(msg)

#--tcpClient-------------------------------------------------------------------
    def serverStop(self):
        self.terminate = True

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class testThread(threading.Thread):
    """ Thread to test the TCP server.""" 
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.testPort = 5005
        self.server = tcpServer(None, self.testPort, connctNum=1)

    def msgHandler(self, msg):
        """ Test handler method to handle the incomming message."""
        print("Incomming message: %s" %str(msg))
        return msg

    def run(self):
        """ Main loop to handle the data feed back."""
        print("Server thread start.")
        self.server.serverStart(handler=self.msgHandler)
        print("Server thread end.")

    def stop(self):
        self.server.serverStop()
        endClient = tcpClient(('127.0.0.1', self.testPort))
        endClient.disconnect()
        endClient = None

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def testCase(mode):
    print("Start TCP client-server test.")
    testPort = 5005
    if mode == 1:
        print("Start the TCP Server.")
        servThread = testThread(3, "server thread", 1)
        servThread.start()
        print("Start the TCP Client.")
        ipAddr = ('127.0.0.1', testPort)
        client = tcpClient(ipAddr)
        for i in range(2):
            msg = "Test data %s" %str(i)
            result = client.sendMsg(msg, resp=True)
            print(result)
        print("Test reconnect.")
        client.connect()
        print(client.sendMsg('Re-connected', resp=True))
        print("Test client disconnect.")
        client.disconnect()
        client = None
        print("Test server stop.")
        servThread.stop()
        print("Test end")
    else:
        print("Add more other exception test here.")
#-----------------------------------------------------------------------------
if __name__ == '__main__':
    testCase(1)







        
