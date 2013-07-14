def sieve(x):
	primes = [True]*x
	listofprimes = []
	for i in range(2, len(primes)):
		if primes[i]:
			j = 2
			while i*j < len(primes):
				primes[i*j] = False
				j+=1
		else:
			continue
	for i in range(2, x):
		if primes[i]:
			listofprimes.append(i)
		
	return listofprimes

if __name__=='__main__':
	s = sieve(2000000)
	summ = 0
	for j in range(0, len(s)):
		summ += s[j]
	print summ
