def getnames():
	filename = "names.txt"
	f = open(filename, 'r')
	for line in f:
		line.strip()
		x = line.split(",")
		returnval = []
		for j in x:
			a = list(j)
			a.pop(0)
			a.pop()
			h = ''
			for k in a:
				h += k
			returnval.append(h)
		returnval = sorted(returnval)
		return returnval

def p22():
	d = {'A': 1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, '"':0}
	x = getnames()
	summ = 0
	for j in range(0, len(x)):
		s = list(x[j])
		for i in range(0, len(s)):
			temp = 0
			temp += d[s[i]]
			summ += temp*(j+1)
				 
	return summ
if __name__=='__main__':
	print p22()
