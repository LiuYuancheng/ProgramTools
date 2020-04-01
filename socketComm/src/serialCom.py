#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        serialCom.py
#
# Purpose:     This module will packaged the python built-in serial module to 
#              provide a automatically serial port serach and connection 
#
# Author:      Yuancheng Liu
#
# Created:     2019/04/01
# Copyright:   
# License:     
#-----------------------------------------------------------------------------
import os
import sys
import glob
import serial

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class serialCom(object):
    def __init__(self, parent, serialPort=None, baudRate=9600):
        self.serComm = None
        conIdx = 0     # port index used for connection.
        # Automatically find the serial port which can read
        if serialPort is None:
            if sys.platform.startswith('win'):
                ports = ['COM%s' % (i + 1) for i in range(256)]
                self.conIdx = -1
            elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
                # this excludes your current terminal "/dev/tty"
                ports = glob.glob('/dev/tty[A-Za-z]*')
            elif sys.platform.startswith('darwin'):
                ports = glob.glob('/dev/tty.*')
            else:
                raise EnvironmentError('Serial Port comm connection error: Unsupported platform.')
            portList = []
            for port in ports:
                # Check whether the ports can be open.
                try:
                    s = serial.Serial(port)
                    s.close()
                    portList.append(port)
                except (OSError, serial.SerialException):
                    pass
            print(('COM connection: the serial port can be used :%s' % str(portList)))
            serialPort = portList[conIdx]
        # Conne
        try:
            self.serComm = serial.Serial(serialPort, baudRate, 8, 'N', 1, timeout=1)
        except:
            print("Serial connection: serial port open error.")
            return None

#-----------------------------------------------------------------------------
    def readComm(self, byteNum=100, decodeType=None):
        msg = self.serComm.read(byteNum)
        if decodeType: msg.decode(decodeType)

#-----------------------------------------------------------------------------
    def wirteComm(self, msgStr, encodeType=None):
        self.serComm.write(msgStr.encode(encodeType))

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def testCase(testMode):

    print("Start serial port communication test. Test mode %s \n" %str(testMode))
    if testMode == 1:
        print("Test Case 1: test connect to the un-readable port.")
        connector = serialCom(None,serialPort="COM_NOT_EXIST", baudRate=115200)
        result = 'Pass' if connector is None else 'Fail'
        print(" - Test result: %s \n" %result)

    print("Test Case 2: test connect to com port.")
    connector = serialCom(None, baudRate=115200)
    connector.wirteComm('Test String', encodeType='utf-8')
    msg = connector.readComm(byteNum=1024, decodeType='utf-8')
    print("Read message from the com: %s" %str(msg))

#-----------------------------------------------------------------------------
if __name__ == '__main__':
    testCase(1)