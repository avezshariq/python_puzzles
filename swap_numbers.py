# This might look like a stupid question

# a = 5
# b = 6

# c = a
# a = b
# b = c
# print(a,b)

# The challenge is to swap 2 numbers without using a third variable
# This is an interview question

a = 5
b = 6

a = a + b
b = a - b
a = a - b
print(a,b)

