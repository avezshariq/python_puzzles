# This program is intentionally made to look very complicated so that the person receiveng the file will not be able to unsderstand what's going on
# One digit prime numbers
prime = [1, 2, 3, 5, 7]

# All Prime numbers are less than 10
variab = 10

sum1 = 0
for i in range(17):
	sum1 += i
store = chr(int((sum1 + 10)/2 ))
print(store)
thin = chr(int(prime[0] * 100 + prime[2]))
thinner = chr(int(str(prime[0]) + str(prime[0]) + str(prime[0])))
thinnest = chr(int(sum(prime)*6.5 - 1))
print(thin + thinner + thinnest)
now = chr(ord(thin) - 1)
then = chr(prime[0]*101 + prime[-1])
print(now + thinner*2 + then + chr(prime[0]*100 + prime[0]) + chr(ord(now)-2))
move = chr(10**2 - 2)
print(move + chr(11**2))
fin = chr(prime[2]*2*10 + (prime[-1] - prime[1]))
contrast = chr((int(str(ord(fin))[0]) + 2)* 10 + 6)
kelado = chr(ord(contrast) - sum(prime) + 1)
justice = 0
for j in prime:
	justice += j*10
justice /= 2
ender = chr(int(justice))
print(fin + contrast + kelado + ender)
