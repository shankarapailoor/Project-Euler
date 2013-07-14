def nextRotations(x):
	t = list(str(x))
	counter = len(t)-1
	summ = 0
	rotations = []
	for i in range(1, len(t)):
		summ += (10**counter)*(int(t[i]))
		counter -= 1
	summ += int(t[0])
	return summ

def getRotations(x):
	rotations = []
	if nextRotations(x) == x:
		rotations.append(x)
		return rotations
	while nextRotations(x) not in rotations:
		rotations.append(nextRotations(x))
		x = nextRotations(x)
	return rotations

if __name__=='__main__':
	print getRotations(7195678)
