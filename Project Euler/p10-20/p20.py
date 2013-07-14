import time

def p20():
	summ = 0
	j = 1
	for i in range(1, 101):
		"""if i == 10 or i == 100 or i % 10 == 5:
			continue
		elif i!= 10 and i!= 100 and i%10 == 0:
			j*= (i/10)

		elif i%10 == 4:
			j *= i*(i+1)/10"""
		j*=i
		

		
	j = str(j)
	for t in range(0, len(j)):
		summ += int(j[t])
	return summ

if __name__=='__main__':
	start = time.time()
	x = p20()
	end = time.time()-start
	print x, end
		
