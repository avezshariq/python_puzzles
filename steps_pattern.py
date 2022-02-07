# Simple Steps pattern

n = 15 # Change this number for the number of steps
for ind in range(1,n):
	if ind % 2 == 0:
		print(' ' * (ind-1), end = '')
		print('|')
	else:
		print(' ' * (ind-1), end = '')
		print('_')

print('OR, IF YOU PREFER IT THIS WAY')
for ind in range(1,n):
	print(' ' * (ind-1), end = '')
	print(7)
