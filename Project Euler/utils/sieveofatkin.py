from math import sqrt, floor
from copy import deepcopy

def sieve(x):
	limit = x
	isPrime = [False for i in range(5, limit)]
	for x in range(1, int(floor(sqrt(limit))) +1):
		for y in range(1, int(floor(sqrt(limit)))+1):
			n = 4*x**2 + y**2
			if n <= limit and (n%12 == 1 or n %12 == 5):
				isPrime[n-5] = not isPrime[n-5]
			n = 3*x**2 + y**2
			if n <= limit and (n%12 == 7):
				isPrime[n-5] = not isPrime[n-5]
	
			n = 3*x**2 - y**2
			if x > y and n <= limit and n % 12 == 11:
				isPrime[n-5] = not isPrime[n-5]

	for n in range(5, int(floor(sqrt(limit)))+1):
		if isPrime[n-5]:
			k = 1
			temp = deepcopy(n)
			while temp < limit-1:
				isPrime[temp-5] == False
				temp = k*n**2
				k += 1
	arr = []
	for j in range(0, len(isPrime)):
		if isPrime[j]:
			arr.append(j+5)
	primes = {}
	for j in range(0, len(arr)):
		primes[j] = 1
	return arr


if __name__=='__main__':
	x = sieve(100000)
	print x

		
		
