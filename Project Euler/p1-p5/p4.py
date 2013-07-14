def isPalindrome(x):
	temp = str(x)
	if temp[::-1] == temp:
		return 1
	else:
		return 0

def getLargestPalindrome():
	largestPalindrome = 0
	for i in range(100, 1000):
		for j in range(100, 1000):
			if isPalindrome(i*j):
				if i*j > largestPalindrome:
					largestPalindrome = i*j
					j += 1
				else:
					j += 1
			else:
				j += 1
		i += 1
	return largestPalindrome

if __name__=='__main__':
	print getLargestPalindrome()
	
