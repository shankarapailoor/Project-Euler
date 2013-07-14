from sieveoferatosthenes import sieve
from copy import deepcopy

def p27():
	x = sieve()
	y = deepcopy(x)	
	for j in range(0, len(x)):
		x.insert(0, -1*y[j])
	print x
	maxnumofprimes = 0
	coefficients = (0,0)
	prod = 1
	for i in range(0, len(x)):
		for j in range(0, len(x)):
			t = 0
			while (t**2 + x[i]*t + x[j]) in x:
				t+=1
			if t > maxnumofprimes:
				maxnumofprimes = t
				prod = x[i]*x[j]
				coefficients = x[i], x[j]
	return coefficients

if __name__=='__main__':
	print p27()
