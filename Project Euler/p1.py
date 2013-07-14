def multiples():
	sum3 = 0
	sum5 = 0
	sum15 = 0
	for i in range(0, 1000):
		if i%3==0:
			sum3 += i
		elif i%5==0:
			sum5 += i
		elif i%15==0:
			sum15 += i
	return sum3 + sum5 + sum15


if __name__=='__main__':
	
	print multiples()
