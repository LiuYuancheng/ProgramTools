#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        BgCtrl.py
#
# Purpose:     This module is used to create a background program controler: when 
#              we want to run a program in back ground with a loop. Some time it is
#              difficult for us to track whether the program is running or stop. This
#              module is used to create a record file to record the background program 
#              running and a system value for the user to check and control.
#          
# Author:      Yuancheng Liu
#
# Created:     2020/08/31
# Copyright:   
# License:     
#-----------------------------------------------------------------------------

import os
import datetime

import psutil   # >> pip install psutil
BG_RCD = "bgProgramRcd.txt"

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class BgController(object):
    def __init__(self, progName):
        dirpath = os.getcwd()
        self.progName = progName
        self.rcdFile = os.path.join(dirpath, BG_RCD)
        try:
            self.pId = os.getpid()
            fh = open(self.rcdFile, 'w')
            fh.write("Program Name\t:%s\n" %str(self.progName))
            fh.write("Process ID\t:%s\n" %str(self.pId))
            fh.write("Execute Time\t:%s\n" %str(datetime.datetime.now()))
            fh.close()
        except Exception as e:
            print("Create the background record file failed: %s." %str(e))
            if os.path.exists(self.rcdFile): os.remove(self.rcdFile)
            
    def bgRun(self):
        """ Check whether the program can be run in the background. 
            return True/False.
        """
        return os.path.exists(self.rcdFile)

#-----------------------------------------------------------------------------

def main(mode=0):
    print("Check the background program running situation:")
    dirpath = os.getcwd()
    processID = None
    rcdFile = os.path.join(dirpath, BG_RCD)
    if os.path.exists(rcdFile):
        with open(rcdFile, 'r') as fh:
            for line in fh.readlines():
                print(line)
                if "Process ID" in line:
                    processID = int(line.rstrip().split(':')[-1])
    else:
        print("No background record file, the program is not running.")
        exit()
    
    if psutil.pid_exists(processID):
        print("The program is running. Do you want end it [Y/N]:")
    else:
        print("The program is NOT running. Do you want to remove the record [Y/N]:")
    uInput = str(input()).lower()
    if uInput == 'y':
        os.remove(rcdFile)
        print("-> removed the program background record at the same time.\n")
    print("Finished.")

#-----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
