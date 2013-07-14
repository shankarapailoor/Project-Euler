def generate_primes():
	x = 600851475143
	factors = []
	remaining_number = x
	i = 2
	while remaining_number > 1:
		if remaining_number % i == 0:
			factors.append(i)
			print factors
			remaining_number = remaining_number/i
			i = 2
			
		else:
			i += 1
	return factors
	



def isPrime(x):
	for i in range(2, x):
		if x % i == 0:
			return 0
		else:
			continue
	return 1


if __name__=='__main__':
	print generate_primes()
