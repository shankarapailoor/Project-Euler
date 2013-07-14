def p33():
	for j in range(1, 10):
		for k in range(j+1, 10):
			for i in range(j+1, 10):
				x = (10.0/k - 1.0/j)*i
				if x == 9.0:
					print 10*j + i, 10*i + k


if __name__ == '__main__':
	print p33()
