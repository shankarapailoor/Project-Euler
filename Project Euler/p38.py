def concatenate(x, y):
	if y == 0:
		return x
	elif x == 0:
		return y
	t = len(list(str(y)))
	x = 10**t*x
	return x + y

def isPandigital(x):
	t = list(str(x))
	for i in range(0, len(t)):
		if len(t) == len(list(set(t))):
			return True
	return False

def getPandigital(x):
	summ = 0
	t = 0
	pandigits = []
	for i in range(1, 9):
		summ += len(str(x*i))
		pandigits.append(x*i)
		if summ < 9:
			continue
		elif summ > 9:
			break
			pandigits = []
		else:
			break
	if len(pandigits) > 0:
		for j in range(0, len(pandigits)):
			t = concatenate(t, pandigits[j])
		if isPandigital(t):
			return t
	return 0
def p38():
	pandigital_numbers = []
	for i in range(1, 20000):
		x = getPandigital(i)
		if x > 0:
			pandigital_numbers.append(x)
	return pandigital_numbers
	




if __name__=='__main__':
	x = concatenate(192, 384)
	y =  concatenate(x, 567)
	print p38()
