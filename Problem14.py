'''Problem 14
05 April 2002

The following iterative sequence is defined for the set of positive integers:

n ? n/2 (n is even)
n ? 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 ? 40 ? 20 ? 10 ? 5 ? 16 ? 8 ? 4 ? 2 ? 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it #has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

import time

def problem_fourteen():
	max_length = 0
	length = 0
	
	start = time.time()
	print start

	for number in range(3, 1000000, 2):
		current_num = number
		length = 0
		while current_num != 1:
			if current_num % 2 == 0:
				current_num = current_num / 2
			else:
				current_num = 3 * current_num + 1
			length += 1
		if length > max_length:
			max_length = length
			ans = number
	end = time.time()
	print end
	print end - start

	print 'ans ' , ans

problem_fourteen()
# 837799

'''
runtime - ~38seconds -> can it be optimized further to reduce runtime /
found a solution ?
reduced to 20 seconds considering odd numbers only
'''
