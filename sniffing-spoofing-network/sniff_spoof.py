from scapy.all import *

def sniff_and_spoof(packet):
    # Check if the packet is an ICMP echo request (type 8)
    if ICMP in packet and packet[ICMP].type == 8:
        # Extract the source and destination IP from the original packet
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Craft a spoofed ICMP echo reply (type 0)
        ip = IP(src=dst_ip, dst=src_ip)  # Swap source and destination IP
        icmp = ICMP(type=0, id=packet[ICMP].id, seq=packet[ICMP].seq)  # Echo reply

        # Copy the raw data from the original packet
        raw_data = packet[Raw].load

        # Combine the IP, ICMP, and raw data to create the new packet
        newpacket = ip / icmp / raw_data

        # Send the spoofed packet
        send(newpacket, verbose=0)

# Sniff ICMP packets on the network
pkt = sniff(filter="icmp", prn=sniff_and_spoof)