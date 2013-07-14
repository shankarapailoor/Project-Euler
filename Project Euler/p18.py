import sys

def getgraph():
	filename = sys.argv[1]
	f = open(filename, 'r')
	arr = []
	for line in f:
		temp = []
		line.strip()
		for j in range(0, len(line.split())):
			temp.append(int(line.split()[j]))
		arr.append(temp)
	adjacency_list = {}
	i = 0
	for j in range(0, len(arr)):
		for t in range(0, len(arr[j])):
			adjacency_list[(i, arr[j][t])] = []
			i+=1
	temp = 0
	temp1 = 0	
	for k in range(0, len(arr)-1):
		for j in range(0, len(arr[k])):
			for i in range(0, len(arr[k+1])):
				
				if i == j:
					if temp > 0 and j > 0 and (temp1, arr[k+1][j]) in adjacency_list[temp-1, arr[k][j-1]]:
						adjacency_list[(temp, arr[k][i])].append((temp1, arr[k+1][i]))
					else:
						temp1+=1
						adjacency_list[(temp, arr[k][j])].append((temp1, arr[k+1][i]))
				elif i == j+1:
					temp1+=1
					adjacency_list[(temp, arr[k][j])].append((temp1, arr[k+1][i]))
				else:
					continue
			temp+=1
	return adjacency_list

def max_length(x, d):
	maxl = 0
	max_lengths = {}
	for j in d:
		max_lengths[j] = 0
	array = []
	if d[x] == []:
		max_lengths[x] = x[1]

	else:
		temp = 0
		for j in d[x]:
			if max_lengths[j] != 0 and max_lengths[j] > temp:
				temp = max_lengths[j]
			elif max_lengths[j] != 0 and max_lengths[j] <= temp:
				continue
			else:
				max_lengths[j] = max_length(j, d)[j]
				if max_lengths[j] < temp:
					continue
				else:
					temp = max_lengths[j]
		max_lengths[x] = x[1]+temp
	return max_lengths

if __name__=='__main__':
	d = getgraph()
	print max_length((0, 75), d)[(0, 75)]




