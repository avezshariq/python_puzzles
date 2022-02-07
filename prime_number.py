# This program checks whether the given number is Prime or not


num = int(input('Enter a Positive integer: '))

if num == 1:
    print('1 is considered neither Prime nor Composite number')
elif num == 2:
    print('2 is a Prime number')
else:
    for i in range(2, num):
        if num % i == 0:
            break
        print(i)
    if i == num-1:
        print(num,'is a Prime number')
    else:
        print(num,'is NOT a Prime number')
