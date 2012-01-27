#Problem 13
#22 March 2002

#Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
def problemEleven():
	#create a list of 100 strings of length 50
	ans = ""
	input = open('input.txt', 'r')
	li = []
	for line in input:
		newline = line
		li.append(newline[:50])
		
	carry = 0
	for i in range(50 - 1, -1, -1):
		sum = 0
		for index in range(0,len(li)):
			sum += int(li[index][i])
		sum += carry
		carry = int(str(sum)[:-1])
		ans = str(sum)[-1] + ans
	ans = str(carry) + ans
	print ans[:10]
	input.close()

problemEleven()
#5537376230