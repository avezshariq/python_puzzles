# Check if a string is a palindrome
# reverse string and original strings are same
# malayalam = malayalam

s = "HanNah"
s = s.lower()
r = ''
for i in s:
    r = i + r

if r == s:
    print('It is a palindrome')
else:
    print('It is not a palindrome')
