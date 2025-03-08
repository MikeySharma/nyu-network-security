import nmap

def scan_network(ip_range):
    nm = nmap.PortScanner()
    
    # Perform SYN scan (-sS), OS detection (-O), and service detection (-sV)
    nm.scan(hosts=ip_range, arguments="-sS -O -sV")

    devices = []

    for host in nm.all_hosts():
        device_info = {
            "ip": host,
            "mac": nm[host]["addresses"].get("mac", "Unknown"),
            "hostname": nm[host]["hostnames"][0]["name"] if nm[host]["hostnames"] else "Unknown",
            "vendor": nm[host]["vendor"].get(nm[host]["addresses"].get("mac", ""), "Unknown"),
            "os": nm[host]["osmatch"][0]["name"] if nm[host].get("osmatch") else "Unknown",
            "ports": []
        }

        # Get open ports and services
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                device_info["ports"].append({
                    "port": port,
                    "service": nm[host][proto][port].get("name", "Unknown"),
                    "state": nm[host][proto][port].get("state", "Unknown")
                })

        devices.append(device_info)

    return devices

if __name__ == "__main__":
    ip_range = "192.168.18.1/24"  # Replace with your subnet
    devices = scan_network(ip_range)

    print("\nConnected Devices:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}, Hostname: {device['hostname']}")
        print(f"OS: {device['os']}, Vendor: {device['vendor']}")
        print("Open Ports:")
        for port in device["ports"]:
            print(f" - Port {port['port']} ({port['service']}): {port['state']}")
        print("-" * 50)
