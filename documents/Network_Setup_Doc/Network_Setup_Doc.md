# Network Setup Doc

**This document will show the steps to setup different network device control program on Rank 7 and Rank 8. The device list:**

**Server Room**

Router R2

**Data Center**

| Rank7(WE-07)        | Function         | Rank8(WE-08)         | Function   |
| ------------------- | ---------------- | -------------------- | ---------- |
| FORTINET 300D       | Firewall         | Cisco 2960 X         | A          |
| Catalyst 3650       | 48PS-8           | Cisco 2960 X         | B          |
| Catalyst 3650       | 48QS-8           | FORTINET 300D        | Firewall   |
| Cisco ASA 5516-X    | Firewall         | Catalyst 3650        | 48PS-7     |
| Attivo Botsink 3200 | Thread detection | Catalyst 3650        | 48QS-7     |
| HP DL360            | ENGRG_ESX        | Cisco 2900           | Router     |
| HP DL360            | RD-INC_ESX       | Pulse Secure Mag2600 | VPN server |
| HP DL360            | CEN_SERV         | Palo-alto PA500      | Firewall   |
| HP DL360            | ENGRG_SERV_1     | HP DL360             | DMZ_ESX    |
| HP DL360            | ENGRG_SERV_2     | HP DL360             | RD_SVN     |
|                     |                  | HP DL360             | RD_SERV_1  |
|                     |                  | HP DL360             | INC_SERV_1 |

**The format follow below:** 

**Device [Idx] :** device name/brand

**Connection Type:** http/https/ssh(with the putty seting)

**Setup Details:** 

1. example: add a new VPN user. 
2. ...



**HPE account:** yuancheng.liu@trustwave.com



[TOC]

------

##### Device [00] : Pulse Secure MAG2600 Gateway/VPN Server

**Connection Type:** Http:ipaddr/admin

**Setup Details:** 

1. Add a new VPN user: 

   Login => Authentication => Auth.Servers => System Local => Users => New

2. Assign user a role: 

   Users => User Reams => Local Users => Role Mapping => "username is"  => "* Rule IF username..."

3. Normal user password expired: 

   Let the user change them self: login http without "/admin" => General => update password. 

------

##### Device [01] : CISCO 2960X 

**Connection Type:** SSh Putty: IP:Port(22) connection type[Telnet]

**Setup Details:** 

https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3850/software/release/3se/vlan/configuration_guide/b_vlan_3se_3850_cg/b_vlan_3se_3850_cg_chapter_0110.html



------

##### **Device [02] :** Fortinet FG-300D-7 MGMT Firewall

**Connection Type:** http

**Setup Details:** 

1. Check the firewall machine warranty: 

     Login => Dashboard => Main => Licenses => FortiCare Support.

2. ...

------

##### **Device [03] :** Catalyst 3650

**Connection Type:** CAT-5 Cable

**Setup Details:** 

1. Access the supper admin port 

    Plug in Cat-5 cable in port "VLAN300", set computer static IP to 172.16.240.12, gateway  172.16.240.1

2. ...

------

