# -*- coding: utf-8 -*- 
'''
Problem 16
03 May 2002

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000 ?
concept of Arbitrary precision arithmetic
'''

def problem_sixteen():
	num = pow(2, 1000)
	sum_of_digits = 0
	for digit in str(num):
		sum_of_digits += int(digit)
	print sum_of_digits

problem_sixteen()
# 1366
