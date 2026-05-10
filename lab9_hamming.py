import random

# User input
data = input("Enter 4-bit data: ")

# Convert to integer list
d = list(map(int, data))

# Calculate parity bits
p1 = d[0] ^ d[1] ^ d[3]
p2 = d[0] ^ d[2] ^ d[3]
p4 = d[1] ^ d[2] ^ d[3]

# Generate Hamming Code
hamming = f"{p1}{p2}{d[0]}{p4}{d[1]}{d[2]}{d[3]}"

print("\nData:", data)
print("Hamming Code:", hamming)

# Receiver Side
received = list(map(int, hamming))

# Automatically generate random error position
error_pos = random.randint(1, 7)

# Introduce error
received[error_pos - 1] ^= 1

print("Error introduced at position:", error_pos)
print("Received Code:", ''.join(map(str, received)))

# Error Detection
c1 = received[0] ^ received[2] ^ received[4] ^ received[6]
c2 = received[1] ^ received[2] ^ received[5] ^ received[6]
c4 = received[3] ^ received[4] ^ received[5] ^ received[6]

detected_error = c4 * 4 + c2 * 2 + c1

print("Detected Error Position:", detected_error)

# Error Correction
if detected_error != 0:
    received[detected_error - 1] ^= 1
    print("Error Corrected")

print("Corrected Code:", ''.join(map(str, received)))

# Enter 4-bit data: 1011