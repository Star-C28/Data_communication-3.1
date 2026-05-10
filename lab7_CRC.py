def crc(data, key):
    data = list(data)

    for i in range(len(data) - len(key) + 1):
        if data[i] == '1':
            for j in range(len(key)):
                if data[i+j] == key[j]:
                    data[i+j] = '0'
                else:
                    data[i+j] = '1'

    return ''.join(data[-(len(key)-1):])


data = input("Enter data: ")
key = input("Enter key: ")

rem = crc(data + '0' * (len(key)-1), key)
codeword = data + rem

print("Remainder:", rem)
print("Codeword:", codeword)

received = input("Enter received codeword: ")

check = crc(received, key)

print("Receiver Remainder:", check)

if check == '0' * (len(key)-1):
    print("No Error Detected")
else:
    print("Error Detected")

# Enter data: 100100
# Enter key: 1101
