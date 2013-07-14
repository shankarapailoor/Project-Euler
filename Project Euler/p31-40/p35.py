from copy import deepcopy
from time import time
from sieveoferatosthenes import sieve
from rotations import *

def getpermutations(x):
	permutations = []
	if len(x) == 1:
		permutations.append(x)
		return permutations
	t = deepcopy(x)
	y = list(t)
	
	for j in range(0, len(y)):
		z = deepcopy(y)
		z.pop(j)
		g = ''
		for k in z:
			g += k
		x = getpermutations(g)

		
		for k in range(0, len(x)):
			permutations.append(y[j]+x[k])
			
	return permutations

def getlongesttail(x):
	x = str(x)
	g = ''
	g += x[len(x)-1]
	for i in range(1, len(x)):
		if x[len(x)-i-1] >= x[len(x)-i]:
			g += x[len(x)-i-1]
		else:
			return g, len(x)-i
	return g, len(x)

def toString(a):
	g = ''
	for i in range(0, len(a)):
		g += a[i]	
	return g
def nextPermutation(a):
	t, s = getlongesttail(a)
	a = str(a)
	#print t==a
	if len(a)==1 or (t==a):
		return a
	f = deepcopy(a[s-1])
	small = 10
	x = int(a[s-1])
	
	for i in range(0, len(t)):
		if int(t[i]) < small and (int(t[i]) > x):
			small = int(t[i])
	
	#print small
	n = len(a)-1 - a[::-1].index(str(small))
	#print n
	
	z = list(a)
	z[s-1] = a[n]
	z[n] = f
	m = ''
	for i in range(s, len(z)):
		m += z[i]
	m = m[::-1]
	for j in range(0, len(m)):
		z[j+s] = m[j]
	return toString(z)

def sort_string(string):
	return "".join(sorted(string))

def generatepermutations(a):
	a = str(a)
	
	a = sort_string(a)
	t = [int(a)]
	s = nextPermutation(a)
	v = 0
	while int(s) not in t:
		c = deepcopy(s)
		t.append(int(c))
		
		s = nextPermutation(s)
	return t

def p35():
	bad_primes = []
	
	circular_primes = []
	x = sieve(1000000)
	
	even = ['2', '4', '6', '8', '0']
	for i in range(0, len(x)):
		counter = 0
		if set(str(x[i])).intersection(set(even)):
			continue
		elif x[i] in bad_primes:
			continue
		elif x[i] in circular_primes:
			continue
		else:
			s = getRotations(x[i])	
			
			for j in s:
				if j in x:
					counter += 1
			if counter == len(s):
				circular_primes = circular_primes + s
			else:
				bad_primes = bad_primes + s

		
	return list(set(circular_primes))
	
			
if __name__=='__main__':
	#print getlongesttail('131')
	#print generatepermutations(1193)
	start = time()
	x = p35()
	end = time() - start
	print end

	
	
		

 
