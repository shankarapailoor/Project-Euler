from sieveofatkin import sieve
from copy import deepcopy
import time

def getprimefactors():
	primefactortable = {}
	filename = "p23file.txt"
	f = open(filename, 'r')
	for line in f:
		line.strip()
		x = line.split(",")
		for j in range(0, len(x)):
			t = list(x[j])
			v = deepcopy(t)
			key = ''
			value = ''
			marker = 100000000
			for j in range(0, len(v)):

				if v[j] == ' ':
					continue
				elif v[j] == ':':
					k = deepcopy(j)
					marker = k+2
				elif j >= marker and v[j]!= ' ':
					value = value + v[j]
				else:
					key = key + v[j]
			primefactortable[int(key)] = int(value) 
	return primefactortable

def p23():
	x = getprimefactors()
	summ = 0
	arr = []
	arr1 = []
	temp = []
	for j in x:
		if x[j] > j:
			arr.append(j)
	for j in range(0, len(arr)):
		for k in range(j, len(arr)):
			if arr[j] + arr[k] > 28123:
				continue
			else:
				temp.append(arr[j] + arr[k])
	temp = list(set(temp))
	for j in range(0, 28123):
		arr1.append(j+1)
	newtemp = list(set(arr1).difference(set(temp)))
	for j in newtemp:
		summ += j
	return summ
		
def prime_factorization(x, y):
	y.insert(0, 3)
	y.insert(0, 2)
	prime_factors = {}
	for j in range(0, len(y)):
		prime_factors[y[j]] = 0
	while x > 1:
		for k in range(0, len(y)):
			if x%y[k] == 0:
				prime_factors[y[k]] += 1
				x = x/y[k]
			else:
				continue
	prime_factors2 = dict(prime_factors)
	for k in prime_factors:
		if prime_factors[k] == 0:
			del prime_factors2[k]

	return prime_factors2

def sum_divisors(x, y):
	summ = 1
	z = prime_factorization(x, y)
	for j in z:
		summ *= (j**(z[j]+1) - 1)/(j-1)
	return summ - x

def get_divisor_dict(y):
	divisordict = {}
	for j in range(2, 28123):
		divisordict[j] = sum_divisors(j, y)
	return divisordict
			

if __name__=='__main__':
	start = time.time()
	x = p23()
	end = time.time()-start
	print x, end
	
