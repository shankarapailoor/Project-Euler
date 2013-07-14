from sieveoferatosthenes import sieve
from time import time
from copy import deepcopy

s = sieve(1000000)

righttrunctable = [23, 37, 53, 73, 233, 293, 313, 317, 373, 593, 733, 797, 2333, 2393, 3137, 3733, 3793, 3797, 7193, 7333, 7393, 23333, 23993, 31193, 37337, 37397, 59393, 71933, 233993, 239933, 373393, 593933, 593993, 719333, 739393, 739397]

def binSearch(x, s):
	low = 0
	high = len(s)-1
	t = (high + low)/2
	if x == s[low] or x == s[high]:
		return True
	while x!= s[t]:
		
		if x > s[t] and (high-low >= 2):
			low = deepcopy(t)
			t = (high+low)/2
			
		elif x < s[t] and (high-low >= 2):
			
			high = deepcopy(t)
			t = (high + low)/2
		elif (high-low == 1) and s[t] != x:
			return False
		elif x == s[t]:
			return True
	return True

def flp(x):
	x = list(str(x))
	if binSearch(int(x[0]), s) and binSearch(int(x[len(x)-1]), s):
		return True
	else:
		return False

def isRightTrunctable(x):
	while x > 10:
		
		if binSearch(x, s):
			y = x%10
			x= (x-y)/10
		else:
			return False
	if x in s:
		return True
	else:
		return False

def toString(a):
	g = ''
	for i in range(0, len(a)):
		g += a[i]	
	return g

def isLeftTrunctable(x):
	while x > 10:
		if binSearch(x, s):
			t = list(str(x))
			y = t.pop(0)
			y = toString(t)
			x = int(y)
		else:
			break
	if x in s:
		return True
	else:
		return False
			

def getRightTrunctable():
	rightTrunctable = []
	for i in range(6, len(s)):
		if flp(s[i]):
			if isRightTrunctable(s[i]):
				rightTrunctable.append(s[i])
		else:
			continue
	return rightTrunctable

def solve():
	summ = 0
	for j in righttrunctable:
		if isLeftTrunctable(j):
			summ += j
	return summ
		
if __name__=='__main__':
	a = [1, 2, 3, 5, 5, 7, 7, 8, 9, 10]
	#print getRightTrunctable()
	print solve()

		
