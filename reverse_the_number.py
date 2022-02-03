# Ask the user for an integer number
# Print the same number in reverse order

# Example: User input = 123456
#          print      = 654321

print('This program takes an input from the user and reverse prints it')
print('Example, the user gives - 123456, then the program prints - 654321')
num = int(input('Enter a number :'))

num  = str(num)
for char in num:
  print(char)
