# Network Setup Doc

**This document will show the steps to setup different network device control program. The format follow below:** 

**Device [Idx] :** device name/brand

**Connection Type:** http/https/ssh(with the putty seting)

**Setup Details:** 

1. example: add a new VPN user. 
2. ...

[TOC]

------

##### Device [0] : Pulse Secure MAG2600 Gateway/VPN Server

**Connection Type:** Http:ipaddr/admin

**Setup Details:** 

1. Add a new VPN user: 

   Login => Authentication => Auth.Servers => System Local => Users => New

2. Assign user a role: 

   Users => User Reams => Local Users => Role Mapping => "username is"  => "* Rule IF username..."

3. 

------

##### Device [0] : CISCO 2960X 

**Connection Type:** SSh Putty: IP:Port(22) connection type[Telnet]

**Setup Details:** 

https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3850/software/release/3se/vlan/configuration_guide/b_vlan_3se_3850_cg/b_vlan_3se_3850_cg_chapter_0110.html