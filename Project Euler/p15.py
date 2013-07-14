#solved by combinatorics, but this is a coded algorithm using DP
def f1():
	arr = []
	for i in range(0, 20):
		temp = []
		for k in range(0, 20):
			temp.append(k)
		arr.append(temp)
	return arr

def find_routes(start, finish):
	num_paths = {}
	if start[0] < 20 and start[1] < 20:
		if (start[0]+1, start[1]) in num_paths:
			print 'I am in the if loop'	
			num_paths[start] += num_paths[(start[0]+1, start[1])]
		elif (start[0], start[1]+1) in num_paths:
			print 'I am in the elif loop'
			num_paths[start] += num_paths[(start[0], start[1]+1)]
		else:
			print 'I am in the else loop'
			num_paths.update(find_routes((start[0]+1, start[1]), finish))
			num_paths.update(find_routes((start[0], start[1]+1), finish))
			num_paths[start] = num_paths[(start[0], start[1]+1)] + num_paths[(start[0]+1, start[1])]
	elif start[1] <= 20 and start[0]==20:
		print "I am out of the else loop"
		num_paths[start] = 1
	elif start[0] <= 20 and start[1]==20:
		print "I am out of the else loop"
		num_paths[start] = 1
	return num_paths

if __name__=='__main__':
	start = (10, 10)
	end = (20, 20)
	x = find_routes(start, end)
	print x[start]
	
