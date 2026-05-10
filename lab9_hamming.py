def generate_hamming(data):

    l = list(map(int, data))
    # Data bits
    d7 = l[0]
    d6 = l[1]
    d5 = l[2]
    d3 = l[3]

    # Calculate parity bits
    p1 = d3 + d5 + d7
    p2 = d3 + d6 + d7
    p4 = d5 + d6 + d7
    
    p1 = 0 if(p1 % 2 ==0) else 1
    p2 = 0 if(p2 % 2 ==0) else 1
    p4 = 0 if(p4 % 2 ==0) else 1
    
    hamming_code = [d7 , d6 , d5 , p4 , d3, p2 , p1]
    
    output = ''.join(map(str , hamming_code))
    
    return output


# Function to detect and correct error
def detect_and_correct(code):

    b = list(map(int, code))

    # Received bits
    d7 = b[0]
    d6 = b[1]
    d5 = b[2]
    p4 = b[3]
    d3 = b[4]
    p2 = b[5]
    p1 = b[6]

    # Recalculate parity bits
    c1 = p1 + d3 + d5 + d7
    c2 = p2 + d3 + d6 + d7
    c4 = p4 + d5 + d6 + d7
    c1 = 0 if (c1 % 2 == 0) else 1
    c2 = 0 if (c2 % 2 == 0) else 1
    c4 = 0 if (c4 % 2 == 0) else 1
    
    # Find error position
    error_position = c4 * 4 + c2 * 2 + c1

    # Correct error if exists
    if error_position != 0:

        print("\nError Detected at Position:", error_position)

        # Flip the bit
        b[7-error_position] ^= 1

        print("Corrected Code:")
        corrected_code = ''.join(map(str , b))
        print (corrected_code)

    else:
        print("\nNo Error Detected")

    return b



data = input("Enter 4-bit binary data: ")

# Generate Hamming Code
hamming_code = generate_hamming(data)

print("Generated Hamming Code : " , hamming_code )


	
# Receive code
received = input("\nEnter received 7-bit code: ")

# Detect and Correct Error
detect_and_correct(received)
