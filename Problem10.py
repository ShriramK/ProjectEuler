'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
2 and check odd numbers below two million
'''

import time
UPPER_NUM = 2000000# 2e+06

def print_info(info):
	print info

def problem_ten():
	total = 0
	temp = []
	
	start = time.time()
	print_info(start)
	temp = [-1] * UPPER_NUM
		
	for i in range(2, UPPER_NUM, 2):
		temp[i] = 0
		
	total += 2
	for i in range(3, UPPER_NUM, 2):
		if temp[i] == -1:
			# print 'i ', i,
			total += i
			for j in range(i, UPPER_NUM, i):# 1, UPPER_NUM/i+1):
				# if i * j < UPPER_NUM:
				# if temp[i * j] == -1:
				temp[j] = 0 # i * j] = 0
				# else:
					# break
		# print
	end = time.time()
	print_info(end)

	print_info(end - start)
	print_info(total)

"""	
	# only store odd numbers and figure out primes from it
	for i in range(3, 2000000, 2):
		temp.append(-1)
	# new_tot = 2
	total += 2
	
	for i in range(3, 2000000, 2):
		if temp[i] == -1:
			total += i
			for j in range(i , 2000000, 2 * i):
				# print j
				temp[j] = 0
"""

'''
Note:
Average of ~1.57 seconds runtime.
Could it be optimized further or an alternative approach that helps reduce
the runtime to milliseconds	?
'''

"""
	num = 2
	primes = []
	tot = 0
	while num < 2000000:
		val = True
		for i in primes:
			if 2 * i <= num and num % i == 0:
				val = False
				break
		if val == True:	
			primes.append(num)
			# print num
			tot += num
		if num == 2:
			num = 3
		else:
			num += 2
	print tot
	# print primes
# 142913828922
"""
"""		num += 1			
	while start < 2000000:		
			start = 2
			for j in range(start, 2000000, start * i):
				temp[i] = 0
			if start == 2:
				start = 3
			else:
				start += 2

	while last < end:
		while num != 1:
			while num % div == 0:
				primes.append(div)
				tot += div
			if div == 2:
				div = 3
			else:
				div += 2 # only account for odd numbers
# another version, an attempt to optimize
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
# 2 and check odd numbers below two million
import time
def problem_ten():
	total = 0
	temp = []
	d = {}
	start = time.time()
	print start

	# only store odd numbers and figure out primes from it
	for i in range(3, 2000000 + 1, 2):
		# temp.append([i, -1])
		d[i] = -1
	# print len(temp)
	# new_tot = 2
	total += 2
	
	# for i in range(0, len(temp)):# 2000000):
	for i in range(3, 2000000 + 1, 2):
		# if temp[i][1] == -1:
		if d[i] == -1:
			total += i
			# cnt = 0
			# for j in range(temp[i][0], 1000000, 2 * temp[i][0]):
				# if j % 2 != 0:
			for j in range(2 * i, 2000000, i):
					# print j
					# cnt += 1
					# print cnt
					# temp[j][1] = 0
					d[j+i] = 0
	end = time.time()
	print end

	print end - start
	print total
problem_ten()
# 2.01 seconds
"""

problem_ten()
# 142913828922
