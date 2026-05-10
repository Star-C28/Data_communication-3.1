n = int(input("Enter number of data words: "))

data = []

for i in range(n):
    word = input(f"Enter 8-bit binary word {i+1}: ")
    data.append(word)

sum_value = 0

for word in data:
    sum_value += int(word, 2)

while sum_value > 255:
    sum_value = (sum_value & 255) + 1

checksum = bin(~sum_value & 255)[2:].zfill(8)

print("\nSender Side:")
for word in data:
    print(word)

print("Checksum:", checksum)

print("\n--- Receiver Side ---")

received = []

for i in range(n):
    word = input(f"Enter received 8-bit word {i+1}: ")
    received.append(word)

received_checksum = input("Enter received checksum: ")

received_sum = 0

for word in received:
    received_sum += int(word, 2)

received_sum += int(received_checksum, 2)

while received_sum > 255:
    received_sum = (received_sum & 255) + 1

if received_sum == 255:
    print("No Error")
else:
    print("Error Detected")

# Enter number of data words: 3
# Enter 8-bit binary word 1: 10011001
# Enter 8-bit binary word 2: 11100010
# Enter 8-bit binary word 3: 00100100


# Enter received 8-bit word 1: 10011001
# Enter received 8-bit word 2: 11100010
# Enter received 8-bit word 3: 00100100
# for error->
# Enter received checksum: 10111111