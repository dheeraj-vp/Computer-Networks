def get_address_count(host_bits):
    return 2 ** host_bits

def advance_ip(ip):
    ip[3] += 1
    for i in range(3, 0, -1):
        if ip[i] > 255:
            ip[i] = 0
            ip[i - 1] += 1
    if ip[0] > 255:
        print("Error: IP range exceeded.")
        exit(1)

def display_subnet(group, customer, ip, prefix, host_bits, remaining_ips):
    needed_ips = get_address_count(host_bits)
    if needed_ips > remaining_ips:
        print(f"Not enough IPs left for Group {group} - Customer {customer}. Skipping...")
        return remaining_ips  # No change in assigned count

    print(f"Group {group} - Customer {customer}: {'.'.join(map(str, ip))}/{prefix} -> ", end="")
    for _ in range(needed_ips - 1):
        advance_ip(ip)
    print(f"{'.'.join(map(str, ip))}/{prefix}")
    advance_ip(ip)
    
    return remaining_ips - needed_ips  # Deduct allocated IPs

ip_input = input("Enter IP in CIDR format (e.g., 192.168.1.0/24): ").strip()
if '/' not in ip_input:
    print("Invalid format. Use CIDR notation.")
    exit(1)

ip_str, prefix = ip_input.split('/')
ip = list(map(int, ip_str.split('.')))
prefix = int(prefix)
total_ips = get_address_count(32 - prefix)
remaining_ips = total_ips  # Track available IPs

for g in range(1, int(input("Enter number of groups: ")) + 1):
    print(f"\nGroup {g}")
    for c in range(1, int(input("Enter number of customers: ")) + 1):
        required = int(input("Addresses required: ")) + 2  # Include network & broadcast
        bits = required.bit_length()
        subnet_prefix = 32 - bits

        remaining_ips = display_subnet(g, c, ip, subnet_prefix, bits, remaining_ips)

        if remaining_ips <= 0:
            print("\nNo more IPs available.")
            break  # Stop allocating if out of IPs

print(f"\nTotal available: {total_ips}, Assigned: {total_ips - remaining_ips}, Remaining: {remaining_ips}")
