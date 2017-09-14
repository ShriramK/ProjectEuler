'''Problem 13
22 March 2002
Work out the first ten digits of the sum of the following
one-hundred 50-digit numbers.
'''

def problem_thirteen():
	# create a list of 100 strings of length 50
	ans = ""
	input_random_text = open('input.txt', 'r')
	li = []
	for line in input_random_text:
		newline = line
		li.append(newline[:50])
		
	carry = 0
	for i in range(50 - 1, -1, -1):
		sum_of_nums = 0
		for index in range(0, len(li)):
			sum_of_nums += int(li[index][i])
		sum_of_nums += carry
		carry = int(str(sum_of_nums)[:-1])
		ans = str(sum_of_nums)[-1] + ans
	ans = str(carry) + ans
	print ans[:10]
	input_random_text.close()

problem_thirteen()
# 5537376230
