#I solved this problem by just staring at the number, but here is a coded solution
#We read in p8number.txt and brute force a solution
#a better solution would be to create a queue that gets the sum from either direction
#this reduces the runtime by half


def getnumber():
	filename = "p8number.txt"
	f = open(filename)
	digits = []
	for line in f:
		digits += line.strip()
	for i in range(0, len(digits)):
		digits[i] = int(digits[i])
	return digits

def arrayprod(array):
	i = 1
	for j in range(0, len(array)):
		i *= array[j]
	return i

def getSum(digits):
	queuefront = []
	queueback = []
	maxprodfront = 0
	maxprodback = 0
	i = 0
	while len(queuefront)!= 5:
		queuefront.append(digits[i])
		i+= 1
	
	while len(queueback)!= 5:
		queueback.append(digits[len(digits)-1-i])
		i+=1
		

	while i < len(digits):
		x = arrayprod(queuefront)
		y = arrayprod(queuefront)
		z = 0
		if x > maxprodfront:
			maxprodfront = x
			queuefront.pop(0)
			queuefront.append(digits[i])
			i += 1

		if y > maxprodback:
			maxprodback = x
			queueback.pop(0)
			queueback.append(digits[len(digits)-1-i])
			i += 1
		
		elif y <= maxprodback:
			queueback.pop(0)
			queueback.append(digits[len(digits)-1-i])
			i += 1

		elif x <= maxprodfront:
			queuefront.pop(0)
			queuefront.append(digits[i])
			i += 1
		if i > (len(digits)-i):
			z = max(maxprodfront, maxprodback)
			return z
		

	return z



if __name__=='__main__':
	x = getnumber()
	print getSum(x)


