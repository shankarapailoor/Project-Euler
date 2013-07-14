def sumsquare(x):
	return x*(x+1)*(2*x+1)/6

def squaresum(x):
	return (x**2)*((x+1)**2)/4

if __name__=='__main__':
	print squaresum(100)-sumsquare(100)
