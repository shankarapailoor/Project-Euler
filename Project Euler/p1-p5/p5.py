from fractions import gcd

def lcm(a,b):
	return a*b/gcd(a,b)
def elem20(y):
	a = []
	x = 1
	for i in range(2, y):
		a.append(i)
	while a != []:
		temp = a.pop(0)
		x = lcm(x, temp)
	return x
	

if __name__=='__main__':
	print elem20(20)
	
	
	
