def coinsums():
	cointypes = [1, 2, 5, 10, 20, 50, 100, 200]
	table = [0]*201
	table[0] = 1
	for i in range(0, len(cointypes)):
		for j in range(cointypes[i], 201):
			table[j] += table[j-cointypes[i]]
	return table[200]

if __name__=='__main__':
	print coinsums()
