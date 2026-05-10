# Number of data rows
n = int(input("Enter number of data rows: "))

data = []

# Input binary rows
for i in range(n):
    row = input(f"Enter binary data row {i+1}: ")
    data.append(row)

lrc = ""

# Generate LRC
for col in range(len(data[0])):
    ones = 0

    for row in data:
        if row[col] == '1':
            ones += 1

    if ones % 2 == 0:
        lrc += '0'
    else:
        lrc += '1'

# Display Sender Side Data
print("\nSender Side Data Block:")
for row in data:
    print(row)

print("Generated LRC:", lrc)

# ---------------- Receiver Side ----------------

print("\n--- Receiver Side ---")

received = []

# User inputs received codewords
for i in range(n):
    row = input(f"Enter received data row {i+1}: ")
    received.append(row)

received_lrc = input("Enter received LRC: ")

# Add received LRC to received data
received.append(received_lrc)

# Error Checking
error = False

for col in range(len(received[0])):
    ones = 0

    for row in received:
        if row[col] == '1':
            ones += 1

    if ones % 2 != 0:
        error = True

# Result
print("\nReceived Block:")
for row in received[:-1]:
    print(row)

print("Received LRC:", received_lrc)

if error:
    print("Error Detected")
else:
    print("No Error")

# Enter number of data rows: 3
# Enter binary data row 1: 1011
# Enter binary data row 2: 1100
# Enter binary data row 3: 1001


# Enter received data row 1: 1011
# Enter received data row 2: 1100
# Enter received data row 3: 1001
# Enter received LRC: 1110