from math import floor, sqrt


def generate_primes():
	listofprimes = [2, 3, 5, 7]
	i = 8
	while len(listofprimes) < 10002:
		for j in listofprimes:
			print j
			print floor(sqrt(i))
			print j < floor(sqrt(i))
			if j <= floor(sqrt(i)) and i % j == 0:
				i+=1	
				break

			elif j > floor(sqrt(i)):
				print "i is a prime"
				listofprimes.append(i)
				i+=1	
				break
				
			elif j <= floor(sqrt(i)) == True and i % j != 0:
				continue
				
	return listofprimes
			


if __name__=='__main__':
	print generate_primes()
