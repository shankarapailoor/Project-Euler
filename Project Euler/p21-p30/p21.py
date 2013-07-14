from math import sqrt, floor
def fastdivisor(n):
	x = int(floor(sqrt(n)))
	divisorsum = 0
	for i in range(1, x+1):
		if n % (x+1-i)==0 and i != 1:
			divisorsum += (x + 1-i) + n/(x + 1 - i)
		elif n % (x)==0:
			divisorsum += x
			
	return divisorsum - n

def getdivisorsum():
	d = {}
	for i in range(1, 10000):
		d[i] = fastdivisor(i)
	return d

def getamicablenumbers():
	amicable_numbers = []
	d = getdivisorsum()
	for j in d:
		for k in d:
			if d[j] == k and d[k] == j and j!= k:
				amicable_numbers.append(j)
				amicable_numbers.append(k)
	amicable_numbers = list(set(amicable_numbers))
	return amicable_numbers


if __name__=='__main__':
	print getamicablenumbers()
		
