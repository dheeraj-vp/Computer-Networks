def classify_ip(ip_address):
    try:
        octets = list(map(int, ip_address.split(".")))
        if len(octets) != 4 or any(o < 0 or o > 255 for o in octets):
            return "Invalid IP address"
    except ValueError:
        return "Invalid IP address"

    first_octet = octets[0]
    return ("Class A" if 1 <= first_octet <= 126 else
            "Class B" if 128 <= first_octet <= 191 else
            "Class C" if 192 <= first_octet <= 223 else
            "Class D" if 224 <= first_octet <= 239 else
            "Class E")

ip = input("Enter an IP address: ")
print("IP belongs to:", classify_ip(ip))