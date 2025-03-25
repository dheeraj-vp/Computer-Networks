def compute_checksum(data):
    total = sum(data)
    while total >> 16:
        total = (total & 0xFFFF) + (total >> 16)
    return ~total & 0xFFFF

def verify_checksum(data):
    return compute_checksum(data) == 0

def get_input(count, fmt):
    return [int(input(), 16) if fmt == 1 else int(input(), 2) for _ in range(count)]

def process_side(is_sender):
    count, fmt = int(input("Enter number of 16-bit words: ")), int(input("Enter data format (1: Hexadecimal, 2: Binary): "))
    print(f"Enter {count} values:")
    data = get_input(count, fmt)
    if is_sender:
        data.append(compute_checksum(data))
        print("Computed Checksum:", f"{data[-1]:04X}" if fmt == 1 else format(data[-1], '016b'))
        print("Transmitted Data:")
    print(*[f"{x:04X}" if fmt == 1 else format(x, '016b') for x in data], sep="\n" if fmt == 2 else " ")
    if not is_sender:
        print("Data is correct (No errors detected)." if verify_checksum(data) else "Error detected in received data!")

while True:
    choice = int(input("\n--- Checksum Menu ---\n1. Sender's Side\n2. Receiver's Side\n3. Exit\nEnter your choice: "))
    if choice in (1, 2): process_side(choice == 1)
    elif choice == 3: print("Exiting..."); break
    else: print("Invalid choice! Please enter 1, 2, or 3.")