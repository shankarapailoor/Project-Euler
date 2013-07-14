def getdigits():
	filename = "p12number.txt"
	f = open(filename)
	lastdigits = []
	temp = 0
	
	for line in f:
		temp1 = []
		line = line.strip()
		lastdigits.append(int(line))
	for j in range(0, len(lastdigits)):
		temp += lastdigits[j]
	return lastdigits, temp

if __name__=='__main__':
	print getdigits()
		
