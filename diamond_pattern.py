n = 15 # Size of Diamond pattern
for ind in range(n):
	print(' ' * (n-ind), end = '')
	print('|' *(2*ind+1))

print(' '*((2*n+1 - 11)//2), end = '')
print('AVEZ SHARIQ')

for ind in range(n-1, -1, -1):
	print(' ' * (n-ind), end = '')
	print('|' *(2*ind+1))
