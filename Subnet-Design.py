def ip_to_int(ip):
    return sum(int(octet) << (24 - 8 * i) for i, octet in enumerate(ip.split('.')))

def int_to_ip(ip):
    return '.'.join(str((ip >> (8 * i)) & 0xFF) for i in range(3, -1, -1))

def subnet_details(ip, mask):
    ip, mask = ip_to_int(ip), ip_to_int(mask)
    network = ip & mask
    broadcast = network | ~mask & 0xFFFFFFFF
    return {
        "Network Address": int_to_ip(network),
        "Broadcast Address": int_to_ip(broadcast),
        "First Usable IP": int_to_ip(network + 1),
        "Last Usable IP": int_to_ip(broadcast - 1),
        "Total Usable Hosts": broadcast - network - 1
    }

ip = input("Enter IP Address: ")
mask = input("Enter Subnet Mask: ")

details = subnet_details(ip, mask)
print("\nSubnet Details:")
for key, value in details.items():
    print(f"{key}: {value}")
