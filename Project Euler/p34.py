from time import time

from math import factorial
t = [5, 6, 7, 8, 9]

def p34():
	for k in range(t[0], t[len(t)-1]):
		for i in range(factorial(t[0]), factorial(t[1])):
			summ = 0
			x = list(str(i))
			for j in x:
				if int(j) in t and (int(j)!= t[0]):
					break
				else:
					summ += factorial(int(j))
			if summ == i:
				print i
		t.pop(0)


if __name__=='__main__':
	start = time()
	p34()
	end = time()-start
	print end
