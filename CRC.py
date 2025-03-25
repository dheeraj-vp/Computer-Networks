def compute_crc(data, poly):
    temp = list(data + '0' * (len(poly) - 1))
    for i in range(len(data)):
        if temp[i] == '1':
            for j in range(len(poly)):
                temp[i + j] = '0' if temp[i + j] == poly[j] else '1'
    return ''.join(temp[len(data):])

def sender_side():
    data, poly = input("Enter data (binary): "), input("Enter divisor (binary): ")
    crc = compute_crc(data, poly)
    print(f"\nComputed CRC: {crc}\nTransmitted Data with CRC: {data + crc}")

def receiver_side():
    received, poly = input("Enter received data (binary): "), input("Enter divisor (binary): ")
    print("No error detected. Data is correct." if '1' not in compute_crc(received, poly) else "Error detected in received data.")

while True:
    choice = input("\n--- CRC Menu ---\n1. Sender's Side\n2. Receiver's Side\n3. Exit\nEnter your choice: ")
    if choice == '1': sender_side()
    elif choice == '2': receiver_side()
    elif choice == '3': print("Exiting..."); break
    else: print("Invalid choice! Please enter 1, 2, or 3.")
