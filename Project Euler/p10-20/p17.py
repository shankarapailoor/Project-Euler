def f1():
	summ = 0
	digits = {'one':3, 'two': 3, 'three':5, 'four':4, 'five':4, 'six':3, 'seven':5, 'eight':5, 'nine':4}
	tentotwenty = {'eleven': 6, 'twelve': 6, 'thirteen': 8, 'fourteen': 8, 'fifteen': 7, 'sixteen': 7, 'seventeen': 9, 'eighteen': 8, 'nineteen': 8}

	tens = {'twenty': 6, 'thirty': 6, 'forty': 5, 'fifty': 5, 'sixty': 5, 'seventy': 7, 'eighty': 6, 'ninety': 6}
	hundredand = 10
	#get the digits
	for j in digits:
		summ += digits[j]
	summ += 3
	#get the teens
	for k in tentotwenty:
		summ += tentotwenty[k]
	#get twenty, thirty, etc...
	for h in tens:
		summ += tens[h]
	#get one hundred, two hundred, three hundred, ..etc
	for j in digits:
		summ += digits[j] + 7
	#for one thousand
	summ += 11
	#twenty one, twenty two...., thirty one, thirty two, etc...
	for h in tens:
		for i in digits:
			summ += tens[h] + digits[i]

	#one hundred and ten, #two hundred and ten, etc..
	for l in digits:
		summ += digits[l] + hundredand + 3

	for l in digits:
		for j in tens:
			summ += digits[l] + hundredand + tens[j]

	for l in digits:
		for j in digits:
			summ += digits[l] + hundredand + digits[j]
	
	for l in digits:
		for j in tens:
			for k in digits:
				summ += digits[l] + hundredand + tens[j] + digits[k]

	for l in digits:
		for j in tentotwenty:
			summ += digits[l] + hundredand + tentotwenty[j]

	return summ

if __name__=='__main__':
	print f1()
		
