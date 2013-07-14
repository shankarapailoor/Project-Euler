import time

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
	start = time.time()
	x = sieve()
	end = time.time()-start
	print x, end
