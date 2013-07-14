from math import floor
from time import time

def p39():
	maxnum = 0
	returnval = 0
	for i in xrange(1, 1000, 2):
		num = 0
		for j in range(1, (i/3)):
			x = (-1*2*float(j)*float(i) + float(i)**2)/(-1*2*float(j) + 2*float(i))
			
			if (floor(x) == x):
				num += 1
		if num > maxnum:
			maxnum = num
			returnval = i
	return returnval, maxnum

if __name__=='__main__':
	start = time()
	x = p39
	end = time()-start
	print end
