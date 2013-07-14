def sumdigits():
	x = 2**1000
	x = str(x)
	x = list(x)
	summ = 0
	for i in range(0, len(x)):
		x[i] = int(x[i])
		summ += x[i]
	return summ

if __name__=='__main__':
	print sumdigits()
