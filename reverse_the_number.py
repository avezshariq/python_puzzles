# Ask the user for an integer number
# Print the same number in reverse order

# Example: User input = 123456
#          print      = 654321

print('This program takes an input from the user and reverse prints it')
print('Example, the user gives - 123456, then the program prints - 654321')
num = int(input('Enter a number :'))

num  = str(num)
length = len(num)
for char in range(length-1, -1, -1): # Writing a loop to access the numbers from last to first
  print(num[char], end='')
print()

