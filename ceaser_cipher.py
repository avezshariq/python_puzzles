# This program is to encrypt a message using one of the oldest techniques called the Ceaser Cipher
# There is a variable known as shift
# Let's say shift is 4
# Then A --> E, B --> F, C --> G and W --> A, X --> B, Y --> C, Z --> D
# We will use ASCII conversion to achieve this
# a = 97
# A = 65
# z = 122
# Z = 90
# We will ignore numbers and spaces

def encryption(message, shift):
    print('Your encrypted message is ...')
    for i in message:
        conv = ord(i)

        if 97 <= conv <= 122: # Lower Case alphabet  
            conv += shift
            if conv > 122:
                conv = conv - 26
            print(chr(conv), end='')
        elif 65 <= conv <= 90: # Upper Case alphabet  
            conv += shift
            if conv > 122:
                conv = conv - 26
            print(chr(conv), end='')
        else: # For everything else like Numbers, Special Chars etc..
            print(i, end='')

    print('') # Courtesy for next lines

def decryption(message, shift):
    print('Your decrypted message is ...')
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

message = input('Enter a message: ')
shift = int(input('Enter an integer between 1 to 25 for shift: '))
choice = int(input('Do you want to \n 1.Encrypt \n 2.Decrypt\n -->  '))
if choice == 1:
    encryption(message, shift)
elif choice == 2:
    decryption(message, shift)
else:
    print('Bad choice, are you a spy ?')