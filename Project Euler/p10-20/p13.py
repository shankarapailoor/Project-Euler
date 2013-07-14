from copy import deepcopy

def findCollatzSequence(x):
	y = deepcopy(x)
	collatzsequence = [y]
	if x == 1:
		return 1
	while x > 1:
		if x % 2 == 0:
			x = x/2
			t = 0
			t = deepcopy(x)
			collatzsequence.append(t)
		else:
			x = 3*x + 1
			z = 0
			z = deepcopy(x)
			collatzsequence.append(z)
	return len(collatzsequence)
def getNext(x):
	if x % 2 == 0:
		return x/2
	else:
		return 3*x + 1

def getLength1000():
	collatzsequence = {}
	for i in range(0, 10001):
		collatzsequence[i] = findCollatzSequence(i)
	return collatzsequence

def longestCollatzChain():
	dicts = getLength1000()
	longestnum = 0
	maxlength = 0
	i = 1001
	for i in range(1001, 1000000):	
		chainlength = 1
		j = deepcopy(i)
		while j > 1:
			if getNext(i) in dicts:
				chainlength += dicts[getNext(i)]
				j = 1
			else:
				j = getNext(j)
				chainlength += 1
		if chainlength > maxlength:
			longestnum = deepcopy(i)
			maxlength = deepcopy(chainlength)
	return longestnum
	

if __name__=='__main__':
	print findCollatzSequence(837799)
	
	
