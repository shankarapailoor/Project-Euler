import time

def countSundaysyear(startday, d):
	firstofthemonth = startday
	days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
	numSundays = 0

	def getNextfirst(j, firstofthemonth):
		x = days.index(firstofthemonth)
		if d[j][1] == 28:
			firstofthemonth = firstofthemonth
		elif d[j][1] == 30:
			firstofthemonth = days[(x+3)%7-1]
		elif d[j][1] == 31:
			firstofthemonth = days[(x+4)%7-1]
		elif d[j][1] == 29:
			firstofthemonth = days[(x+2)%7-1]
		return firstofthemonth

	for j in range(0, len(d)):
		if firstofthemonth == 'Sunday' and d[j][0] != 'December':
			numSundays +=1
			firstofthemonth = getNextfirst(j, firstofthemonth)
		elif d[j][0] == 'December':
			if firstofthemonth == 'Sunday':
				numSundays +=1
				firstofthemonth = getNextfirst(j, firstofthemonth)
				return numSundays, firstofthemonth
			else:
				firstofthemonth = getNextfirst(j, firstofthemonth)
				return numSundays, firstofthemonth
		else:
			firstofthemonth = getNextfirst(j, firstofthemonth)


def p19(d, d1):
	numSundays = 0
	firstofyear = 'Tuesday'
	year = 1901
	while year < 2001:
		if year == 1900:
			numSundays += countSundaysyear(firstofyear, d)[0]
			firstofyear = countSundaysyear(firstofyear, d)[1]
		elif year != 1900 and year % 4 == 0:
			numSundays += countSundaysyear(firstofyear, d1)[0]
			firstofyear = countSundaysyear(firstofyear, d1)[1]
		else:
			numSundays += countSundaysyear(firstofyear, d)[0]
			firstofyear = countSundaysyear(firstofyear, d)[1]
		year += 1
	return numSundays
	
if __name__=='__main__':
	d1 = [('January', 31), ('Febuary', 29), ('March', 31), ('April', 30), ('May', 31), ('June', 30), ('July', 31), ('August', 31), ('September', 30), ('October', 31), ('November', 30), ('December', 31)]
	
	d = [('January', 31), ('Febuary', 28), ('March', 31), ('April', 30), ('May', 31), ('June', 30), ('July', 31), ('August', 31), ('September', 30), ('October', 31), ('November', 30), ('December', 31)]
	start = time.time()
	x = p19(d, d1)
	elapsed = time.time()-start
	print x, elapsed
