from math import floor, sqrt

def gentrip():
	for i in range(1, 1000):
		for j in range(i, 1000):
			print "j is:", j
			if isTriple(i, j) and (i + j + sqrt(i**2 + j**2) == 1000):
				return i*j*(sqrt(i**2 + j**2))
			else:
				continue
			
			

def isTriple(i, j):
	if sqrt(i**2 + j**2) == floor(sqrt(i**2 + j**2)):
		return True
	else:
		return False


if __name__=='__main__':
	print gentrip()
				
