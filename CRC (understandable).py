def checksum(data):
    total = sum(data)
    while total > 0xFFFF:
        total = (total & 0xFFFF) + (total >> 16)
    return ~total & 0xFFFF

def verify(data):
    return checksum(data) == 0

def get_vals(n, fmt):
    # fmt: 1 for hex, 2 for binary
    return [int(input(), 16) if fmt == 1 else int(input(), 2) for _ in range(n)]

def print_data(data, fmt):
    if fmt == 1:
        print(" ".join(f"{x:04X}" for x in data))
    else:
        for x in data:
            print(f"{x:016b}")

def process(is_sender):
    n = int(input("Enter number of 16-bit words: "))
    fmt = int(input("Enter data format (1: Hex, 2: Binary): "))
    print(f"Enter {n} values:")
    data = get_vals(n, fmt)
    
    if is_sender:
        cs = checksum(data)
        data.append(cs)
        print("Computed Checksum:", f"{cs:04X}" if fmt == 1 else f"{cs:016b}")
        print("Transmitted Data:")
    else:
        print("Received Data:")
    
    print_data(data, fmt)
    
    if not is_sender:
        print("Data is correct." if verify(data) else "Error detected!")

while True:
    print("\n--- Checksum Menu ---")
    print("1. Sender's Side")
    print("2. Receiver's Side")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        process(True)
    elif choice == 2:
        process(False)
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")



