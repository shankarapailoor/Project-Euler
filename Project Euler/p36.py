from time import time

def toString(a):
	g = ''
	for i in range(0, len(a)):
		g += a[i]	
	return g

def toBinary(x):
	y = bin(x)
	t = str(y)
	t = list(t)
	t.pop(0)
	t.pop(0)
	t = toString(t)
	return t

def p36():
	summ = 0
	for i in range(0, 1000000):
		if (str(i) == str(i)[::-1]) and (toBinary(i) == toBinary(i)[::-1]):
			summ += i
	return summ

if __name__=='__main__':
	start = time()
	x = p36()
	end = time()-start
	print end
