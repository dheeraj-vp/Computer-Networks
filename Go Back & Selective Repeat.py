def go_back_n():
    frames = int(input("Enter the number of frames: "))
    window = int(input("Enter the window size: "))
    
    for i in range(1, frames + 1):
        print(f"Frame {i} sent")
        if i % window == 0 or i == frames:
            print(f"Acknowledgment received for frames up to {i}")

def selective_repeat():
    frames = int(input("Enter the number of frames: "))
    status = [False] * frames
    i = 0
    
    while i < frames:
        if not status[i]:
            print(f"Frame {i+1} sent")
            ack = int(input("Enter 1 if acknowledgment received, 0 if lost: "))
            if ack: status[i] = True
            else: continue
        i += 1
    print("All frames sent successfully")

while True:
    print("\n---- Flow Control ----")
    print("1. Go-Back-N\n2. Selective Repeat\n3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1: go_back_n()
    elif choice == 2: selective_repeat()
    elif choice == 3: break
    else: print("Invalid choice. Please try again.")