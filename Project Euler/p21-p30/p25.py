from math import *
from copy import deepcopy
import time

def calculate_Fibonnaci():
	fn = 0
	n = 10
	while len(str(fn)) < 1000:
		fn = 1/sqrt(5)*((2/(-1 + sqrt(5)))**(n+1) - (2/(-1-sqrt(5)))**(n+1))
		n += 1

	return int(fn)


def addtwoarrays(a, b):
	c = [0]*len(a)
	rem = 0
	if len(a) != len(b):
		print "Array Lengths not compatible"
	else:	
		for i in range(0, len(a)):
			temp = a[i] + b[i] + rem
			y = getmodulo(temp)
			c[i] = y[0]
			rem = y[1]
	return c
		

def getmodulo(n):
	x = str(n)
	y = list(x)
	g = ''
	if n > 10:
		t = int(y.pop())
	else:
		return n, 0
	
	for i in y:
		g += i
	g = int(g)
	return t, g

def fibonnaci_numbers():
	a = []
	for i in range(0, 1000):
		a.append(0)
	a[0] = 1
	b = []
	b = deepcopy(a)
	c = deepcopy(a)
	x = 1
	while b[999] == 0:
		x += 1
		c = addtwoarrays(a,b)
		a = deepcopy(b)
		b = deepcopy(c)
	return x
	


if __name__=='__main__':
	a = [5, 9, 2, 0, 0, 0]
	b = [9, 9, 0, 0, 0, 0]
	
	start = time.time()
	x = fibonnaci_numbers()
	end = time.time() - start
	print x, end
