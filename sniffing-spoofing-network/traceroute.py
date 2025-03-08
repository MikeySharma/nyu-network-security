from scapy.all import *

# Destination IP address
destination = "8.8.8.8"

# Initialize TTL
ttl = 1

while True:
    # Create an IP packet with the destination and current TTL
    a = IP(dst=destination, ttl=ttl)
    
    # Create an ICMP packet (echo request)
    b = ICMP()
    
    # Combine IP and ICMP to form the final packet
    p = a/b
    
    # Send the packet and wait for a response
    pkt = sr1(p, verbose=0, timeout=2)  # Timeout after 2 seconds if no response
    
    # Check if a response was received
    if pkt is None:
        print(f"TTL: {ttl}, No response from router")
    elif pkt[ICMP].type == 0:  # ICMP echo reply (destination reached)
        print(f"TTL: {ttl}, Destination reached: {pkt[IP].src}")
        break
    else:  # ICMP time exceeded (router response)
        print(f"TTL: {ttl}, Router: {pkt[IP].src}")
    
    # Increment TTL for the next hop
    ttl += 1