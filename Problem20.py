# -*- coding: utf-8 -*- 
'''
Problem 20
21 June 2002

n! means n × (n - 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import math

def problem_twenty():
	sum_of_digits = 0
	num = math.factorial(100)
	for digit in str(num):
		sum_of_digits += int(digit)
	print sum_of_digits

problem_twenty()
# 648
