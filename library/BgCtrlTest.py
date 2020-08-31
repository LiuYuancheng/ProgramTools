#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        BgCtrlTest.py
#
# Purpose:     TestCase Program for the BgCtrl module. This program will create 
#              a dummy background execution program.
#          
# Author:      Yuancheng Liu
#
# Created:     2020/08/31
# Copyright:   
# License:     
#-----------------------------------------------------------------------------
import time
import BgCtrl as bg

def main(mode=0):
    print("BgCtrl TestCase() program start:")
    bgctrler = bg.BgController("TestCase Program")
    time.sleep(1)
    while(bgctrler.bgRun()):
        print("Current time: %s" %str(time.time()))
        time.sleep(1)
    print("Program End")

#-----------------------------------------------------------------------------
if __name__ == '__main__':
    main()