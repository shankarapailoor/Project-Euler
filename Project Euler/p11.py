from math import floor
from math import sqrt

def fastfactorcount(number):
	numfactors = 0
	x = int(sqrt(number))
	if number==1:
		return 1
	for j in range(1, x):
		if x**2 == number:
			numfactors -= 1
		elif number % (x-j) == 0:
			numfactors += 2
	return numfactors
			
def p12():
	i = 1
	j = 1
	while fastfactorcount(j) <= 500:
		i += 1
		j = i*(i+1)/2
	print i
	return j
		
if __name__=='__main__':
	print fastfactorcount(17907120)
	print p12()

	
