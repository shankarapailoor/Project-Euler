def Fibonnaci():
	evensum = 0
	fibonnaci_terms = []
	fibonnaci_terms.append(0)
	fibonnaci_terms.append(1)
	while fibonnaci_terms[-1] < 4000000:
		fibonnaci_terms.append(fibonnaci_terms.pop(0) + fibonnaci_terms[0])
		print fibonnaci_terms[-1]
		if fibonnaci_terms[-1]%2 == 0:
			print fibonnaci_terms[-1]
			evensum += fibonnaci_terms[-1]
		else:
			continue
	return evensum






if __name__=='__main__':
	x = Fibonnaci()
	print x
	
