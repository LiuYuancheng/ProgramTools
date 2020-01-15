#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        udpCom.py
#
# Purpose:     This module will provide a UDP client + server API and a multi-thread
#              test case which may be used for other project.
#
# Author:      Yuancheng Liu
#
# Created:     2019/01/15
# Copyright:   
# License:     
#-----------------------------------------------------------------------------

import time
import socket
import threading    # create multi-thread test case.

BUFFER_SZ = 4096    # TCP buffer size.

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class udpClient(object):
    """ UDP client module."""
    def __init__(self, ipAddr):
        self.ipAddr = ipAddr
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def sendMsg(self, msg, resp=False, ipAddr=None):
        if not ipAddr is None: self.ipAddr = ipAddr
        if not isinstance(msg, bytes): msg = str(msg).encode('utf-8')
        self.client.sendto(msg, self.ipAddr)
        if resp:
            data, _ = self.client.recvfrom(BUFFER_SZ)
            return data
        return None

    def disconnect(self):
        """ Send a empty message and close the socket.
        """
        self.sendMsg(msg='')
        self.client.close()

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class udpServer(object):
    """ UDP server module."""
    def __init__(self, parent, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind(('0.0.0.0', port))
        self.terminate = False  # Server terminate flag.

#--udpServer-------------------------------------------------------------------
    def serverStart(self, handler=None):
        """ Start the TCP server to handle the incomming message."""
        while not self.terminate:
            data, address = self.server.recvfrom(BUFFER_SZ)
            print("Accepted connection from %s" % str(address))
            msg = handler(data) if not handler is None else data
            if not msg is None: # don't response client if the handler feed back is None
                if not isinstance(msg, bytes): msg = str(msg).encode('utf-8')
                self.server.sendto(msg, address)
        self.server.close()

#--udpServer-------------------------------------------------------------------
    def serverStop(self):
        self.terminate = True

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class testThread(threading.Thread):
    """ Thread to test the UDP server.""" 
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.testPort = 5005
        self.server = udpServer(None, self.testPort)

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
        endClient = udpClient(('127.0.0.1', self.testPort))
        endClient.disconnect()
        endClient = None

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def testCase(mode):
    print("Start UDP client-server test.")
    testPort = 5005
    if mode == 1:
        print("Start the UDP Server.")
        servThread = testThread(1, "server thread", 1)
        servThread.start()
        print("Start the UDP Client.")
        ipAddr = ('127.0.0.1', testPort)
        client = udpClient(ipAddr)
        for i in range(2):
            msg = "Test data %s" %str(i)
            result = client.sendMsg(msg, resp=True)
            print(result)
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