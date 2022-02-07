# This program is to decrypt a message using one of the oldest techniques called the Ceaser Cipher
# For more info check encrypt file

message = input('Enter message to decrypt: ')
shift = int(input('Enter an integer between 1 to 25 for shift: '))


# a = 97
# A = 65
# z = 122
# Z = 90

for i in message:
    conv = ord(i)

    if 97 <= conv <= 122: # Lower Case alphabet  
        conv -= shift
        if conv < 97:
            conv = conv + 26
        print(chr(conv), end='')
    elif 65 <= conv <= 90: # Upper Case alphabet  
        conv -= shift
        if conv < 65:
            conv = conv + 26
        print(chr(conv), end='')
    else: # For everything else like Special Chars, Symbols etc..
        print(i, end='')

print('') # Courtesy for next lines
