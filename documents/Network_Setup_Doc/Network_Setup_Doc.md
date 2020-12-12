# Network Setup Doc

#### Introduction 

**This document will show the steps to setup different network device control program on WE7 and WE 8 server stack.**

[TOC]

------

#### Device Location and List

###### Server Room

Router R2 (USB interface)

###### Data Center

| Rank7(WE-07)           | Function         | Rank8(WE-08)                 | Function   |
| ---------------------- | ---------------- | ---------------------------- | ---------- |
| FORTINET 300D          | Firewall         | Cisco 2960 X                 | router A   |
| Catalyst 3650          | 48PS-8           | Cisco 2960 X                 | router B   |
| Catalyst 3650          | 48QS-8`          | FORTINET 300D                | Firewall   |
| Cisco ASA 5516-X       | Firewall         | Catalyst 3650                | 48PS-7     |
| Attivo Botsink 3200    | Thread detection | Catalyst 3650                | 48QS-7     |
| HP DL360(128GB/8TB)    | ENGRG_ESX        | Cisco 2900                   | Router     |
| HP DL360(256GB/8TB)    | RD-INC_ESX       | Pulse Secure Mag2600         | VPN server |
| HP DL360(256GB/4.48TB) | CEN_SERV         | Palo-alto PA500              | Firewall   |
| HP DL360(32GB/2TB)     | ENGRG_SERV_1     | HP DL360(128GB/8TB)          | DMZ_ESX    |
| HP DL360(32GB/2TB)     | ENGRG_SERV_2     | HP DL360 (192GB/5TB)         | RD_SVN     |
|                        |                  | HP DL360(160GB/3.6TB)        | RD_SERV_1  |
|                        |                  | HP DL360(128GB/8TB)          | INC_SERV_1 |
|                        |                  | HP GPU server(512GB/8.960TB) |            |



#### Device Configuration Setup

#### 

**The format follow below:** 

###### Device [Idx] : device name/brand

**Connection Type:** http/https/ssh(with the putty seting)

**Setup Details:** 

1. example: add a new VPN user. 
2. ...



------

###### Device [00] : Pulse Secure MAG2600 Gateway/VPN Server

**Connection Type:** Http:ipaddr/admin

**Setup Details:** 

1. Add a new VPN user: 

   Login => Authentication => Auth.Servers => System Local => Users => New

2. Assign user a role: 

   Users => User Reams => Local Users => Role Mapping => "username is"  => "* Rule IF username..."

3. Normal user password expired: 

   Let the user change them self: login http without "/admin" => General => update password. 

4. The user can not log in because of  win10 vpn said the server certificate is not trusted as the user download the pulse secure VPN client from the Windows App store: 

   - Let the user uninstalled  the pulse secure VPN client from the Windows App store. 
   - Download the Pulse secure VPN client  and re-install this Pulse Secure VPN client on user's  machine (https://www.pulsesecure.net/trynow/client-download/ and let the user Login again.

5. 

   

------

###### Device [01] : CISCO 2960X 

**Connection Type:** SSh Putty: IP:Port(22) connection type[Telnet]

**Setup Details:** 

https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3850/software/release/3se/vlan/configuration_guide/b_vlan_3se_3850_cg/b_vlan_3se_3850_cg_chapter_0110.html

=> If not understand how the cmd work, just add the char '?' behind the command. 

1. How to remove a session: 

   Switch>enable

   Switch#show run

   Switch#configure

   Switch(config)#no monitor session 2 source interface Gi2/0/13 - 14 

   Switch(config)#exit

   Switch#show run

   Switch#copy run start

   Switch#[press enter to confirm.]

2. How to add a monitor session: 

   Switch>enable

   Switch#config

   Switch(config)#monitor session 2 source interface gigabitEthernet 2/0/20 rx 

   Switch(config)#exit

   Switch#show run

   Switch#copy run start

   Switch#[press enter to confirm.]

3. 

------

###### Device [02] : Fortinet FG-300D-7 MGMT Firewall

**Connection Type:** http

**Setup Details:** 

1. Check the firewall machine warranty: 

     Login => Dashboard => Main => Licenses => FortiCare Support.

2. Check the service information: 

     => Login Fortinet service web[https://support.fortinet.com/Main.aspx] with account yuancheng.liu@trustwave.com

     => Asset => Mange/view product

3. 

------

###### Device [03] : Catalyst 3650

**Connection Type:** CAT-5 Cable

**Setup Details:** 

1. Access the supper admin port 

    Plug in Cat-5 cable in port "VLAN300", set computer static IP to 172.16.240.12, gateway  172.16.240.1

2. ...

------

###### Device [04] : HP GPU server

**Connection Type:** http

**Setup Details:** 

1. Check machine warranty expired time

   => Login Hewlett Packard Enterprise Support Center[https://support.hpe.com/hpesc/public/home] with account yuancheng.liu@trustwave.com

   => Contracts and warranties => View my contracts & warranties => Linked warranties

2. ...



------

###### Device [05] : HP DL360 ESXi VM Server

**Connection Type:** http

**Setup Details:** 

1. Create A VM on the server: 

   => Login the VM server => Select "Create/Register VM" => follow the step to create the VM => 1.Select create type =>2.select a name and guest OS => 3.select storage => 4.Customize Settings[Click the "Hard Disk1" ->Disk Provisioning -> select "**Thin provisioned**"(important)] => Ready to complete.

2. Created VM shows error: 

   PXE-M0F: Exiting iontel PXE ROM. 

   Operating system not found

   => Edit => CD/DVD Drive 1=> Select "DataStore ISO file" => CD/DVD Media => Browse =>  dataSore1 => ISO => select needed system iso => save. 

   => reboot the VM and install the system.

3. 



------

#### Network IP Mapping Configuration



------

#### Device License and warranty check

**HPE account:** yuancheng.liu@trustwave.com

**Fortinet account**: yuancheng.liu@trustwave.com


