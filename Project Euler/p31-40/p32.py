import time
t = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def pandigit():
	pandigitproducts  = []
	summ = 0
	for i in range(100, 999):
		for j in range(10, 100):
			if isrearrangement(str(i) + str(j) + str(i*j)):
				summ += i*j
	for i in range(0, 10):
		for j in range(1000, 10000):
			if isrearrangement(str(i) + str(j) + str(i*j)):
				summ += i*j
	return summ
			

def isrearrangement(x):
	seen_digits = []
	if len(str(x)) != 9:
		return None
	else:
		for i in range(0, len(list(str(x)))):
			if int(list(str(x))[i]) in t and (int(list(str(x))[i]) not in seen_digits):
				seen_digits.append(int(list(str(x))[i]))
				continue
				
			else:
				return None		
	return 1

if __name__=='__main__':
	start = time.time()
	x = pandigit()
	end = time.time()-start
	print x, end
