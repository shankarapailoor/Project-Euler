from sieveofatkin import *
from copy import deepcopy

def primefactorization(n, prime_factorization_table):
	x = deepcopy(n)
	while n > 1:
		for j in prime_factorization_table:
			if n % j == 0:
				prime_factorization_table[j] += 1
				n = n/j
			else:
				continue
	summ = 1
	for j in prime_factorization_table:
		if prime_factorization_table[j] != 0:
		  	summ *= (1+prime_factorization_table[j])

	return prime_factorization_table, summ

"""def p21alt():
	arr[1] = 0
	d = 0
	for i in range(1, 10001):
		d = primefactorization(i)
		arr[i] = d"""


if __name__=='__main__':
	x = []
	x = sieve()
	x.insert(0, False)
	x.insert(0, True)
	x.insert(0, True)
	x.insert(0, False)
	x.insert(0, False)
	prime_factorization_table = {}
	for i in range(0, len(x)):
		if x[i] == True:
			prime_factorization_table[i] = 0
		
	print primefactorization(20, prime_factorization_table)
	
