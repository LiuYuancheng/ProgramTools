# ProgramTools - [socketComm] 
#### Introduction

This project is used to provide different socket communication program API and the related test case. 

- TCP Client-Server communication. 
- UDP Client-Server communication.
- ZMQ Pub-Sub communication. 
- ZMQ router-dealer communication.
- Serial Port communication(RS232/485)
- PLC modeBus TCP communication (Schneider/Siemens).



------

#### Program Setup

###### Development Environment : python 3.7

###### Additional Lib/Software Need : 

snap7 for PLC

> http://simplyautomationized.blogspot.com/2014/12/raspberry-pi-getting-data-from-s7-1200.html

###### Hardware Needed : None

###### Program File List :

| Program File  | Execution Env | Description                                                  |
| ------------- | ------------- | ------------------------------------------------------------ |
| tcpCom.py     | python 3.7    | This module will provide TCP client and server communication API. |
| tcpComTest.py | python 3.7    | This module will provide a muti-thread test case program to test the TCP communication modules by using port 5005. |
| udpCom.py     | python3.7     | This module will provide a UDP client and server communication API. |
| udpComTest.py | python3.7     | This module will provide a muti-thread test case program to test the UDP communication modules by using port 5005. |
| M2PLC221.py   | python2.7/3.7 | This module is used to connect to the Schneider M2xx PLC.    |
| S7PLC1200.py  | python3.7     | This module is used to connect to the siemens s7-1200 PLC.   |
| serialCom.py  | python3.7     | This module will inheritance the python built-in serial module with automatically serial port search and connection function. |
| zmqCom.py     | python3.7     | This module will provide ZMQ router-dealer communication module. |



------

> Last edit by LiuYuancheng(liu_yuan_cheng@hotmail.com) at 18/04/2020