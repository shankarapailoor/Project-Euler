from math import floor, sqrt


def generate_primes():
	listofprimes = [2, 3, 5, 7]
	i = 8
	k = 0
	while listofprimes[len(listofprimes)-1] < 2000000:
		if i%2 == 0:
			continue
		for j in listofprimes:
			if j <= floor(sqrt(i)) and i % j == 0:
				i+=1	
				break

			elif j > floor(sqrt(i)):
				listofprimes.append(i)
				i+=1	
				break
				
			elif j <= floor(sqrt(i)) == True and i % j != 0:
				continue
				
	for j in range(0, len(listofprimes)):
		k+= listofprimes[j]
	return k

if __name__=='__main__':
	print generate_primes()
