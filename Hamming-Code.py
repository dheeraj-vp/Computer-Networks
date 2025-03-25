def calculate_parity(bits, pos):
    parity = 0
    i = pos - 1  # Convert to 0-based index
    while i < len(bits):
        for j in range(i, min(i + pos, len(bits))):# Check 'pos' number of bits, then skip 'pos' bits
            parity ^= bits[j]
        i += 2 * pos  # Skip to next parity block
    return parity

def hamming_encode(data):
    n = len(data)
    p = 0
    while 2**p < n + p + 1:
        p += 1    
    code = []
    data_iter = iter(data)
    for i in range(n + p):
        if (i + 1) & i == 0:  # Check for power-of-two positions
            code.append(0)
        else:
            code.append(next(data_iter))    
    for i in range(p):    # Calculate parity bits
        pos = 2**i
        code[pos-1] = calculate_parity(code, pos)    
    return code

def hamming_decode(code):
    p = 0
    while 2**p < len(code):
        p += 1    
    error = 0
    for i in range(p):
        pos = 2**i
        if calculate_parity(code, pos):
            error += pos    
    if error:
        code[error-1] ^= 1
        print(f"Error at position {error}, corrected code: {code}")
    else:
        print("No errors detected")
    return code

data = list(map(int, input("Enter data bits (space-separated): ").split()))
encoded = hamming_encode(data)
print("Encoded:", encoded)
received = list(map(int, input("Enter received code (space-separated): ").split()))
hamming_decode(received)