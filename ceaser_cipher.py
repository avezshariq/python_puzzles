# This program is to encrypt a message using one of the oldest techniques called the Ceaser Cipher
# There is a variable known as shift
# Let's say shift is 4
# Then A --> E, B --> F, C --> G and W --> A, X --> B, Y --> C, Z --> D
# We will use ASCII conversion to achieve this
# We will ignore numbers and spaces

message = input('Enter your message: ')
shift = int(input('Enter an integer between 1 to 25 for shift: '))


# a = 97
# A = 65
# z = 122
# Z = 90

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
    else: # For everything else like numbers etc..
        print(i, end='')
print('') # Courtesy for next lines