#We know that any 9 digit pandigital number is divisible by 9
#since the sum of the digits is equal to 45.
#Similarly and 8 digit pandigital number is divisible by 3
#Thus the solution space is reduced to finding any 7 digit 
#pandigital number. If there weren't any I would just go down to 6

from copy import deepcopy


def sieve(x):
	arr = []
	primes = [True]*x
	for i in range(2, len(primes)):
		if primes[i]:
			for j in range(2, len(primes)/i):
				primes[j*i] = False
	for k in range(2, len(primes)-1):
		if primes[k]:
			arr.append(k)
	return arr

def binSearch(x, s):
	low = 0
	high = len(s)-1
	t = (high + low)/2
	if x == s[low] or x == s[high]:
		return True
	while x!= s[t]:
		
		if x > s[t] and (high-low >= 2):
			low = deepcopy(t)
			t = (high+low)/2
			
		elif x < s[t] and (high-low >= 2):
			
			high = deepcopy(t)
			t = (high + low)/2
		elif (high-low == 1) and s[t] != x:
			return False
		elif x == s[t]:
			return True
	return True

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

if __name__=='__main__':
	x = sieve(10000000)
	s7 = generatepermutations(1234567)
	for j in range(0, len(s7)):
		if binSearch(s7[len(s7)-j-1], x):
			print s7[len(s7)-j-1]
			break

		

