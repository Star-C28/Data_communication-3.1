# Sender Side

# Take binary data from user
data = input("Enter binary data: ")

# Count number of 1's
ones = data.count('1')

# Generate Even Parity Bit
parity = '0' if ones % 2 == 0 else '1'

# Create codeword
codeword = data + parity

# Display transmitted data
print("\n--- Sender Side ---")
print("Data:", data)
print("Parity Bit:", parity)
print("Transmitted Codeword:", codeword)


# Receiver Side

# Take received codeword from user
received = input("\nEnter received codeword: ")

# Check parity
if received.count('1') % 2 == 0:
    print("No Error Detected")
else:
    print("Error Detected")

 # Data: 1100001
