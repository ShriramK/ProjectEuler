# -*- coding: utf-8 -*- 
'''A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def problem_four():
	largest_palindrome = 0
	for i in range(100, 1000):
		for j in range(100, 1000):
			stri = str(i * j)
			if stri == stri[::-1]:
				if int(stri) > largest_palindrome:
					largest_palindrome = int(stri)
	print largest_palindrome
			
problem_four()
# 906609
